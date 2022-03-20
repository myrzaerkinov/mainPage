from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status
from datetime import date, datetime
from business_accounts.models import SalonService



class CreateListRecordsAPIView(APIView):
    def get(self, request):
        model = models.Records.objects.all()
        data = serializers.RecordsSerializers(model, many=True).data
        return Response(data=data)

    def post(self, request):
        serializer = serializers.CreateRecordsAPIViewSerializer(data= request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status = status.HTTP_406_NOT_ACCEPTABLE)
        user_id = request.data.get('user_id')
        data = request.data.get('data')
        time = request.data.get('time')
        price = request.data.get('price')
        promo_code = request.data.get('promo_code')
        staff_id = request.data.get('staff_id')
        service_id = request.data.get('service_id')
        if models.Records.objects.filter(data=data, time=time).count() == 0 and datetime.now() < datetime.strptime(data+time, "%Y-%m-%d%H:%M"):
            records = models.Records.objects.create(user_id=user_id,data=data, time=time, price=price,promo_code=promo_code,staff_id=staff_id, service_id=service_id)
        else:
            return Response(data ={'message': 'Дата с таким временем уже занята!'})
        return Response(data= serializers.RecordsSerializers(records).data, status=status.HTTP_201_CREATED)


        # or date_now.time() < datetime.strptime(time)

        # if models.Records.objects.filter(data=data, time=time).count() == 0:    
        #     records = models.Records.objects.create(user_id=user_id,data=data, time=time, price=price,promo_code=promo_code,staff_id=staff_id, service_id=service_id)
        # else:
        #     return Response(data ={'message': 'Дата с таким временем уже занята!'})
        # return Response(data= serializers.RecordsSerializers(records).data, status=status.HTTP_201_CREATED)

