from rest_framework import serializers
from .models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ['id', 'name']
      # fields = '__all__'
      # exclude = ['name']


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