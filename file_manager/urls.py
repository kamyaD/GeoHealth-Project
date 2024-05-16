"""
URL configuration for file_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.admin import admin_site 

urlpatterns = [
    path("admin/", admin_site.urls),
    path('', include('core.urls')),
    path('', include('mamalucy.urls')),
    path('', include('mbagathi.urls')),
    path('', include('metropolitan.urls')),
    path('', include('nairobi.urls')),
    path('', include('mata.urls')),
    path('', include('bam.urls')),
    path('', include('chs.urls')),
    path('', include('spirometry.urls')),
    path('', include('quanta_aq.urls')),
    path('', include('air_qo.urls')),
    path('', include('e_smarpler.urls')),
    path('', include('database.urls')),
    path('', include('draft_papers.urls')),
    path('', include('published_papers.urls')),
    path('', include('proposals.urls')),
    path('', include('analysis_reports.urls')),
    path('', include('anual_reports.urls')),
    path('', include('cycle_reports.urls')),
    path('', include('datasharing.urls')),
    path('', include('every_week_reports.urls')),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=[settings.MEDIA_ROOT])
