from django.shortcuts import render

def page_one(request):
    return render(request, 'app_one/page_one.html')