from django.shortcuts import render

# Create your views here.
def dolly(request):
    return render(request,'dolly.html')

def strap(request):
    return render(request,'strap.html')

def paste(request):
    return render(request,'paste.html') 

   
