# Generated by Django 4.0.4 on 2022-05-07 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('iet', '0003_alter_transactions_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='user_balance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='user_balance', to='iet.userbalance'),
        ),
    ]
