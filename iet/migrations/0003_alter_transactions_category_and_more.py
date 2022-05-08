# Generated by Django 4.0.4 on 2022-05-07 12:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iet', '0002_alter_transactions_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='category', to='iet.category'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='expense', to='iet.expensetype'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='category', to=settings.AUTH_USER_MODEL),
        ),
    ]