from django import forms # type: ignore
from .models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'birthday']
