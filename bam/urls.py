from django.urls import path
from . import views

urlpatterns = [
    path('upload-bam-data/', views.upload_bam_data, name='upload-bam-data'),
    path('list-bam-data/', views.list_bam_data, name='list-bam-data'),
    path('download-bam-file/<int:pk>/', views.download_bam_data, name='download-bam-file'),
    path('delete-bam-file/<int:pk>', views.delete_bam_data, name="delete-bam-file"),  
]