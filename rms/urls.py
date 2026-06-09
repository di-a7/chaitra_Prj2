from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryModelViewset, basename='category')
router.register('food', FoodModelViewset, basename='food')
router.register('order', OrderModelViewset, basename='order')

urlpatterns = [
   # Class Based:
   # path('category/',CategoryViewSet.as_view({'get':'list','post':'create'})),
   # path('category/<id>/',CategoryDetailViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update','delete':'destroy'}))
   # path('category/', CategoryGerenicAPIView.as_view()),
   # path('category/<pk>/', CategoryDetail.as_view())
   
   # Function based:
   # path('category/', category),
   # path('category/<id>/', category_detail)
] + router.urls