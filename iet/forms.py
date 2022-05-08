from django import forms

from .models import Transactions


class AddTransaction(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['created', 'expense', 'category', 'amount', 'note', ]
        labels = {
            'created': 'Date',
            'expense': 'Type',
            'category': 'Category',
            'amount': 'Amount',
            'note': 'Note',
        }
        widgets = {
            'created': forms.DateTimeInput(attrs={'class': 'form-control form-control-sm', 'type': 'datetime-local'}),
            'expense': forms.Select(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Select Type'}),
            'category': forms.Select(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Select Type'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Amount'}),
            'note': forms.Textarea(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Add Note', 'rows': 3}),
        }
