# forms.py

from django import forms
from .models import Submission

class StartSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'description']

class BackgroundInfoForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['background_info']  #need to update later


class InvolvedStudentsForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['involved_students']  #need to update later
