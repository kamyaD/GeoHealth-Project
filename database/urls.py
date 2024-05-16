from django.urls import path
from . import views

urlpatterns = [
    #Agakhan URLs
    path('upload-database-agakhan-data/', views.upload_database_agakhan_data, name='upload-database-agakhan-data'),
    path('list-database-agakhan-data/', views.list_database_agakhan_data, name='list-database-agakhan-data'),
    path('download-database-agakhan-file/<int:pk>/', views.download_database_agakhan_data, name='download-database-agakhan-file'),
    path('delete-database-agakhan-file/<int:pk>', views.delete_database_agakhan_data, name="delete-database-agakhan-file"),  
    
    #Mamalucy URLs
    path('upload-database-mamalucy-data/', views.upload_database_mamalucy_data, name='upload-database-mamalucy-data'),
    path('list-database-mamalucy-data/', views.list_database_mamalucy_data, name='list-database-mamalucy-data'),
    path('download-database-mamalucy-file/<int:pk>/', views.download_database_mamalucy_data, name='download-database-mamalucy-file'),
    path('delete-database-mamalucy-file/<int:pk>', views.delete_database_mamalucy_data, name="delete-database-mamalucy-file"), 

    #Mbagathi URLs
    path('upload-database-mbagathi-data/', views.upload_database_mbagathi_data, name='upload-database-mbagathi-data'),
    path('list-database-mbagathi-data/', views.list_database_mbagathi_data, name='list-database-mbagathi-data'),
    path('download-database-mbagathi-file/<int:pk>/', views.download_database_mbagathi_data, name='download-database-mbagathi-file'),
    path('delete-database-mbagathi-file/<int:pk>', views.delete_database_mbagathi_data, name="delete-database-mbagathi-file"),

    #Metropolitan URLs
    path('upload-database-metropolitan-data/', views.upload_database_metropolitan_data, name='upload-database-metropolitan-data'),
    path('list-database-metropolitan-data/', views.list_database_metropolitan_data, name='list-database-metropolitan-data'),
    path('download-database-metropolitan-file/<int:pk>/', views.download_database_metropolitan_data, name='download-database-metropolitan-file'),
    path('delete-database-metropolitan-file/<int:pk>', views.delete_database_metropolitan_data, name="delete-database-metropolitan-file"),

    #Nairobi URLs
    path('upload-database-nairobi-data/', views.upload_database_nairobi_data, name='upload-database-nairobi-data'),
    path('list-database-nairobi-data/', views.list_database_nairobi_data, name='list-database-nairobi-data'),
    path('download-database-nairobi-file/<int:pk>/', views.download_database_nairobi_data, name='download-database-nairobi-file'),
    path('delete-database-nairobi-file/<int:pk>', views.delete_database_nairobi_data, name="delete-database-nairobi-file"),

    #Mata URLs
    path('upload-database-mata-data/', views.upload_database_mata_data, name='upload-database-mata-data'),
    path('list-database-mata-data/', views.list_database_mata_data, name='list-database-mata-data'),
    path('download-database-mata-file/<int:pk>/', views.download_database_mata_data, name='download-database-mata-file'),
    path('delete-database-mata-file/<int:pk>', views.delete_database_mata_data, name="delete-database-mata-file"),

    #Bam URLs
    path('upload-database-bam-data/', views.upload_database_bam_data, name='upload-database-bam-data'),
    path('list-database-bam-data/', views.list_database_bam_data, name='list-database-bam-data'),
    path('download-database-bam-file/<int:pk>/', views.download_database_bam_data, name='download-database-bam-file'),
    path('delete-database-bam-file/<int:pk>', views.delete_database_bam_data, name="delete-database-bam-file"),

    #CHS URLs
    path('upload-database-chs-data/', views.upload_database_chs_data, name='upload-database-chs-data'),
    path('list-database-chs-data/', views.list_database_chs_data, name='list-database-chs-data'),
    path('download-database-chs-file/<int:pk>/', views.download_database_chs_data, name='download-database-chs-file'),
    path('delete-database-chs-file/<int:pk>', views.delete_database_chs_data, name="delete-database-chs-file"),

    #spirometry URLs
    path('upload-database-spirometry-data/', views.upload_database_spirometry_data, name='upload-database-spirometry-data'),
    path('list-database-spirometry-data/', views.list_database_spirometry_data, name='list-database-spirometry-data'),
    path('download-database-spirometry-file/<int:pk>/', views.download_database_spirometry_data, name='download-database-spirometry-file'),
    path('delete-database-spirometry-file/<int:pk>', views.delete_database_spirometry_data, name="delete-database-spirometry-file"),

    #QuontaAQ URLs
    path('upload-database-quontAQ-data/', views.upload_database_quontAQ_data, name='upload-database-quontAQ-data'),
    path('list-database-quontAQ-data/', views.list_database_quontAQ_data, name='list-database-quontAQ-data'),
    path('download-database-quontAQ-file/<int:pk>/', views.download_database_quontAQ_data, name='download-database-quontAQ-file'),
    path('delete-database-quontAQ-file/<int:pk>', views.delete_database_quontAQ_data, name="delete-database-quontAQ-file"),

    #AirQo URLs
    path('upload-database-airQo-data/', views.upload_database_airQo_data, name='upload-database-airQo-data'),
    path('list-database-airQo-data/', views.list_database_airQo_data, name='list-database-airQo-data'),
    path('download-database-airQo-file/<int:pk>/', views.download_database_airQo_data, name='download-database-airQo-file'),
    path('delete-database-airQo-file/<int:pk>', views.delete_database_airQo_data, name="delete-database-airQo-file"),

    #E-smarpler URLs
    path('upload-database-e-smapler-data/', views.upload_database_e_smapler_data, name='upload-database-e-smapler-data'),
    path('list-database-e-smapler-data/', views.list_database_e_smapler_data, name='list-database-e-smapler-data'),
    path('download-database-e-smapler-file/<int:pk>/', views.download_database_e_smapler_data, name='download-database-e-smapler-file'),
    path('delete-database-e-smapler-file/<int:pk>', views.delete_database_e_smapler_data, name="delete-database-e-smapler-file"),

]
