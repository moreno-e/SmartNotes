from django.urls import path
from django.views.defaults import page_not_found

from . import views

def custom_404_handler(request, exception):
    return page_not_found(request, exception, template_name="errors_404.html")


urlpatterns = [
    # READ
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),

    #UPDATE
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),

    # CREATE
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),

    # DELETE
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),

]

# Assign the custom 404 handler
handler404 = custom_404_handler