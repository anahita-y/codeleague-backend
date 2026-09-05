from django.db import models
from problems.models import Problem , Language
from users.models import User

class Submission(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending", "Pending"
        ACCEPTED = "Accepted", "Accepted"
        WRONG_ANSWER = "WrongAnswer", "Wrong Answer"
        TIME_LIMIT_EXCEEDED = "TimeLimitExceeded", "Time Limit Exceeded"
    problem = models.ForeignKey(Problem , on_delete = models.CASCADE , related_name = "submissions")
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "submissions")
    language = models.ForeignKey(Language , on_delete = models.PROTECT)
    source_code = models.TextField()
    status = models.CharField(max_length = 20 , choices = Status.choices , default = Status.PENDING)
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user} - {self.problem} ({self.status})"