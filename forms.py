from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import LeaveRequest

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['leave_type', 'start_date', 'end_date']
        widgets = {
            'leave_type': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Leave Type'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Start Date', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'End Date', 'type': 'date'}),
        }