from django.shortcuts import render

def page_two(request):
    return render(request, 'app_two/page_two.html')