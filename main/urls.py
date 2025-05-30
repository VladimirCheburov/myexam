from django.urls import path
from . import views

urlpatterns = [
    path('vcexam/', views.vcexam_list, name='vcexam_list'),
] 