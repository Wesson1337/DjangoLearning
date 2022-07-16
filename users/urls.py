from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('anotherlogin/', views.AnotherLoginView.as_view(), name='another_login'),
    path('', views.main, name='users'),
    path('logout/', views.logout_view, name='logout')
]
