from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, OrderItem
from .serializer import CategoryModelSerializer
# Create your views here.
# Viewset:
from rest_framework import viewsets
class CategoryModelViewset(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategoryModelSerializer
   
   def destroy(self,request, pk):
      category = Category.objects.get(pk = pk)
      items = OrderItem.objects.filter(food__category=category).count()
      if items > 0:
         return Response({"detail":"Category can not be deleted. Protected in OrderItem"})
      category.delete()
      return Response({"detail": "Category deleted successfully"})

# class CategoryViewSet(viewsets.ViewSet):
#    def list(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)
#       return Response(serializer.data)
   
#    def create(self,request):
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)


# class CategoryDetailViewSet(viewsets.ViewSet):
#    def retrieve(self, request, pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    def update(self,request, pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category, data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def partial_update(self, request, pk=None):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category, data = request.data, partial=True)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def destroy(self,request, pk):
#       category = Category.objects.get(pk = pk)
#       items = OrderItem.objects.filter(food__category=category).count()
#       if items > 0:
#          return Response({"detail":"Category can not be deleted. Protected in OrderItem"})
#       category.delete()
#       return Response({"detail": "Category deleted successfully"})



# Mixins: 
# from rest_framework import mixins, generics

# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# class CategoryGerenicAPIView(ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer

# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def delete(self,request,pk):
#       items = OrderItem.objects.filter(food__category= self.get_object()).count()
#       if items > 0:
#          return Response({"detail":"Category can not be deleted. Protected in OrderItem"})
#       self.get_object().delete()
#       return Response({"detail": "Category deleted successfully"})


# Class Based: APIView
# from rest_framework.views import APIView

# class CategoryAPIView(APIView):
#    def get(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)
#       return Response(serializer.data)
   
#    def post(self,request):
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)

# class CategoryDetail(APIView):
#    def get(self, request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)

# post, delete methods

# Table api






# Function based: api_view()
# @api_view(['GET','POST'])
# def category(request):
#    if request.method == "GET":
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)   # serialize: to convert queryset to json format
#       return Response(serializer.data)
#    elif request.method == 'POST':
#       serializer = CategorySerializer(data = request.data)  # deserialize: json format convert to model instance
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)

# @api_view(['GET','POST','DELETE'])
# def category_detail(request, id):
#    category = Category.objects.get(id = id)
#    if request.method == "GET":
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
#    elif request.method == 'POST':
#       serializer = CategorySerializer(category, data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
#    elif request.method == 'DELETE':
#       items = OrderItem.objects.filter(food__category=category).count()
#       if items > 0:
#          return Response({"detail":"Category can not be deleted. Protected in OrderItem"})
#       category.delete()
#       return Response({"detail": "Category deleted successfully"})



# create Table api
