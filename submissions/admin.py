from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    def problem_title(self , obj):
        return obj.problem.title
    problem_title.short_description = 'Problem'

    def user_username(self , obj):
        return obj.user.username
    user_username.short_description = "User"

    def language_display_name(self , obj):
        return obj.language.display_name 
    language_display_name.short_description = "Language"

    list_display = ['problem_title' , 'user_username' , 'language_display_name' , 'status' , 'submitted_at']
    list_editable = ['status']
    search_fields = ['user__username' , 'problem__title']
    list_filter = ['status' , 'submitted_at']
