from django import forms

from .models import FairTradeBorrower


class RegisterBorrowerForm(forms.ModelForm):
    class Meta:
        model = FairTradeBorrower
        exclude = ['account_type', 'repayment_score']
