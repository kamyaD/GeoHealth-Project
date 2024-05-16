from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import EveryWeekReportsData
from .forms import EveryWeekReportsDataForm



# Create your views here.
def upload_every_week_reports_data(request):
    if request.method == 'POST':
        text_file = EveryWeekReportsDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-every-week-reports-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-every-week-reports-data.html', context)
    else:
        context = {'form': EveryWeekReportsDataForm()}  # Form instance without 'request'
        return render(request, 'upload-every-week-reports-data.html', context)


def list_every_week_reports_data(request):
    uploads = EveryWeekReportsData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-every-week-reports-data.html', context)

def download_every_week_reports_data(request, pk):
    uploaded_file = EveryWeekReportsData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_every_week_reports_data(request, pk):
    upload = get_object_or_404(EveryWeekReportsData, pk=pk)
    upload.delete()
    return redirect('list-every-week-reports-data')
    