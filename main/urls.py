"""DjangoLearning URL Configuration

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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from profiles.views import UserFromView, UserEditFormView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Описание проекта",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
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
    path('i18n', include('django.conf.urls.i18n')),
    path('rest_app/', include('rest_app.urls')),
    path('lib/', include('books.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('blog/', include('blog.urls')),
    path('__debug__', include(debug_toolbar.urls))
]

