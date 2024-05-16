from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import CycleReportsData
from .forms import CycleReportsDataForm


# Create your views here.
def upload_cylce_reports_data(request):
    if request.method == 'POST':
        text_file = CycleReportsDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-cycle-reports-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-cylce-reports-data.html', context)
    else:
        context = {'form': CycleReportsDataForm()}  # Form instance without 'request'
        return render(request, 'upload-cylce-reports-data.html', context)


def list_cylce_reports_data(request):
    uploads = CycleReportsData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-cylce-reports-data.html', context)

def download_cylce_reports_data(request, pk):
    uploaded_file = CycleReportsData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_cylce_reports_data(request, pk):
    upload = get_object_or_404(CycleReportsData, pk=pk)
    upload.delete()
    return redirect('list-cycle-reports-data')
    