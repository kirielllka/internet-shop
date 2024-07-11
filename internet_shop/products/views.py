from rest_framework.response import Response
from .models import Products
from categories.models import Categories
from .serializer import ProductSerializer, ProductSerializerTwo
from Base.BaseVIewSet import BaseViewSet
from database import session_maker
from authentication.dependencies import role_required
from Base.responces import SuccessResponce,BadGetResponce
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter
from .ProductDAO import ProductsDAO
class ProductViewSet(BaseViewSet):
    serializer_class = ProductSerializer
    model = Products

    @role_required(1, 3, 4, 2)
    def list(self, request):
        session = session_maker()
        products = session.query(Products).all()
        # product = session.select(Products, Categories.category_name).select_from(join(Products,Categories, Products.category==Categories.id))
        # product = session.query(Products, Categories.category_name).join(Categories, Products.category == Categories.id)
        serializer = ProductSerializer(products, many=True)
        for product in serializer.data:
            product = session.select()
            category_id = product['category']
            category_name = session.query(Categories).get(category_id).category_name
            product['category'] = category_name
        return Response(serializer.data)

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

    @role_required(1, 2, 3)
    def create(self, request, *args, **kwargs):
        return super().create(request)

    @role_required(5, 6, 7, 8)
    @extend_schema(
        parameters=[OpenApiParameter('product_name', type=OpenApiTypes.STR,
                                     description='Enter the product name to search for',
                                     required=True)],
        responses={200: serializer_class(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_product(self, request):
        product_name = request.query_params.get('product_name', None)
        if product_name is not None:
            products = ProductsDAO.find_by_name(product_name)
            if not products:
                return BadGetResponce(data=[])
            serializer = self.serializer_class(products, many=True)
            return SuccessResponce(data=serializer.data)
        return BadGetResponce(data=[])






