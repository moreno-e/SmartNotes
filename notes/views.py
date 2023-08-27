from django.shortcuts import render

# Create your views here.

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()

    # sending all notes from DB to notes_list.html
    return render(request, 'notes/notes_list.html', {'notes': all_notes})