from django.urls import path
from . import views

urlpatterns = [
    path('upload-mbagathi-data/', views.upload_mbagathi_data, name='upload-mbagathi-data'),
    path('list-mbagathi-data/', views.list_mbagathi_data, name='list-mbagathi-data'),
    path('download/<int:pk>/', views.download_mbagathi_data, name='download-mama-lucy-file'),
    path('delete-mbagathi-file/<int:pk>', views.delete_mbagathi_data, name="delete-mbagathi-file"),
    
]