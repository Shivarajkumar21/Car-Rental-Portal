from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
from owner.models import AddCustomer,AddDriver,CarBooking,CarDetails,login,Complaint,RentDetails,TripChart,register,Booking
# Create your views here.

def cars(request):
    return render(request,'car.html')


def agent(request):
    return render(request,'agent_home.html')

def customer(request):
    return render(request,'customer_home.html')

def logcheck(request):
    if request.method == "POST":
        username = request.POST.get('t1', '')
        request.session['username']=username
        password = request.POST.get('t2', '')

        checklogin = register.objects.filter(Username=username).values()
        for a in checklogin:
            utype = a['utype']
            print(" u",utype)
            upass= a['Password']
            if(upass == password):
                if (utype == "agent"):
                    return render(request, 'agent_home.html', context={'msg': 'welcome to Organizer'})
                if (utype == "customer"):
                    return render(request, 'customer_home.html', context={'msg': 'welcome to Customer'})
            else:
                return render(request,'login.html')
                messages.error(request,'Username or Password is Incorrect')

    return render(request,'login.html')

def signup(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        register.objects.create(Username=s1,utype=s2,mobileno=s3,emailid=s4,Password=s5)
        return render(request, "register.html")
    return render(request, "register.html")

def Viewregister(request):
    userdict=register.objects.all()
    return render(request, "viewregister.html",{"user_dict":userdict})

def Viewlogin(request):
    userdict=login.objects.all()
    return render(request, "viewlogin.html",{"user_dict":userdict})

def insertAddCustomer(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")

        AddCustomer.objects.create(cust_id = s1, name = s2, address = s3, mobile_no = s4, email_id = s5, cust_type = s6)
        return render(request, "AddCustomer.html")

    return render(request, "AddCustomer.html")


def ViewAddCustomer(request):
    userdict=AddCustomer.objects.all()
    return render(request, "Viewcustomer.html",{"user_dict":userdict})


def insertAddDriver(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        AddDriver.objects.create(driver_id=s1, name=s2, address=s3, mobile_no = s4, reference_given = s5,liscense_no = s6,liscense_type = s7, expire_date = s8, aadhar_no = s9)
        return render(request, "AddDriver.html")

    return render(request, "AddDriver.html")


def ViewAddDriver(request):
    userdict=AddDriver.objects.all()
    return render(request, "Viewdriver.html",{"user_dict":userdict})


def insertCarBooking(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        CarBooking.objects.create(booking_id = s1, cust_id = s2, car_id = s3, booking_date = s4,reg_date = s5, to_place = s6, no_of_days = s7, rent_id = s8, status = s9)
        return render(request, "CarBooking.html")

    return render(request, "CarBooking.html")


def ViewCarBooking(request):
    userdict=CarBooking.objects.all()
    return render(request, "Viewcarbooking.html",{"user_dict":userdict})

def index(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        Booking.objects.create(City_Airport_Station_etc = s1, City_Airport_Station = s2, book_pick_date = s3, book_off_date = s4,Time = s5)
        return render(request, "index.html")

    return render(request, "index.html")


def ViewBooking(request):
    userdict=Booking.objects.all()
    return render(request, "Viewbooking.html",{"user_dict":userdict})


def insertCarDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")

        CarDetails.objects.create(car_id = s1, company = s2, rent = s3, make = s4,reg_no= s5, fuel_type = s6, capacity = s7, photo = s8)
        return render(request, "CarDetails.html")

    return render(request, "CarDetails.html")


def ViewCarDetails(request):
    userdict=CarDetails.objects.all()
    return render(request, "Viewcardetails.html",{"user_dict":userdict})


def insertComplaint(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")

        Complaint.objects.create(cust_id = s1, trip_id = s2, complaint_type = s3, details = s4, date = s5, status = s6)
        return render(request, "Complaint.html")

    return render(request, "Complaint.html")


def ViewComplaint(request):
    userdict=Complaint.objects.all()
    return render(request, "ViewComplaint.html",{"user_dict":userdict})


def insertRentDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")

        RentDetails.objects.create(rent_id=s1, car_id=s2, rateper_km=s3, driver_charges=s4)
        return render(request, "RentDetails.html")

    return render(request, "RentDetails.html")


def ViewRentDetails(request):
    userdict=RentDetails.objects.all()
    return render(request, "Viewrentdetails.html",{"user_dict":userdict})


def insertTripChart(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        TripChart.objects.create(booking_id=s1, cust_id=s2, driver_name=s3, start_date=s4, start_km=s5, end_date=s6,end_km=s7, total_kms=s8, total_days=s9)
        return render(request, "TripChart.html")

    return render(request, "TripChart.html")


def ViewTripChart(request):
    userdict=TripChart.objects.all()
    return render(request, "Viewtripchart.html",{"user_dict":userdict})








