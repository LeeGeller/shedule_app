from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput
from django.db.models import Prefetch
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from shedule.forms import NewsletterForm
from shedule.models import Newsletter


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm

    success_url = reverse_lazy("shedule:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get('clients')

        newsletter.save()

        newsletter.clients.clear()

        for client in selected_clients:
            newsletter.clients.add(client)

        # Возвращаем успешный ответ
        return super().form_valid(form)


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm

    def get_success_url(self):
        return reverse("shedule:newsletter_list")

    def form_valid(self, form):
        # Получаем объект формы, но еще не сохраняем его в базу данных
        newsletter = form.save(commit=False)

        # Получаем выбранных клиентов из данных формы
        selected_clients = form.cleaned_data.get('clients')

        # Сохраняем объект формы в базу данных
        newsletter.save()

        # Очищаем связанных клиентов, чтобы избежать дублирования
        newsletter.clients.clear()

        # Добавляем выбранных клиентов к объекту Newsletter
        for client in selected_clients:
            newsletter.clients.add(client)
        print(newsletter)

        # Возвращаем успешный ответ
        return super().form_valid(form)


class NewsletterDeleteView(DeleteView):
    model = Newsletter

    def get_success_url(self):
        return reverse("shedule:newsletter_list")
