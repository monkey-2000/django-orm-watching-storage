
from datacenter.model_interaction_tools import get_visitor_in_storage_now
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = get_visitor_in_storage_now()
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
