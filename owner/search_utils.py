from django.db.models import Q
from .models import CarDetails, CarBooking, AddCustomer, AddDriver, Complaint
from datetime import datetime, timedelta

class CarSearchFilter:
    """Advanced car search and filtering utility"""
    
    def __init__(self):
        self.queryset = CarDetails.objects.all()
    
    def filter_by_company(self, company):
        """Filter cars by company"""
        if company:
            self.queryset = self.queryset.filter(company__icontains=company)
        return self
    
    def filter_by_fuel_type(self, fuel_type):
        """Filter cars by fuel type"""
        if fuel_type:
            self.queryset = self.queryset.filter(fuel_type=fuel_type)
        return self
    
    def filter_by_capacity(self, min_capacity=None, max_capacity=None):
        """Filter cars by seating capacity"""
        if min_capacity:
            self.queryset = self.queryset.filter(capacity__gte=min_capacity)
        if max_capacity:
            self.queryset = self.queryset.filter(capacity__lte=max_capacity)
        return self
    
    def filter_by_rent(self, min_rent=None, max_rent=None):
        """Filter cars by rent price"""
        if min_rent:
            self.queryset = self.queryset.filter(rent__gte=min_rent)
        if max_rent:
            self.queryset = self.queryset.filter(rent__lte=max_rent)
        return self
    
    def search_text(self, query):
        """Search cars by text query"""
        if query:
            self.queryset = self.queryset.filter(
                Q(company__icontains=query) |
                Q(make__icontains=query) |
                Q(reg_no__icontains=query) |
                Q(fuel_type__icontains=query)
            )
        return self
    
    def filter_available_cars(self, start_date=None, end_date=None):
        """Filter cars that are available for booking"""
        if start_date and end_date:
            # Get cars that are not booked during the specified period
            booked_cars = CarBooking.objects.filter(
                booking_date__range=[start_date, end_date],
                status__in=['Confirmed', 'Ongoing']
            ).values_list('car_id', flat=True)
            
            self.queryset = self.queryset.exclude(car_id__in=booked_cars)
        return self
    
    def order_by_rent(self, ascending=True):
        """Order cars by rent price"""
        if ascending:
            self.queryset = self.queryset.order_by('rent')
        else:
            self.queryset = self.queryset.order_by('-rent')
        return self
    
    def get_results(self):
        """Get filtered results"""
        return self.queryset

class BookingAnalytics:
    """Booking analytics and reporting utility"""
    
    @staticmethod
    def get_popular_cars(limit=10):
        """Get most frequently booked cars"""
        from django.db.models import Count
        return CarBooking.objects.values('car_id').annotate(
            booking_count=Count('car_id')
        ).order_by('-booking_count')[:limit]
    
    @staticmethod
    def get_revenue_by_period(start_date, end_date):
        """Calculate revenue for a specific period"""
        bookings = CarBooking.objects.filter(
            booking_date__range=[start_date, end_date],
            status='Completed'
        )
        
        total_revenue = 0
        for booking in bookings:
            try:
                car = CarDetails.objects.get(car_id=booking.car_id)
                days = int(booking.no_of_days) if booking.no_of_days else 1
                total_revenue += float(car.rent) * days
            except (CarDetails.DoesNotExist, ValueError):
                continue
        
        return total_revenue
    
    @staticmethod
    def get_booking_trends(days=30):
        """Get booking trends for the last N days"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        
        bookings = CarBooking.objects.filter(
            reg_date__range=[start_date, end_date]
        ).extra(
            select={'day': 'date(reg_date)'}
        ).values('day').annotate(
            count=Count('id')
        ).order_by('day')
        
        return list(bookings)
    
    @staticmethod
    def get_customer_statistics():
        """Get customer booking statistics"""
        from django.db.models import Count, Avg
        
        stats = CarBooking.objects.aggregate(
            total_bookings=Count('id'),
            unique_customers=Count('cust_id', distinct=True),
            avg_days_per_booking=Avg('no_of_days')
        )
        
        return stats

class ComplaintAnalytics:
    """Complaint analytics utility"""
    
    @staticmethod
    def get_complaint_summary():
        """Get complaint summary by type and status"""
        from django.db.models import Count
        
        by_type = Complaint.objects.values('complaint_type').annotate(
            count=Count('id')
        ).order_by('-count')
        
        by_status = Complaint.objects.values('status').annotate(
            count=Count('id')
        ).order_by('-count')
        
        return {
            'by_type': list(by_type),
            'by_status': list(by_status),
            'total_complaints': Complaint.objects.count()
        }
    
    @staticmethod
    def get_pending_complaints():
        """Get all pending complaints"""
        return Complaint.objects.filter(
            status__in=['Open', 'In Progress']
        ).order_by('-date')

def get_dashboard_data():
    """Get comprehensive dashboard data"""
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    
    return {
        'total_cars': CarDetails.objects.count(),
        'total_customers': AddCustomer.objects.count(),
        'total_drivers': AddDriver.objects.count(),
        'total_bookings': CarBooking.objects.count(),
        'pending_bookings': CarBooking.objects.filter(status='Pending').count(),
        'confirmed_bookings': CarBooking.objects.filter(status='Confirmed').count(),
        'weekly_bookings': CarBooking.objects.filter(reg_date__gte=week_ago).count(),
        'monthly_revenue': BookingAnalytics.get_revenue_by_period(month_ago, today),
        'popular_cars': BookingAnalytics.get_popular_cars(5),
        'recent_complaints': Complaint.objects.filter(date__gte=week_ago).count(),
        'pending_complaints': ComplaintAnalytics.get_pending_complaints().count(),
    }
