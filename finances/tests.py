from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Income, Expense, SavingsGoal

class FinancialAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        self.income = Income.objects.create(
            amount=1000.00,
            source="Salary",
            date="2024-04-01",
            user=self.user
        )
        self.expense = Expense.objects.create(
            amount=500.00,
            category="Rent",
            date="2024-04-02",
            user=self.user
        )
        self.savings_goal = SavingsGoal.objects.create(
            target_amount=5000.00,
            current_savings=1000.00,
            target_date="2024-12-31",
            user=self.user
        )

    def test_create_income(self):
        data = {"amount": 1200.00, "source": "Freelance", "date": "2024-04-10"}
        response = self.client.post("/api/income/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_income(self):
        response = self.client.get(f"/api/income/{self.income.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_expense(self):
        data = {"amount": 300.00, "category": "Groceries", "date": "2024-04-11"}
        response = self.client.post("/api/expense/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_expense(self):
        response = self.client.get(f"/api/expense/{self.expense.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_savings_goal(self):
        data = {"target_amount": 10000.00, "current_savings": 2000.00, "target_date": "2025-06-30"}
        response = self.client.post("/api/savings_goal/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_savings_goal(self):
        response = self.client.get(f"/api/savings_goal/{self.savings_goal.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_total_income(self):
        response = self.client.get("/total-income/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_income(self):
        response = self.client.delete(f"/api/income/{self.income.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_expense(self):
        response = self.client.delete(f"/api/expense/{self.expense.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_savings_goal(self):
        response = self.client.delete(f"/api/savings_goal/{self.savings_goal.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get("/api/income/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
