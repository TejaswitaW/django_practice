from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label="Your Name",label_suffix="::",initial="Kush",required=False,disabled=False,
                           help_text="Please provide your name")


