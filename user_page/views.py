from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from datetime import datetime
from business_accounts.models import SalonService,\
    Staff, Records, PromoCode, TimeRecords, StaffTimetable, BusinessAccount, Category
import calendar
from django.db.models import Avg, Count
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView


class CreateListRecordsAPIView(APIView):
    def get(self, request):
        model = Records.objects.all()
        data = serializers.RecordsSerializers(model, many=True).data
        return Response(data=data)

    def post(self, request):
        serializer = serializers.CreateRecordsAPIViewSerializer(data= request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status = status.HTTP_406_NOT_ACCEPTABLE)
        user_id = request.data.get('user_id')
        data = request.data.get('data')
        time = request.data.get('time')
        staff_id = request.data.get('staff_id')
        service_id = request.data.get('service_id')
        businessaccount_id = request.data.get('businessaccount_id')
        promo_code = request.data.get('promo_code')
        service = SalonService.objects.get(id = service_id)


        if promo_code == None:
            price = service.price
            discount = 0
        elif PromoCode.objects.filter(promo_code = promo_code).count() == 0:
                return Response(data={'message': 'Такого промокода не существует!'})
        else:
            promocode = PromoCode.objects.get(promo_code = promo_code)
            discount = promocode.discount
            price = (service.price - discount)
        if Records.objects.filter(data=data, time=time, staff_id=staff_id).count() == 0 and datetime.now() < datetime.strptime(data+time, "%Y-%m-%d%H:%M"):
            records = Records.objects.create(user_id=user_id,data=data, time=time,promo_code=promo_code, discount=discount, price= price, staff_id=staff_id, service_id=service_id, businessaccount_id=businessaccount_id)
        else:
            return Response(data ={'message': 'Дата с таким временем уже занята!'})
        return Response(data= serializers.RecordsSerializers(records).data, status=status.HTTP_201_CREATED)




class ListTimeRecordsAPIView(APIView):
    def get(self, request, id):
        if request.GET.get('data') != None:
            date = request.GET.get('data')
        else:
            date = datetime.now()
        model = TimeRecords.objects.filter(staff_id=id)
        free_time = []
        for i in model:
            if Records.objects.filter(time= i.time, data=date).count() ==0:
                free_time.append(i)
        return Response(data=[{'free_time': i.time} for i in free_time])
        

class ListFreeDayAPIView(APIView):
    def get(self, request, id):
        model = TimeRecords.objects.filter(staff_id=id)
        day_off = StaffTimetable.objects.get(staff_id = id)
        day = {}
        if request.GET.get('data') !=None:
            date = datetime.strptime(request.GET.get('data'), "%Y-%m-%d")
        else:
            date = datetime.now()
        for i in range(1, calendar.monthrange(date.year, date.month)[1]+1):
            d = f'{date.year}-{date.month}-{i}'
            if datetime.strptime(d, "%Y-%m-%d") < date.now() or int(day_off.day_off) == datetime.strptime(d, "%Y-%m-%d").weekday():
                day[d] = "gray_day"
            elif Records.objects.filter(data =d, staff_id = id).count() == len(model):
                day[d] = "red_day"
            else:
                day[d] = "green_day"
        return Response(data=day)


class ListUserRecordsAPIView(APIView):
    def get(self, request, id):
        model = Records.objects.filter(staff_id=id)
        data = serializers.ListUserRecordsAPIViewSerializers(model, many=True).data
        return Response(data=data)

class ListCategoryAPIView(APIView):
    def get(self, request, id):
        model = Category.objects.filter(id=id)
        data = serializers.CategoryAPIViewSerializers(model, many=True).data
        return Response(data=data)

class CategoryListAPIView(APIView):
    def get(self, request):
        model = Category.objects.all()
        data = serializers.CategoryAPIViewSerializers(model, many=True).data
        return Response(data=data)

class ListSalonAPIView(APIView):
    def get(self, request, id):
        model = BusinessAccount.objects.filter(id=id)
        data = serializers.BusinessAccountAPIViewSerializers(model, many=True).data
        return Response(data=data)

class SalonListAPIView(APIView):
    def get(self, request):
        model = BusinessAccount.objects.annotate(rtg=Count('rating')
                                               ).order_by('-rtg')
        data = serializers.BusinessAccountAPIViewSerializers(model, many=True).data
        return Response(data=data)
from user_page.serializers import BusinessAccountAPIViewSerializers

class SearchSalonAPIView(ListCreateAPIView):
    queryset = BusinessAccount.objects.all()
    serializer_class = BusinessAccountAPIViewSerializers
    filter_fields = ['*']