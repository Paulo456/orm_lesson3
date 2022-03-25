from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard.id)
    this_passcard_visits = []
    for visit in visits:
      this_passcard_visits.append({
              'entered_at': visit.entered_at.strftime("%Y-%m-%d %H:%M:%S"),
              'duration': visit.format_duration(),
              'is_strange': visit.is_long(),
          })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
