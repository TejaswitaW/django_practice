from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()


    def clean_name(self):
        nameval = self.cleaned_data['name']
        if len(nameval) < 3:
            raise forms.ValidationError("Please enter name with more than 3 letters")
        return nameval

