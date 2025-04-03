from django.shortcuts import render
from .models import Income, Expense, SavingsGoal
from .serializers import IncomeSerializer, ExpenseSerializer, SavingsGoalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters  
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .permissions import IsOwner


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]

# Define filterable fields
    filterset_fields = ['date', 'amount', 'source']
    
    # Define searchable fields
    search_fields = ['source']
    
    # Define ordering fields
    ordering_fields = ['date', 'amount']

    def perform_create(self, serializer):
        # Automatically set the user to the logged-in user
        serializer.save(user=self.request.user)

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SavingsGoalViewSet(viewsets.ModelViewSet):
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingsGoalSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TotalIncomeView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        total_income = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        return Response({"total_income": total_income})
    
