from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import Category, Product, SupportContact, TeamMember, Feedback

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone')

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'phone')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone': {'required': False}
        }

    def validate_first_name(self, value):
        if not value.replace(' ', '').replace('-', '').isalpha():
            raise serializers.ValidationError("Имя может содержать только буквы, пробелы и дефис.")
        return value

    def validate_last_name(self, value):
        if not value.replace(' ', '').replace('-', '').isalpha():
            raise serializers.ValidationError("Фамилия может содержать только буквы, пробелы и дефис.")
        return value

    def validate_phone(self, value):
        if value and not value.startswith('+7'):
            raise serializers.ValidationError("Телефон должен начинаться с +7")
        if value and len(value) != 12:
            raise serializers.ValidationError("Телефон должен содержать 11 цифр после +7")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data.get('phone', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image_url(self, obj):
        # Если есть загруженное изображение - возвращаем его URL
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        # Иначе возвращаем image_url из базы
        return obj.image_url

class SupportContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportContact
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'