from django.forms.widgets import SelectMultiple

from django.utils.translation import ugettext as _


class MuscleTranslatedSelectMultiple(SelectMultiple):
    '''
    A SelectMultiple widget that translates the options
    '''

    def render_option(self, selected_choices, option_value, option_label):

        # No translation, output only the original
        if option_label == _(option_label):
            out_string = option_label

        # There is a translation, show both
        else:
            out_string = u'{0} - {1}'.format(option_label, _(option_label))

        return super(MuscleTranslatedSelectMultiple, self).render_option(selected_choices,
                                                                         option_value,
                                                                         out_string)
