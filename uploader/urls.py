from django.urls import path
from uploader import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('download/', views.download, name='download')
]
