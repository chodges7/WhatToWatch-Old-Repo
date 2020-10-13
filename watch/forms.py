from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . import models

class ProfileForm(forms.Form):
    profile_bio = forms.CharField(label='Your new Bio', max_length=500)
    profile_fname = forms.CharField(label='Your corrected first name', max_length=50)
    profile_lname = forms.CharField(label='Your corrected last name', max_length=50)

class BioForm(forms.Form):
    profile_bio = forms.CharField(label='Your new Bio', max_length=500)

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        required=True
    )

    profile_bio = forms.CharField(label='Your Bio', max_length=500)
    profile_fname = forms.CharField(label='Your first name', max_length=50)
    profile_lname = forms.CharField(label='Your last name', max_length=50)

    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = models.UserM
        fields = ("username", "email","password")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            new_pro = models.Profile()
            new_pro.profile_user = user
            new_pro.profile_bio = self.cleaned_data["profile_bio"]
            new_pro.profile_fname = self.cleaned_data["profile_fname"]
            new_pro.profile_lname = self.cleaned_data["profile_lname"]
            new_pro.save()
        return user
