from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pet
import json

# Create your views here.
@csrf_exempt
def create_pet(request):
    if request.method == 'POST':
        # Assuming the request contains JSON data for the pet
        data = json.loads(request.body)
        pet = Pet(
            id=data.get('id'),
            name=data.get('name'),
            species=data.get('species'),
            age=int(data.get('age')),
            owner=int(data.get('owner')),
            breed=data.get('breed'),
            characteristics=data.get('characteristics'),
            weight=float(data.get('weight'))
        )
        pet.save()
        return JsonResponse({'message': 'Pet created successfully'}, status=201)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=405)

def ping(request):
    return JsonResponse({'message': 'pong'}, status=200)