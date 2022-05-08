from django.db import models

from accounts.models import User


class ExpenseType(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.name


class Category(models.Model):
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, null=True, blank=True)
    category_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.expense_type.name}|{self.category_name}"


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    balance_amount = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Balance'

    def __str__(self):
        return str(f"{self.user.name}-{self.balance_amount}")


class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='category')
    created = models.DateTimeField(null=True, blank=True, )
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
    expense = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, null=True, blank=True, related_name='expense')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='category')
    amount = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    closing_balance = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        user_account_balance_obj = UserBalance.objects.get(user=self.user)
        if "Income" in self.expense.name:
            account_balance = user_account_balance_obj.balance_amount
            transaction_amount = self.amount
            user_account_balance_obj.balance_amount = int(account_balance) + int(transaction_amount)
            user_account_balance_obj.save()
            self.closing_balance = user_account_balance_obj.balance_amount
        elif "Expense" in self.expense.name:
            account_balance = user_account_balance_obj.balance_amount
            transaction_amount = self.amount
            user_account_balance_obj.balance_amount = int(account_balance) - int(transaction_amount)
            user_account_balance_obj.save()
            self.closing_balance = user_account_balance_obj.balance_amount
        super().save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return str(self.user)
