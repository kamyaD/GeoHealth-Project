from django.urls import path
from . import views

urlpatterns = [
    path('upload-cycle-reports-data/', views.upload_cylce_reports_data, name='upload-cycle-reports-data'),
    path('list-cycle-reports-data/', views.list_cylce_reports_data, name='list-cycle-reports-data'),
    path('download-cylce-reports-file/<int:pk>/', views.download_cylce_reports_data, name='download-cylce-reports-file'),
    path('delete-cylce-reports-file/<int:pk>', views.delete_cylce_reports_data, name="delete-cylce-reports-file"),  
]

