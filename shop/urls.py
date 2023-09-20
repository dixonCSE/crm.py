from django.urls import path
from . import views 

 
urlpatterns = [
    path("",  views.ProductViewSet.as_view(), name="detail"),
    path('xxx/', views.UserViewSet.as_view(), name ='user_api'),

]