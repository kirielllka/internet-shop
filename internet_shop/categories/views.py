from database import session_maker

from .models import Categories

from .serializer import CategorySerializer
from Base.BaseVIewSet import BaseViewSet

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter
from authentication.dependencies import role_required
class CategoryViewSet(BaseViewSet):
    serializer_class = CategorySerializer
    model = Categories


    @role_required(1,3,4,2)
    @extend_schema(
        parameters=[OpenApiParameter('category_name', type=OpenApiTypes.STR,
                                     description='Enter the category name',required=True)],
        responses={200:CategorySerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_category(self,request):
        category_name = request.query_params.get('category_name', None)
        session = session_maker()
        if category_name is not None:
            categories = session.query(Categories).filter(Categories.category_name.ilike(f'%{category_name}%')).all()
            if categories == []:
                return Response({'msg':'category is not found'})
            elif categories != []:
                session.close()
                serializer = self.serializer_class(categories, many=True)
                return Response(serializer.data)
        else:
            return Response({'msg':'bad request'})

    @role_required(1,3,4,2)
    def list(self, request, *args, **kwargs):
        return super().list(request)
    @role_required(1, 2)
    def update(self, request, *args, **kwargs):
        return super().update(request, **kwargs)

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

    # @role_required(1, 3, 4, 5)





