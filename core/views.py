from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AgakhanData
from .forms import AgakhanDataForm

# Create your views here.
def about(request):
    return render(request,'about.html')


def upload_agakhan_data(request):
    if request.method == 'POST':
        text_file = AgakhanDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-agakhan-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-agakhan-data.html', context)
    else:
        context = {'form': AgakhanDataForm()}  # Form instance without 'request'
        return render(request, 'upload-agakhan-data.html', context)


def list_agakhan_data(request):
    uploads = AgakhanData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-agakhan-data.html', context)

def download_agakhan_data(request, pk):
    uploaded_file = AgakhanData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_agakhan_data(request, pk):
    upload = get_object_or_404(AgakhanData, pk=pk)
    upload.delete()
    return redirect('list-agakhan-data')
    