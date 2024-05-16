from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import PublishedPapersData
from .forms import PublishedPapersDataForm


# Create your views here.
def upload_published_papers_data(request):
    if request.method == 'POST':
        text_file = PublishedPapersDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-published-papers-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-published-papers-data.html', context)
    else:
        context = {'form': PublishedPapersDataForm()}  # Form instance without 'request'
        return render(request, 'upload-published-papers-data.html', context)


def list_published_papers_data(request):
    uploads = PublishedPapersData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-published-papers-data.html', context)

def download_published_papers_data(request, pk):
    uploaded_file = PublishedPapersData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_published_papers_data(request, pk):
    upload = get_object_or_404(PublishedPapersData, pk=pk)
    upload.delete()
    return redirect('list-published-papers-data')
    