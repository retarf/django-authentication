from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'content': 'Success'}
    return render(request, 'core/index.html', context)
