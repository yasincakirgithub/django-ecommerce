from django.urls import path
from contact.views import (ContactPage)
urlpatterns = [
    path('',ContactPage,name='contact-page')
]
