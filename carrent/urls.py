"""carrent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from owner import views, api_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('cars', views.cars, name='cars'),
    path('index', views.index, name='index'),
    path('agent', views.agent, name='agent'),
    path('customer', views.customer, name='customer'),
    path('logcheck', views.logcheck, name='logcheck'),
    path('signup', views.signup, name='signup'),
    path('Viewregister', views.Viewregister, name='Viewregister'),
    path('Viewlogin', views.Viewlogin, name='Viewlogin'),
    path('insertAddCustomer', views.insertAddCustomer, name='insertAddCustomer'),
    path('ViewAddCustomer', views.ViewAddCustomer, name='ViewAddCustomer'),
    path('insertAddDriver', views.insertAddDriver, name='insertAddDriver'),
    path('ViewAddDriver', views.ViewAddDriver, name='ViewAddDriver'),
    path('insertCarBooking', views.insertCarBooking, name='insertCarBooking'),
    path('ViewCarBooking', views.ViewCarBooking, name='ViewCarBooking'),
    path('insertCarDetails', views.insertCarDetails, name='insertCarDetails'),
    path('ViewCarDetails', views.ViewCarDetails, name='ViewCarDetails'),
    path('insertComplaint', views.insertComplaint, name='insertComplaint'),
    path('ViewComplaint', views.ViewComplaint, name='ViewComplaint'),
    path('insertRentDetails', views.insertRentDetails, name='insertRentDetails'),
    path('ViewRentDetails', views.ViewRentDetails, name='ViewRentDetails'),
    path('insertTripChart', views.insertTripChart, name='insertTripChart'),
    path('ViewTripChart', views.ViewTripChart, name='ViewTripChart'),
    path('ViewBooking', views.ViewBooking, name='ViewBooking'),
    
    # API endpoints
    path('api/login/', api_views.api_login, name='api_login'),
    path('api/register/', api_views.api_register, name='api_register'),
    path('api/cars/', api_views.api_cars, name='api_cars'),
    path('api/book/', api_views.api_book_car, name='api_book_car'),
    path('api/bookings/', api_views.api_bookings, name='api_bookings'),
    path('api/complaint/', api_views.api_complaint, name='api_complaint'),
    path('api/search/', api_views.api_search_cars, name='api_search_cars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
