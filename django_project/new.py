from django.shortcuts import render


def Web(request):
    return render(request,'index.html')