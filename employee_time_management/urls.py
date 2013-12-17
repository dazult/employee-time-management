from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'employee_time_management.views.index'),
	url(r'^timesheet_success/(?P<in_or_out>\w+)/$', 'employee_time_management.views.timesheet_success'),
	url(r'^vacation_pending/$', 'employee_time_management.views.vacation_pending'),
	url(r'^sick_leave/$', 'employee_time_management.views.sick_leave'),
	url(r'^mgnt_clocking/$', 'employee_time_management.views.mgnt_clocking'),
	url(r'^holiday_request/(?P<action>\w+)/(?P<holiday_request_id>\w+)/$', 'employee_time_management.views.holiday_request_action'),
	url(r'^mgnt/$', 'employee_time_management.views.login'),   		
	url(r'^auth_view/$', 'employee_time_management.views.auth_view'),  
	url(r'^logout/$', 'employee_time_management.views.logout'),
	url(r'^loggedin/$', 'employee_time_management.views.loggedin'),
	url(r'^invalid_login/$', 'employee_time_management.views.invalid_login'),
)
