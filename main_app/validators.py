import re

from django.core.exceptions import ValidationError


# Task 1
def validate_name(value):
    for ch in value:
        if not (ch.isalpha() or ch.isspace()):
            raise ValidationError('Name can only contain letters and spaces')


def validate_phone_number(value):
    if not re.match(r'^\+359\d{9$}', value):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
