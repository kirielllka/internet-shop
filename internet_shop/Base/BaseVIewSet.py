from rest_framework import viewsets, status
from rest_framework.response import Response
from .responces import (BadGetResponce,SuccessResponce,
                        BadPostResponce,BadPutResponce,BadPatchResponce,
                        BadDeleteResponce,SuccessDeleteResponce)


from database import session_maker
from authentication.dependencies import role_required
from rest_framework import serializers
from database import Base

from .BaseDAO import BaseDAO


class BaseViewSet(viewsets.ModelViewSet):
    serializer_class: serializers.Serializer
    model: Base

    


    def list(self, request, *args, **kwargs):
        queryset = BaseDAO.find_all(model=self.model)
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data:
            return SuccessResponce(data=serializer.data)
        return BadGetResponce(data=[])

    def perform_create(self, serializer):
        session = session_maker()
        result = self.model(**serializer.validated_data)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return result

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = BaseDAO.add(self.model, serializer.data)
        if result:
            response_serializer = self.get_serializer(result)
            return SuccessResponce(data=response_serializer.data)
        return BadGetResponce(data=[])

    
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = BaseDAO.find_all(model=self.model,model_id=pk)
        if result is None:
            return BadPostResponce(data=[], status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(result)
        return SuccessResponce(data=serializer.data)

    
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = BaseDAO.find_all(model=self.model,model_id=pk)
        if result is None:
            return BadPutResponce(data=[])
        serializer = self.get_serializer(result, data=request.data)
        serializer.is_valid(raise_exception=True)
        result = BaseDAO.update(model=self.model, model_id=pk, data=request.data)
        serializer = self.serializer_class(result)
        return SuccessResponce(data=serializer.data)

    
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            BaseDAO.delete(model=self.model,model_id=pk)
            return SuccessDeleteResponce(data={'msg': 'Success delete'})

        except Exception:
            return BadDeleteResponce(data={"msg":'result error'})
