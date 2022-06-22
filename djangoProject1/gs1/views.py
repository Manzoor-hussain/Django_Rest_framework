import io

from django.shortcuts import render
from rest_framework.serializers import Serializer
# Create your views here.
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import responses
from django.views.decorators.csrf import csrf_exempt

from gs1.serializers import StudentSerializer
from django.http import HttpResponse


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            json_data = JSONRenderer.render(res , serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
