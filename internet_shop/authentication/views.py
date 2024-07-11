import datetime

import jwt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .authDAO import UserDAO

from Base.responces import BadPatchResponce, SuccessResponce

from database import session_maker
from .models import Users
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UsersPasswordUpdateSerializers
from Base.BaseVIewSet import BaseViewSet

from .dependencies import role_required, hashing
class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "msg": "Регистрация прошла успешно"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, )


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        if not request.COOKIES.get('key'):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                email = serializer.validated_data['email']
                session = session_maker()
                user = session.query(Users).filter_by().first()
                session.close()
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
                }
                token = jwt.encode(payload, 'secret', algorithm="HS256")
                response = Response()
                response.set_cookie(key='key', value=token, expires=datetime.datetime.now() + datetime.timedelta(hours=1),
                                    httponly=True)
                response.data = {"message": "Вход выполонен успешно", "token": token}
                return response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, )
        else:
            return Response(data={'msg':'You was loggined'})

class LogoutView(APIView):

    def post(self, request):
        response = Response()
        if request.COOKIES.get('key'):
            response.delete_cookie('key')
            response.data = {'message': 'success'}
            return response
        response.data = {'message':'You not loggined'}
        return response.data

# class UsersViewSet(BaseViewSet):
#     model = Users
#     serializer_class = UserSerializer
#
#     @role_required(1)
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args,**kwargs)
#
#     @role_required(1)
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args,**kwargs)

    # @role_required(1,4)
    # def partial_update(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     result = UserDAO.find_by_email(self.model, pk)
    #     if result is None:
    #         return BadPatchResponce(data=[])
    #     hashed_passsword = hashing(request.data['hashed_password'])
    #     result = UserDAO.update(self.model, pk, {'hashed_password':hashed_passsword})
    #     serializer = self.serializer_class(result)
    #     return SuccessResponce(data=serializer.data)

class UserPasswordUpdate(APIView):
    serializer_class = UsersPasswordUpdateSerializers


    @role_required(1)
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = UserDAO.find_by_id(Users, pk)
        if result is None:
            return BadPatchResponce(data=[])
        hashed_passsword = hashing(request.data['password'])
        result = UserDAO.update(self.model, pk, {'hashed_password': hashed_passsword})
        serializer = self.serializer_class(result)
        return SuccessResponce(data=serializer.data)

class UserAPIVIEW(APIView):
    serializer_class = UserSerializer

    @role_required(1)
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            users = UserDAO.find_all(Users)
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)
        else:
            result = UserDAO.find_by_id(Users, pk)
            if result is None:
                return Response(data=[])
            serializer = self.serializer_class(result[0])
            return Response(serializer.data)

    def

