from django.urls import path

from activity.views import hello

urlpatterns = [
    path('hello/', hello)
]
