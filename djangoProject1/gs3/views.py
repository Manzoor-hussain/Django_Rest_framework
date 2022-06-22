import io

from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Student

from .serializer import StudentSerializer


# Create your views here.
def student_api(request):
    if request.method == 'GET':

        # json_data = JSONRenderer.render(data)

        json_data = request.body
        print(json_data)
        print('khan')
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        print(id)
        print ('yesii')
        if id is not None:
            stu = Student.objects.get(id=id)

            serializer = StudentSerializer(stu)
            print(serializer.data)
            #return JsonResponse(serializer.data, safe=True)
            data = { 'msgt':'gettting data'}

            json_data = JSONRenderer.render(serializer.data,data)
            return HttpResponse(json_data, content_type='application/json')

        # serializer = StudentSerializer(stu, many=True)
        # return HttpResponse(json_data, content_type='application/json')
