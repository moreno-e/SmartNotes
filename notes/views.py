from django.shortcuts import render
from django.http import Http404

# Create your views here.

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()

    # sending all notes from DB to notes_list.html
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

# creating a way to visualize details for a particular note
def detail(request, pk):
    # if we don't use try/catch, if pk is pass that is not found an exception will be thrown
    try:
        note = Notes.objects.get(pk=pk)
    except:
        # raise Http404("Note doesn't exist")
        return render(request, 'errors/errors_404.html', status=404)
    return render(request, 'notes/notes_detail.html', {'note': note})

# In case you want to use the built-in shortcut get_object_or_404 instead of manual try-except:
# def detail(request, pk):
#     note = get_object_or_404(Notes, pk=pk)
#     return render(request, 'errors/errors_detail.html', {'note': note})