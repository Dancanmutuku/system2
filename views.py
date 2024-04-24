from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from human.forms import LeaveRequestForm
from human.models import *

@login_required
def index(request):
    # Get the logged-in user
    logged_in_user = request.user
    # Assuming your User model has a OneToOneField to Employee model
    try:
        employee = logged_in_user.employee
    except Employee.DoesNotExist:
        employee = None
    # Fetch payroll data for the logged-in employee if available
    if employee:
        payroll = Payroll.objects.filter(employee=employee).first()
        leave_request = LeaveRequest.objects.filter(employee=employee).first()
        address = Address.objects.filter(employee=employee).first()
    else:
        payroll = None
        leave_request = None
        address = None
    # Pass the employee and payroll data to the template context
    context = {
        'leave_request' : leave_request,
        'employee': employee,
        'payroll': payroll,
        'address': address
    }
    return render(request, "pages/index.html", context)
@login_required
def leave(request):
    # Get the logged-in user
    logged_in_user = request.user

    # Assuming your User model has a OneToOneField to Employee model
    try:
        employee = logged_in_user.employee
    except Employee.DoesNotExist:
        employee = None

    # Fetch payroll data for the logged-in employee if available
    if employee:
        payroll = Payroll.objects.filter(employee=employee).first()
        leave_request = LeaveRequest.objects.filter(employee=employee).first()
        address = Address.objects.filter(employee=employee).first()

        # Initialize the form with instance if leave_request exists, else with None
        form = LeaveRequestForm(instance=leave_request)

        # Check if the form is submitted
        if request.method == 'POST':
            form = LeaveRequestForm(request.POST, instance=leave_request)
            if form.is_valid():
                leave_request = form.save(commit=False)
                leave_request.employee = employee
                leave_request.save()
                return redirect('leave')  # Redirect to the same view after form submission

    else:
        payroll = None
        leave_request = None
        address = None
        form = None

    context = {
        'leave_request': leave_request,
        'employee': employee,
        'payroll': payroll,
        'address': address,
        'form': form,  # Include the form in the context
    }
    return render(request, "pages/leave.html", context)
def custom_logout(request):
    logout(request)
    # Redirect to a different page after logout
    return redirect('login') 