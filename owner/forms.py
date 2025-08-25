from django import forms
from .models import CarDetails, register, AddCustomer, AddDriver, CarBooking, Complaint
from .authentication import validate_password, validate_email, validate_mobile

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = CarDetails
        fields = ['photo']

class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")
    
    class Meta:
        model = register
        fields = ['Username', 'utype', 'mobileno', 'emailid', 'Password']
        widgets = {
            'Password': forms.PasswordInput(),
            'Username': forms.TextInput(attrs={'class': 'form-control'}),
            'utype': forms.Select(attrs={'class': 'form-control'}),
            'mobileno': forms.TextInput(attrs={'class': 'form-control'}),
            'emailid': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def clean_Password(self):
        password = self.cleaned_data.get('Password')
        is_valid, message = validate_password(password)
        if not is_valid:
            raise forms.ValidationError(message)
        return password
    
    def clean_emailid(self):
        email = self.cleaned_data.get('emailid')
        if not validate_email(email):
            raise forms.ValidationError("Please enter a valid email address")
        return email
    
    def clean_mobileno(self):
        mobile = self.cleaned_data.get('mobileno')
        if not validate_mobile(mobile):
            raise forms.ValidationError("Please enter a valid 10-digit mobile number")
        return mobile
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('Password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data

class CustomerForm(forms.ModelForm):
    class Meta:
        model = AddCustomer
        fields = ['cust_id', 'name', 'address', 'mobile_no', 'email_id', 'cust_type']
        widgets = {
            'cust_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'cust_type': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_mobile_no(self):
        mobile = self.cleaned_data.get('mobile_no')
        if not validate_mobile(mobile):
            raise forms.ValidationError("Please enter a valid 10-digit mobile number")
        return mobile

class DriverForm(forms.ModelForm):
    class Meta:
        model = AddDriver
        fields = ['driver_id', 'name', 'address', 'mobile_no', 'reference_given', 
                 'liscense_no', 'liscense_type', 'expire_date', 'aadhar_no']
        widgets = {
            'driver_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control'}),
            'reference_given': forms.TextInput(attrs={'class': 'form-control'}),
            'liscense_no': forms.TextInput(attrs={'class': 'form-control'}),
            'liscense_type': forms.Select(attrs={'class': 'form-control'}),
            'expire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'aadhar_no': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '12'}),
        }
    
    def clean_aadhar_no(self):
        aadhar = self.cleaned_data.get('aadhar_no')
        if len(aadhar) != 12 or not aadhar.isdigit():
            raise forms.ValidationError("Aadhar number must be exactly 12 digits")
        return aadhar

class CarDetailsForm(forms.ModelForm):
    class Meta:
        model = CarDetails
        fields = ['car_id', 'company', 'rent', 'make', 'reg_no', 'fuel_type', 'capacity', 'photo']
        widgets = {
            'car_id': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_no': forms.TextInput(attrs={'class': 'form-control'}),
            'fuel_type': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['cust_id', 'trip_id', 'complaint_type', 'details', 'date', 'status']
        widgets = {
            'cust_id': forms.TextInput(attrs={'class': 'form-control'}),
            'trip_id': forms.TextInput(attrs={'class': 'form-control'}),
            'complaint_type': forms.Select(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }