from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("this is your home page")
def new (request):
    return render(request,'web.html')   
def destiny(request):
    return render(request,'destinations.html')
def about(request):
        return render(request,'about.html')
def regi(request):
     return render(request,'regisration.html') 

