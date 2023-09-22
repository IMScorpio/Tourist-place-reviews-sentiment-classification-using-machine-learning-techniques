
from django import forms
from django.core import validators

from turstguide.models import *

class guideForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    location = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    def __str__(self):
        return self.mail


    class Meta:
        model = guidemodel
        fields=['name','passwd','cwpasswd','mail','mobileno','location','status']




class uploadForm(forms.ModelForm):
    class Meta:
        model = upload
        fields=('placename','information','package','file')
