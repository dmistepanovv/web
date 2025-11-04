<template>
  <div class="support-section">
    <h2>📞 Служба поддержки</h2>
    <p>Мы всегда готовы помочь вам! Выберите удобный способ связи.</p>

    <div class="contact-grid">
      <!-- Контактная информация -->
      <div class="contact-card">
        <h3>🕒 График работы</h3>
        <div class="contact-info">
          <p><strong>Пн-Пт:</strong> 9:00 - 20:00</p>
          <p><strong>Сб-Вс:</strong> 10:00 - 18:00</p>
          <p><strong>Технические перерывы:</strong> 13:00-14:00</p>
        </div>
      </div>

      <div class="contact-card">
        <h3>📞 Телефоны</h3>
        <div class="contact-info">
          <p><strong>Общие вопросы:</strong> 8-800-555-35-35</p>
          <p><strong>Техподдержка:</strong> 8-800-555-35-36</p>
          <p><strong>Продажи:</strong> 8-800-555-35-37</p>
          <p><em>Звонок бесплатный по всей России</em></p>
        </div>
      </div>

      <div class="contact-card">
        <h3>✉️ Электронная почта</h3>
        <div class="contact-info">
          <p><strong>Общие вопросы:</strong> info@strawberries.ru</p>
          <p><strong>Поддержка:</strong> support@strawberries.ru</p>
          <p><strong>Партнерство:</strong> partner@strawberries.ru</p>
        </div>
      </div>

      <div class="contact-card">
        <h3>📍 Адрес магазина</h3>
        <div class="contact-info">
          <p><strong>г. Белгород, ул. Костюкова, д. 46</strong></p>
          <p>ТЦ "ПОВ-ТАС", 4 этаж, павильон 429</p>
          <p><em>Ближайшая автобусная остановка: Костюкова</em></p>
        </div>
      </div>
    </div>

    <!-- Карта -->
    <div class="map-section">
      <h3>🗺️ Как нас найти</h3>
      <div class="map-placeholder">
        <img src="@/assets/img/map-placeholder.jpg" alt="Карта проезда">
        <p>Интерактивная карта с маршрутом</p>
      </div>
    </div>

    <!-- Социальные сети -->
    <div class="social-section">
      <h3>🌐 Мы в соцсетях</h3>
      <div class="social-links">
        <a href="#" class="social-link vk">VKontakte</a>
        <a href="#" class="social-link telegram">Telegram</a>
        <a href="#" class="social-link youtube">YouTube</a>
      </div>
    </div>

    <!-- Администраторы -->
    <div class="admins-section">
      <h3>👥 Наша команда</h3>
      <div class="admins-grid">
        <div class="admin-card">
          <div class="admin-photo">
            <img src="@/assets/img/admin1.jpg" alt="Иван Петров">
          </div>
          <div class="admin-info">
            <h4>Иван Петров</h4>
            <p class="admin-role">Генеральный директор</p>
            <p class="admin-bio">Основатель маркетплейса. Автомобильный эксперт с 15-летним опытом.</p>
            <p class="admin-contact">ivan@strawberries.ru</p>
          </div>
        </div>

        <div class="admin-card">
          <div class="admin-photo">
            <img src="@/assets/img/admin2.jpg" alt="Артур Пирожков">
          </div>
          <div class="admin-info">
            <h4>Артур Пирожков</h4>
            <p class="admin-role">Менеджер по продажам</p>
            <p class="admin-bio">Специалист по подбору и оценке ретро-автомобилей. Работает с 2018 года.</p>
            <p class="admin-contact">artur@strawberries.ru</p>
          </div>
        </div>

        <div class="admin-card">
          <div class="admin-photo">
            <img src="@/assets/img/admin3.jpg" alt="Алексей Козлов">
          </div>
          <div class="admin-info">
            <h4>Алексей Козлов</h4>
            <p class="admin-role">Технический специалист</p>
            <p class="admin-bio">Механик с 20-летним стажем. Проводит техническую экспертизу всех лотов.</p>
            <p class="admin-contact">alexey@strawberries.ru</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Форма обратной связи -->
    <div class="feedback-section">
      <h3>💬 Форма обратной связи</h3>
      <form class="feedback-form">
        <div class="form-row">
          <div class="form-group">
            <label for="name">Ваше имя:</label>
            <input type="text" id="name" name="name" required placeholder="Иван Иванов">
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="ivan@example.com">
          </div>
        </div>

        <div class="form-group">
          <label for="topic">Тема обращения:</label>
          <select id="topic" name="topic" required>
            <option value="">Выберите тему</option>
            <option value="general">Общий вопрос</option>
            <option value="technical">Техническая поддержка</option>
            <option value="sales">Вопрос по покупке</option>
            <option value="partnership">Партнерство</option>
            <option value="other">Другое</option>
          </select>
        </div>

        <div class="form-group">
          <label for="message">Сообщение:</label>
          <textarea id="message" name="message" required placeholder="Опишите ваш вопрос подробно..." rows="5"></textarea>
        </div>

        <button type="submit" class="btn">Отправить сообщение</button>
      </form>
    </div>
  </div>
</template>

<style>
.support-section {
  max-width: 1200px;
  margin: 1rem auto;
}

.support-section h2 {
  text-align: center;
  color: #ee5a24;
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.support-section > p {
  text-align: center;
  font-size: 1.2rem;
  margin-bottom: 30px;
  color: #666;
}

/* Контактная сетка */
.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 5px;
}

.contact-card:hover {
  transform: translateY(-5px);
}

.contact-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.contact-card h3 {
  color: #D836C4;
  margin-bottom: 10px;
  font-size: 1.3rem;
}

.contact-info p {
  margin-bottom: 8px;
  line-height: 1.2;
}

/* Карта */
.map-section {
  margin: 30px 0;
}

.map-section h3 {
  color: #ee5a24;
  margin-bottom: 20px;
  text-align: center;
}

.map-placeholder {
  background: #f8f9fa;
  border: 2px dashed #ddd;
  border-radius: 10px;
  padding: 3rem;
  text-align: center;
  margin-bottom: 3rem;
}

.map-placeholder img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 10px;
}

/* Социальные сети */
.social-section {
  margin: 30px 0;
}

.social-section h3 {
  color: #ee5a24;
  margin-bottom: 15px;
  text-align: center;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

.social-link {
  padding: 12px 25px;
  border-radius: 25px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  transition: all 0.3s ease;
  min-width: 140px;
  text-align: center;
}

.social-link.vk { background: #4C75A3; }
.social-link.telegram { background: #2AABEE; }
.social-link.youtube { background: #FF0000; }

.social-link:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

/* Администраторы */
.admins-section {
  margin: 20px 0;
}

.admins-section h3 {
  color: #ee5a24;
  margin-bottom: 20px;
  text-align: center;
}

.admins-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(40%, 1fr));
  gap: 20px;
}

.admin-card {
  background: white;
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  display: flex;
  gap: 20px;
  align-items: flex-start;
  transition: transform 0.3s ease;
}

.admin-card:hover {
  transform: translateY(-5px);
}

.admin-photo {
  flex-shrink: 0;
}

.admin-photo img {
  max-width: 100%;
  width: 100px;
  height: 100px;
  border-radius: 20%;
  object-fit: cover;
  border: 3px solid #D836C4;
}

.admin-info h4 {
  color: #D836C4;
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}

.admin-role {
  color: #ee5a24;
  font-weight: bold;
  margin-bottom: 8px;
  font-size: 0.9rem;
}

.admin-bio {
  color: #666;
  margin-bottom: 8px;
  line-height: 1.4;
}

.admin-contact {
  color: #D836C4;
  font-weight: bold;
}

/* Форма обратной связи */
.feedback-section {
  margin: 30px 0;
  background: white;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.feedback-section h3 {
  color: #ee5a24;
  margin-bottom: 20px;
  text-align: center;
}

.feedback-form {
  max-width: 800px;
  margin: 0 auto;
}

.form-row {
  display: grid;
  grid-template-columns: 400px 400px;
  gap: 1rem;
}

.feedback-form .form-group {
  margin-bottom: 15px;
}

.feedback-form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.feedback-form textarea {
  padding: 5px 10px;
  width: 100%;
  border-radius: 5px;
}
</style>