from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title' : 'About Us',
        'heading' : 'RIOT GAMES',
        'subheading' : 'We develope for anyone!'
    }
    return render(request, "about/index.html", context)