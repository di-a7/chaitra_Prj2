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

class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      fields = ['food']

class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   item = OrderItemSerializer(many=True)
   status = serializers.CharField(read_only = True)
   payment_status = serializers.CharField(read_only = True)
   total_price = serializers.IntegerField(read_only=True)
   class Meta:
      model = Order
      fields = ['id','user','total_price','status','payment_status','item']

   def create(self, validated_data):
      items = validated_data.pop('item')
      total = 0
      for item in items:
         food_item = item.get('food')        # food_item = 3040
         total += food_item.price
      order =  Order.objects.create(total_price = total, **validated_data)    
      for item in items:
         OrderItem.objects.create(order = order, food = item.get('food'))  
      return order


# validated_data = {user}
# items = {"item": [{"food":3040},{"food":3041},{"food":3042}]}























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