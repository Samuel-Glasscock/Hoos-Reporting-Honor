# forms.py

from django import forms
from .models import Submission

class StartSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'description']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['background_info']  #need to update later

