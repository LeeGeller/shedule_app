from django.db import models

FREQUENCY_CHOICES = [('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'), ]
STATUS_OF_NEWSLETTER = [("Create", 'Создана'), ("Started", 'Отправлено'), ("Done", 'Завершена'), ]


class Client(models.Model):
    contact_email = models.CharField(max_length=250, verbose_name='контактный email')
    fullname = models.TextField(verbose_name='фио')
    comment = models.CharField(max_length=250, verbose_name='комментарий')

    def __str__(self):
        return f"{self.contact_email} {self.fullname} {self.comment}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class TextForNewsletter(models.Model):
    subject = models.CharField(max_length=200, verbose_name='тема')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return f"{self.subject} {self.text}"

    class Meta:
        verbose_name = "Текст для отправки"
        verbose_name_plural = "Тексты для рассылок"


class Newsletter(models.Model):
    start_time = models.DateTimeField(verbose_name='время начала рассылки', blank=True, null=True)
    end_time = models.DateTimeField(verbose_name='время окончания рассылки', blank=True, null=True)
    frequency = models.CharField(max_length=300, choices=FREQUENCY_CHOICES)
    status_of_newsletter = models.CharField(max_length=150, verbose_name='статус рассылки',
                                            choices=STATUS_OF_NEWSLETTER)
    clients = models.ManyToManyField(Client)
    message = models.ForeignKey(TextForNewsletter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_newsletter} {self.frequency} {self.status_of_newsletter} {self.clients} {self.message}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingAttempt(models.Model):
    status_of_last_attempt = models.BooleanField(verbose_name='Статус попытки', blank=True,
                                                 null=True)

    clients_list = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент рассылки', blank=True,
                                     null=True)

    server_response = models.CharField(verbose_name='ответ почтового сервера', blank=True, null=True)

    def __str__(self):
        return f" {self.status_of_last_attempt} {self.clients_list} {self.server_response}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
