from django.urls import path
from . import views


urlpatterns = [
    path('upload-published-papers-data/', views.upload_published_papers_data, name='upload-published-papers-data'),
    path('list-published-papers-data/', views.list_published_papers_data, name='list-published-papers-data'),
    path('download-published-papers-file/<int:pk>/', views.download_published_papers_data, name='download-published-papers-file'),
    path('delete-published-papers-file/<int:pk>', views.delete_published_papers_data, name="delete-published-papers-file"),  
]