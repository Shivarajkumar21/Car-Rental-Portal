from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps
from .models import register
import re

def hash_password(password):
    """Hash password using Django's built-in hasher"""
    return make_password(password)

def verify_password(password, hashed_password):
    """Verify password against hash"""
    return check_password(password, hashed_password)

def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    return True, "Password is valid"

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_mobile(mobile):
    """Validate mobile number format"""
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, mobile) is not None

def require_auth(user_type=None):
    """Decorator to require authentication"""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            username = request.session.get('username')
            if not username:
                return redirect('login')
            
            if user_type:
                try:
                    user = register.objects.get(Username=username)
                    if user.utype != user_type:
                        return redirect('login')
                except register.DoesNotExist:
                    return redirect('login')
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

def get_current_user(request):
    """Get current logged-in user"""
    username = request.session.get('username')
    if username:
        try:
            return register.objects.get(Username=username)
        except register.DoesNotExist:
            return None
    return None
