from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    print(stu)
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)
    data = serializer.data
    #json_data = JSONRenderer.render(serializer.data)
    return JsonResponse(data, safe=False)
    #return HttpResponse(json_data , content_type='application/json')


def student_list(request):
    stu = Student.objects.all()

    serializer = StudentSerializer(stu , many= True)
    data = serializer.data
    # json_data = JSONRenderer.render(data)
    return JsonResponse(data, safe=False)
