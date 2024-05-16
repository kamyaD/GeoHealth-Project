from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AnualReportsData
from .forms import AnualReportsDataForm


# Create your views here.
def upload_anual_reports_data(request):
    if request.method == 'POST':
        text_file = AnualReportsDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-anual-reports-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-anual-reports-data.html', context)
    else:
        context = {'form': AnualReportsDataForm()}  # Form instance without 'request'
        return render(request, 'upload-anual-reports-data.html', context)


def list_anual_reports_data(request):
    uploads = AnualReportsData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-anual-reports-data.html', context)

def download_anual_reports_data(request, pk):
    uploaded_file = AnualReportsData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_anual_reports_data(request, pk):
    upload = get_object_or_404(AnualReportsData, pk=pk)
    upload.delete()
    return redirect('list-anual-reports-data')
    