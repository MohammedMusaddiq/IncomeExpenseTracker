# Generated by Django 4.0.4 on 2022-05-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('iet', '0005_remove_transactions_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]