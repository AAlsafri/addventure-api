from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Destination
from .serializers import DestinationSerializer


class DestinationList(APIView):
    """
    Handles listing and creating destinations.
    """

    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DestinationDetail(APIView):
    """
    Handles retrieving, updating, and deleting a specific destination.
    """

    def get(self, request, pk):
        destination = get_object_or_404(Destination, pk=pk)
        serializer = DestinationSerializer(destination)
        return Response(serializer.data)

    def put(self, request, pk):
        destination = get_object_or_404(Destination, pk=pk)
        serializer = DestinationSerializer(destination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        destination = get_object_or_404(Destination, pk=pk)
        destination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)