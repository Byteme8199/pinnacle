import logging
from django.contrib.auth.decorators import permission_required

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy
from django.utils.translation import ugettext as _

from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from exercises.models import Exercise
from exercises.models import ExerciseImage
from exercises.forms import ExerciseImageForm

from utils.generic_views import WgerFormMixin
from utils.generic_views import WgerDeleteMixin
from utils.generic_views import WgerPermissionMixin


logger = logging.getLogger('custom')

'''
Exercise images
'''


class ExerciseImageEditView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    Generic view to update an existing exercise image
    '''

    model = ExerciseImage
    title = ugettext_lazy('Edit exercise image')
    permission_required = 'exercises.change_exerciseimage'
    form_class = ExerciseImageForm

    def get_success_url(self):
        return reverse('exercise-view', kwargs={'id': self.object.exercise.id})

    # Send some additional data to the template
    def get_context_data(self, **kwargs):
        context = super(ExerciseImageEditView, self).get_context_data(**kwargs)
        context['enctype'] = 'multipart/form-data'
        context['form_action'] = reverse('exerciseimage-edit',
                                         kwargs={'pk': self.object.id})

        return context


class ExerciseImageAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    Generic view to add a new exercise image
    '''

    model = ExerciseImage
    title = ugettext_lazy('Add exercise image')
    permission_required = 'exercises.add_exerciseimage'
    form_class = ExerciseImageForm

    def form_valid(self, form):
        form.instance.exercise = Exercise.objects.get(pk=self.kwargs['exercise_pk'])
        form.instance.set_author(self.request)
        return super(ExerciseImageAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('exercise-view', kwargs={'id': self.object.exercise.id})

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(ExerciseImageAddView, self).get_context_data(**kwargs)
        context['enctype'] = 'multipart/form-data'
        context['form_action'] = reverse('exerciseimage-add',
                                         kwargs={'exercise_pk': self.kwargs['exercise_pk']})

        return context


class ExerciseImageDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    Generic view to delete an existing exercise image
    '''

    model = ExerciseImage
    messages = ugettext_lazy('Successfully deleted')
    permission_required = 'exercises.delete_exerciseimage'

    def get_success_url(self):
        '''
        Return to exercise image
        '''
        return reverse('exercise-view', kwargs={'id': self.kwargs['exercise_pk']})

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        pk = self.kwargs['pk']
        exercise_pk = self.kwargs['exercise_pk']
        context = super(ExerciseImageDeleteView, self).get_context_data(**kwargs)

        context['title'] = _('Delete exercise image?')
        context['form_action'] = reverse('exerciseimage-delete',
                                         kwargs={'pk': pk, 'exercise_pk': exercise_pk})

        return context


@permission_required('exercises.change_exerciseimage')
def accept(request, pk):
    '''
    Accepts a pending user submitted image and emails the user, if possible
    '''
    image = get_object_or_404(ExerciseImage, pk=pk)
    image.status = ExerciseImage.STATUS_ACCEPTED
    image.save()
    # image.send_email(request)

    return HttpResponseRedirect(image.exercise.get_absolute_url())


@permission_required('exercises.change_exerciseimage')
def decline(request, pk):
    '''
    Declines and deletes a pending user submitted image
    '''
    image = get_object_or_404(ExerciseImage, pk=pk)
    image.status = ExerciseImage.STATUS_DECLINED
    image.save()
    # image.send_email(request)

    return HttpResponseRedirect(image.exercise.get_absolute_url())
