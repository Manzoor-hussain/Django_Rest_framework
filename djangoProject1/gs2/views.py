import io

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Student

from .serializer import StudentSerializer
from rest_framework.response import Response


# Create your views here.
@api_view()
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)

        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "data is created"}
            print("here")
            #json_data = JSONRenderer.render(res)
            #return HttpResponse(json_data, content_type='application/json')
            return Response(data=serializer.data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        print(id)
        if id is not None:
            stu = Student.objects.get(id=id)

            serializer = StudentSerializer(stu)
            data=serializer.data
            json_data = JSONRenderer.render(data)
            return HttpResponse(json_data, content_type='application/json')