from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def home(request):
    example_response = " This is my homepage"
    return render(request, "index.html")
    #return HttpResponse(example_response)
