from django.contrib import admin
from django.urls import path, include
from shop import urls as shop_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',  include('rest_framework.urls',  namespace='rest_framework')),
    path('shop/', include(shop_urls)),
   
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
