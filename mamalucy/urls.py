from django.urls import path
from . import views

urlpatterns = [
    path('upload-mamalucy-data/', views.upload_mamalucy_data, name='upload-mamalucy-data'),
    path('list-mamalucy-data/', views.list_mamalucy_data, name='list-mamalucy-data'),
    path('download-mamalucy-file/<int:pk>/', views.download_mamalucy_data, name='download-mamalucy-file'),
    path('delete-mamalucy-file/<int:pk>', views.delete_mamalucy_data, name="delete-mamalucy-file"),
    
]