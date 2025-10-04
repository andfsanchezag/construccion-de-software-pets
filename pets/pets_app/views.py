import base64
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from .models import Pet
import json


def encrypt_document(document):
    return base64.b64encode(document.encode()).decode()

def decrypt_document(document_enc):
    return base64.b64decode(document_enc.encode()).decode()

@method_decorator(csrf_exempt, name='dispatch')
class PetView(View):
    def get(self, request, pet_id=None, documento=None):
        if pet_id:
            try:
                pet = Pet.objects.get(id=pet_id)
                data = {
                    "id": pet.id,
                    "name": pet.name,
                    "species": pet.species,
                    "age": pet.age,
                    "owner": pet.owner,
                    "breed": pet.breed,
                    "characteristics": pet.characteristics,
                    "weight": pet.weight,
                    "owner_document": decrypt_document(pet.owner_document)
                }
                return JsonResponse(data)
            except Pet.DoesNotExist:
                return HttpResponseNotFound("Pet not found")
        elif documento:
            enc_doc = encrypt_document(documento)
            pets = Pet.objects.filter(owner_document=enc_doc)
            data = [
                {
                    "id": pet.id,
                    "name": pet.name,
                    "species": pet.species,
                    "age": pet.age,
                    "owner": pet.owner,
                    "breed": pet.breed,
                    "characteristics": pet.characteristics,
                    "weight": pet.weight,
                    "owner_document": documento
                }
                for pet in pets
            ]
            return JsonResponse(data, safe=False)
        else:
            return HttpResponseBadRequest("Missing pet_id or documento")

    def post(self, request):
        try:
            data = json.loads(request.body)
            required_fields = ["id", "name", "species", "age", "owner", "breed", "characteristics", "weight", "owner_document"]
            for field in required_fields:
                if field not in data:
                    return HttpResponseBadRequest(f"Missing field: {field}")
            pet = Pet.objects.create(
                id=data["id"],
                name=data["name"],
                species=data["species"],
                age=data["age"],
                owner=data["owner"],
                breed=data["breed"],
                characteristics=data["characteristics"],
                weight=data["weight"],
                owner_document=encrypt_document(data["owner_document"])
            )
            return JsonResponse({"message": "Pet created", "id": pet.id})
        except Exception as e:
            return HttpResponseBadRequest(str(e))

    def put(self, request, pet_id):
        try:
            pet = Pet.objects.get(id=pet_id)
            data = json.loads(request.body)
            for field in ["name", "species", "age", "owner", "breed", "characteristics", "weight", "owner_document"]:
                if field in data:
                    if field == "owner_document":
                        setattr(pet, field, encrypt_document(data[field]))
                    else:
                        setattr(pet, field, data[field])
            pet.save()
            return JsonResponse({"message": "Pet updated", "id": pet.id})
        except Pet.DoesNotExist:
            return HttpResponseNotFound("Pet not found")
        except Exception as e:
            return HttpResponseBadRequest(str(e))