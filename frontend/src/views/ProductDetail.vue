<template>
  <div class="product-detail">
    <div class="breadcrumb">
      <router-link to="/catalog">Каталог</router-link> / {{ product.name }}
    </div>

    <div class="product-content">
      <div class="product-image">
        <img :src="product.image_url" :alt="product.name" @error="handleImageError">
      </div>

      <div class="product-info">
        <h1>{{ product.name }}</h1>
        <p class="price">{{ formatPrice(product.price) }} ₽</p>
        <p class="description">{{ product.description }}</p>

        <div class="action-buttons">
          <button class="btn-primary" @click="contactSeller"><RouterLink to="/support">Связаться с продавцом</RouterLink></button>

          <button class="btn-secondary" @click="$router.back()">Назад к каталогу</button>
        </div>
      </div>
    </div>

    <div class="technical-details" v-if="hasTechnicalDetails">
      <h2>Технические характеристики</h2>
      <div class="specs-grid">
        <div class="spec-item" v-if="product.year">
          <span class="spec-label">Год выпуска:</span>
          <span class="spec-value">{{ product.year }}</span>
        </div>
        <div class="spec-item" v-if="product.fuel_consumption">
          <span class="spec-label">Расход топлива:</span>
          <span class="spec-value">{{ product.fuel_consumption }}</span>
        </div>
        <div class="spec-item" v-if="product.max_speed">
          <span class="spec-label">Максимальная скорость:</span>
          <span class="spec-value">{{ product.max_speed }}</span>
        </div>
        <div class="spec-item" v-if="product.engine_power">
          <span class="spec-label">Мощность двигателя:</span>
          <span class="spec-value">{{ product.engine_power }}</span>
        </div>
        <div class="spec-item" v-if="product.transmission">
          <span class="spec-label">Коробка передач:</span>
          <span class="spec-value">{{ product.transmission }}</span>
        </div>
        <div class="spec-item" v-if="product.drive_type">
          <span class="spec-label">Привод:</span>
          <span class="spec-value">{{ product.drive_type }}</span>
        </div>
        <div class="spec-item" v-if="product.color">
          <span class="spec-label">Цвет:</span>
          <span class="spec-value">{{ product.color }}</span>
        </div>
        <div class="spec-item" v-if="product.mileage">
          <span class="spec-label">Пробег:</span>
          <span class="spec-value">{{ product.mileage }}</span>
        </div>
      </div>
    </div>

    <div class="additional-info" v-if="product.technical_condition || product.features">
      <div class="info-section" v-if="product.technical_condition">
        <h3>Техническое состояние</h3>
        <p>{{ product.technical_condition }}</p>
      </div>

      <div class="info-section" v-if="product.features">
        <h3>Особенности</h3>
        <p>{{ product.features }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { productService } from '@/services/api'

export default {
  name: 'ProductDetail',
  data() {
    return {
      product: {},
      loading: false
    }
  },
  computed: {
    hasTechnicalDetails() {
      return this.product.year ||
          this.product.fuel_consumption ||
          this.product.max_speed ||
          this.product.engine_power ||
          this.product.transmission ||
          this.product.drive_type ||
          this.product.color ||
          this.product.mileage
    }
  },
  async mounted() {
    await this.loadProduct()
  },
  methods: {
    async loadProduct() {
      this.loading = true
      try {
        const productId = this.$route.params.id
        const response = await productService.getProduct(productId)
        this.product = response.data
      } catch (error) {
        console.error('Ошибка загрузки товара:', error)
        alert('Ошибка загрузки товара')
      } finally {
        this.loading = false
      }
    },

    formatPrice(price) {
      return new Intl.NumberFormat('ru-RU').format(price)
    },

    contactSeller() {
      alert('Функция связи с продавцом будет реализована позже')
    },

    handleImageError(event) {
      event.target.src = '/src/assets/img/placeholder.jpg'
    }
  }
}
</script>

<style scoped>
.product-detail {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.breadcrumb {
  margin-bottom: 20px;
  color: #666;
}

.breadcrumb a {
  color: #D836C4;
  text-decoration: none;
}

.product-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  margin-bottom: 40px;
}

.product-image img {
  max-width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 10px;
  margin-top: 10px;
}

.product-info h1 {
  color: #333;
  margin-bottom: 10px;
}

.price {
  font-size: 30px;
  color: #ee5a24;
  font-weight: bold;
  margin: 20px 20px;
}

.description {
  font-size: 16px;
  line-height: 1.6;
  color: #666;
  margin-bottom: 30px;
}

.action-buttons {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.btn-primary {
  background: linear-gradient(135deg, #D836C4, #ee5a24);
  color: white;
  padding: 12px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition: all 0.3s ease;
}

.btn-secondary {
  background: #f8f9fa;
  color: #333;
  padding: 12px 30px;
  border: 1px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition: all 0.3s ease;
}

.btn-primary:hover, .btn-secondary:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.technical-details, .additional-info {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  margin-bottom: 30px;
}

.additional-info h3 {
  color: #333;
  margin-bottom: 20px;
}

.technical-details h2{
  color: #333;
  margin-bottom: 20px;
  text-align: center;
}

.specs-grid {
  display: flex;
  flex-direction: column;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 15px;
}

.spec-item {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

.spec-label {
  font-weight: bold;
  color: #666;
}

.spec-value {
  color: #333;
}

.info-section {
  margin-bottom: 20px;
}

.info-section:last-child {
  margin-bottom: 0;
}

@media (max-width: 768px) {
  .product-content {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .specs-grid {
    grid-template-columns: 1fr;
  }
}
</style>