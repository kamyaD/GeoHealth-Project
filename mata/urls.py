from django.urls import path
from . import views

urlpatterns = [
    path('upload-mata-data/', views.upload_mata_data, name='upload-mata-data'),
    path('list-mata-data/', views.list_mata_data, name='list-mata-data'),
    path('download-mata-file/<int:pk>/', views.download_mata_data, name='download-mata-file'),
    path('delete-mata-file/<int:pk>', views.delete_mata_data, name="delete-mata-file"), 
]