from django.db import models


class FairTradeBorrower(models.Model):
    account_type = models.BooleanField(default=True)
    username = models.EmailField(primary_key=True)
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    pan = models.CharField(max_length=32)
    education = models.IntegerField(default=1)
    capital=models.FloatField(default=0)
    income = models.FloatField(default=0)
    debt = models.FloatField(default=0)
    interest = models.FloatField(default=3)
    credit_score = models.IntegerField(default=100)
    repayment_score = models.IntegerField(default=1)

    def check_password(self, password):
        return self.password == password

    def get_data(self):
        return [
            self.account_type,
            self.username,
            self.first_name,
            self.last_name,
            self.dob,
            self.pan,
            self.education,
            self.capital,
            self.income,
            self.debt,
            self.interest,
            self.credit_score,
            self.repayment_score,
        ]
