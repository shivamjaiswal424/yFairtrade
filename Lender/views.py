from django.shortcuts import render, redirect

from .forms import RegisterLenderForm
from Borrower.models import FairTradeBorrower


def reg_lend(request):
    if request.method == 'POST':
        form = RegisterLenderForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account_type = False
            instance.save()
            return redirect('home_lend')
    else:
        form = RegisterLenderForm()
    return render(request, 'Reg_Lend.html', {'form': form})


def home_lend(request):
    return render(request, 'Home_Lend.html', {'users_list': FairTradeBorrower.objects.all().order_by('username')})
