import logging

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from exercises.models import Muscle

from utils.generic_views import WgerFormMixin
from utils.generic_views import WgerDeleteMixin
from utils.generic_views import WgerPermissionMixin
from utils.language import load_item_languages
from config.models import LanguageConfig

logger = logging.getLogger('custom')


class MuscleListView(ListView):
    '''
    Overview of all muscles and their exercises
    '''
    model = Muscle
    queryset = Muscle.objects.all().order_by('-is_front', 'name'),
    context_object_name = 'muscle_list'
    template_name = 'muscles/overview.html'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(MuscleListView, self).get_context_data(**kwargs)
        context['active_languages'] = load_item_languages(LanguageConfig.SHOW_ITEM_EXERCISES)
        return context


class MuscleAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    Generic view to add a new muscle
    '''

    model = Muscle
    success_url = reverse_lazy('muscle-overview')
    title = ugettext_lazy('Add muscle')
    form_action = reverse_lazy('muscle-add')
    permission_required = 'exercises.add_muscle'


class MuscleUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    Generic view to update an existing muscle
    '''

    model = Muscle
    title = ugettext_lazy('Edit muscle')
    success_url = reverse_lazy('muscle-overview')
    permission_required = 'exercises.change_muscle'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(MuscleUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('muscle-edit', kwargs={'pk': self.object.id})
        context['title'] = _(u'Edit %s') % self.object.name
        return context


class MuscleDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    Generic view to delete an existing muscle
    '''

    model = Muscle
    success_url = reverse_lazy('muscle-overview')
    permission_required = 'exercises.delete_muscle'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(MuscleDeleteView, self).get_context_data(**kwargs)
        context['title'] = _(u'Delete muscle %s?') % self.object.name
        context['form_action'] = reverse('muscle-delete', kwargs={'pk': self.kwargs['pk']})
        return context
