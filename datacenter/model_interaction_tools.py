from datacenter.models import Visit


def serialize_visits(visits):

    serialized_visits = []

    for visit in visits:

        answer = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(first_format=False),
        }
        serialized_visits.append(answer)

    return serialized_visits


def serialize_this_passcard_visits(passcard):
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