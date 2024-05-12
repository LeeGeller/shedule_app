from time import sleep

from django.apps import AppConfig


class SheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shedule'

    def ready(self):
        from shedule.script_for_mailing import start
        sleep(2)
        start()
