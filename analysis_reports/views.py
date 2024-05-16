from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AnalysisReportsData
from .forms import AnalysisReportsDataForm



# Create your views here.
def upload_analysis_reports_data(request):
    if request.method == 'POST':
        text_file = AnalysisReportsDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-analysis-reports-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-analysis-reports-data.html', context)
    else:
        context = {'form': AnalysisReportsDataForm()}  # Form instance without 'request'
        return render(request, 'upload-analysis-reports-data.html', context)


def list_analysis_reports_data(request):
    uploads = AnalysisReportsData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-analysis-reports-data.html', context)

def download_analysis_reports_data(request, pk):
    uploaded_file = AnalysisReportsData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_analysis_reports_data(request, pk):
    upload = get_object_or_404(AnalysisReportsData, pk=pk)
    upload.delete()
    return redirect('list-analysis-reports-data')
    