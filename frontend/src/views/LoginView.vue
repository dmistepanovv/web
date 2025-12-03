<template>
  <div id="login-page" class="page">
    <h2 class="page-title">{{ showRegister ? 'Регистрация' : 'Вход в систему' }}</h2>

    <form class="auth-form" @submit.prevent="handleSubmit">
      <!-- Поля для регистрации -->
      <div v-if="showRegister" class="form-group">
        <label for="username">Имя пользователя *</label>
        <input
            type="text"
            id="username"
            v-model="form.username"
            required
            placeholder="Придумайте имя пользователя"
            :class="{ 'error': errors.username }"
        >
        <span v-if="errors.username" class="error-text">{{ errors.username }}</span>
      </div>

      <div class="form-group">
        <label for="email">{{ showRegister ? 'Email *' : 'Имя пользователя или Email *' }}</label>
        <input
            type="text"
            id="email"
            v-model="form.email"
            required
            :placeholder="showRegister ? 'Ваш email' : 'Введите ваш логин'"
            :class="{ 'error': errors.email }"
        >
        <span v-if="errors.email" class="error-text">{{ errors.email }}</span>
      </div>

      <div class="form-group">
        <label for="password">Пароль *</label>
        <input
            type="password"
            id="password"
            v-model="form.password"
            required
            placeholder="Введите ваш пароль"
            :class="{ 'error': errors.password }"
        >
        <span v-if="errors.password" class="error-text">{{ errors.password }}</span>
      </div>

      <div v-if="showRegister" class="form-group">
        <label for="password2">Подтверждение пароля *</label>
        <input
            type="password"
            id="password2"
            v-model="form.password2"
            required
            placeholder="Повторите пароль"
            :class="{ 'error': errors.password2 }"
        >
        <span v-if="errors.password2" class="error-text">{{ errors.password2 }}</span>
      </div>

      <!-- Дополнительные поля для регистрации -->
      <div v-if="showRegister" class="form-row">
        <div class="form-group">
          <label for="first_name">Имя *</label>
          <input
              type="text"
              id="first_name"
              v-model="form.first_name"
              placeholder="Ваше имя"
          >
        </div>

        <div class="form-group">
          <label for="last_name">Фамилия *</label>
          <input
              type="text"
              id="last_name"
              v-model="form.last_name"
              placeholder="Ваша фамилия"
          >
        </div>
      </div>

      <div v-if="showRegister" class="form-group">
        <label for="phone">Телефон</label>
        <input
            type="tel"
            id="phone"
            v-model="form.phone"
            placeholder="+7 (999) 123-45-67"
        >
      </div>

      <button
          type="submit"
          class="btn btn-primary"
          :disabled="loading"
      >
        <span v-if="loading" class="spinner"></span>
        {{ loading ? 'Загрузка...' : (showRegister ? 'Зарегистрироваться' : 'Войти') }}
      </button>

      <div class="auth-switch">
        <p>
          {{ showRegister ? 'Уже есть аккаунт?' : 'Еще нет аккаунта?' }}
          <a href="#" @click.prevent="toggleMode">
            {{ showRegister ? 'Войти' : 'Зарегистрироваться' }}
          </a>
        </p>
      </div>
    </form>

    <!-- Сообщения об ошибках -->
    <div v-if="authError" class="message error">
      <strong>Ошибка:</strong> {{ authError }}
    </div>

    <!-- Сообщения об успехе -->
    <div v-if="successMessage" class="message success">
      {{ successMessage }}
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth'
import { mapState, mapActions } from 'pinia'

export default {
  name: 'LoginView',
  data() {
    return {
      showRegister: false,
      form: {
        username: '',
        email: '',
        password: '',
        password2: '',
        first_name: '',
        last_name: '',
        phone: ''
      },
      errors: {},
      successMessage: ''
    }
  },
  computed: {
    ...mapState(useAuthStore, ['loading', 'error']),

    authError() {
      if (this.error) {
        if (typeof this.error === 'string') return this.error
        if (this.error.error) return this.error.error
        if (this.error.detail) return this.error.detail

        // Обработка ошибок валидации Django
        const firstError = Object.values(this.error)[0]
        if (Array.isArray(firstError)) return firstError[0]
        return JSON.stringify(this.error)
      }
      return null
    }
  },
  methods: {
    ...mapActions(useAuthStore, ['login', 'register', 'clearError']),

    toggleMode() {
      this.showRegister = !this.showRegister
      this.clearForm()
      this.clearError()
      this.successMessage = ''
    },

    clearForm() {
      this.form = {
        username: '',
        email: '',
        password: '',
        password2: '',
        first_name: '',
        last_name: '',
        phone: ''
      }
      this.errors = {}
    },

    validateForm() {
      this.errors = {}

      if (this.showRegister) {
        if (!this.form.username.trim()) {
          this.errors.username = 'Имя пользователя обязательно'
        }
        if (this.form.username.length < 3) {
          this.errors.username = 'Имя пользователя должно быть не менее 3 символов'
        }
      }

      if (!this.form.email.trim()) {
        this.errors.email = 'Email обязателен'
      } else if (!/\S+@\S+\.\S+/.test(this.form.email) && this.showRegister) {
        this.errors.email = 'Некорректный формат email'
      }

      if (!this.form.password) {
        this.errors.password = 'Пароль обязателен'
      } else if (this.form.password.length < 6) {
        this.errors.password = 'Пароль должен быть не менее 6 символов'
      }

      if (this.showRegister && this.form.password !== this.form.password2) {
        this.errors.password2 = 'Пароли не совпадают'
      }

      return Object.keys(this.errors).length === 0
    },

    async handleSubmit() {
      if (!this.validateForm()) return // Проверяем форму перед отправкой

      // Подготавливаем данные для отправки
      const credentials = this.showRegister
          ? { ...this.form } // Для регистрации - все поля
          : {
            username: this.form.email,
            password: this.form.password
          } // Для входа - только логин и пароль

      try {
        let result
        if (this.showRegister) {
          result = await this.register(credentials) // POST запрос на регистрацию
        } else {
          result = await this.login(credentials) // POST запрос на вход
        }

        if (result.success) { // Если успешно
          this.successMessage = this.showRegister
              ? 'Регистрация прошла успешно! Добро пожаловать!'
              : 'Вход выполнен успешно!'

          // Перенаправление после успешной аутентификации
          setTimeout(() => {
            this.$router.push('/')
          }, 1500)
        }
      } catch (error) {
        console.error('Auth error:', error)
      }
    }
  },

  mounted() {
    this.clearError()
  }
}
</script>

<style scoped>
.page {
  max-width: 500px;
  margin: 0 auto;
  padding: 2rem;
}

.page-title {
  text-align: center;
  color: #ee5a24;
  margin-bottom: 2rem;
  font-size: 2rem;
}

.auth-form {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
  border: 2px solid #f0f0f0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #333;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

.form-group input:focus {
  outline: none;
  border-color: #D836C4;
  box-shadow: 0 0 0 3px rgba(216, 54, 196, 0.1);
}

.form-group input.error {
  border-color: #e74c3c;
}

.error-text {
  color: #e74c3c;
  font-size: 0.875rem;
  margin-top: 0.25rem;
  display: block;
}

.btn-primary {
  background: linear-gradient(135deg, #D836C4, #ee5a24);
  color: white;
  padding: 14px 20px;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  margin-bottom: 1rem;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid transparent;
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-right: 8px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.auth-switch {
  text-align: center;
  margin-top: 1rem;
  color: #666;
}

.auth-switch a {
  color: #D836C4;
  text-decoration: none;
  font-weight: bold;
}

.auth-switch a:hover {
  text-decoration: underline;
}

.message {
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
  text-align: center;
  font-weight: bold;
}

.message.error {
  background-color: #ffebee;
  color: #c62828;
  border: 1px solid #ffcdd2;
}

.message.success {
  background-color: #e8f5e8;
  color: #2e7d32;
  border: 1px solid #c8e6c9;
}

@media (max-width: 768px) {
  .page {
    padding: 1rem;
  }

  .auth-form {
    padding: 1.5rem;
  }

  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>