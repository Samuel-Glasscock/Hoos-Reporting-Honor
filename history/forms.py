from django import forms
from shared.models import Report, User

class CaseForm(forms.ModelForm):
    user_password = forms.CharField(label="Password", 
                                    widget=forms.TextInput(attrs={'placeholder': 'Password', 
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