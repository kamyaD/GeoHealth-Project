from django.urls import path
from . import views

urlpatterns = [
    path('upload-metropolitan-data/', views.upload_metropolitan_data, name='upload-metropolitan-data'),
    path('list-metropolitan-data/', views.list_metropolitan_data, name='list-metropolitan-data'),
    path('download/<int:pk>/', views.download_metropolitan_data, name='download-metropolitan-file'),
    path('delete-metropolitan-file/<int:pk>', views.delete_metropolitan_data, name="delete-metropolitan-file"),
    
]