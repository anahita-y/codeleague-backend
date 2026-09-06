from rest_framework import viewsets , permissions
from .models import User , UniversityMember , StudentProfile , TeacherProfile
from .serializers import (UserSerializer , 
    UniversityMemberSerializer , 
    StudentProfileSerializer , 
    TeacherProfileSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id = self.request.user.id)


class UniversityMemberViewSet(viewsets.ModelViewSet):
    queryset = UniversityMember.objects.all()
    serializer_class = UniversityMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return StudentProfile.objects.all()
        return StudentProfile.objects.filter(university_member__user = self.request.user)
    

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return TeacherProfile.objects.all()
        return TeacherProfile.objects.filter(university_member__user = self.request.user)