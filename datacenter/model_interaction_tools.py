from datacenter.models import Visit


def get_visitor_in_storage_now():
    active_storage_visitors = Visit.objects.filter(leaved_at=None)

    active_visits_for_request = []

    for visit in active_storage_visitors:

        answer = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(first_format=False),
        }
        active_visits_for_request.append(answer)

    return active_visits_for_request