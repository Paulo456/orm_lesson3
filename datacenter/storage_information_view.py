from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(entered_at__isnull=False,
                                    leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.strftime("%Y-%m-%d %H:%M:%S"),
            'duration': visit.format_duration(),
            'is_strange': visit.is_long(),
        })
        

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
