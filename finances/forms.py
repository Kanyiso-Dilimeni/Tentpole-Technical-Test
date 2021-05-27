from django import forms
from .models import Customer

# Creates a customer form from the Customer model.
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name',
            'date_of_birth', 'income_expense_file'
        ]
