"""NinjaSushi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profiles.views import UserFromView, UserEditFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advertisement/', include('advertisement.urls')),
    path('profiles/', UserFromView.as_view()),
    path('profiles/<int:profile_id>/edit/', UserEditFormView.as_view()),
    path('news/', include('news.urls')),
    path('users/', include('users.urls')),
    path('media/', include('media.urls')),
    path('goods/', include('goods.urls')),
    path('logic/', include('logic.urls')),
    path('pages/', include('pages.urls')),
    path('118n', include('django.conf.urls.i18n'))
]
