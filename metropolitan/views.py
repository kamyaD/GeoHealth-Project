from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MetropolitanData
from .forms import MetropolitanDataForm


# Create your views here.
def upload_metropolitan_data(request):
    if request.method == 'POST':
        text_file = MetropolitanDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-metropolitan-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-metropolitan-data.html', context)
    else:
        context = {'form': MetropolitanDataForm()}  # Form instance without 'request'
        return render(request, 'upload-metropolitan-data.html', context)


def list_metropolitan_data(request):
    uploads = MetropolitanData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-metropolitan-data.html', context)

def download_metropolitan_data(request, pk):
    uploaded_file = MetropolitanData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_metropolitan_data(request, pk):
    upload = get_object_or_404(MetropolitanData, pk=pk)
    upload.delete()
    return redirect('list-metropolitan-data')
    