from django.shortcuts import render, redirect
import requests

from .forms import RegisterBorrowerForm
from Lender.models import FairTradeLender

from prometheus_client import Counter, Gauge, generate_latest
from django.http import HttpResponse
import logging

logger = logging.getLogger("django-app-logger")
# Prometheus metrics
request_counter = Counter("repayment_score_requests_total", "Total number of repayment score requests")
health_status = Gauge("app_health_status", "Health status of the application")

def reg_borrow(request):
    if request.method == "POST":
        form = RegisterBorrowerForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account_type = True
            try:
                response = requests.post(
                    "http://flask-ml:5000/get_repayment_score",
                    json={
                        "education": instance.education,
                        "capital": instance.capital,
                        "income": instance.income,
                        "debt": instance.debt,
                        "interest": instance.interest,
                        "credit_score": instance.credit_score,
                    },
                )
                # Increment the Prometheus counter for each request
                request_counter.inc()

                instance.repayment_score = response.json()["repayment_score"]
                instance.save()

                # Set health status to healthy
                health_status.set(1)
                logger.info("Registration successful.")
                return redirect("home_borrow")
            except requests.exceptions.JSONDecodeError:
                # Log error and set health status to unhealthy
                health_status.set(0)
                logger.info("Error calculating repayment score!")
    else:
        form = RegisterBorrowerForm()
    return render(request, "Reg_Borrow.html", {"form": form})

# Expose Prometheus metrics
def prometheus_metrics(request):
    metrics = generate_latest()  # Generate metrics in Prometheus format
    return HttpResponse(metrics, content_type="text/plain")

# Health check view
def health_check(request):
    return HttpResponse("Healthy", content_type="text/plain")

def home_borrow(request):
    return render(
        request,
        "Home_Borrow.html",
        {"users_list": FairTradeLender.objects.all().order_by("username")},
    )