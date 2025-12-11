# yourapp/validators.py

from django.core.exceptions import ValidationError

def allow_only_gmail(value):
    if not value.endswith("@gmail.com"):
        raise ValidationError("Only Gmail addresses are allowed.")
