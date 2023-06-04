from django.shortcuts import render

# Create your views here.
def wishes(request):
    d={'name':'JINGA'}
    return render(request,'wishes.html',context=d)