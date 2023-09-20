from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from .serializers import ProductSerializer, UserSerializers
from .models import Product

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .com import Com

# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# JWT_authenticator = JWTAuthentication()

class ProductViewSet(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(APIView):
    permission_classes = [IsAuthenticated]
    
    # def ppp(self, *args, **kwargs):
    #     return self.request.user.id

    def get(self, request, *args, **kwargs):

        
        # response = JWT_authenticator.authenticate(request)
        # if response is not None:
        #     msg = "this is decoded token claims"
        #     user , token = response
        #     print(user.id)
        # else:
        #     msg = "no token is provided in the header or the header is missing"
        

        msg = "ok"
        pp = Com.bal(request)
        # pp = self.ppp()
        # queryset = User.objects.all()
        # serializer = UserSerializers(queryset, many=True)
        serializer = UserSerializers(request.user)

        return Response(
            {
                'data':serializer.data, 
                'p':pp, 
                'error':0, 
                'msg':msg,
            }, 
            status=status.HTTP_200_OK
        )


