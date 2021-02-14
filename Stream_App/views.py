from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Stream_App/home.html', context={})
