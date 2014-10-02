#import logging

from tastypie.authorization import ReadOnlyAuthorization

#logger = logging.getLogger('custom')


class UserObjectsOnlyAuthorization(ReadOnlyAuthorization):
    '''
    Custom authorization class to limit the user's access to his own objects
    '''

    def read_detail(self, object_list, bundle):

        # For models such as userprofile where we don't have an owner function
        if hasattr(bundle.obj, 'user'):
            return bundle.obj.user == bundle.request.user

        try:
            return bundle.obj.get_owner_object().user == bundle.request.user
        # Objects without owner information can be accessed
        except AttributeError:
            return True
