# Register your models here.
from django.contrib import admin
from .models import Income, Expense, SavingsGoal

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(SavingsGoal)
