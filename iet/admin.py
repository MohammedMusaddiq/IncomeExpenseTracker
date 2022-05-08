from django.contrib import admin

from .models import (
    ExpenseType,
    Category,
    Transactions,
    UserBalance,
)


@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['expense_type', 'category_name']
    list_filter = ['expense_type']


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date_time',
        'expense',
        'category',
        'amount',
        'note',
        'closing_balance',
    ]


@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'balance_amount',
    ]
