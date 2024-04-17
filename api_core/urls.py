from django.contrib import admin
from django.urls import path,include

from mail_sender.api.views import EmailAPIView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('send-mail', include('mail_sender.urls')),
]
