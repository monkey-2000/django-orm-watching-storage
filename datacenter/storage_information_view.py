import django

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def get_duration(visit):
    """duration in seconds"""
    now = django.utils.timezone.localtime()
    entered_at = django.utils.timezone.localtime(value=visit.entered_at)
    delta = now - entered_at
    d_seconds = delta.total_seconds()
    return d_seconds


def format_duration(duration):
    hours = int(duration // 3600)
    duration %= 3600
    min = int(duration // 60)
    return '{}ч {}мин'.format(hours, min)


def get_visitor_in_storage_now(visit_set):
    active_storage_visitors = visit_set.objects.filter(leaved_at=None)

    active_visits_for_request = []

    for visitor in active_storage_visitors:
        duration = get_duration(visitor)
        answer = {
            'who_entered': visitor.passcard.owner_name,
            'entered_at': visitor.entered_at,
            'duration': format_duration(duration),
        }
        active_visits_for_request.append(answer)

    return active_visits_for_request


def storage_information_view(request):
    # Программируем здесь
    visitor = Visit.objects.all()
    non_closed_visits = get_visitor_in_storage_now(Visit)
    # non_closed_visits = [
    #     {
    #         'who_entered': 'Richard Shaw',
    #         'entered_at': '11-04-2018 25:34',
    #         'duration': '25:03',
    #     }
    # ]
    context = {
        'non_closed_visits': non_closed_visits  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
