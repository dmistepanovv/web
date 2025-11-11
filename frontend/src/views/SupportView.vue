<template>
  <div class="support-section">
    <h2>📞 Служба поддержки</h2>
    <p>Мы всегда готовы помочь вам! Выберите удобный способ связи.</p>

    <div class="contact-grid">
      <!-- Контактная информация -->
      <div class="contact-card" v-for="contact in supportContacts" :key="contact.id">
        <h3>{{ getContactIcon(contact.type) }} {{ contact.title }}</h3>
        <div class="contact-info">
          <p><strong>{{ contact.value }}</strong></p>
          <p v-if="contact.description">{{ contact.description }}</p>
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
        <div class="admin-card" v-for="member in teamMembers" :key="member.id">
          <div class="admin-photo">
            <img :src="getImageUrl(member.photo_url)" :alt="member.name">
          </div>
          <div class="admin-info">
            <h4>{{ member.name }}</h4>
            <p class="admin-role">{{ member.position }}</p>
            <p class="admin-bio">{{ member.bio }}</p>
            <p class="admin-contact">{{ member.email }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Форма обратной связи -->
    <div class="feedback-section">
      <h3>💬 Форма обратной связи</h3>
      <form class="feedback-form" @submit.prevent="submitFeedback">
        <div class="form-row">
          <div class="form-group">
            <label for="name">Ваше имя:</label>
            <input type="text" id="name" v-model="feedback.name" required placeholder="Иван Иванов">
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="feedback.email" required placeholder="ivan@example.com">
          </div>
        </div>

        <div class="form-group">
          <label for="topic">Тема обращения:</label>
          <select id="topic" v-model="feedback.topic" required>
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
          <textarea id="message" v-model="feedback.message" required placeholder="Опишите ваш вопрос подробно..." rows="5"></textarea>
        </div>

        <button type="submit" class="btn">Отправить сообщение</button>
      </form>
    </div>
  </div>
</template>

<script>
import { supportService, teamService, feedbackService } from '@/services/api'

export default {
  name: 'SupportView',
  data() {
    return {
      supportContacts: [],
      teamMembers: [],
      feedback: {
        name: '',
        email: '',
        topic: '',
        message: ''
      }
    }
  },
  async mounted() {
    await this.loadSupportContacts()
    await this.loadTeamMembers()
  },
  methods: {
    async loadSupportContacts() {
      try {
        const response = await supportService.getSupportContacts()
        this.supportContacts = response.data
      } catch (error) {
        console.error('Ошибка загрузки контактов:', error)
      }
    },

    async loadTeamMembers() {
      try {
        const response = await teamService.getTeamMembers()
        this.teamMembers = response.data
      } catch (error) {
        console.error('Ошибка загрузки команды:', error)
      }
    },

    async submitFeedback() {
      try {
        await feedbackService.createFeedback(this.feedback)
        alert('Сообщение отправлено успешно!')
        this.feedback = {
          name: '',
          email: '',
          topic: '',
          message: ''
        }
      } catch (error) {
        console.error('Ошибка отправки сообщения:', error)
        alert('Ошибка отправки сообщения. Попробуйте еще раз.')
      }
    },

    getContactIcon(type) {
      const icons = {
        'phone': '📞',
        'email': '✉️',
        'address': '📍',
        'schedule': '🕒'
      }
      return icons[type] || '📋'
    },

    getImageUrl(imageUrl) {
      if (imageUrl) {
        // Если путь начинается с /assets/, используем фронтенд
        if (imageUrl.startsWith('/assets/')) {
          return imageUrl
        }
        return `http://localhost:8000${imageUrl}`
      }
      return '/src/assets/img/placeholder.jpg'
    }
  }
}
</script>

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

.feedback-form input,
.feedback-form select,
.feedback-form textarea {
  width: 100%;
  padding: 10px;
  border: 2px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.feedback-form textarea {
  resize: vertical;
}

.btn {
  background: linear-gradient(135deg, #D836C4, #ee5a24);
  color: white;
  padding: 12px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
  width: 100%;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
</style>