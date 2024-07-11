from Base.BaseVIewSet import BaseViewSet
from .serializer import ClientSerializer
from .models import Client
from authentication.dependencies import role_required
class ClientViewSet(BaseViewSet):
    serializer_class = ClientSerializer
    model = Client

    @role_required(1, 2, 3)
    def list(self, request, *args, **kwargs):
        return super().list(request)

    @role_required(1, 2)
    def update(self, request, *args, **kwargs):
        return super().update(request,**kwargs)

    @role_required(1, 2)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request,**kwargs)

    @role_required(1, 2)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request,**kwargs)

    @role_required(1, 3, 4, 2)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, **kwargs)

    @role_required(1,3, 4, 2)
    def create(self, request, *args, **kwargs):
        return super().create(request)