from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import SpirometryData
from .forms import SpirometryDataForm


# Create your views here.
def upload_spirometry_data(request):
    if request.method == 'POST':
        text_file = SpirometryDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-spirometry-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-spirometry-data.html', context)
    else:
        context = {'form': SpirometryDataForm()}  # Form instance without 'request'
        return render(request, 'upload-spirometry-data.html', context)


def list_spirometry_data(request):
    uploads = SpirometryData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-spirometry-data.html', context)

def download_spirometry_data(request, pk):
    uploaded_file = SpirometryData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_spirometry_data(request, pk):
    upload = get_object_or_404(SpirometryData, pk=pk)
    upload.delete()
    return redirect('list-spirometry-data')
    