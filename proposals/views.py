from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ProposalsData
from .forms import ProposalsDataForm


# Create your views here.
def upload_proposals_data(request):
    if request.method == 'POST':
        text_file = ProposalsDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-proposals-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-proposals-data.html', context)
    else:
        context = {'form': ProposalsDataForm()}  # Form instance without 'request'
        return render(request, 'upload-proposals-data.html', context)


def list_proposals_data(request):
    uploads = ProposalsData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-proposals-data.html', context)

def download_proposals_data(request, pk):
    uploaded_file = ProposalsData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_proposals_data(request, pk):
    upload = get_object_or_404(ProposalsData, pk=pk)
    upload.delete()
    return redirect('list-proposals-data')
    