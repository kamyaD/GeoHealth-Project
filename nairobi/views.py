from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import NairobiData
from .forms import NairobiDataForm


# Create your views here.
def upload_nairobi_data(request):
    if request.method == 'POST':
        text_file = NairobiDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-nairobi-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-nairobi-data.html', context)
    else:
        context = {'form': NairobiDataForm()}  # Form instance without 'request'
        return render(request, 'upload-nairobi-data.html', context)


def list_nairobi_data(request):
    uploads = NairobiData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-nairobi-data.html', context)

def download_nairobi_data(request, pk):
    uploaded_file = NairobiData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_nairobi_data(request, pk):
    upload = get_object_or_404(NairobiData, pk=pk)
    upload.delete()
    return redirect('list-nairobi-data')
    