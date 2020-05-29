from django import forms

from .models import FairTradeLender


class RegisterLenderForm(forms.ModelForm):
    class Meta:
        model = FairTradeLender
        exclude = ['account_type']
