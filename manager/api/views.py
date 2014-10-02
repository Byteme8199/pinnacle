import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import link

from manager.api.serializers import WorkoutSerializer
from manager.api.serializers import WorkoutCanonicalFormSerializer
from manager.api.serializers import DaySerializer
from manager.api.serializers import SettingSerializer
from manager.api.serializers import SetSerializer
from manager.api.serializers import ScheduleSerializer
from manager.api.serializers import WorkoutLogSerializer
from manager.api.serializers import WorkoutSessionSerializer

from manager.models import Workout
from manager.models import Set
from manager.models import ScheduleStep
from manager.models import Schedule
from manager.models import Day
from manager.models import Setting
from manager.models import WorkoutLog
from manager.models import WorkoutSession
from utils.viewsets import WgerOwnerObjectModelViewSet


class WorkoutViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for workout objects
    '''
    model = Workout
    serializer_class = WorkoutSerializer
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('comment',
                     'creation_date')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return Workout.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        '''
        Set the owner
        '''
        obj.user = self.request.user

    @link()
    def canonical_representation(self, request, pk):
        '''
        Output the canonical representation of a workout

        This is basically the same form as used in the application
        '''

        out = WorkoutCanonicalFormSerializer(self.get_object().canonical_representation).data
        return Response(out)


class WorkoutSessionViewSet(WgerOwnerObjectModelViewSet):
    '''
    API endpoint for workout sessions objects
    '''
    model = WorkoutSession
    serializer_class = WorkoutSessionSerializer
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('date',
                     'workout',
                     'notes',
                     'impression',
                     'time_start',
                     'time_end')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return WorkoutSession.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        '''
        Set the owner
        '''
        obj.date = datetime.date.today()  # TODO: actually, this should be editable
        obj.user = self.request.user

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(Workout, 'workout')]


class ScheduleStepViewSet(WgerOwnerObjectModelViewSet):
    '''
    API endpoint for schedule step objects
    '''

    model = ScheduleStep
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('schedule',
                     'workout',
                     'duration',
                     'order')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return ScheduleStep.objects.filter(schedule__user=self.request.user)

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(Workout, 'workout'),
                (Schedule, 'schedule')]


class ScheduleViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for schedule objects
    '''
    model = Schedule
    serializer_class = ScheduleSerializer
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('is_active',
                     'is_loop',
                     'start_date',
                     'name')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return Schedule.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        '''
        Set the order
        '''
        obj.user = self.request.user


class DayViewSet(WgerOwnerObjectModelViewSet):
    '''
    API endpoint for training day objects
    '''
    model = Day
    serializer_class = DaySerializer
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('description',
                     'training',
                     'day')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return Day.objects.filter(training__user=self.request.user)

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(Workout, 'training')]


class SetViewSet(WgerOwnerObjectModelViewSet):
    '''
    API endpoint for workout set objects
    '''
    model = Set
    serializer_class = SetSerializer
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('exerciseday',
                     'order',
                     'sets',
                     'exercises')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return Set.objects.filter(exerciseday__training__user=self.request.user)

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(Day, 'exerciseday')]


class SettingViewSet(WgerOwnerObjectModelViewSet):
    '''
    API endpoint for repetition setting objects
    '''
    model = Setting
    serializer_class = SettingSerializer
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('exercise',
                     'order',
                     'reps',
                     'set',
                     'order')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return Setting.objects.filter(set__exerciseday__training__user=self.request.user)

    def pre_save(self, obj):
        '''
        Set the order
        '''
        obj.order = 1

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(Set, 'set')]


class WorkoutLogViewSet(WgerOwnerObjectModelViewSet):
    '''
    API endpoint for workout log objects
    '''
    model = WorkoutLog
    serializer_class = WorkoutLogSerializer
    is_private = True
    ordering_fields = '__all__'
    filter_fields = ('date',
                     'exercise',
                     'reps',
                     'weight',
                     'workout')

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''

        return WorkoutLog.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        '''
        Set the order
        '''
        obj.user = self.request.user

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(Workout, 'workout')]
