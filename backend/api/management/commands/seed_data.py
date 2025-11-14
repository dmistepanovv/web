from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Category, Product, SupportContact, TeamMember, Feedback

User = get_user_model()

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **options):
        # Создаем суперпользователя
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@strawberries.ru',
                password='admin',
                first_name='Администратор',
                last_name='Системы'
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь создан: admin/admin'))

        # Создаем тестового пользователя
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Тест',
                'last_name': 'Пользователь',
                'phone': '+79991234567'
            }
        )
        if created:
            user.set_password('testpassword123')
            user.save()

        # Создаем категории
        russian_cat, _ = Category.objects.get_or_create(
            name="Российская техника",
            description="Легендарные автомобили и мотоциклы советской и российской эпохи"
        )

        foreign_cat, _ = Category.objects.get_or_create(
            name="Иномарки",
            description="Иностранные автомобили с историей"
        )

        products_data = [
            {
                'name': 'ВАЗ 2101 "Копейка"',
                'description': 'Легендарный автомобиль советской эпохи 1973 года выпуска. Полностью восстановлен, оригинальный двигатель. Отличное техническое состояние, все документы в порядке.',
                'price': 450000,
                'category': russian_cat,
                'category_type': 'russian',
                'year': 1973,
                'transmission': 'Механика, 5 передач',
                'engine_power': '67 л.с.',
                'mileage': '100000 км',
                'drive_type': 'Передний',
                'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/VAZ_2101_BW_2016-09-03_13-51-58.jpg/1200px-VAZ_2101_BW_2016-09-03_13-51-58.jpg'
            },


            {
                'name': 'ИЖ Планета-4',
                'description': 'Культовый советский мотоцикл 1985 года. Надежный двигатель, классический дизайн. Полностью оригинальные детали, полная комплектация.',
                'price': 85000,
                'category': russian_cat,
                'category_type': 'russian',
                'year': 1985,
                'transmission': 'Механика, 4 передачи',
                'engine_power': '34 л.с.',
                'mileage': '270000',
                'drive_type': 'Зданий',
                'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIlSPvISOM2BNuU69eGfpuJoXPQ4JQj1mxdQ&s'
            },
            {
                'name': 'УАЗ-469',
                'description': 'Внедорожник 1990 года. Легенда бездорожья. Полный привод, усиленная подвеска. Идеален для охоты и рыбалки.',
                'price': 320000,
                'category': russian_cat,
                'category_type': 'russian',
                'year': 1990,
                'transmission': 'Механика, 5 передач',
                'engine_power': '80 л.с.',
                'mileage': '420000',
                'drive_type': 'Полный',
                'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQI7y6kneM9vPBahilosLEsswyEqesIx03k0g&s'
            },
            {
                'name': 'Volkswagen Golf II',
                'description': 'Немецкий хэтчбек 1990 года. Культовая модель в отличном состоянии.',
                'price': 350000,
                'category': foreign_cat,
                'category_type': 'foreign',
                'year': 1990,
                'transmission': 'Механика, 5 передач',
                'engine_power': '106 л.с.',
                'mileage': '280000',
                'drive_type': 'Передний',
                'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSw8hL6Sb1R2YfT8vP8oxQIeeY4HzvauBUknw&s'
            },
            {
                'name': 'BMW 5 серии 525d IV (E39) Рестайлинг',
                'description': 'Немецкий седан 2002 года. Тот случай, когда пословица "Четыре колеса возят возят тело, а два душу" становится неуместной',
                'price': 700000,
                'category': foreign_cat,
                'category_type': 'foreign',
                'year': 2002,
                'transmission': 'Автомат',
                'engine_power': '130 л.с.',
                'mileage': '595000',
                'drive_type': 'Передний',
                'image_url': 'https://a.d-cd.net/bVof-E8jnEeP4IzsKnM7oPMS9Uc-960.jpg'
            },
            {
                'name': 'Skoda Octavia III (A7) Рестайлинг',
                'description': 'Чешский лифтбек 2018 года. По тюнингу говорим сразу нет, мы стейджами не занимаемся!!!',
                'price': 1600000,
                'category': foreign_cat,
                'category_type': 'foreign',
                'year': 2018,
                'transmission': 'Автомат',
                'engine_power': '110 л.с.',
                'mileage': '70000',
                'drive_type': 'Передний',
                'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFbEc_qMr7l5pBrh5NPc52zBYREiaw3T1q4Q&s'
            },
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if not created:
                # Обновляем существующие записи
                for key, value in product_data.items():
                    setattr(product, key, value)
                product.save()

        # Создаем контакты поддержки
        contacts_data = [
            {'type': 'schedule', 'title': 'Пн-Пт', 'value': '9:00 - 20:00', 'order': 1},
            {'type': 'schedule', 'title': 'Сб-Вс', 'value': '10:00 - 18:00', 'order': 2},
            {'type': 'phone', 'title': 'Общие вопросы', 'value': '8-800-555-35-35', 'order': 3},
            {'type': 'phone', 'title': 'Техподдержка', 'value': '8-800-555-35-36', 'order': 4},
            {'type': 'email', 'title': 'Общие вопросы', 'value': 'info@strawberries.ru', 'order': 5},
            {'type': 'address', 'title': 'Адрес магазина', 'value': 'г. Белгород, ул. Костюкова, д. 46', 'order': 6},
        ]

        for contact_data in contacts_data:
            SupportContact.objects.get_or_create(
                title=contact_data['title'],
                type=contact_data['type'],
                defaults=contact_data
            )

        team_data = [
            {
                'name': 'Иван Петров',
                'position': 'Генеральный директор',
                'bio': 'Основатель маркетплейса. Автомобильный эксперт с 15-летним опытом.',
                'email': 'ivan@strawberries.ru',
                'photo_url': 'https://img06.rl0.ru/afisha/e1200x1200i/daily.afisha.ru/uploads/images/b/1e/b1e04a4fe92b08a09ebb0eadbfc9e737.jpg',
                'order': 1
            },
            {
                'name': 'Артур Пирожков',
                'position': 'Менеджер по продажам',
                'bio': 'Специалист по подбору и оценке ретро-автомобилей. Работает с 2018 года.',
                'email': 'artur@strawberries.ru',
                'photo_url': 'https://assets3.klops.ru/media/W1siZiIsIjIwMjFcLzA3XC8wNVwvNWNldWJwaHJ4aV9maWxlLmpwZWciXSxbInAiLCJ0aHVtYiIsIjc5MHg2MzYrMCswIl0sWyJwIiwidGh1bWIiLCI4NjB4Il0sWyJwIiwiZW5jb2RlIiwianBnIiwiLXF1YWxpdHkgODUgLXN0cmlwIC1pbnRlcmxhY2UgUGxhbmUiXV0=/file.jpg?sha=0bc2614edc4a8577',
                'order': 2
            },
            {
                'name': 'Алексей Козлов',
                'position': 'Технический специалист',
                'bio': 'Механик с 20-летним стажем. Проводит техническую экспертизу всех лотов.',
                'email': 'alexey@strawberries.ru',
                'photo_url': 'https://newcdn.igromania.ru/mnt/news/2/c/f/2/9/7/115210/d1020b677c03b727_original.jpg',
                'order': 3
            },
            {
                'name': 'Сильвестр Стальной',
                'position': 'Менеджер закупок',
                'bio': 'Достанет нужную технику практически из любой точки мира.',
                'email': 'silva@strawberries.ru',
                'photo_url': 'https://news.store.rambler.ru/img/56958f33bb011f2035d12b3572e37a9c?img-format=auto&img-1-resize=height:400,fit:max&img-2-filter=sharpen',
                'order': 4
            },
        ]

        for member_data in team_data:
            member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if not created:
                # Обновляем существующие записи
                for key, value in member_data.items():
                    setattr(member, key, value)
                member.save()

        # Создаем тестовые отзывы
        feedback_data = [
            {
                'name': 'Аркадий Парамонов',
                'email': 'arcady@my.ru',
                'topic': 'sales',
                'message': 'У вас есть тепловозы в наличии?'
            },
        ]

        for feedback_item in feedback_data:
            Feedback.objects.get_or_create(
                name=feedback_item['name'],
                email=feedback_item['email'],
                defaults=feedback_item
            )

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены!'))