from django.shortcuts import render

def index(request):
    return render(request, 'folder1/index.html')



