from rest_framework import serializers
from .models import User , UniversityMember , StudentProfile , TeacherProfile 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'username' , 'email' , 'first_name' , 'last_name' , 'avatar' , 'bio' , 'phone_number' , 'rating']
        read_only_fields = ['rating']


class UniversityMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityMember
        fields = '__all__'
        read_only_fields = ['user']


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"



class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = TeacherProfile
        fields = "__all__"

