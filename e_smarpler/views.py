from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import EsmarplerData
from .forms import EsmarplerDataForm


# Create your views here.
def upload_e_smarpler_data(request):
    if request.method == 'POST':
        text_file = EsmarplerDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-e-smarpler-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-e-smarpler-data.html', context)
    else:
        context = {'form': EsmarplerDataForm()}  # Form instance without 'request'
        return render(request, 'upload-e-smarpler-data.html', context)


def list_e_smarpler_data(request):
    uploads = EsmarplerData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-e-smarpler-data.html', context)

def download_e_smarpler_data(request, pk):
    uploaded_file = EsmarplerData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_e_smarpler_data(request, pk):
    upload = get_object_or_404(EsmarplerData, pk=pk)
    upload.delete()
    return redirect('list-e-smarpler-data')
    