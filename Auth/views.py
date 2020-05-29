from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from Borrower.models import FairTradeBorrower
from Lender.models import FairTradeLender
from current import *
from .forms import CustomerLoginForm


def login_view(request):
    current_user_data = get_cur_user()
    if current_user_data:
        if current_user_data[0]:
            return redirect('borrow/home_borrow')
        else:
            return redirect('lend/home_lend')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            db_user = FairTradeLender.objects.get(username=username)
            if db_user.check_password(password):
                add_cur_user(db_user.get_data())
                return redirect('lend/home_lend')
            else:
                print('Incorrect password')
        except ObjectDoesNotExist:
            try:
                db_user = FairTradeBorrower.objects.get(username=username)
                if db_user.check_password(password):
                    add_cur_user(db_user.get_data())
                    return redirect('borrow/home_borrow')
                else:
                    print('Incorrect password')
            except ObjectDoesNotExist:
                print('No such account')
    form = CustomerLoginForm()
    return render(request, 'Login.html', {'form': form})


def logout_view(request):
    del_cur_user()
    return redirect('/')
