from django.shortcuts import render
from rest_framework import viewsets
from .models import Income, Expense, SavingsGoal
from .serializers import IncomeSerializer, ExpenseSerializer, SavingsGoalSerializer
from rest_framework import viewsets
from .models import Income
from .serializers import IncomeSerializer
from rest_framework.permissions import IsAuthenticated

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access this view

    def perform_create(self, serializer):
        # Automatically set the user to the logged-in user
        serializer.save(user=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class SavingsGoalViewSet(viewsets.ModelViewSet):
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingsGoalSerializer
