from django.urls import reverse
from django.views.generic import ListView

from shedule.models import MailingAttempt, Newsletter


class MailingAttemptListView(ListView):
    model = MailingAttempt

    def get_success_url(self):
        return reverse("shedule:mailingattempt_list")

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        return context_data
