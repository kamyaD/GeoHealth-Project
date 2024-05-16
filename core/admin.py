from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# from core.models import AgakhanData
from accounts.admin import AccountsDataAdmin
from accounts.models import AccountsData
from weekly_meetings.admin import WeeklyMeetingsAdmin
from weekly_meetings.models import WeeklyMeetingsData
from weekly_progress_reports.admin import WeeklyProgressReportsAdmin
from weekly_progress_reports.models import WeeklyProgressReportsData




class MyAdminSite(AdminSite):
    site_header = 'GeoHealth Data Management System'
    site_title = 'Data Management System Admin Portal'
    index_title = 'Welcome to Administrator Portal'

# Custom User Admin class
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')



admin_site = MyAdminSite()
admin_site.register(User, CustomUserAdmin)
admin_site.register(AccountsData, AccountsDataAdmin)
admin_site.register(WeeklyMeetingsData, WeeklyMeetingsAdmin)
admin_site.register(WeeklyProgressReportsData, WeeklyProgressReportsAdmin)
