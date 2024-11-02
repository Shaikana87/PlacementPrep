# from socket import fromshare
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'text',
                                    'id':'loginName'
                                }))
    password = forms.CharField(label='Password',
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'password',
                                    'id':'loginPassword'
                                }))