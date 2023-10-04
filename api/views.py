from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import *
from .permissions import *
from study.models import *

@api_view(['GET', 'POST'])
@permission_classes([StudyCenterPermission])
def studycenter(request):
    if request.method == 'GET':
        centers = StudyCenter.objects.all()
        serializer = StudyCenterSerializer(centers, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudyCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([StudyCenterDetailPermission])
def studycenter_detail(request, pk):
    center = StudyCenter.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = StudyCenterSerializer(center)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudyCenterSerializer(center, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        center.delete()
        return Response(status=HTTP_204_NO_CONTENT)
   

@api_view(['GET', 'POST'])
@permission_classes([TeacherPermission])
def teacher(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TeacherDetailPermission])
def teacher_detail(request, pk):

    teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    
    elif request.method == 'PUT':
        serializer = StudyCenterSerializer(teacher)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentrSerializer(students, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = StudentrSerializer(student)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudentrSerializer(student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)