from django.urls import path
from . import views

urlpatterns = [
    path('upload-analysis-reports-data/', views.upload_analysis_reports_data, name='upload-analysis-reports-data'),
    path('list-analysis-reports-data/', views.list_analysis_reports_data, name='list-analysis-reports-data'),
    path('download-analysis-reports-file/<int:pk>/', views.download_analysis_reports_data, name='download-analysis-reports-file'),
    path('delete-analysis-reports-file/<int:pk>', views.delete_analysis_reports_data, name="delete-analysis-reports-file"),  
]

