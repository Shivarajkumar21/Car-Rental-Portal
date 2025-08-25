from django.db import models
class login(models.Model):
    Username=models.CharField(max_length=200,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    utype=models.CharField(max_length=50,null=True,blank=True)

class register(models.Model):
    Username=models.CharField(max_length=200,null=True,blank=True)
    utype = models.CharField(max_length=50, null=True, blank=True)
    mobileno = models.CharField(max_length=20, null=True, blank=True)
    emailid = models.EmailField(max_length=500, null=True, blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)

class Booking(models.Model):
    City_Airport_Station_etc=models.CharField(max_length=200,null=True,blank=True)
    City_Airport_Station=models.CharField(max_length=200,null=True,blank=True)
    book_pick_date=models.CharField(max_length=200,null=True,blank=True)
    book_off_date=models.DateField(null=True,blank=True)
    Time=models.TimeField(null=True,blank=True)

class CarBooking(models.Model):
    booking_id=models.CharField(max_length=200,null=True,blank=True)
    cust_id=models.CharField(max_length=200,null=True,blank=True)
    car_id=models.CharField(max_length=200,null=True,blank=True)
    booking_date=models.DateField(null=True,blank=True)
    reg_date=models.DateField(null=True,blank=True)
    to_place=models.CharField(max_length=200,null=True,blank=True)
    no_of_days=models.CharField(max_length=150,null=True,blank=True)
    rent_id=models.CharField(max_length=20,null=True,blank=True)
    status=models.CharField(max_length=200,null=True,blank=True)

class CarDetails(models.Model):
    car_id=models.CharField(max_length=250,null=True,blank=True)
    company=models.CharField(max_length=200,null=True,blank=True)
    rent=models.CharField(max_length=200,null=True,blank=True)
    make=models.CharField(max_length=200,null=True,blank=True)
    reg_no=models.CharField(max_length=200,null=True,blank=True)
    fuel_type=models.CharField(max_length=150,null=True,blank=True)
    capacity=models.CharField(max_length=100,null=True,blank=True)
    photo=models.ImageField(upload_to='owner/static/images/', blank=True, verbose_name="Afbeelding")




class Complaint(models.Model):
    cust_id=models.CharField(max_length=20,null=True,blank=True)
    trip_id=models.CharField(max_length=20,null=True,blank=True)
    complaint_type=models.CharField(max_length=200,null=True,blank=True)
    details=models.CharField(max_length=200,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=200,null=True,blank=True)

class AddCustomer(models.Model):
    cust_id=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    mobile_no=models.CharField(max_length=20,null=True,blank=True)
    email_id=models.EmailField(max_length=500,null=True,blank=True)
    cust_type=models.CharField(max_length=100,null=True,blank=True)

class AddDriver(models.Model):
    driver_id=models.CharField(max_length=20,null=True,blank=True)
    name=models.CharField(max_length=150,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    mobile_no=models.CharField(max_length=20,null=True,blank=True)
    reference_given=models.CharField(max_length=200,null=True,blank=True)
    liscense_no=models.CharField(max_length=150,null=True,blank=True)
    liscense_type=models.CharField(max_length=200,null=True,blank=True)
    expire_date=models.DateField(null=True,blank=True)
    aadhar_no=models.CharField(max_length=12,null=True,blank=True)



class RentDetails(models.Model):
    rent_id=models.CharField(max_length=20,null=True,blank=True)
    car_id=models.CharField(max_length=20,null=True,blank=True)
    rateper_km=models.CharField(max_length=100,null=True,blank=True)
    driver_charges=models.CharField(max_length=200,null=True,blank=True)

class TripChart(models.Model):
    booking_id=models.CharField(max_length=20,null=True,blank=True)
    cust_id=models.CharField(max_length=20,null=True,blank=True)
    driver_name=models.CharField(max_length=70,null=True,blank=True)
    start_date=models.DateField(null=True,blank=True)
    start_km=models.CharField(max_length=200,null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    end_km=models.CharField(max_length=200,null=True,blank=True)
    total_kms=models.CharField(max_length=200,null=True,blank=True)
    total_days=models.CharField(max_length=100,null=True,blank=True)

