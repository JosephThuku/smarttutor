from django.contrib.auth.models import User
from django.db import models

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    learning_style = models.CharField(max_length=20, choices=LEARNING_STYLES)
    skill_level = models.JSONField(default=dict)  # {"math": "advanced", ...}
    progress = models.JSONField(default=dict)

class Concept(models.Model):
    topic = models.CharField(max_length=255)
    simple_explanation = models.TextField()
    detailed_explanation = models.TextField()
    advanced_explanation = models.TextField()
    visual_aid = models.FileField(upload_to='visuals/')

class StudentInteraction(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    questions_asked = models.JSONField(default=list)
    quiz_results = models.JSONField(default=dict)