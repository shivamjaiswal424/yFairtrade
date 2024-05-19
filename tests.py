import requests
import logging
from unittest.mock import patch  # For mocking external requests

from django.test import TestCase, Client
from django.urls import reverse

from Borrower.forms import RegisterBorrowerForm
from Lender.models import FairTradeLender
from Borrower.models import FairTradeBorrower
from current import add_cur_user, get_cur_user, del_cur_user


class AppViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    # About and Contact Us Views
    def test_about_view(self):
        with self.assertLogs(
            "django-app-logger", level="INFO"
        ) as cm:  # to check if logger message is created
            response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "About.html")
        self.assertIn("INFO:django-app-logger:Rendering About page...", cm.output[0])

    def test_contact_us_view(self):
        with self.assertLogs("django-app-logger", level="INFO") as cm:
            response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ContactUs.html")
        self.assertIn(
            "INFO:django-app-logger:Rendering Contact Us page...", cm.output[0]
        )

    @patch("requests.post")
    def test_reg_borrow_view(self, mock_post):
        mock_post.return_value.json.return_value = {"repayment_score": 9}
        data = {
            "account_type": True,
            "username": "honey@gmail.com",
            "password": "honey",
            "first_name": "Honey",
            "last_name": "Singh",
            "dob": "1998-03-02",
            "pan": "ABCDE1234F",
            "education": 3,
            "capital": 9000000,
            "income": 60000,
            "debt": 800000,
            "interest": 4,
            "credit_score": 78,
        }

        response = self.client.post(
            reverse("reg_borrow"), data, follow=True
        )  # Follow the redirect

        # Assert that the redirect occurred and we're at the home_borrow page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Home_Borrow.html")

        self.assertTrue(FairTradeBorrower.objects.exists())  # Borrower created
        borrower = FairTradeBorrower.objects.first()
        self.assertEqual(borrower.repayment_score, 9)

    def test_home_borrow_view(self):
        FairTradeLender.objects.create(
            account_type=False,
            username="honey@gmail.com",
            password="honey",
            first_name="Honey",
            last_name="Singh",
            dob="1998-03-02",
            pan="ABCDE1234F",
            wallet_credit=9800000,
        )
        response = self.client.get(reverse("home_borrow"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Home_Borrow.html")
        self.assertEqual(len(response.context["users_list"]), 1)

    # Lender Views
    def test_reg_lend_view(self):
        data = {
            "account_type": False,
            "username": "honey@gmail.com",
            "password": "honey",
            "first_name": "Honey",
            "last_name": "Singh",
            "dob": "1998-03-02",
            "pan": "ABCDE1234F",
            "wallet_credit": 9800000,
        }
        response = self.client.post(reverse("reg_lend"), data)
        self.assertRedirects(response, reverse("home_lend"))
        self.assertTrue(FairTradeLender.objects.exists())

    def test_home_lend_view(self):
        FairTradeBorrower.objects.create(
            account_type=True,
            username="honey@gmail.com",
            password="honey",
            first_name="Honey",
            last_name="Singh",
            dob="1998-03-02",
            pan="ABCDE1234F",
            education=3,
            capital=9000000,
            income=60000,
            debt=800000,
            interest=4,
            credit_score=78,
        )
        response = self.client.get(reverse("home_lend"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Home_Lend.html")
        self.assertEqual(len(response.context["users_list"]), 1)

    # Auth Views
    def test_login_view_and_logout_view(self):
        FairTradeLender.objects.create(
            account_type=False,
            username="honey@gmail.com",
            password="honey",
            first_name="Honey",
            last_name="Singh",
            dob="1998-03-02",
            pan="ABCDE1234F",
            wallet_credit=9800000,
        )
        data = {"username": "honey@gmail.com", "password": "honey"}

        # Login
        response = self.client.post(reverse("login"), data)
        self.assertRedirects(response, "/lend/home_lend")
        self.assertIsNotNone(get_cur_user())

        # Logout
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, "/")
        self.assertIsNone(get_cur_user())
