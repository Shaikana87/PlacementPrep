# from socket import fromshare
from django import forms
from django.core.validators import RegexValidator

fname_validator = RegexValidator(r'^[a-zA-Z ]+$', "First Name can only contain Alphabets !")

lname_validator = RegexValidator(r'^[a-zA-Z ]+$', "Last Name can only contain Alphabets !")
# Minimum eight characters, at least one letter, one number and one special character:

psw_validator = RegexValidator(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', "Minimum eight characters, at least one letter, one number and one special character required in password !")

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First name', 
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'text',
                                    'id':'registerFirstName'
                                }),
                                validators = [fname_validator])
    last_name = forms.CharField(label='Last name',
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'text',
                                    'id':'registerLastName'
                                }),
                                validators = [lname_validator])
    username = forms.CharField(label='Username',
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'text',
                                    'id':'registerUsername'
                                }))
    email = forms.CharField(label='Email',
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'email',
                                    'id':'registerEmail'
                                }))
    password = forms.CharField(label='Password',
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'password',
                                    'id':'registerPassword'
                                }),
                                validators = [psw_validator])
    repeat_password =  forms.CharField(label='Repeat Password',
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'type': 'password',
                                    'id':'registerRepeatPassword'
                                }))
