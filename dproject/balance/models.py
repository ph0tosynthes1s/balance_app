from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(blank=True, decimal_places=2, max_digits=12,
                                  validators=[MinValueValidator(Decimal('0.01'))])
