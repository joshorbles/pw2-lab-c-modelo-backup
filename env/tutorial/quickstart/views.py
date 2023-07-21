from django.contrib.auth.models import User, Group
from rest_framework import generics
from .models import Organization, Plan, Semester, Course, Group, Teacher, Student
from .serializers import CourseSerializer, GroupSerializer, StudentSerializer

class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentInGroupListView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Student.objects.filter(group