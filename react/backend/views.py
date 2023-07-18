from django.shortcuts import render
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse

from . models import Info
from . serializers import InfoSerializer
# Create your views here.
@csrf_exempt
def info_list(request,location=None):
    if request.method == 'GET':
        if location is not None:
            try:
                info = Info.objects.get(country_name=location)
                serializer = InfoSerializer(info)
                return JsonResponse(serializer.data)
            except Info.DoesNotExist:
                return JsonResponse({'error': 'Location does not exist'})
        info = Info.objects.all()
        serializer = InfoSerializer(info, many=True)
        return JsonResponse(serializer.data,safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InfoSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  JsonResponse(serializer.data,status=201)
        
        return JsonResponse(serializer.errors,status=400)
   