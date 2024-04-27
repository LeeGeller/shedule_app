import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0002_alter_client_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.CharField(max_length=250, verbose_name='контактный email')),
                ('fullname', models.TextField(verbose_name='ФИО')),
                ('comment', models.CharField(max_length=250, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='TextForNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='тема')),
                ('text', models.TextField(verbose_name='текст')),
            ],
            options={
                'verbose_name': 'Текст для отправки',
                'verbose_name_plural': 'Тексты для рассылок',
            },
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_of_last_attempt', models.BooleanField(blank=True, null=True, verbose_name='Статус попытки')),
                ('server_response', models.CharField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('clients_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shedule.client', verbose_name='Клиент рассылки')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылок',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='время начала рассылки')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='время окончания рассылки')),
                ('frequency', models.CharField(choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], max_length=300)),
                ('status_of_newsletter', models.CharField(choices=[('Create', 'Создана'), ('Started', 'Отправлено'), ('Done', 'Завершена')], max_length=150, verbose_name='статус рассылки')),
                ('clients', models.ManyToManyField(to='shedule.client')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shedule.textfornewsletter')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
