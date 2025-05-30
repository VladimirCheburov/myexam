from django.shortcuts import render
from .models import vcexam

# Create your views here.

def vcexam_list(request):
    exams = vcexam.objects.filter(is_public=True)
    return render(request, 'main/vcexam_list.html', {'exams': exams})
