from rest_framework import serializers

from datawar.models import Person, PersonVehicle, Vehicle


class VehicleSerializer(serializers.Serializer):

    registration_plate = serializers.CharField(max_length=100)


class PersonVehicleSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    vehicles = VehicleSerializer(many=True)

    def save(self):
        person_obj, created = Person.objects.update_or_create(
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"]
        )

        for vehicle in self.validated_data["vehicles"]:
            vehicle_obj, created = Vehicle.objects.get_or_create(
                registration_plate=vehicle["registration_plate"])
            personvehicle_obj, created = PersonVehicle.objects.update_or_create(
                vehicle=vehicle_obj, defaults={"person": person_obj}
            )
