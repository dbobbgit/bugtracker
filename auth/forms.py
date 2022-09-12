from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)