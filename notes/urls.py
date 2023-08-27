from django.urls import path
from django.views.defaults import page_not_found

from . import views

def custom_404_handler(request, exception):
    return page_not_found(request, exception, template_name="errors_404.html")


urlpatterns = [
    #path('notes', views.list),
    # With the name, now we telling django what endpoint to link to
    # That's all we need for Django dynamically define each endpoint we are pointing to, no matter if you're on localhost or production.
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    #path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
]

# Assign the custom 404 handler
handler404 = custom_404_handler