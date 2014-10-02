from django.core.management.base import BaseCommand
from exercises.models import Exercise


class Command(BaseCommand):
    '''
    Read out the user submitted exercise.

    Used to generate the AUTHORS file for a release
    '''

    help = 'Read out the user submitted exercise'

    def handle(self, *args, **options):

        exercises = Exercise.objects.accepted()
        usernames = []
        for exercise in exercises:
            if exercise.user not in usernames:
                usernames.append(exercise.user)
                self.stdout.write(exercise.user)
