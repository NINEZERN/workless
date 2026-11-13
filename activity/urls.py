from django.urls import path

from activity.views import hello, start_session

urlpatterns = [
    path('hello/', hello),
    path('start_session/', start_session)
]
