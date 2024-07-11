from Base.BaseVIewSet import BaseViewSet

from database import session_maker
from rest_framework.response import Response
from .models import OrderHistory
from products.models import Products
from categories.models import Categories
from clients.models import Client
from .serializer import OrderSerializer
from products.serializer import ProductSerializer
from authentication.dependencies import role_required
class OrderListViewSet(BaseViewSet):
    model = OrderHistory
    serializer_class = OrderSerializer

    @role_required(1,2,3)
    def list(self, request, *args, **kwargs):
        session = session_maker()
        order = session.query(OrderHistory).all()
        serializer = OrderSerializer(order, many=True)
        for order in serializer.data:
            product = order['product']
            product = session.query(Products).get(product)
            category_name = session.query(Categories).get(product.category).category_name
            client = order['client']
            client = session.query(Client).get(client).full_name
            order['product'] = {
                'id':product.id,
                'product_name':product.product_name,
                'category':category_name,
                'des':product.description,
                'cost':product.cost,
                'count_of_sells':product.count_of_sells,
                'discount':product.discount
            }
            order['client'] = client
        return Response(serializer.data)

    @role_required(1,2,3)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @role_required(1,2,3,4)
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    @role_required(1,2,3,4)
    def create(self, request, *args, **kwargs):
        return super().create(request,*args, **kwargs)

    @role_required(1,2,3)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request,*args,**kwargs)

    @role_required(1,2)
    def update(self, request, *args, **kwargs):
        return super().update(request,*args,**kwargs)

    @role_required(1,2)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request,*args,**kwargs)
    
    @role_required(1,2)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request,*args,**kwargs)