import pickle
from django.shortcuts import render, redirect
from pandas import DataFrame
from numpy import array
from sklearn.preprocessing import StandardScaler

from .forms import RegisterBorrowerForm


def get_repayment_score(instance):
    with open('model.pkl', 'rb') as file:
        pickle_model = pickle.load(file)
    with open('scalar.pkl', 'rb') as file:
        scalar = pickle.load(file)

    x = array(
        [
            instance.education,
            instance.capital,
            instance.income,
            instance.debt,
            instance.interest,
            instance.credit_score,
        ]
    )
    print(x)
    print(x.shape)
    x_test = scalar.transform(x.reshape(1, -1))
    print(x_test)
    print(x_test.shape)
    return pickle_model.predict(x_test)


def reg_borrow(request):
    if request.method == 'POST':
        form = RegisterBorrowerForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account_type = True
            instance.repayment_score = get_repayment_score(instance)
            instance.save()
            return redirect('home_borrow')
    else:
        form = RegisterBorrowerForm()
    return render(request, 'Reg_Borrow.html', {'form': form})


def home_borrow(request):
    return render(request, 'Home_Borrow.html')
