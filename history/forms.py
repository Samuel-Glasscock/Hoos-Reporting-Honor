from django import forms
from shared.models import Report, User

class CaseForm(forms.ModelForm):
    user__password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Report
        fields = ["id"]