from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from activity.models import PlaySession


# Create your views here.
def home(request):
    return render(request, "activity/index.html")

@login_required
@require_POST
def start_session(request):
    user = request.user
    _, created = PlaySession.objects.get_or_create(user=user, finished_at=None)

    if created:
        return HttpResponse(b"STARTING SESSION")

    return HttpResponse(b"Session is already opened")
