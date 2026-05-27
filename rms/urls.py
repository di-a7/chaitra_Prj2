from django.urls import path
from .views import CategoryAPIView, CategoryDetail

urlpatterns = [
   # Class Based:
   path('category/', CategoryAPIView.as_view()),
   path('category/<id>/', CategoryDetail.as_view())
   
   # Function based:
   # path('category/', category),
   # path('category/<id>/', category_detail)
]