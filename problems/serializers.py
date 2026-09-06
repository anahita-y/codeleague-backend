from rest_framework import serializers
from .models import Problem , TestCase , Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
        read_only_fields = ['created_by' , 'slug' , 'created_at' , 'updated_at']



class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'


