from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
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


@login_required
@require_POST
def finish_session(request):
    user = request.user
    updated_count = PlaySession.objects.filter(user=user, finished_at=None).update(finished_at=timezone.now())
    if updated_count:
        return HttpResponse(b"Finishing session")
    return HttpResponse(b"Nothing to be done")
