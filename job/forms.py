from django import forms
from .models import Apply



class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['full_name', 'email', 'website', 'cv','cover_letter']