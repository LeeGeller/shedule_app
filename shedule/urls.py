from shedule.apps import SheduleConfig
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shedule.views import ClientsListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    NewsletterListView, NewsletterCreateView, NewsletterUpdateView, NewsletterDeleteView, TextForNewsletterListView, \
    TextForNewsletterCreateView, TextForNewsletterUpdateView, TextForNewsletterDeleteView, \
    MailingAttemptListView

app_name = SheduleConfig.name

urlpatterns = [
    path("", MailingAttemptListView.as_view(), name="mailingattempt_list"),


    path("client_list/", ClientsListView.as_view(), name="client_list"),
    path("client_form/", ClientCreateView.as_view(), name="client_form"),
    path("<int:pk>/client_update", ClientUpdateView.as_view(), name="client_update"),
    path("<int:pk>/client_delete", ClientDeleteView.as_view(), name="client_delete"),

    path("newsletter_list/", NewsletterListView.as_view(), name="newsletter_list"),
    path("newsletter_form/", NewsletterCreateView.as_view(), name="newsletter_form"),
    path("<int:pk>/newsletter_update", NewsletterUpdateView.as_view(), name="newsletter_update"),
    path("<int:pk>/newsletter_delete", NewsletterDeleteView.as_view(), name="newsletter_delete"),

    path("textfornewsletter_list/", TextForNewsletterListView.as_view(), name="textfornewsletter_list"),
    path("textfornewsletter_form/", TextForNewsletterCreateView.as_view(), name="textfornewsletter_form"),
    path("<int:pk>/textfornewsletter_update", TextForNewsletterUpdateView.as_view(), name="textfornewsletter_update"),
    path("<int:pk>/textfornewsletter_delete", TextForNewsletterDeleteView.as_view(), name="textfornewsletter_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
