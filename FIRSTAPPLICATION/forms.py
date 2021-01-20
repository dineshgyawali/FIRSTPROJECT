from django import forms
from .models import Customer, Staff, Support

class AttendanceForm(forms.Form):
    Name = forms.CharField(label="Participant's Name", max_length=20)
    Attendance = forms.CharField(label="Present/Absent", max_length=3)
    Email = forms.EmailField(label="Email",max_length=20)

class Customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class Staff_form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

class Support_form(forms.ModelForm):
    class Meta:
        model = Support
        fields = "__all__"