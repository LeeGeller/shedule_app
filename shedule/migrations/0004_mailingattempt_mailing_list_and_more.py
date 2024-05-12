# Generated by Django 5.0.4 on 2024-04-27 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0003_remove_mailingattempt_datetime_last_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingattempt',
            name='mailing_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shedule.newsletter', verbose_name='Письма для рассылки'),
        ),
        migrations.AddField(
            model_name='mailingattempt',
            name='time_attempt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата и время последней попытки'),
        ),
        migrations.AlterField(
            model_name='client',
            name='fullname',
            field=models.TextField(verbose_name='фио'),
        ),
        migrations.AlterField(
            model_name='mailingattempt',
            name='clients_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shedule.client', verbose_name='Клиенты для рассылки'),
        ),
    ]
