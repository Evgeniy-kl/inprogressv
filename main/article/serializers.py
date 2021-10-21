from rest_framework import serializers
from .models import Article, User


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'mini_description', 'image', 'author']


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class ArticleDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', ]

        extra_kwargs = {
            'password': {'read_only': True},
        }

    def update(self, instance, validated_data,):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
            instance.save()
            return instance
