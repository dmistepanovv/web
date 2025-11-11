from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'support-contacts', views.SupportContactViewSet)
router.register(r'team-members', views.TeamMemberViewSet)
router.register(r'feedback', views.FeedbackViewSet)

urlpatterns = [
    path('test/', views.test_api, name='test_api'),
    path('static-data/', views.static_data_api, name='static_data'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/profile/', views.profile_view, name='profile'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('products/<int:pk>/detail/', views.product_detail, name='product_detail'),
]