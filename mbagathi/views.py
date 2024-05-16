from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MbagathiData
from .forms import MbagathiDataForm

# Create your views here.
def about(request):
    return render(request,'about.html')


def upload_mbagathi_data(request):
    if request.method == 'POST':
        text_file = MbagathiDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-mbagathi-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-mbagathi-data.html', context)
    else:
        context = {'form': MbagathiDataForm()}  # Form instance without 'request'
        return render(request, 'upload-mbagathi-data.html', context)


def list_mbagathi_data(request):
    uploads = MbagathiData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-mbagathi-data.html', context)

def download_mbagathi_data(request, pk):
    uploaded_file = MbagathiData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_mbagathi_data(request, pk):
    upload = get_object_or_404(MbagathiData, pk=pk)
    upload.delete()
    return redirect('list-mbagathi-data')
    