from .models import UserM
from django import forms

class UserF(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserM
        fields = ('username', 'email', 'password')
