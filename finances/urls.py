from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, SavingsGoalViewSet

router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'savings_goal', SavingsGoalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]


