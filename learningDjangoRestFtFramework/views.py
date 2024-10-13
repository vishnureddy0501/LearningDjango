from django.shortcuts import render

from .models import usersCollection
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework import status

class UsersView(APIView):
    # GET: Fetch all users
    def get(self, request):
        users = list(usersCollection.find({}, {'_id': 0}))  # Exclude _id from the result
        return Response(users, status=status.HTTP_200_OK)

    # POST: Create a new user
    def post(self, request):
        user_data = request.data
        result = usersCollection.insert_one(user_data)
        return Response({"message": "User created", "user_id": str(result.inserted_id)}, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    
    # GET: Fetch a specific user by email
    def get(self, request):
        email = request.query_params.get('email')
        user = usersCollection.find_one({"email": email}, {'_id': 0})
        if user:
            return Response(user, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE: Delete a user by email
    def delete(self, request):
        email = request.query_params.get('email')
        result = usersCollection.delete_one({"email": email})
        if result.deleted_count == 1:
            return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

# this is an example of functional type view
@api_view(['DELETE'])
def delete_user(request):
    email = request.query_params.get('email')
    result = usersCollection.delete_one({"email": email})
    if result.deleted_count == 1:
        return Response({"message": "User deleted successfully"})
    else:
        return Response({"error": "User not found"})