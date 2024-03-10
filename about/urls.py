from django.urls import path
from about.views import (AboutPage)
urlpatterns = [
    path('',AboutPage,name='about-page')
]
