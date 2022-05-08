"""
from django.db.models.signals import post_save
from .models import (
    UserBalance,
    Transactions,
)


def update_user_balance(instance, created, **kwargs):
    if created:
        user_balance_obj = UserBalance.objects.get(user=instance.user)
        existing_balance = user_balance_obj.balance_amount
        transaction_amount = instance.amount
        if instance.expense.name == 'Income':
            user_balance_obj.balance_amount = int(existing_balance) + int(transaction_amount)
            user_balance_obj.save()
        if instance.expense.name == 'Expense':
            user_balance_obj.balance_amount = int(existing_balance) - int(transaction_amount)
            user_balance_obj.save()


post_save.connect(update_user_balance, sender=Transactions)
"""
