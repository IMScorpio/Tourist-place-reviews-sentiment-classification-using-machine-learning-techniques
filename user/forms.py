from django import forms
from django.core import validators
from user.models import *





class userForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    qualification = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    def __str__(self):
        return self.mail

    class Meta:
        model = userdata
        fields=['name', 'passwd', 'cwpasswd', 'mail', 'mobileno', 'qualification', 'status']



class feedbackform(forms.ModelForm):
    placename = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    package = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    #file = forms.FileField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    rating = forms.ChoiceField(choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    review = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    class Meta:
        model = feedback
        fields = ('placename', 'package','rating','review')








