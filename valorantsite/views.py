from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Valorant',
        'heading' : 'Welcome to Valorant',
        'subheading' : 'Get for Free Now!'
    }
    
    return render(request, 'index.html', context)