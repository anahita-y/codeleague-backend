from django.db import models
from django.utils.text import slugify
from users.models import User
class Problem(models.Model):
    class DifficultyLevel(models.TextChoices):
        EASY = "Easy" ,"Easy"
        MEDIUM = "Medium" , "Medium"
        HARD = "Hard" , "Hard"

    class Status(models.TextChoices):
        DRAFT = "Draft" , "Draft"
        PUBLISHED = "Published" , "Published"

    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 220 , unique = True)
    statement = models.TextField()
    difficulty_level = models.CharField(max_length = 10 ,choices = DifficultyLevel.choices , default = DifficultyLevel.EASY)
    time_limit_ms = models.IntegerField(default = 1000)
    memory_limit_mb = models.IntegerField(default = 256)
    status = models.CharField(max_length = 20 , choices = Status.choices , default = Status.DRAFT)
    created_by = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "problems")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args , **kwargs)
    
class TestCase(models.Model):
    class Meta:
        ordering = ["order_index"]
    problem = models.ForeignKey(Problem , on_delete = models.CASCADE , related_name = "test_cases")
    input_data = models.TextField()
    expected_output = models.TextField()
    is_sample = models.BooleanField(default = False)
    order_index = models.IntegerField(default = 0)

    def __str__(self):
        return f"TestCase for {self.problem}"

class Language(models.Model):
    display_name = models.CharField(max_length = 50 , unique = True )
    code = models.CharField(max_length = 20 , unique = True)
    compile_command = models.TextField(null = True , blank = True)
    run_command = models.TextField()
    docker_image = models.CharField(max_length = 150)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.display_name

