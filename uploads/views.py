from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

from uploads.models import Document
from uploads.forms import DocumentForm


class HomePageView(TemplateView):
    template_name = "uploads/home.html"

class AboutPageView(TemplateView):
    template_name = "uploads/about.html"

def model_form_upload(request):
    print(request.user)
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
