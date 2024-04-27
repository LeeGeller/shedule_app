from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from shedule.models import MailingAttempt
from shedule.views_for_views.client_crud import ClientsListView, ClientCreateView, ClientUpdateView, ClientDeleteView
from shedule.views_for_views.mailing_attempt_crud import MailingAttemptListView
from shedule.views_for_views.newslatter_crud import NewsletterListView, NewsletterCreateView, NewsletterUpdateView, \
    NewsletterDeleteView
from shedule.views_for_views.text_for_newsletter_crud import TextForNewsletterListView, TextForNewsletterCreateView, \
    TextForNewsletterUpdateView, TextForNewsletterDeleteView


MailingAttemptListView()


ClientsListView()
ClientCreateView()
ClientUpdateView()
ClientDeleteView()

NewsletterListView()
NewsletterCreateView()
NewsletterUpdateView()
NewsletterDeleteView()

TextForNewsletterListView()
TextForNewsletterCreateView()
TextForNewsletterUpdateView()
TextForNewsletterDeleteView()
