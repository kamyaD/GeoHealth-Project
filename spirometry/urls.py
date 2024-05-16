from django.urls import path
from . import views

urlpatterns = [
    path('upload-spirometry-data/', views.upload_spirometry_data, name='upload-spirometry-data'),
    path('list-spirometry-data/', views.list_spirometry_data, name='list-spirometry-data'),
    path('download-spirometry-file/<int:pk>/', views.download_spirometry_data, name='download-spirometry-file'),
    path('delete-spirometry-file/<int:pk>', views.delete_spirometry_data, name="delete-spirometry-file"), 
]