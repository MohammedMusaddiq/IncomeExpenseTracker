# Generated by Django 4.0.4 on 2022-05-07 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('iet', '0006_alter_transactions_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='user_balance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='iet.userbalance'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
