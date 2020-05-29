from django.db import models


class FairTradeLender(models.Model):
    account_type = models.BooleanField()
    username = models.EmailField(primary_key=True)
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    pan = models.CharField(max_length=32)
    wallet_credit = models.FloatField()

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
            self.wallet_credit
        ]
