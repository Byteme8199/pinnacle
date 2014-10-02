from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authentication import MultiAuthentication
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from core.api.resources import DaysOfWeekResource
from exercises.api.resources import ExerciseResource
from utils.resources import UserObjectsOnlyAuthorization
from manager.models import WorkoutSession
from manager.models import Workout
from manager.models import Schedule
from manager.models import ScheduleStep
from manager.models import Day
from manager.models import Set
from manager.models import Setting
from manager.models import WorkoutLog


class WorkoutResource(ModelResource):
    '''
    Resource for workouts
    '''

    days = fields.ToManyField('manager.api.resources.DayResource', 'day_set')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(user=bundle.request.user)

    class Meta:
        queryset = Workout.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     "comment": ALL,
                     "creation_date": ALL}


class WorkoutSessionResource(ModelResource):
    '''
    Resource for workout sessions
    '''

    workout = fields.ToOneField('manager.api.resources.WorkoutResource', 'workout')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(user=bundle.request.user)

    class Meta:
        queryset = WorkoutSession.objects.all()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     "date": ALL,
                     "time_start": ALL,
                     "time_end": ALL}


class ScheduleStepResource(ModelResource):
    '''
    Resource for schedule steps
    '''

    workout = fields.ToOneField(WorkoutResource, 'workout')
    schedule = fields.ToOneField('manager.api.resources.ScheduleResource', 'schedule')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(schedule__user=bundle.request.user)

    class Meta:
        queryset = ScheduleStep.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     'schedule': ALL_WITH_RELATIONS,
                     'workout': ALL_WITH_RELATIONS}


class ScheduleResource(ModelResource):
    '''
    Resource for schedules
    '''

    steps = fields.ToManyField(ScheduleStepResource, 'schedulestep_set')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(user=bundle.request.user)

    class Meta:
        queryset = Schedule.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     'is_active': ALL,
                     'is_loop': ALL,
                     'name': ALL}


class DayResource(ModelResource):
    '''
    Resource for training days
    '''

    workout = fields.ToOneField(WorkoutResource, 'training')
    days_of_week = fields.ToManyField(DaysOfWeekResource, 'day')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(training__user=bundle.request.user)

    class Meta:
        queryset = Day.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     'description': ALL,
                     'workout': ALL_WITH_RELATIONS}


class SetResource(ModelResource):
    '''
    Resource for training sets
    '''

    day = fields.ToOneField(DayResource, 'exerciseday')
    exercises = fields.ToManyField(ExerciseResource, 'exercises')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(exerciseday__training__user=bundle.request.user)

    class Meta:
        queryset = Set.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     'day': ALL_WITH_RELATIONS,
                     'order': ALL,
                     'sets': ALL}


class SettingResource(ModelResource):
    '''
    Resource for training settings
    '''

    set = fields.ToOneField(SetResource, 'set')
    exercise = fields.ToOneField(ExerciseResource, 'exercise')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(set__exerciseday__training__user=bundle.request.user)

    class Meta:
        queryset = Setting.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     'exercise': ALL_WITH_RELATIONS,
                     'order': ALL,
                     'reps': ALL,
                     'set': ALL_WITH_RELATIONS}


class WorkoutLogResource(ModelResource):
    '''
    Resource for a workout log
    '''

    exercise = fields.ToOneField(ExerciseResource, 'exercise')
    workout = fields.ToOneField(WorkoutResource, 'workout')

    def authorized_read_list(self, object_list, bundle):
        '''
        Filter to own objects
        '''
        return object_list.filter(user=bundle.request.user)

    class Meta:
        queryset = WorkoutLog.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {'id': ALL,
                     'date': ALL,
                     'exercise': ALL_WITH_RELATIONS,
                     'reps': ALL,
                     'weight': ALL,
                     'workout': ALL_WITH_RELATIONS}
