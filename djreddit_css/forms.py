from django import forms

import models

class RedditUserForm(forms.ModelForm):
    
    class Meta:
        model = models.RedditUser