from django.db import models

# Create a customer model with the given fields/attributes.


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    income_expense_file = models.FileField(upload_to='files/')
