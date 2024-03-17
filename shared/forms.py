from django import forms
from .models import Report, File

class ReportModel(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["id", "title", "description", "status"]


class FileModel(forms.Form): # not a ModelForm since uploading multiple files
    file_fileds = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)