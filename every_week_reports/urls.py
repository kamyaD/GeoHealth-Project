from django.urls import path
from . import views

urlpatterns = [
    path('upload-every-week-reports-data/', views.upload_every_week_reports_data, name='upload-every-week-reports-data'),
    path('list-every-week-reports-data/', views.list_every_week_reports_data, name='list-every-week-reports-data'),
    path('download-every-week-reports-file/<int:pk>/', views.download_every_week_reports_data, name='download-every-week-reports-file'),
    path('delete-every-week-reports-file/<int:pk>', views.delete_every_week_reports_data, name="delete-every-week-reports-file"),  
]

