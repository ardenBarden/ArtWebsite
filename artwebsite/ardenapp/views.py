from django.shortcuts import render
from django.http import HttpResponse

# Display a simple welcome page where users can navigate to various pages. 
# Initially, let's start with an about page.
def home(request):
    if request.method == 'POST':
        #trying to make it so that revisiting a page doesnt replay animations
        name = {
            'name': request.POST.get('name'),
        } 
        return render(request, 'ardenapp/namegiven.html', name)
    else: 
        return render(request, 'ardenapp/home.html')
    
#for when he's revisiting and doesn't need the animations 
def homeagain(request):
    if request.method == 'POST':
        #trying to make it so that revisiting a page doesnt replay animations
        name = {
            'name': request.POST.get('name'),
        } 
        return render(request, 'ardenapp/namegiven.html', name)
    else: 
        return render(request, 'ardenapp/homeagain.html')

def invite(request):
    return render(request, 'ardenapp/cordialinvite.html')

def agenda(request):
    return render(request, 'ardenapp/agenda.html')