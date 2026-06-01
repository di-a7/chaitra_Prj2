from rest_framework import serializers
from .models import *

class CategoryModelSerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ['id', 'name']
      # fields = '__all__'
      # exclude = ['name']
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      category = Category.objects.filter(name = validated_data.get('name')).count()
      if category > 0:
         raise serializers.ValidationError({"name":"Category with this name already exists."})
      return super().save(**kwargs)
   
   # def create(self, validated_data):
   #    category = Category.objects.filter(name = validated_data.get('name')).count()
   #    if category > 0:
   #       raise serializers.ValidationError({"name":"Category with this name already exists."})
   #    return super().create(validated_data)


class FoodSerializer(serializers.ModelSerializer):
   category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
   category = serializers.StringRelatedField()
   price_with_vat = serializers.SerializerMethodField()
   class Meta:
      model = Food
      fields = ['id','name','description','price','price_with_vat','category_id','category']
   
   def get_price_with_vat(self, food:Food):
      return food.price * 0.13 + food.price

   
   # price with discount method 

























# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only = True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       category = Category.objects.create(name = validated_data.get('name'))
#       return category
   
#    def update(self, instance, validated_data):
#       instance.name = validated_data.get('name', instance.name)
#       instance.save()
#       return instance

# validated_data = {"name":"abc"}