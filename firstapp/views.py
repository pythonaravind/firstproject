from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wellcome(request):
    s='<h1> hello world </h1>'
    return HttpResponse(s)
