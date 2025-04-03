from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, SavingsGoalViewSet, TotalIncomeView

router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'savings_goal', SavingsGoalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('total-income/', TotalIncomeView.as_view(), name='total-income'),
]
