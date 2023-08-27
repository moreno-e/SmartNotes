from django.urls import path
from django.views.defaults import page_not_found

from . import views

def custom_404_handler(request, exception):
    return page_not_found(request, exception, template_name="errors_404.html")


urlpatterns = [
    #path('notes', views.list),
    path('notes', views.NotesListView.as_view()),
    #path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
]

# Assign the custom 404 handler
handler404 = custom_404_handler