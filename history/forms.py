from django import forms
from shared.models import Report, User

class CaseForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["id", "user__password"]