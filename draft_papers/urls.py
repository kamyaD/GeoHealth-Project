from django.urls import path
from . import views

urlpatterns = [
    path('upload-draft-papers-data/', views.upload_draft_papers_data, name='upload-draft-papers-data'),
    path('list-draft-papers-data/', views.list_draft_papers_data, name='list-draft-papers-data'),
    path('download-draft-papers-file/<int:pk>/', views.download_draft_papers_data, name='download-draft-papers-file'),
    path('delete-draft-papers-file/<int:pk>', views.delete_draft_papers_data, name="delete-draft-papers-file"),  
]
