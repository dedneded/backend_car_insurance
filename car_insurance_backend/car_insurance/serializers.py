from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    DateDel = serializers.DateTimeField(allow_null=True, required=False)

    class Meta:
        model = Client
        fields = ['Phone', 'Email', 'DateAdd', 'DateDel']


class EmployeeSerializer(serializers.ModelSerializer):
    DateDel = serializers.DateTimeField(allow_null=True, required=False)

    class Meta:
        model = Employee
        fields = ['FIO', 'Phone', 'Email', 'DateAdd', 'DateDel']


class PassportPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportPhoto
        fields = '__all__'


class PassportSerializer(serializers.ModelSerializer):
    Photos = PassportPhotoSerializer(many=True, read_only=False)

    class Meta:
        model = Passport
        fields = ['IssuedByWhom', 'DateOfIssue', 'DivisionCode', 'Series', 'Number', 'FIO', 'IsMale',
                  'DateOfBirth', 'PlaceOfBirth', 'ResidenceAddress', 'Client', 'Photos']


class LicensePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensePhoto
        fields = '__all__'


class LicenseSerializer(serializers.ModelSerializer):
    Photos = LicensePhotoSerializer(many=True, read_only=False)

    class Meta:
        model = License
        fields = ['DateOfIssue', 'ExpirationDate', 'CodeGIBDD', 'Series', 'Number', 'TransmissionType',
                  'VehicleCategories', 'Client', 'Photos']


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    Photos = CarPhotoSerializer(many=True, read_only=False)

    class Meta:
        model = Car
        fields = ['RegistrationNumber', 'IdNumber', 'Brand', 'Model', 'TCType', 'TCCategory', 'YearOfIssue',
                  'EngineModel', 'EngineNumber', 'ChassisNumber', 'CarBodyNumber', 'Color', 'EnginePower',
                  'EngineDisplacement', 'Series', 'Number', 'MaxWeightPermitted', 'WeightWithoutCapacity',
                  'NameOwner', 'PlaceRegistration', 'PlaceOfIssue', 'DateOfIssue', 'Client', 'Photos']


