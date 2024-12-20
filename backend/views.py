from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Destination, Continent
from .serializers import DestinationSerializer, ContinentSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegisterUser(APIView):
    """
    API endpoint to handle user registration.
    Creates a new user and generates a token for authentication.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    """
    API endpoint to handle user login.
    Authenticates user credentials and provides a token upon success.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(APIView):
    """
    API endpoint to handle user logout.
    Deletes the user's token to log them out.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class DestinationList(APIView):
    """
    API endpoint to list or create destinations for the authenticated user.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        destinations = Destination.objects.filter(user=request.user)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = DestinationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DestinationDetail(APIView):
    """
    API endpoint to retrieve, update, or delete a specific destination for the authenticated user.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        destination = get_object_or_404(Destination, pk=pk, user=request.user)
        serializer = DestinationSerializer(destination)
        return Response(serializer.data)

    def put(self, request, pk):
        destination = get_object_or_404(Destination, pk=pk, user=request.user)

        # Ensure the user field remains the same
        data = request.data
        data['user'] = request.user.id

        serializer = DestinationSerializer(destination, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        destination = get_object_or_404(Destination, pk=pk, user=request.user)
        destination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContinentViewSet(ModelViewSet):
    """
    API endpoint to list, retrieve, create, update, or delete continents.
    Requires authentication.
    """
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []