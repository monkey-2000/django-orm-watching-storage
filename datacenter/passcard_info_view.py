from datacenter.seralizers import serialize_this_passcard_visits
from datacenter.models import Passcard
from django.shortcuts import render


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = serialize_this_passcard_visits(passcard)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
