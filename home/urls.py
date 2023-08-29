from django.urls import path
from . import views

urlpatterns = [

    # we base the home funciton here
    # path('home', views.home),

    # passing the HomeView Class
    # need to class the as_view()
    path('', views.HomeView.as_view(), name='home'),

    # path('authorized', views.authorize)
    # dont need anymore
    #path('authorized', views.AuthorizedView.as_view()),

    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup')

]