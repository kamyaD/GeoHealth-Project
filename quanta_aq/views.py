from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import QuantaAqData
from .forms import QuantaAqDataForm


# Create your views here.
def upload_quanta_aq_data(request):
    if request.method == 'POST':
        text_file = QuantaAqDataForm(request.POST, request.FILES)  # Form instance without 'request'
        if text_file.is_valid():
            text_file.save(request=request) 
            return redirect('list-quanta-aq-data')
        else: 
            context = {'form': text_file}
            return render(request, 'upload-quanta-aq-data.html', context)
    else:
        context = {'form': QuantaAqDataForm()}  # Form instance without 'request'
        return render(request, 'upload-quanta-aq-data.html', context)


def list_quanta_aq_data(request):
    uploads = QuantaAqData.objects.all()
    context = {'uploads': uploads}
    return render(request, 'list-quanta-aq-data.html', context)

def download_quanta_aq_data(request, pk):
    uploaded_file = QuantaAqData.objects.get(pk=pk)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_quanta_aq_data(request, pk):
    upload = get_object_or_404(QuantaAqData, pk=pk)
    upload.delete()
    return redirect('list-quanta-aq-data')
    