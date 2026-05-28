from django.urls import path
from .views import CategoryGerenicAPIView, CategoryDetail

urlpatterns = [
   # Class Based:
   path('category/', CategoryGerenicAPIView.as_view()),
   path('category/<pk>/', CategoryDetail.as_view())
   
   # Function based:
   # path('category/', category),
   # path('category/<id>/', category_detail)
]