from rest_framework import serializers
from study.models import *

class StudyCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCenter
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'