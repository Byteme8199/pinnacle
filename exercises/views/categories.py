import logging

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from exercises.models import ExerciseCategory

from utils.generic_views import WgerFormMixin
from utils.generic_views import WgerDeleteMixin
from utils.generic_views import WgerPermissionMixin
from utils.language import load_language


logger = logging.getLogger('custom')


# ************************
#   Exercise categories
# ************************


class ExerciseCategoryAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    Generic view to add a new exercise category
    '''

    model = ExerciseCategory
    success_url = reverse_lazy('exercise-overview')
    title = ugettext_lazy('Add category')
    form_action = reverse_lazy('exercisecategory-add')
    messages = ugettext_lazy('Category was successfully created')
    permission_required = 'exercises.add_exercisecategory'

    def form_valid(self, form):
        form.instance.language = load_language()
        return super(ExerciseCategoryAddView, self).form_valid(form)


class ExerciseCategoryUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    Generic view to update an existing exercise category
    '''

    model = ExerciseCategory
    success_url = reverse_lazy('exercise-overview')
    messages = ugettext_lazy('Category successfully edited')
    permission_required = 'exercises.change_exercisecategory'

    # Send some additional data to the template
    def get_context_data(self, **kwargs):
        context = super(ExerciseCategoryUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('exercisecategory-edit', kwargs={'pk': self.object.id})
        context['title'] = _(u'Edit %s') % self.object.name

        return context

    def form_valid(self, form):
        form.instance.language = load_language()

        return super(ExerciseCategoryUpdateView, self).form_valid(form)


class ExerciseCategoryDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    Generic view to delete an existing exercise category
    '''

    model = ExerciseCategory
    success_url = reverse_lazy('exercise-overview')
    delete_message = ugettext_lazy('This will also delete all exercises in this category.')
    messages = ugettext_lazy('Category successfully deleted')
    permission_required = 'exercises.delete_exercisecategory'

    # Send some additional data to the template
    def get_context_data(self, **kwargs):
        context = super(ExerciseCategoryDeleteView, self).get_context_data(**kwargs)

        context['title'] = _(u'Delete category %s?') % self.object.name
        context['form_action'] = reverse('exercisecategory-delete', kwargs={'pk': self.object.id})

        return context
