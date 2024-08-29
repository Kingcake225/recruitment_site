from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing-page'), # Second argument specifies view which we want to handle the logic.
    path('route/', views.route, name='routes-page'),
    path('blog/', views.blog, name='blog-page'),
]
