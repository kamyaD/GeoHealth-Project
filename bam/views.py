from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BamData
from .forms import BamDataForm


# Create your views here.
def upload_bam_data(request):
    if request.method == 'POST':
        text_file = BamDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-bam-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-bam-data.html', context)
    else:
        context = {'form': BamDataForm()}  # Form instance without 'request'
        return render(request, 'upload-bam-data.html', context)


def list_bam_data(request):
    uploads = BamData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-bam-data.html', context)

def download_bam_data(request, pk):
    uploaded_file = BamData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_bam_data(request, pk):
    upload = get_object_or_404(BamData, pk=pk)
    upload.delete()
    return redirect('list-bam-data')
    