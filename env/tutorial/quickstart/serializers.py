# serializers.py

from rest_framework import serializers
from .models import Plan, Semester, Course, Group, Teacher, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.course_name')
    teacher_name = serializers.CharField(source='teacher.teacher_name')

    class Meta:
        model = Group
        fields = ['plan', 'semester', 'course_name', 'hours_lab', 'group_name', 'teacher_name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['cui', 'user_id__user_last_name', 'user_id__user_name', 'user_id__user_email']