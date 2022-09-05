from django.shortcuts import render
from . import plot

# Create your views here.

def index(request):

    return render(request,"polls/index.html")