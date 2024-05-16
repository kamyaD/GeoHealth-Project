from django.contrib import admin
from weekly_progress_reports.models import WeeklyProgressReportsData

# Register your models here.
@admin.register(WeeklyProgressReportsData)
class WeeklyProgressReportsAdmin(admin.ModelAdmin):
    model = WeeklyProgressReportsData
    list_display = ("name", "file", "uploaded_at","updated_by")
