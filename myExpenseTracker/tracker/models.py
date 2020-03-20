from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class categories(TimeStampMixin):
    cat_name = models.TextField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class expense(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(categories,models.PROTECT)
    exp_type = models.BooleanField()
    amount = models.IntegerField()

class budget(TimeStampMixin):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    monthly_budget = models.IntegerField()
