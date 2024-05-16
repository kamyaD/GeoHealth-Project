from django.urls import path
from . import views

urlpatterns = [
    path('upload-chs-data/', views.upload_chs_data, name='upload-chs-data'),
    path('list-chs-data/', views.list_chs_data, name='list-chs-data'),
    path('download-chs-file/<int:pk>/', views.download_chs_data, name='download-chs-file'),
    path('delete-chs-file/<int:pk>', views.delete_chs_data, name="delete-chs-file"),
    
]