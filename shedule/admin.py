from django.contrib import admin

from shedule.models import Client, TextForNewsletter, Newsletter, MailingAttempt


@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ('pk', 'contact_email', 'fullname', 'comment',)


@admin.register(TextForNewsletter)
class TextForNewsletter(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'text',)


@admin.register(Newsletter)
class Newsletter(admin.ModelAdmin):
    list_display = ('pk', 'start_time', 'end_time', 'frequency', 'status_of_newsletter',)


@admin.register(MailingAttempt)
class MailingAttempt(admin.ModelAdmin):
    list_display = (
        'pk', 'status_of_last_attempt', 'clients_list', 'server_response',)
