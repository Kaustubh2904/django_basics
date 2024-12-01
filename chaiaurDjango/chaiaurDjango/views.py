from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("Hello, Django!") ye jo hai wo mereko just jo likha hia wo deta hai cool 
    return render(request, 'website/index.html')#ye jo hia wo mereko ek html file return kr raha hai jo ki templates/website folder me hai

def superman(request):
    return render(request, 'website/index.html')

def ganja(request):
    return HttpResponse("Hello!")