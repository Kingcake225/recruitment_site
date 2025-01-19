from django.urls import path
from . import views

app_name = 'cv_upload'

urlpatterns = [
    path('upload/', views.upload_cv, name='upload'),
]
