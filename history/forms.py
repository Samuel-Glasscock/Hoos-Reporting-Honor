from django import forms
from shared.models import Report, User

class CaseSearchForm(forms.ModelForm):
    case_id = forms.UUIDField(label="Case ID", 
                                widget=forms.TextInput(attrs={'placeholder': 'Case ID', 
                                                                  'class': 'form-control', 
                                                                  'required': True}))
    class Meta:
        model = Report
        fields = ["id"]
        labels = {"id": "Case ID"}
        widgets = {
            'id': forms.TextInput(attrs={'placeholder': 'Case ID', 
                                         'class': 'form-control',
                                         'required': True})
        }