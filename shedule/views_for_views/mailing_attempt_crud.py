from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from shedule.models import MailingAttempt


class MailingAttemptListView(ListView):
    model = MailingAttempt

    def get_success_url(self):
        return reverse("shedule:attempt_list")

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        return context_data
