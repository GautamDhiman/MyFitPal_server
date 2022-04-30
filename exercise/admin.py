from django.contrib import admin
from exercise.models import BodyPart, TargetMuscle, Equipment, Exercise

# Register your models here.
admin.site.register(BodyPart)
admin.site.register(TargetMuscle)
admin.site.register(Equipment)
admin.site.register(Exercise)