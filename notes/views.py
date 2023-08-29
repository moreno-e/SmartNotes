from django.shortcuts import render
from django.http import Http404

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm
from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'

    # Django expects a certain name for their template
    # It expects it to be named notes/note_confirm_delete.html
    # However we named it notes_delete thus, we have to add below
    template_name = 'notes/notes_delete.html'

class NotesCreateView(CreateView):
    # so the endpoint notes what it's regarding to
    model = Notes

    # attributes from the model that we allow a user to fill
    # fields = ['title', 'text']
    form_class = NotesForm

    # want to redirect the user to the list of updated notes
    success_url = '/smart/notes' 

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"

class NotesDetailView (DetailView):
    model = Notes
    context_object_name = "note"