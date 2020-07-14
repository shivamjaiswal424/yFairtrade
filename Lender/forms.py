from django import forms

from .models import FairTradeLender


class RegisterLenderForm(forms.ModelForm):
    class Meta:
        model = FairTradeLender
        exclude = ['account_type']

    def __init__(self, *args, **kwargs):
        super(RegisterLenderForm, self).__init__(*args, **kwargs)
        for value in self.fields.values():
            value.widget.attrs.update({'class' : 'form-control'})