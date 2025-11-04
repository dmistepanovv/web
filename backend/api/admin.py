from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category, Product, SupportContact, TeamMember

# Временно закомментируем CustomUser
# from .models import CustomUser

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff')
#     fieldsets = UserAdmin.fieldsets + (
#         ('Дополнительная информация', {'fields': ('phone', 'avatar')}),
#     )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'category_type', 'year', 'is_available', 'created_at')
    list_filter = ('category', 'category_type', 'is_available', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_available')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SupportContact)
class SupportContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'value', 'order')
    list_editable = ('order',)
    list_filter = ('type',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'order')
    list_editable = ('order',)