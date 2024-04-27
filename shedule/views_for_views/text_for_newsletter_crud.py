from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from shedule.models import TextForNewsletter


class TextForNewsletterListView(ListView):
    model = TextForNewsletter


class TextForNewsletterCreateView(CreateView):
    model = TextForNewsletter
    fields = ('subject', 'text',)
    success_url = reverse_lazy("shedule:textfornewsletter_list")


class TextForNewsletterUpdateView(UpdateView):
    model = TextForNewsletter
    fields = ('subject', 'text',)

    def get_success_url(self):
        return reverse("shedule:textfornewsletter_list")


class TextForNewsletterDeleteView(DeleteView):
    model = TextForNewsletter

    def get_success_url(self):
        return reverse("shedule:textfornewsletter_list")
