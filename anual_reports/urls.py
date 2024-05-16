from django.urls import path
from . import views

urlpatterns = [
    path('upload-anual-reports-data/', views.upload_anual_reports_data, name='upload-anual-reports-data'),
    path('list-anual-reports-data/', views.list_anual_reports_data, name='list-anual-reports-data'),
    path('download-anual-reports-file/<int:pk>/', views.download_anual_reports_data, name='download-anual-reports-file'),
    path('delete-anual-reports-file/<int:pk>', views.delete_anual_reports_data, name="delete-anual-reports-file"),  
]

