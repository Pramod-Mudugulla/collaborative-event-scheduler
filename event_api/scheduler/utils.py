from datetime import datetime
from .models import Event

def has_conflict(user, start_time, end_time):
    return Event.objects.filter(
        owner=user,
        start_time__lt=end_time,
        end_time__gt=start_time
    ).exists()
