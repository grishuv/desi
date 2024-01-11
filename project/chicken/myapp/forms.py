# your_app_name/forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    full_name = forms.CharField(max_length=100)
    contact_no = forms.CharField(max_length=15)
    email_id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
