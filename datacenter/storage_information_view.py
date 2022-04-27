from datacenter.seralizers import serialize_visits
from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request):
    active_storage_visitors = Visit.objects.filter(leaved_at=None)

    non_closed_visits = serialize_visits(active_storage_visitors)

    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
