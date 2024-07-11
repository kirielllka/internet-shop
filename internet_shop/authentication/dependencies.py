import jwt
from database import session_maker
from authentication.models import Users
from rest_framework import status
from rest_framework.response import Response
from functools import wraps
import hashlib
def get_user_from_token(request):
    token = request.COOKIES.get('key')
    if not token:
        return None
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        session = session_maker()
        user = session.query(Users).filter_by(id=payload['id']).first()
        session.close()
        if not user:
            return None
        else:
            return user
    except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
        return None

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(view,request,*args,**kwargs):
            user = get_user_from_token(request)
            if not user or user.role not in roles:
                return Response({'msg':'Stop'})
            return view_func(view,request,*args,**kwargs)
        return wrapper
    return decorator

def hashing(password:str)->str:
    return hashlib.md5(password.encode()).hexdigest()