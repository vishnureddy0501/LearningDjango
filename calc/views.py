import json
from django.shortcuts import render
from .models import usersCollection

# Create your views here.

from django.http import HttpResponse, JsonResponse

# Define a view that returns 'Hello world'
def home(request):
    return HttpResponse('Hello world')
# Define a view that returns 'Hello world'

def root(request):
    return HttpResponse('Root Page')

def getAllUsers(request):
    users = usersCollection.find()
    return HttpResponse(users)

def insertUser(request):
    try:
        result = usersCollection.insert_one({"name": "vishnu", "age": 20, "email": "helloreddy@gmail.com"})
        return JsonResponse({"success": True, "inserted_id": str(result.inserted_id)})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})

def handle_get_request(request):
    name = request.GET.get('name', 'default_name')
    age = request.GET.get('age', 'unknown')
    return JsonResponse({"success": True, "name": name, "age": age})

def handle_post_request(request):
    body_data = json.loads(request.body)
    name = body_data.get('name')
    age = body_data.get('age')
    email = body_data.get('email')
    print(name, age, email)
    return JsonResponse({"success": True, "name": name, "age": age})

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def test_view(request):
    return Response({"message": "Django REST Framework is installed!"})


