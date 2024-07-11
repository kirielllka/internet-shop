from database import session_maker
from internet_shop.authentication.models import Users
import hashlib
from internet_shop.roles.models import Roles

def reg_us():
    email = input('Email:')
    password = input('Password:')
    role = int(input('Role:'))
    session = session_maker()
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    user = Users(email=email,hashed_password=hashed_password, role=role)
    session.add(user)
    session.commit()
    session.close()

reg_us()
