from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
import json
from pets.models import Pet
#from accounts.models import Pet
from .common.encoders import PetSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class PetApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                account = Pet.objects.get(pk=pk)
                serializer = PetSerializer(account)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            except Pet.DoesNotExist:
                return Response({
                    'error': 'Account not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    def post (self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            pet = Pet.objects.create_user(
                name=serializer.validated_data['name'],
                breed=serializer.validated_data['breed'],
                age=serializer.validated_data['age'],
                weight=serializer.validated_data['weight'],
                #owner=owner
            )
            pass