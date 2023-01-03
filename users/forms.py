from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        field_classes = {"username": UsernameField} #UsernameField 專屬欄位
