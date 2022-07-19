from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from media.forms import UploadFileForm, DocumentForm


def upload_file(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=f'{file.size} bytes, {file.name}', status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'media/upload_file.html', context=context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'media/file_form_upload.html', {
            'form': form
        })
