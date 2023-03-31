from django.urls import path
from . import views

urlpatterns = [
    path('', views.DecadeList.as_view(), name='decade_list'),
    path('fads', views.FadsList.as_view(), name='fads_list'),
    path('decades/<int:pk>/', views.DecadeDetail.as_view(), name='decade_detail'),
    path('fads/<int:pk>/', views.FadsDetail.as_view(), name='fad_detail'),
]
