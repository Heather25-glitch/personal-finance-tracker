
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, SavingsGoalViewSet, TotalIncomeView

# Registering the ViewSets with the router
router = DefaultRouter()
router.register(r'income', IncomeViewSet, basename='income')
router.register(r'expense', ExpenseViewSet, basename='expense')
router.register(r'savings_goal', SavingsGoalViewSet, basename='savings_goal')

urlpatterns = [
    path('', include(router.urls)),  
    path('total-income/', TotalIncomeView.as_view(), name='total-income'),
]
