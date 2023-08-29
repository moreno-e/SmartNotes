from django.urls import path
from . import views

urlpatterns = [

    # we base the home funciton here
    # path('home', views.home),

    # passing the HomeView Class
    # need to class the as_view()
    path('home', views.HomeView.as_view()),

    # path('authorized', views.authorize)
    path('authorized', views.AuthorizedView.as_view()),

    path('login', views.LoginInterfaceView.as_view())

]