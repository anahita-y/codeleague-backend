from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UniversityMember, StudentProfile, TeacherProfile, RefreshToken


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'rating', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        ('Supplementary Information', {'fields': ('avatar', 'bio', 'phone_number', 'rating')}),
    )

@admin.register(UniversityMember)
class UniversityMemberAdmin(admin.ModelAdmin):
    list_display = ['user' , 'faculty' , 'department' , 'member_type' , 'joined_at' , 'is_active']
    list_editable = ['is_active']
    search_fields = ['faculty','department','user__username']
    list_filter = ['joined_at' , 'is_active']


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['university_member' , 'student_number' , 'major' , 'degree' , 'entry_year']
    search_fields = ['student_number' , 'major' , 'degree']
    list_filter = ['entry_year', 'degree']


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ['university_member' , 'employee_number' , 'academic_rank' , 'office']
    search_fields = ['employee_number' , 'academic_rank' , 'office']
    list_filter = ['academic_rank']


@admin.register(RefreshToken)
class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ['user' , 'device_info' , 'issued_at' , 'expires_at' , 'is_revoked']
    list_editable = ['is_revoked']
    search_fields = ['device_info']
    list_filter = ['issued_at' , 'expires_at' , 'is_revoked']