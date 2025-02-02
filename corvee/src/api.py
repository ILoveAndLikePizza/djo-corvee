from django.http.response import JsonResponse
from django.views import View

from corvee.src.models import Persoon


class SelectedV1(View):
    def get(self, request, *args, **kwargs):
        selected = Persoon.objects.filter(selected=True)
        present = Persoon.objects.filter(absent=False)
        names = [person.short_name for person in selected]
        present_names = [person.short_name for person in present]
        return JsonResponse({"selected": names, "present": present_names})
