from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import CHSData
from .forms import CHSDataForm


# Create your views here.
def upload_chs_data(request):
    if request.method == 'POST':
        text_file = CHSDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-chs-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-chs-data.html', context)
    else:
        context = {'form': CHSDataForm()}  # Form instance without 'request'
        return render(request, 'upload-chs-data.html', context)


def list_chs_data(request):
    uploads = CHSData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-chs-data.html', context)

def download_chs_data(request, pk):
    uploaded_file = CHSData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_chs_data(request, pk):
    upload = get_object_or_404(CHSData, pk=pk)
    upload.delete()
    return redirect('list-chs-data')
    