from django.urls import path
from media import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('upload_file/', views.model_form_upload, name='upload_file2')
]
