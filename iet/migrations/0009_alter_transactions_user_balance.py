# Generated by Django 4.0.4 on 2022-05-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('iet', '0008_alter_userbalance_balance_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='user_balance',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]