from django import forms

from .models import FairTradeBorrower


class RegisterBorrowerForm(forms.ModelForm):
    class Meta:
        model = FairTradeBorrower
        exclude = ['account_type', 'repayment_score']

    def __init__(self, *args, **kwargs):
        super(RegisterBorrowerForm, self).__init__(*args, **kwargs)
        for value in self.fields.values():
            value.widget.attrs.update({'class' : 'form-control'})
