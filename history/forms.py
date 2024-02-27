from django import forms
from shared.models import Report

class CaseForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["id"]