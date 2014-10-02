from rest_framework import exceptions
from rest_framework import viewsets


class WgerOwnerObjectModelViewSet(viewsets.ModelViewSet):
    '''
    Custom viewset that makes sure the user can only create objects for himself
    '''
    def create(self, request, *args, **kwargs):
        '''
        Check for creation (PUT, POST)
        '''
        for entry in self.get_owner_objects():
            if request.DATA.get(entry[1]):
                pk = request.DATA.get(entry[1])
                obj = entry[0].objects.get(pk=pk)
                if obj.get_owner_object().user != request.user:
                    raise exceptions.PermissionDenied('You are not allowed to do this')
        else:
            return super(WgerOwnerObjectModelViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        '''
        Check for updates (PUT, PATCH)
        '''
        for entry in self.get_owner_objects():
            if request.DATA.get(entry[1]):
                pk = request.DATA.get(entry[1])
                obj = entry[0].objects.get(pk=pk)
                if obj.get_owner_object().user != request.user:
                    raise exceptions.PermissionDenied('You are not allowed to do this')
        else:
            return super(WgerOwnerObjectModelViewSet, self).update(request, *args, **kwargs)
