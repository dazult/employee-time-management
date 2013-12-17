from django.contrib import admin
from employee_time_management.models import Department, JobRole, EmployeeProfile, Timesheet, AnnualLeave, SickLeave

admin.site.register(Department)
admin.site.register(JobRole)
admin.site.register(EmployeeProfile)
admin.site.register(Timesheet)
admin.site.register(AnnualLeave)
admin.site.register(SickLeave)
