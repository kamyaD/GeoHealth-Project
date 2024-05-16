from django.urls import path
from . import views



urlpatterns = [
    path('upload-e-smarpler-data/', views.upload_e_smarpler_data, name='upload-e-smarpler-data'),
    path('list-e-smarpler-data/', views.list_e_smarpler_data, name='list-e-smarpler-data'),
    path('download-e-smarpler-file/<int:pk>/', views.download_e_smarpler_data, name='download-e-smarpler-file'),
    path('delete-e-smarpler-file/<int:pk>', views.delete_e_smarpler_data, name="delete-e-smarpler-file"),  
]