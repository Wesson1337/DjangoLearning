from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdvertisementListView.as_view(), name='adv_list'),
    path('about/', views.About.as_view(), name='about'),
    path('<int:pk>', views.AdvertisementDetailView.as_view(), name='adv_list_detail_view')
]
