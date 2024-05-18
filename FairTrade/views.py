from django.shortcuts import render
import logging

logger = logging.getLogger("django-app-logger")

def about(request):
    logger.info("Rendering About page...")
    return render(request, 'About.html')


def contact_us(request):
    logger.info("Rendering Contact Us page...")
    return render(request, 'ContactUs.html')
