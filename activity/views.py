from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from activity.models import PlaySession


def home(request):
    active_session = None
    if request.user.is_authenticated:
        active_session = PlaySession.objects.filter(
            user=request.user, finished_at=None
        ).first()

    return render(request, "activity/index.html", {
        "active_session": active_session,
        "current_time": timezone.localtime(),
        "TIME_ZONE": timezone.get_current_timezone_name(),
    })


@login_required
@require_POST
def start_session(request):
    PlaySession.objects.get_or_create(user=request.user, finished_at=None)
    return redirect("home")


@login_required
@require_POST
def finish_session(request):
    PlaySession.objects.filter(user=request.user, finished_at=None).update(
        finished_at=timezone.now()
    )
    return redirect("home")
