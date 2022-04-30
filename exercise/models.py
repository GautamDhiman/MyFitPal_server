from django.db import models

# Create your models here.
class BodyPart(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TargetMuscle(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    target_muscle = models.ForeignKey(TargetMuscle, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name