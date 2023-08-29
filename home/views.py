from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# removed since switching from function to class based view
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    # Need to add below
    # Need to make sure that only people that are not logged in can access he signup page
    # can do this by overriding the get method and redirecting the user if they are already logged in
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

# Create your views here.

# CLASS BASED VIEW
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


# FUNCTION BASED VIEW
# def home(request):

#     # return HttpResponse('Hello World')

#     # Instead of using HTTPResponse, use the function render
#     # from Django shortcuts

#     # All though we are writing an HTML page, Django is using a template 
#     # framework to create the final HTML page in the browser

#     # {} will allow us to pass down information from the view to the template

#     # args(original request, name of the template, empty brackets)
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

# FUNCTION BASED VIEW
# @login_required(login_url='/admin')
# def authorize(request):
#     return render(request, 'home/authorize.html', {})