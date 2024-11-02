from django.db import models

# Create your models here.
ANSWER_CHOICES = [
    ('a', 'optionA'),
    ('b', 'optionB'),
    ('c', 'optionC'),
    ('d', 'optionD'),
]

class QuizQuestion(models.Model):
    question_statement  = models.TextField()
    optionA             = models.CharField(max_length=250)
    optionB             = models.CharField(max_length=250)
    optionC             = models.CharField(max_length=250)
    optionD             = models.CharField(max_length=250)
    correct_ans         = models.CharField(choices=ANSWER_CHOICES, max_length=20)