from rest_framework import serializers
from .models import Income, Expense, SavingsGoal

from rest_framework import serializers
from .models import Income


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'amount', 'source', 'date', 'user']  # Ensure 'id' is included
        read_only_fields = ['id', 'user']  # Make 'id' and 'user' read-only

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = '__all__'


