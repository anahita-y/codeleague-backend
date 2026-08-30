from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.CharField(max_length = 255 , null = True , blank = True)
    bio = models.TextField(null = True , blank = True)
    phone_number = models.CharField(max_length = 15 , null = True , blank = True , unique = True)
    rating = models.IntegerField(default=1500)

    def __str__(self):
        return self.username

class UniversityMember(models.Model):
    class MemberType(models.TextChoices):
        TEACHER = "Teacher" ,"Teacher"
        STUDENT = "Student" , "Student"
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    faculty = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100 , null = True , blank = True)
    member_type = models.CharField(max_length = 20 ,choices = MemberType.choices , default = MemberType.STUDENT)
    joined_at = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default =  True)
    def __str__(self):
        return self.member_type


class StudentProfile(models.Model):
    university_member =  models.OneToOneField(UniversityMember , on_delete = models.CASCADE)
    student_number = models.CharField(max_length = 20 , unique = True)
    major = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 20)
    entry_year = models.IntegerField()

    def __str__(self):
        return self.student_number

class TeacherProfile(models.Model):
    university_member = models.OneToOneField(UniversityMember , unique = True , on_delete = models.CASCADE)
    employee_number = models.CharField(max_length = 20 , unique = True)
    academic_rank = models.CharField(max_length = 30 , null = True , blank = True)
    office = models.CharField(max_length = 20 , null = True , blank =  True)

    def __str__(self):
        return self.employee_number

class RefreshToken(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    token_hash = models.CharField(max_length = 255 , unique = True)
    device_info = models.CharField(max_length = 255, null = True , blank = True)
    issued_at = models.DateTimeField(auto_now_add = True)
    expires_at = models.DateTimeField()
    is_revoked = models.BooleanField(default = False)
