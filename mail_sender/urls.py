from django.urls import path

from mail_sender.api.views import EmailAPIView

urlpatterns = [
    path('', EmailAPIView.as_view(),name= 'send-mail')
]