
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    hours = int(duration // 3600)
    duration %= 3600
    min = int(duration // 60)
    return '{}ч {}мин'.format(hours, min)


def get_visitor_in_storage_now():
    active_storage_visitors = Visit.objects.filter(leaved_at=None)

    active_visits_for_request = []

    for visit in active_storage_visitors:

        answer = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
        }
        active_visits_for_request.append(answer)

    return active_visits_for_request


def storage_information_view(request):

    non_closed_visits = get_visitor_in_storage_now()
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
