from rest_framework import viewsets, mixins
from rest_framework.response import Response

# https://gist.github.com/ivlevdenis/a0c8f5b472b6b8550bbb016c6a30e0be


class ExtendViewSet:
    """
    This viewset mixin class with extended options list.
    """

    serializer_class_map = {}
    permission_classes_map = {}
    throttle_scope_map = {}
    throttle_class_map = {}

    def get_serializer_class(self):
        self.serializer_class = self.serializer_class_map.get(
            self.action, self.serializer_class
        )
        return super().get_serializer_class()

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        throttle_scope = self.throttle_scope_map.get(self.action, None)
        throttle_class = self.throttle_class_map.get(self.action, None)
        if throttle_scope:
            self.throttle_scope = throttle_scope
        if throttle_class:
            self.throttle_classes = throttle_class
        return request

    def get_permissions(self):
        perms = self.permission_classes_map.get(self.action, None)
        if perms and not isinstance(perms, (tuple, list)):
            perms = (perms,)
            self.permission_classes = perms
        return super().get_permissions()


class ExtendedModelViewSet(ExtendViewSet, viewsets.ModelViewSet):
    """
    Examples:
    class MyModelViewSet(ExtendedModelViewSet):
        serializer_class_map = {
            'list': ListMyModelSerializer,
            'retrieve': RetrieveMyModelSerializer,
            'update': UpdateMyModelSerializer,
            ...
        }
        permission_classes_map = {
            'list': AllowAny,
            'retrieve': IsAuthenticated,
            'update': (IsOwner | IsAdminUser),
            ...
        }
    """

    pass


class RUDExtendedModelViewSet(
    ExtendViewSet,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass
