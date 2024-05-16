from django.urls import path
from . import views

urlpatterns = [
    path('upload-proposals-data/', views.upload_proposals_data, name='upload-proposals-data'),
    path('list-proposals-data/', views.list_proposals_data, name='list-proposals-data'),
    path('download-proposals-file/<int:pk>/', views.download_proposals_data, name='download-proposals-file'),
    path('delete-proposals-file/<int:pk>', views.delete_proposals_data, name="delete-proposals-file"),  
]

