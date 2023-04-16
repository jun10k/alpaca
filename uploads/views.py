from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from uploads.models import Document
from uploads.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'uploads/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploads/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'uploads/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'uploads/model_form_upload.html', {
        'form': form
    })
