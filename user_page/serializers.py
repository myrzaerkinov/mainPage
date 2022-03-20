from django.forms import ValidationError
from rest_framework import serializers
from . import models
from user.models import User
from business_accounts.models import Staff, SalonService


class RecordsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Records
        fields = '__all__'


class CreateRecordsAPIViewSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    data = serializers.DateField()
    time = serializers.TimeField()
    price = serializers.IntegerField()

    staff_id = serializers.IntegerField()
    service_id = serializers.IntegerField()

    def validate_user_id(self, id):
        try:
            User.objects.get(id=id)
        except:
            raise ValidationError(f'ID Error')
        return id
    
    def validate_staff_id(self, id):
        try:
            Staff.objects.get(id=id)
        except:
            raise ValidationError(f'ID Error')
        return id

    def validate_service_id(self, id):
        try:
            SalonService.objects.get(id=id)
        except:
            raise ValidationError(f'ID Error')
        return id