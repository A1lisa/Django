from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_flowers(request):
    return HttpResponse("Hello Students")