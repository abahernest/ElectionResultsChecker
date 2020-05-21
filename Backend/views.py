from django.shortcuts import render


def HomeViews (request):
    return render(request,'index.html')

