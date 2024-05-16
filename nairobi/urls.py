from django.urls import path
from . import views

urlpatterns = [
    path('upload-nairobi-data/', views.upload_nairobi_data, name='upload-nairobi-data'),
    path('list-nairobi-data/', views.list_nairobi_data, name='list-nairobi-data'),
    path('download-nairobi-file/<int:pk>/', views.download_nairobi_data, name='download-nairobi-file'),
    path('delete-nairobi-file/<int:pk>', views.delete_nairobi_data, name="delete-nairobi-file"),
    
]