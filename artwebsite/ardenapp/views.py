from django.shortcuts import render
from django.http import HttpResponse

# Display a simple welcome page where users can navigate to various pages. 
# Initially, let's start with an about page.
def home(request):
    if request.method == 'POST':
        print("ok")
        name = {
            'name': request.POST.get('name'),
        } 
        print(name['name']) # ok so it's there...
        return render(request, 'ardenapp/namegiven.html', name)
    else: 
        return render(request, 'ardenapp/home.html')

def invite(request):
    return render(request, 'ardenapp/cordialinvite.html')