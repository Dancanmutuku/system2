from django.contrib import admin
from human.models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(AttendanceRecord)
admin.site.register(LeaveRequest)
admin.site.register(Payroll)
admin.site.register(Address)