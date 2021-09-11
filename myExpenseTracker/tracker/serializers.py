from rest_framework import fields, serializers
from .models import Categories, Expense
from django.contrib.auth.models import User


class TransactionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField()

    class Meta:
        model = Expense
        fields = ['id', 'user__name',
                  'category__cat_name', 'exp_type', 'amount']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'cat_name', 'user']

    def create(self, validated_data):
        return Categories.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
