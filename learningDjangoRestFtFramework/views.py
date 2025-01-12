from django.shortcuts import render

from .models import usersCollection, sequencesCollection
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse, JsonResponse

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

class Sequences(APIView):
    def getSequenceDetails(self, request):
        node = request.query_params.get('node')
        period = request.query_params.get('period')
        id = request.query_params.get('id')
        data = list(sequencesCollection.find({"node": node, "period": period, "id": id}, {"_id": 0}))
        return JsonResponse({"success": True, "data": data })

    def get(self, request):
        # list api to return all sequences.
        if(request.query_params.get('id')):
            return self.getSequenceDetails(request)
        else: 
            node = request.query_params.get('node')
            period = request.query_params.get('period')
            data = list(sequencesCollection.find_one({}, {"_id": 0})) # excluding _id
            return JsonResponse({"data": data, "success": True })
    
    def post(self, request):
        # list api to return all sequences.
        node = request.query_params.get('node')
        period = request.query_params.get('period')
        data = request.data
        document = { **data, "node": node, "period": period }
        insertedResult = sequencesCollection.insert_one(document)
        # use this json response only
        return JsonResponse({"success": True })
    def updateName(self, request):
        # list api to return all sequences.
        node = request.query_params.get('node')
        period = request.query_params.get('period')
        name = request.query_params.get('name')
        id = request.query_params.get('id')
        userData = { node: "node", period: "period", "id": id}
        insertedResult = sequencesCollection.update_one(userData, {"$set": {"name": name}})
        if (insertedResult.modified_count > 0):
            return JsonResponse({"success": True })
        else:
            return JsonResponse({"success": False })