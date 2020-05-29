from django.shortcuts import render


def about(request):
    return render(request, 'About.html')


def contact_us(request):
    return render(request, 'ContactUs.html')
