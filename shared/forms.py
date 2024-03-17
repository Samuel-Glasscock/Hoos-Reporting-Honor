from django import forms
from .models import Report, File

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["report_text", "status"]


# class FileForm(forms.Form): # not a ModelForm since uploading multiple files
#     file_field = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=False)
class FileForm(forms.Form):
    file_field = forms.FileField(required=False)
