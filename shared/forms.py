from django import forms
from .models import Report, File

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["incident_date", "incident_location", "students_involved", "report_summary", "report_text"]


# class FileForm(forms.Form): # not a ModelForm since uploading multiple files
#     file_field = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=False)
class FileForm(forms.Form):
    model = File
    fields = ["file"]
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
