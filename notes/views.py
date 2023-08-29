from django.shortcuts import render
from django.http import Http404

from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import NotesForm
from .models import Notes

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