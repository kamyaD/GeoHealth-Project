from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import (
    DatabaseAgakhanData,DatabaseMamaLucyData,
    DatabaseMbagathiData,DatabaseMetropolitanData,
    DatabaseNairobiData,DatabaseMataData,
    DatabaseBamData,DatabaseCHSData,
    DatabaseSpirometryData,DatabaseQuontAQData,
    DatabasAirQoData,DatabaseEsmaplerData
)
from .forms import (
    DatabaseAgakhanDataForm,DatabaseMamaLucyDataForm,
    DatabaseMbagathiDataForm,DatabaseMetropolitanDataForm,
    DatabaseNairobiDataForm,DatabaseMataDataForm,
    DatabaseBamDataForm,DatabaseCHSDataForm,
    DatabaseSpirometryDataForm,DatabaseQuontAQDataForm,
    DatabasAirQoDataForm,DatabaseEsmaplerDataForm
)


# Agakhan Views.
def upload_database_agakhan_data(request):
    if request.method == 'POST':
        text_file = DatabaseAgakhanDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-agakhan-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-agakhan-data.html', context)
    else:
        context = {'form': DatabaseAgakhanDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-agakhan-data.html', context)


def list_database_agakhan_data(request):
    uploads = DatabaseAgakhanData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-agakhan-data.html', context)

def download_database_agakhan_data(request, pk):
    uploaded_file = DatabaseAgakhanData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_agakhan_data(request, pk):
    upload = get_object_or_404(DatabaseAgakhanData, pk=pk)
    upload.delete()
    return redirect('list-database-agakhan-data')



# Mamalucy views
def upload_database_mamalucy_data(request):
    if request.method == 'POST':
        text_file = DatabaseMamaLucyDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-mamalucy-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-mamalucy-data.html', context)
    else:
        context = {'form': DatabaseMamaLucyDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-mamalucy-data.html', context)


def list_database_mamalucy_data(request):
    uploads = DatabaseMamaLucyData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-mamalucy-data.html', context)

def download_database_mamalucy_data(request, pk):
    uploaded_file = DatabaseMamaLucyData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_mamalucy_data(request, pk):
    upload = get_object_or_404(DatabaseMamaLucyData, pk=pk)
    upload.delete()
    return redirect('list-database-mamalucy-data')


# Mbagathi views
def upload_database_mbagathi_data(request):
    if request.method == 'POST':
        text_file = DatabaseMbagathiDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-mbagathi-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-mbagathi-data.html', context)
    else:
        context = {'form': DatabaseMbagathiDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-mbagathi-data.html', context)


def list_database_mbagathi_data(request):
    uploads = DatabaseMbagathiData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-mbagathi-data.html', context)

def download_database_mbagathi_data(request, pk):
    uploaded_file = DatabaseMbagathiData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_mbagathi_data(request, pk):
    upload = get_object_or_404(DatabaseMbagathiData, pk=pk)
    upload.delete()
    return redirect('list-database-mbagathi-data')



# Metropolitan views
def upload_database_metropolitan_data(request):
    if request.method == 'POST':
        text_file = DatabaseMetropolitanDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-metropolitan-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-metropolitan-data.html', context)
    else:
        context = {'form': DatabaseMetropolitanDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-metropolitan-data.html', context)


def list_database_metropolitan_data(request):
    uploads = DatabaseMetropolitanData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-metropolitan-data.html', context)

def download_database_metropolitan_data(request, pk):
    uploaded_file = DatabaseMetropolitanData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_metropolitan_data(request, pk):
    upload = get_object_or_404(DatabaseMetropolitanData, pk=pk)
    upload.delete()
    return redirect('list-database-metropolitan-data')



# Nairobi views
def upload_database_nairobi_data(request):
    if request.method == 'POST':
        text_file = DatabaseNairobiDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-nairobi-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-nairobi-data.html', context)
    else:
        context = {'form': DatabaseNairobiDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-nairobi-data.html', context)


def list_database_nairobi_data(request):
    uploads = DatabaseNairobiData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-nairobi-data.html', context)

def download_database_nairobi_data(request, pk):
    uploaded_file = DatabaseNairobiData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_nairobi_data(request, pk):
    upload = get_object_or_404(DatabaseNairobiData, pk=pk)
    upload.delete()
    return redirect('list-database-nairobi-data')




# Mata views
def upload_database_mata_data(request):
    if request.method == 'POST':
        text_file = DatabaseMataDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-mata-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-mata-data.html', context)
    else:
        context = {'form': DatabaseMataDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-mata-data.html', context)


def list_database_mata_data(request):
    uploads = DatabaseMataData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-mata-data.html', context)

def download_database_mata_data(request, pk):
    uploaded_file = DatabaseMataData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_mata_data(request, pk):
    upload = get_object_or_404(DatabaseMataData, pk=pk)
    upload.delete()
    return redirect('list-database-mata-data')



# Bam views
def upload_database_bam_data(request):
    if request.method == 'POST':
        text_file = DatabaseBamDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-bam-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-bam-data.html', context)
    else:
        context = {'form': DatabaseBamDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-bam-data.html', context)


def list_database_bam_data(request):
    uploads = DatabaseBamData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-bam-data.html', context)

def download_database_bam_data(request, pk):
    uploaded_file = DatabaseBamData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_bam_data(request, pk):
    upload = get_object_or_404(DatabaseBamData, pk=pk)
    upload.delete()
    return redirect('list-database-bam-data')



# CHS views
def upload_database_chs_data(request):
    if request.method == 'POST':
        text_file = DatabaseCHSDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-chs-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-chs-data.html', context)
    else:
        context = {'form': DatabaseCHSDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-chs-data.html', context)


def list_database_chs_data(request):
    uploads = DatabaseCHSData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-chs-data.html', context)

def download_database_chs_data(request, pk):
    uploaded_file = DatabaseCHSData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_chs_data(request, pk):
    upload = get_object_or_404(DatabaseCHSData, pk=pk)
    upload.delete()
    return redirect('list-database-chs-data')



# Spirometry views
def upload_database_spirometry_data(request):
    if request.method == 'POST':
        text_file = DatabaseSpirometryDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-spirometry-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-spirometry-data.html', context)
    else:
        context = {'form': DatabaseSpirometryDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-spirometry-data.html', context)


def list_database_spirometry_data(request):
    uploads = DatabaseSpirometryData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-spirometry-data.html', context)

def download_database_spirometry_data(request, pk):
    uploaded_file = DatabaseSpirometryData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_spirometry_data(request, pk):
    upload = get_object_or_404(DatabaseSpirometryData, pk=pk)
    upload.delete()
    return redirect('list-database-spirometry-data')



# QuontAQ views
def upload_database_quontAQ_data(request):
    if request.method == 'POST':
        text_file = DatabaseQuontAQDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-quontAQ-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-quontAQ-data.html', context)
    else:
        context = {'form': DatabaseQuontAQDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-quontAQ-data.html', context)


def list_database_quontAQ_data(request):
    uploads = DatabaseQuontAQData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-quontAQ-data.html', context)

def download_database_quontAQ_data(request, pk):
    uploaded_file = DatabaseQuontAQData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_quontAQ_data(request, pk):
    upload = get_object_or_404(DatabaseQuontAQData, pk=pk)
    upload.delete()
    return redirect('list-database-quontAQ-data')


# AirQo views
def upload_database_airQo_data(request):
    if request.method == 'POST':
        text_file = DatabasAirQoDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-airQo-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-airQo-data.html', context)
    else:
        context = {'form': DatabasAirQoDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-airQo-data.html', context)


def list_database_airQo_data(request):
    uploads = DatabasAirQoData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-airQo-data.html', context)

def download_database_airQo_data(request, pk):
    uploaded_file = DatabasAirQoData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_airQo_data(request, pk):
    upload = get_object_or_404(DatabasAirQoData, pk=pk)
    upload.delete()
    return redirect('list-database-airQo-data')


# E-smarpler views
def upload_database_e_smapler_data(request):
    if request.method == 'POST':
        text_file = DatabasAirQoDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-database-e-smapler-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-database-e-smapler-data.html', context)
    else:
        context = {'form': DatabasAirQoDataForm()}  # Form instance without 'request'
        return render(request, 'upload-database-e-smapler-data.html', context)


def list_database_e_smapler_data(request):
    uploads = DatabasAirQoData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-database-e-smapler-data.html', context)

def download_database_e_smapler_data(request, pk):
    uploaded_file = DatabasAirQoData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_database_e_smapler_data(request, pk):
    upload = get_object_or_404(DatabasAirQoData, pk=pk)
    upload.delete()
    return redirect('list-database-e-smapler-data')



    