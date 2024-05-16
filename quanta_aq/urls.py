from django.urls import path
from . import views

urlpatterns = [
    path('upload-quanta-aq-data/', views.upload_quanta_aq_data, name='upload-quanta-aq-data'),
    path('list-quanta-aq-data/', views.list_quanta_aq_data, name='list-quanta-aq-data'),
    path('download-quanta-aq-file/<int:pk>/', views.download_quanta_aq_data, name='download-quanta-aq-file'),
    path('delete-quanta-aq-file/<int:pk>', views.delete_quanta_aq_data, name="delete-quanta-aq-file"),  
]

