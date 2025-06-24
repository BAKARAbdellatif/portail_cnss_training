from django import forms
from .models import Assure

class FormAssure(forms.ModelForm):
    class Meta:
        model = Assure
        fields = "__all__"
        widgets = {
            'date_naissance': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }