from django.http import JsonResponse
from .models import Specie

def get(request):
    species = Specie.objects.all().values()
    return JsonResponse(list(species), safe=False)

def getById(request, specie_id):
    # specie = Specie.objects.get(pk=specie_id)
    return JsonResponse({'id': specie_id})

# Leave the rest of the views (detail, results, vote) unchanged
