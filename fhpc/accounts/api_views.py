from .models import Account
from .common.encoders import AccountSerializer, AccountSerializerWPassword
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response

class AccountListApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                account = Account.objects.get(pk=pk)
                serializer = AccountSerializer(account)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return Response({'error': 'Account not found.'}, status=status.HTTP_404_NOT_FOUND)

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = AccountSerializerWPassword(data=request.data)
        if serializer.is_valid():
            # Validate password
            password = serializer.validated_data['password']
            try:
                validate_password(password)
            except ValidationError as e:
                return Response(
                    {'error': ', '.join(e.messages)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create the account object using create_user()
            account = Account.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=password,
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                zipcode=serializer.validated_data["zipcode"],
                phone_number=serializer.validated_data["phone_number"],
            )

            return Response(
                AccountSerializer(account).data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
