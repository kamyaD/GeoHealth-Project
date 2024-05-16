from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MataData
from .forms import MataDataForm


# Create your views here.
def upload_mata_data(request):
    if request.method == 'POST':
        text_file = MataDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-mata-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-mata-data.html', context)
    else:
        context = {'form': MataDataForm()}  # Form instance without 'request'
        return render(request, 'upload-mata-data.html', context)


def list_mata_data(request):
    uploads = MataData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-mata-data.html', context)

def download_mata_data(request, pk):
    uploaded_file = MataData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_mata_data(request, pk):
    upload = get_object_or_404(MataData, pk=pk)
    upload.delete()
    return redirect('list-mata-data')
    