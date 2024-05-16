from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MamaLucyData
from .forms import MamaLucyDataForm


# Create your views here.
def upload_mamalucy_data(request):
    if request.method == 'POST':
        text_file = MamaLucyDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-mamalucy-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-mamalucy-data.html', context)
    else:
        context = {'form': MamaLucyDataForm()}  # Form instance without 'request'
        return render(request, 'upload-mamalucy-data.html', context)


def list_mamalucy_data(request):
    uploads = MamaLucyData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-mamalucy-data.html', context)

def download_mamalucy_data(request, pk):
    uploaded_file = MamaLucyData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_mamalucy_data(request, pk):
    upload = get_object_or_404(MamaLucyData, pk=pk)
    upload.delete()
    return redirect('list-mamalucy-data')
    