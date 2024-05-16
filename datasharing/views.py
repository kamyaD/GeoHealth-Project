from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DataSharingData
from .forms import DataSharingDataForm


# Create your views here.
def upload_datasharing_data(request):
    if request.method == 'POST':
        text_file = DataSharingDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-datasharing-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-datasharing-data.html', context)
    else:
        context = {'form': DataSharingDataForm()}  # Form instance without 'request'
        return render(request, 'upload-datasharing-data.html', context)


def list_datasharing_data(request):
    uploads = DataSharingData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-datasharing-data.html', context)

def download_datasharing_data(request, pk):
    uploaded_file = DataSharingData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_datasharing_data(request, pk):
    upload = get_object_or_404(DataSharingData, pk=pk)
    upload.delete()
    return redirect('list-datasharing-data')
    