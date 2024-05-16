from django.urls import path
from . import views

urlpatterns = [
    path('upload-datasharing-data/', views.upload_datasharing_data, name='upload-datasharing-data'),
    path('list-datasharing-data/', views.list_datasharing_data, name='list-datasharing-data'),
    path('download-datasharing-file/<int:pk>/', views.download_datasharing_data, name='download-datasharing-file'),
    path('delete-datasharing-file/<int:pk>', views.delete_datasharing_data, name="delete-datasharing-file"),  
]

