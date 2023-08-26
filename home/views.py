from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    # return HttpResponse('Hello World')

    # Instead of using HTTPResponse, use the function render
    # from Django shortcuts

    # All though we are writing an HTML page, Django is using a template 
    # framework to create the final HTML page in the browser

    # {} will allow us to pass down information from the view to the template

    # args(original request, name of the template, empty brackets)
    return render(request, 'home/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorize(request):
    return render(request, 'home/authorize.html', {})