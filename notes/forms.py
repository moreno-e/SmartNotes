from django import forms
from django.core.exceptions import ValidationError
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
    
    def clean_title(self):
        #cleaned_data is a dictionary
        # The cleaned_data is returned by the form and is userful for fields with strong validaiton (emails, etc.)
        #here it will be the same value as the user passed
        title = self.cleaned_data['title']

        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')
        return