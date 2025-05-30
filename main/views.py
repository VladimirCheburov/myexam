from django.shortcuts import render, redirect
from .models import vcexam

# Create your views here.

def index(request):
    return redirect('vcexam_list')

def vcexam_list(request):
    exams = vcexam.objects.filter(is_public=True)
    return render(request, 'main/vcexam_list.html', {'exams': exams})
