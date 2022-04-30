from django.shortcuts import render
from rest_framework.views import APIView
from exercise.managers.exercise_manager import ExerciseManager
from rest_framework.response import Response
import csv
import os
from django.http import HttpResponse
from .models import *

# Create your views here.
class GetBodyParts(APIView):

    def __init__(self):
        super(GetBodyParts, self).__init__()
        self.exercise_manager = ExerciseManager()
        
    def get(self, request):
        bodyparts = self.exercise_manager.get_bodyparts()
        print(bodyparts)
        data = {
            'bodyparts': bodyparts,
        }
        for bodypart in bodyparts:
            obj = BodyPart(name=bodypart)
            obj.save()

        return Response(data, status=200)

class GetTargetMuscle(APIView):

    def __init__(self):
        super(GetTargetMuscle, self).__init__()
        self.exercise_manager = ExerciseManager()
        
    def get(self, request):
        target_muscles = self.exercise_manager.get_target_muscles()
        print(target_muscles)
        data = {
            'target_muscles': target_muscles,
        }
        for muscle in target_muscles:
            obj = TargetMuscle(name=muscle)
            obj.save()

        return Response(data, status=200)

class GetEquipments(APIView):

    def __init__(self):
        super(GetEquipments, self).__init__()
        self.exercise_manager = ExerciseManager()
        
    def get(self, request):
        equipments = self.exercise_manager.get_equipments()
        print(equipments)
        data = {
            'equipments': equipments,
        }
        for tool in equipments:
            obj = Equipment(name=tool)
            obj.save()

        return Response(data, status=200)

class GetExercises(APIView):

    def __init__(self):
        super(GetExercises, self).__init__()
        self.exercise_manager = ExerciseManager()
        
    def get(self, request):
        exercise_dump = self.exercise_manager.get_exercises()
        # print(exercises)
        data = {
            'exercises': exercise_dump,
        }

        for exercise in exercise_dump:
            obj = Exercise(
                name=exercise.get('name'),
                equipment=Equipment.objects.get(name=exercise.get('equipment')),
                body_part=BodyPart.objects.get(name=exercise.get('bodyPart')),
                target_muscle=TargetMuscle.objects.get(name=exercise.get('target'))
            )
            obj.save()
        # print(exercise_dump[0].get('name'))
        # print(exercise_dump[0].get('bodyPart'))
        # print(exercise_dump[0].get('target'))
        # print(exercise_dump[0].get('equipment'))

        return Response(data, status=200)