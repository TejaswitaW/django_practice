from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs=
                                                    {'autofocus':True,'class':'myuser'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete':'current-password','class':'mypass'}),
    )
