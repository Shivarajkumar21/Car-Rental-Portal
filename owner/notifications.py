from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
from .models import CarBooking, CarDetails, register, Complaint
import logging

logger = logging.getLogger(__name__)

class EmailNotificationService:
    """Email notification service for car rental operations"""
    
    @staticmethod
    def send_booking_confirmation(booking_id):
        """Send booking confirmation email"""
        try:
            booking = CarBooking.objects.get(booking_id=booking_id)
            customer = register.objects.get(id=booking.cust_id)
            car = CarDetails.objects.get(car_id=booking.car_id)
            
            subject = f'Booking Confirmation - {booking.booking_id}'
            
            context = {
                'customer_name': customer.Username,
                'booking_id': booking.booking_id,
                'car_company': car.company,
                'car_make': car.make,
                'booking_date': booking.booking_date,
                'destination': booking.to_place,
                'duration': booking.no_of_days,
                'rent_per_day': car.rent,
                'total_amount': float(car.rent) * int(booking.no_of_days or 1)
            }
            
            html_message = render_to_string('emails/booking_confirmation.html', context)
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer.emailid],
                html_message=html_message,
                fail_silently=False
            )
            
            logger.info(f"Booking confirmation email sent for {booking_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send booking confirmation email: {str(e)}")
            return False
    
    @staticmethod
    def send_booking_cancellation(booking_id, reason=""):
        """Send booking cancellation email"""
        try:
            booking = CarBooking.objects.get(booking_id=booking_id)
            customer = register.objects.get(id=booking.cust_id)
            
            subject = f'Booking Cancelled - {booking.booking_id}'
            
            context = {
                'customer_name': customer.Username,
                'booking_id': booking.booking_id,
                'reason': reason,
                'booking_date': booking.booking_date
            }
            
            html_message = render_to_string('emails/booking_cancellation.html', context)
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer.emailid],
                html_message=html_message,
                fail_silently=False
            )
            
            logger.info(f"Booking cancellation email sent for {booking_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send booking cancellation email: {str(e)}")
            return False
    
    @staticmethod
    def send_complaint_acknowledgment(complaint_id):
        """Send complaint acknowledgment email"""
        try:
            complaint = Complaint.objects.get(id=complaint_id)
            customer = register.objects.get(id=complaint.cust_id)
            
            subject = f'Complaint Received - #{complaint_id}'
            
            context = {
                'customer_name': customer.Username,
                'complaint_id': complaint_id,
                'complaint_type': complaint.complaint_type,
                'trip_id': complaint.trip_id,
                'date_submitted': complaint.date
            }
            
            html_message = render_to_string('emails/complaint_acknowledgment.html', context)
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer.emailid],
                html_message=html_message,
                fail_silently=False
            )
            
            logger.info(f"Complaint acknowledgment email sent for {complaint_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send complaint acknowledgment email: {str(e)}")
            return False
    
    @staticmethod
    def send_welcome_email(user_id):
        """Send welcome email to new users"""
        try:
            user = register.objects.get(id=user_id)
            
            subject = 'Welcome to Car Rental Portal'
            
            context = {
                'username': user.Username,
                'user_type': user.utype
            }
            
            html_message = render_to_string('emails/welcome.html', context)
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.emailid],
                html_message=html_message,
                fail_silently=False
            )
            
            logger.info(f"Welcome email sent to {user.Username}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send welcome email: {str(e)}")
            return False
    
    @staticmethod
    def send_reminder_email(booking_id):
        """Send booking reminder email"""
        try:
            booking = CarBooking.objects.get(booking_id=booking_id)
            customer = register.objects.get(id=booking.cust_id)
            car = CarDetails.objects.get(car_id=booking.car_id)
            
            subject = f'Booking Reminder - {booking.booking_id}'
            
            context = {
                'customer_name': customer.Username,
                'booking_id': booking.booking_id,
                'car_company': car.company,
                'car_make': car.make,
                'booking_date': booking.booking_date,
                'destination': booking.to_place
            }
            
            html_message = render_to_string('emails/booking_reminder.html', context)
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer.emailid],
                html_message=html_message,
                fail_silently=False
            )
            
            logger.info(f"Booking reminder email sent for {booking_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send booking reminder email: {str(e)}")
            return False

class SMSNotificationService:
    """SMS notification service (placeholder for future implementation)"""
    
    @staticmethod
    def send_booking_sms(booking_id, phone_number):
        """Send booking confirmation SMS"""
        # Placeholder for SMS integration (Twilio, AWS SNS, etc.)
        logger.info(f"SMS notification placeholder for booking {booking_id} to {phone_number}")
        return True
    
    @staticmethod
    def send_reminder_sms(booking_id, phone_number):
        """Send booking reminder SMS"""
        # Placeholder for SMS integration
        logger.info(f"SMS reminder placeholder for booking {booking_id} to {phone_number}")
        return True
