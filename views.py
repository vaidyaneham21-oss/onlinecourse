from django.shortcuts import render
from .models import Course

def submit(request):
    return render(request, 'result.html')

def show_exam_result(request):
    return render(request, 'result.html')