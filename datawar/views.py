from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datawar.serializers import PersonVehicleSerializer


@api_view(["POST"])
def PersonVehicle(request):

    ser = PersonVehicleSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    ser.save()

    return Response({"Serialization done"})
