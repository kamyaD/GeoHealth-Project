from django.contrib import admin
from weekly_meetings.models import WeeklyMeetingsData

# Register your models here.
@admin.register(WeeklyMeetingsData)
class WeeklyMeetingsAdmin(admin.ModelAdmin):
    # model = WeeklyMeetingsData
    list_display = ("name", "file", "uploaded_at","updated_by")
