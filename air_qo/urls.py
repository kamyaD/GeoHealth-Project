from django.urls import path
from . import views

urlpatterns = [
    path('upload-air-qo-data/', views.upload_air_qo_data, name='upload-air-qo-data'),
    path('list-air-qo-data/', views.list_air_qo_data, name='list-air-qo-data'),
    path('download-air-qo-file/<int:pk>/', views.download_air_qo_data, name='download-air-qo-file'),
    path('delete-air-qo-file/<int:pk>', views.delete_air_qo_data, name="delete-air-qo-file"),
    
]