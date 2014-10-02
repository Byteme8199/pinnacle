from rest_framework import serializers

from manager.models import Workout
from manager.models import Day
from manager.models import Setting
from manager.models import Set
from manager.models import Schedule
from manager.models import WorkoutLog
from manager.models import WorkoutSession


class WorkoutSerializer(serializers.ModelSerializer):
    '''
    Workout serializer
    '''

    class Meta:
        model = Workout
        exclude = ('user',)


class WorkoutSessionSerializer(serializers.ModelSerializer):
    '''
    Workout session serializer
    '''
    class Meta:
        model = WorkoutSession
        exclude = ('user',)


class WorkoutLogSerializer(serializers.ModelSerializer):
    '''
    Workout session serializer
    '''
    class Meta:
        model = WorkoutLog
        exclude = ('user',)


class ScheduleSerializer(serializers.ModelSerializer):
    '''
    Schedule serializer
    '''
    class Meta:
        model = Schedule
        exclude = ('user',)


class DaySerializer(serializers.ModelSerializer):
    '''
    Workout day serializer
    '''

    class Meta:
        model = Day


class SetSerializer(serializers.ModelSerializer):
    '''
    Workout setting serializer
    '''

    class Meta:
        model = Set


class SettingSerializer(serializers.ModelSerializer):
    '''
    Workout setting serializer
    '''
    class Meta:
        model = Setting


#
# Custom helper serializers for the canonical form of a workout
#
class WorkoutCanonicalFormExerciseListSerializer(serializers.Serializer):
    '''
    Serializer for settings in the canonical form of a workout
    '''
    setting_obj_list = SettingSerializer(many=True)
    setting_list = serializers.Field()
    setting_text = serializers.Field()
    comment_list = serializers.Field()


class WorkoutCanonicalFormExerciseSerializer(serializers.Serializer):
    '''
    Serializer for an exercise in the canonical form of a workout
    '''
    obj = SetSerializer()
    exercise_list = WorkoutCanonicalFormExerciseListSerializer()
    has_settings = serializers.BooleanField()
    is_superset = serializers.BooleanField()
    muscles = serializers.Field()


class DayCanonicalFormSerializer(serializers.Serializer):
    '''
    Serializer for a day in the canonical form of a workout
    '''
    obj = DaySerializer()
    set_list = WorkoutCanonicalFormExerciseSerializer(many=True)
    days_of_week = serializers.Field()
    muscles = serializers.Field()


class WorkoutCanonicalFormSerializer(serializers.Serializer):
    '''
    Serializer for the canonical form of a workout
    '''
    obj = WorkoutSerializer()
    muscles = serializers.Field()
    day_list = DayCanonicalFormSerializer(many=True)
