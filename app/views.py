from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'VANITHA','age':23}
    return render(request,'wish.html',context=d)

def conditions(request):
    d={'a':100 ,'b':200,'c':500}
    return render(request,'conditions.html',context=d)
def loop(request):
    d={'name':'VANITHA'}
    return render(request,'loop.html',d)

