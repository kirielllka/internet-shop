from rest_framework import viewsets, status
from rest_framework.response import Response
from internet_shop.Base.responces import BadGetResponce, SuccessResponce
from .models import Roles
from .serializer import RolesSerializer
from database import session_maker
from authentication.dependencies import role_required
from Base.BaseVIewSet import BaseViewSet
from .RolesDAO import RolesDAO

from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter
class RoleViewSet(BaseViewSet):
    serializer_class = RolesSerializer
    model = Roles

    @role_required(5, 7)
    @extend_schema(
        parameters=[OpenApiParameter('role_name', type=OpenApiTypes.STR,
                                     description='Enter the role name to search for',
                                     required=True)],
        responses={200: RolesSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_category(self, request):
        role_name = request.query_params.get('role_name', None)
        if role_name is not None:
            roles = RolesDAO.find_by_name(role_name)
            if not roles:
                return BadGetResponce(data=[])
            serializer = self.serializer_class(roles, many=True)
            return SuccessResponce(data=serializer.data)
        return BadGetResponce(data=[])

    @role_required(1,2)
    def list(self, request, *args, **kwargs):
        return super().list(request,*args,**kwargs)

    @role_required(1,2,3)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request,*args,**kwargs)
