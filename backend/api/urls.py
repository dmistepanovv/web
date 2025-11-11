from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'support-contacts', views.SupportContactViewSet)
router.register(r'team-members', views.TeamMemberViewSet)

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('test/', views.test_api, name='test_api'),
    path('static-data/', views.static_data_api, name='static_data'),
    path('', include(router.urls)),
]