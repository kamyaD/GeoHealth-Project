from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('upload-agakhan-data/', views.upload_agakhan_data, name='upload-agakhan-data'),
    path('list-agakhan-data/', views.list_agakhan_data, name='list-agakhan-data'),
    path('download/<int:pk>/', views.download_agakhan_data, name='download_file'),
    path('delete-agakhan-file/<int:pk>', views.delete_agakhan_data, name="delete-agakhan-file"),  
]
