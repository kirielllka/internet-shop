from rest_framework.response import Response
from rest_framework import status

class ApiResponce(Response):
    def __init__(self,data:list,status_code:status = status.HTTP_200_OK,**kwargs):
        super().__init__({'status':status_code, 'data':data}, **kwargs)

class SuccessResponce(ApiResponce):
    def __init__(
            self,
            data:dict,
            status_code:status=status.HTTP_200_OK,
            **kwargs):
        super().__init__(data,status_code,**kwargs)

class BadGetResponce(ApiResponce):
    def __init__(
            self,
            data:list,
            status_code:status=status.HTTP_404_NOT_FOUND,
            **kwargs):
        super().__init__(data,status_code,**kwargs)

class BadPostResponce(ApiResponce):
    def __init__(
            self,
            data:dict,
            status_code:status=status.HTTP_400_BAD_REQUEST,
            **kwargs
                ):
        super().__init__(data,status_code,**kwargs)

class BadPutResponce(ApiResponce):
    def __init__(
            self,
            data:dict,
            status_code:status=status.HTTP_400_BAD_REQUEST,
            **kwargs
                ):
        super().__init__(data,status_code,**kwargs)

class BadPatchResponce(ApiResponce):
    def __init__(
            self,
            data:dict,
            status_code:status=status.HTTP_400_BAD_REQUEST,
            **kwargs
                ):
        super().__init__(data,status_code,**kwargs)

class SuccessDeleteResponce(ApiResponce):
    def __init__(
            self,
            data:dict,
            status_code:status=status.HTTP_200_OK,
            **kwargs
                ):
        super().__init__(data,status_code,**kwargs)

class BadDeleteResponce(ApiResponce):
    def __init__(
            self,
            data:dict,
            status_code:status=status.HTTP_400_BAD_REQUEST,
            **kwargs
                ):
        super().__init__(data,status_code,**kwargs)

