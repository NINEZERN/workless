from django.urls import path

from activity.views import finish_session, start_session

urlpatterns = [
    path('start_session/', start_session),
    path('finish_session/', finish_session)
]
