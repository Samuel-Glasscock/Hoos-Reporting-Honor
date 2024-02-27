from django import forms

class CaseForm(forms.ModelForm):
    class Meta:
        fields = ["id"]