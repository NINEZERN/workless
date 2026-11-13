from django.urls import path

from activity.views import start_session

urlpatterns = [
    path('start_session/', start_session)
]
