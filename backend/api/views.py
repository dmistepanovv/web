from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Category, Product, SupportContact, TeamMember
from .serializers import (
    UserSerializer,
    CategorySerializer,
    ProductSerializer,
    SupportContactSerializer,
    TeamMemberSerializer
)

User = get_user_model()


# Простой API endpoint для тестирования
@api_view(['GET'])
def test_api(request):
    return Response({
        'message': 'API is working!',
        'status': 'success',
        'data': {
            'version': '1.0',
            'framework': 'Django REST Framework'
        }
    })


# API endpoint со статическими данными
@api_view(['GET'])
def static_data_api(request):
    static_products = [
        {
            'id': 1,
            'name': 'Тестовый автомобиль 1',
            'price': 100000,
            'description': 'Это статические данные для демонстрации API'
        },
        {
            'id': 2,
            'name': 'Тестовый автомобиль 2',
            'price': 200000,
            'description': 'Эти данные захардкожены в коде'
        }
    ]
    return Response({
        'message': 'Статические данные',
        'products': static_products
    })


# ViewSets для моделей
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Дополнительный action для фильтрации по типу категории
    @action(detail=False, methods=['get'])
    def by_category_type(self, request):
        category_type = request.query_params.get('type', None)
        if category_type:
            products = Product.objects.filter(category_type=category_type)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response([])


class SupportContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SupportContact.objects.all()
    serializer_class = SupportContactSerializer


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer