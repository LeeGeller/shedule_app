from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from shedule.models import Newsletter


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ('frequency', 'clients', 'message',)
    success_url = reverse_lazy("shedule:newsletter_list")


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('frequency', 'clients', 'message',)

    def get_success_url(self):
        return reverse("shedule:newsletter_list")


class NewsletterDeleteView(DeleteView):
    model = Newsletter

    def get_success_url(self):
        return reverse("shedule:newsletter_list")
