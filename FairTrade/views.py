from django.shortcuts import render
import logging

def about(request):
    logging.info("Rendering About page...")
    return render(request, 'About.html')


def contact_us(request):
    logging.info("Rendering Contact Us page...")
    return render(request, 'ContactUs.html')
