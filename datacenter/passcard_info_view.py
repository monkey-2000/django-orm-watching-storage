from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def serialize_this_passcard_visit(passcard):
    serialized_this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        visit_time_report = {
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(),
            'is_strange': visit.is_visit_long()
        }
        serialized_this_passcard_visits.append(visit_time_report)

    return serialized_this_passcard_visits


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = serialize_this_passcard_visit(passcard)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
