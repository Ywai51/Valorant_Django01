from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'title' : 'Agent-004',
        'heading' : 'Viper_004',
        'subheading' : 'The Poison Queen'
    }
    return render(request, 'viper/index.html', context)