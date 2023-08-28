from django.urls import path
from django.views.defaults import page_not_found

from . import views

def custom_404_handler(request, exception):
    return page_not_found(request, exception, template_name="errors_404.html")


urlpatterns = [
    # READ
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),

    # CREATE
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]

# Assign the custom 404 handler
handler404 = custom_404_handler