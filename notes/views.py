from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url)

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    # Means that if a user tried to access the list view and it's not logged in
    # They will be redirected to the /admin instead of seeing a 404
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView (DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/login"