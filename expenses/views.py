from django.shortcuts import render, redirect
from .models import User, Expense, ExactSplit, PercentageSplit
from .forms import UserForm, ExpenseForm, ExactSplitForm, PercentageSplitForm

# Create your views here.

def expenses_home(request):
    return render(request, 'expenses/expenses_home.html')


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm()
    return render(request, 'expenses/create_user.html', {'form': form})


def list_users(request):
    users = User.objects.all()
    return render(request, 'expenses/list_users.html', {'users': users})


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save()
            if expense.split_type == 'exact':
                # Handle Exact Split
                for participant in expense.participants.all():
                    ExactSplit.objects.create(expense=expense, participant=participant, amount=0)  # Adjust amount
            elif expense.split_type == 'percentage':
                # Handle Percentage Split
                for participant in expense.participants.all():
                    PercentageSplit.objects.create(expense=expense, participant=participant, percentage=0)  # Adjust percentage
            return redirect('list_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/create_expense.html', {'form': form})


def list_expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/list_expenses.html', {'expenses': expenses})

