from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
   data= Detail.objects.all()

   return render(request,'index.html',{'data':data})