from django import forms
from .models import User, Expense, ExactSplit, PercentageSplit

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'mobile']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user', 'participants', 'total_amount', 'split_type']


class ExactSplitForm(forms.ModelForm):
    class Meta:
        model = ExactSplit
        fields = ['expense', 'participant', 'amount']


class PercentageSplitForm(forms.ModelForm):
    class Meta:
        model = PercentageSplit
        fields = ['expense', 'participant', 'percentage']
