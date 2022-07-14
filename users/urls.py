from django.urls import path
from users import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('anotherlogin', views.AnotherLoginView.as_view(), name='another_login')
]
