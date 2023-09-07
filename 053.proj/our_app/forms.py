from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError("Name is short")