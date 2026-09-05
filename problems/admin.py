from django.contrib import admin
from .models import Problem , TestCase ,Language

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    def created_by_username(self , obj):
        return obj.created_by.username
    created_by_username.short_description = 'User'
    list_display = ['title' , 'slug' , 'difficulty_level' , 'time_limit_ms' , 'status' , 'created_by_username' , 'created_at' , 'updated_at']
    list_editable = ['status']
    search_fields = ['title' , 'statement']
    list_filter = ['title' , 'difficulty_level' , 'status' , 'created_by' , 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Question Information : ' , 
         {'fields' : ('title' , 'slug' , 'statement' , 'difficulty_level' , 'time_limit_ms')}),
         ('Access status : ' , 
         {'fields' : ('status' ,)}),
         ('Specifications : ' , 
         {'fields' : ('created_by' , 'created_at' , 'updated_at')}),
    )


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    def problem_title(self , obj):
        return obj.problem.title
    problem_title.short_description = 'Problem'
    list_display = ['problem_title' , 'input_data' , 'expected_output' , 'is_sample' , 'order_index']
    list_editable = ['input_data' , 'expected_output' , 'is_sample' , 'order_index']
    list_filter = ['problem__title','is_sample']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['display_name' , 'code' , 'docker_image' , 'is_active']
    list_editable =  ['code' , 'docker_image' , 'is_active']
    list_filter = ['is_active']
