from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DraftPapersData
from .forms import DraftPapersDataForm


# Create your views here.
def upload_draft_papers_data(request):
    if request.method == 'POST':
        text_file = DraftPapersDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-draft-papers-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-draft-papers-data.html', context)
    else:
        context = {'form': DraftPapersDataForm()}  # Form instance without 'request'
        return render(request, 'upload-draft-papers-data.html', context)


def list_draft_papers_data(request):
    uploads = DraftPapersData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-draft-papers-data.html', context)

def download_draft_papers_data(request, pk):
    uploaded_file = DraftPapersData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_draft_papers_data(request, pk):
    upload = get_object_or_404(DraftPapersData, pk=pk)
    upload.delete()
    return redirect('list-draft-papers-data')
    