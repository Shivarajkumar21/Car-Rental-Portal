from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db.models import Q
import json
from .models import CarDetails, CarBooking, AddCustomer, AddDriver, register, Complaint
from .authentication import hash_password, verify_password, get_current_user
from datetime import datetime

@csrf_exempt
@require_http_methods(["POST"])
def api_login(request):
    """API endpoint for user login"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': 'Username and password required'}, status=400)
        
        try:
            user = register.objects.get(Username=username)
            if verify_password(password, user.Password):
                request.session['username'] = username
                return JsonResponse({
                    'success': True,
                    'user_type': user.utype,
                    'message': 'Login successful'
                })
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except register.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
            
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def api_register(request):
    """API endpoint for user registration"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        utype = data.get('utype')
        mobile = data.get('mobile')
        email = data.get('email')
        
        # Validation
        if not all([username, password, utype, mobile, email]):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        
        # Check if user already exists
        if register.objects.filter(Username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=409)
        
        # Hash password and create user
        hashed_password = hash_password(password)
        user = register.objects.create(
            Username=username,
            Password=hashed_password,
            utype=utype,
            mobileno=mobile,
            emailid=email
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Registration successful',
            'user_id': user.id
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def api_cars(request):
    """API endpoint to get available cars with filtering"""
    try:
        # Get query parameters
        company = request.GET.get('company')
        fuel_type = request.GET.get('fuel_type')
        min_capacity = request.GET.get('min_capacity')
        max_rent = request.GET.get('max_rent')
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 10))
        
        # Build query
        cars = CarDetails.objects.all()
        
        if company:
            cars = cars.filter(company__icontains=company)
        if fuel_type:
            cars = cars.filter(fuel_type=fuel_type)
        if min_capacity:
            cars = cars.filter(capacity__gte=min_capacity)
        if max_rent:
            cars = cars.filter(rent__lte=max_rent)
        
        # Pagination
        paginator = Paginator(cars, per_page)
        page_obj = paginator.get_page(page)
        
        cars_data = []
        for car in page_obj:
            cars_data.append({
                'id': car.id,
                'car_id': car.car_id,
                'company': car.company,
                'make': car.make,
                'rent': car.rent,
                'fuel_type': car.fuel_type,
                'capacity': car.capacity,
                'reg_no': car.reg_no,
                'photo_url': car.photo.url if car.photo else None
            })
        
        return JsonResponse({
            'cars': cars_data,
            'pagination': {
                'current_page': page,
                'total_pages': paginator.num_pages,
                'total_cars': paginator.count,
                'has_next': page_obj.has_next(),
                'has_previous': page_obj.has_previous()
            }
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def api_book_car(request):
    """API endpoint to book a car"""
    try:
        user = get_current_user(request)
        if not user:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        
        data = json.loads(request.body)
        car_id = data.get('car_id')
        booking_date = data.get('booking_date')
        to_place = data.get('to_place')
        no_of_days = data.get('no_of_days')
        
        if not all([car_id, booking_date, to_place, no_of_days]):
            return JsonResponse({'error': 'All booking details required'}, status=400)
        
        # Check if car exists
        try:
            car = CarDetails.objects.get(car_id=car_id)
        except CarDetails.DoesNotExist:
            return JsonResponse({'error': 'Car not found'}, status=404)
        
        # Create booking
        booking = CarBooking.objects.create(
            booking_id=f"BK{datetime.now().strftime('%Y%m%d%H%M%S')}",
            cust_id=str(user.id),
            car_id=car_id,
            booking_date=booking_date,
            reg_date=datetime.now().date(),
            to_place=to_place,
            no_of_days=no_of_days,
            status='Pending'
        )
        
        return JsonResponse({
            'success': True,
            'booking_id': booking.booking_id,
            'message': 'Car booked successfully'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def api_bookings(request):
    """API endpoint to get user bookings"""
    try:
        user = get_current_user(request)
        if not user:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        
        bookings = CarBooking.objects.filter(cust_id=str(user.id))
        
        bookings_data = []
        for booking in bookings:
            try:
                car = CarDetails.objects.get(car_id=booking.car_id)
                car_info = {
                    'company': car.company,
                    'make': car.make,
                    'rent': car.rent
                }
            except CarDetails.DoesNotExist:
                car_info = {'company': 'Unknown', 'make': 'Unknown', 'rent': 'N/A'}
            
            bookings_data.append({
                'booking_id': booking.booking_id,
                'car_id': booking.car_id,
                'car_info': car_info,
                'booking_date': booking.booking_date,
                'to_place': booking.to_place,
                'no_of_days': booking.no_of_days,
                'status': booking.status
            })
        
        return JsonResponse({'bookings': bookings_data})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def api_complaint(request):
    """API endpoint to submit a complaint"""
    try:
        user = get_current_user(request)
        if not user:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        
        data = json.loads(request.body)
        trip_id = data.get('trip_id')
        complaint_type = data.get('complaint_type')
        details = data.get('details')
        
        if not all([trip_id, complaint_type, details]):
            return JsonResponse({'error': 'All complaint details required'}, status=400)
        
        complaint = Complaint.objects.create(
            cust_id=str(user.id),
            trip_id=trip_id,
            complaint_type=complaint_type,
            details=details,
            date=datetime.now().date(),
            status='Open'
        )
        
        return JsonResponse({
            'success': True,
            'complaint_id': complaint.id,
            'message': 'Complaint submitted successfully'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def api_search_cars(request):
    """API endpoint for advanced car search"""
    try:
        query = request.GET.get('q', '')
        
        if not query:
            return JsonResponse({'error': 'Search query required'}, status=400)
        
        cars = CarDetails.objects.filter(
            Q(company__icontains=query) |
            Q(make__icontains=query) |
            Q(fuel_type__icontains=query) |
            Q(reg_no__icontains=query)
        )
        
        cars_data = []
        for car in cars:
            cars_data.append({
                'id': car.id,
                'car_id': car.car_id,
                'company': car.company,
                'make': car.make,
                'rent': car.rent,
                'fuel_type': car.fuel_type,
                'capacity': car.capacity,
                'reg_no': car.reg_no,
                'photo_url': car.photo.url if car.photo else None
            })
        
        return JsonResponse({
            'cars': cars_data,
            'total_results': len(cars_data)
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
