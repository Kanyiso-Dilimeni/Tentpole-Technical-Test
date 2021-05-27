from django.contrib import admin
from .models import Customer

# Creates the customer section in the admin page.
admin.site.register(Customer)
