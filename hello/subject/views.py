from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context_dict = {'boldmessage': 'I am bold font from the context'}
    return render(request, 'subject/index.html', context_dict)


def about(request):
    about_dict = {'aboutmessage': 'bazinga'}
    return render(request, 'subject/about.html', about_dict)