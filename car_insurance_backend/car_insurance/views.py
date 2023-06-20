from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.test import TestCase
from .serializers import *
from rest_framework.test import APIClient
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        #serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    client.DateDel = datetime.now()
    client.save()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





