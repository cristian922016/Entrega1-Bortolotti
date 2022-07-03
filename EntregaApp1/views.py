from django.shortcuts import render

# Create your views here.

def una_vista(request):
    return render(request,'index.html')