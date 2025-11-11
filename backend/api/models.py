from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    avatar = models.CharField(max_length=255, blank=True, null=True, verbose_name="Аватар (URL)")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY_TYPE_CHOICES = [
        ('russian', 'Российская техника'),
        ('foreign', 'Иномарки'),
    ]

    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена",
        validators=[MinValueValidator(0)]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    category_type = models.CharField(
        max_length=10,
        choices=CATEGORY_TYPE_CHOICES,
        default='russian',
        verbose_name="Тип категории"
    )

    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Изображение")
    image_url = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ссылка на изображение")

    year = models.IntegerField(
        verbose_name="Год выпуска",
        blank=True,
        null=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2025)]
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

class SupportContact(models.Model):
    CONTACT_TYPE_CHOICES = [
        ('phone', 'Телефон'),
        ('email', 'Email'),
        ('address', 'Адрес'),
        ('schedule', 'График работы'),
    ]

    type = models.CharField(max_length=10, choices=CONTACT_TYPE_CHOICES, verbose_name="Тип контакта")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    value = models.TextField(verbose_name="Значение")
    description = models.TextField(blank=True, verbose_name="Описание")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Контакт поддержки"
        verbose_name_plural = "Контакты поддержки"
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.value}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=100, verbose_name="Должность")
    bio = models.TextField(verbose_name="Биография")
    email = models.EmailField(verbose_name="Email")
    photo_url = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ссылка на фото")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Команда"
        ordering = ['order']

    def __str__(self):
        return self.name

# Добавляем модель для обратной связи
class Feedback(models.Model):
    TOPIC_CHOICES = [
        ('general', 'Общий вопрос'),
        ('technical', 'Техническая поддержка'),
        ('sales', 'Вопрос по покупке'),
        ('partnership', 'Партнерство'),
        ('other', 'Другое'),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_processed = models.BooleanField(default=False, verbose_name="Обработано")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_topic_display()}"