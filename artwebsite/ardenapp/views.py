from django.shortcuts import render
from django.http import HttpResponse

# Display a simple welcome page where users can navigate to various pages. 
# Initially, let's start with an about page.
def home(request):
    return render(request, 'ardenapp/home.html')


def members(request):
    return HttpResponse("Hello world!")