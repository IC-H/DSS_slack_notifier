from django.urls import path
from .controller import Notifier

urlpatterns = [
    path('slack_to_line/', Notifier.slack_to_line, name='slack_to_line'),
]
