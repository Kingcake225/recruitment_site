from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CVUploadForm

@login_required
def upload_cv(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            messages.success(request, 'Your CV has been uploaded successfully!')
            return redirect('profile')
    else:
        form = CVUploadForm()
    return render(request, 'cv_upload/upload.html', {'form': form})
