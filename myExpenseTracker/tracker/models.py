from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TransactionType(models.IntegerChoices):
    DEBIT = 0, 'Debit'
    CREDIT = 1, 'Credit'


class Categories(TimeStampMixin):
    cat_name = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat_name


class Expense(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, models.PROTECT)
    exp_type = models.IntegerField(choices=TransactionType.choices)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.exp_type) + ": " + str(self.amount)


class Budget(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monthly_budget = models.IntegerField()
