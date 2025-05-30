from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vcexam/', views.vcexam_list, name='vcexam_list'),
] 