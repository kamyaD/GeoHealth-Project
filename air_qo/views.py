from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AirQoData
from .forms import AirQoDataForm


# Create your views here.
def upload_air_qo_data(request):
    if request.method == 'POST':
        text_file = AirQoDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-air-qo-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-air-qo-data.html', context)
    else:
        context = {'form': AirQoDataForm()}  # Form instance without 'request'
        return render(request, 'upload-air-qo-data.html', context)


def list_air_qo_data(request):
    uploads = AirQoData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-air-qo-data.html', context)

def download_air_qo_data(request, pk):
    uploaded_file = AirQoData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_air_qo_data(request, pk):
    upload = get_object_or_404(AirQoData, pk=pk)
    upload.delete()
    return redirect('list-air-qo-data')
    