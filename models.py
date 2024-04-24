from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    contact_info = models.CharField(max_length=100)
    employment_history = models.TextField()
    qualifications = models.TextField()
    certifications = models.TextField()

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Address(models.Model):
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employee.fname} {self.employee.lname} from {self.street_address}"

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)

class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Expired', 'Expired'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("End date cannot be before start date.")

    def save(self, *args, **kwargs):
        if self.end_date < timezone.now().date():
            self.status = 'Expired'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.fname} {self.employee.lname} {self.leave_type} {self.status}"

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    goals = models.TextField()
    feedback = models.TextField()

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.DecimalField(max_digits=10, decimal_places=2)
    grosspay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.grosspay = self.salary - self.deductions + self.benefits
        super(Payroll, self).save(*args, **kwargs)

class HRFunctionality(models.Model):
    # Add specific functionalities here
    pass

class ITAdministrator(models.Model):
    # Add specific functionalities here
    pass

class Audit(models.Model):
    # Add specific functionalities here
    pass

class ExecutiveDashboard(models.Model):
    # Add specific functionalities here
    pass