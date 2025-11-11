<template>
  <div class="catalog-section">
    <h3>🪆 Российская техника</h3>
    <div class="about-section">
      <p>Легендарные автомобили и мотоциклы советской и российской эпохи</p>
      <p>Данная техника пользуется большим спросом во всех странах СНГ</p>
    </div>

    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else class="products">
      <div v-for="product in russianProducts" :key="product.id" class="product-card">
        <h4>{{ product.name }}</h4>
        <p>{{ product.description }}</p>
        <img :src="getImageUrl(product.image_url)" :alt="product.name">
        <div class="price">{{ formatPrice(product.price) }} ₽</div>
        <div class="year">Год: {{ product.year }}</div>
        <button class="buy-btn">Подробнее</button>
      </div>
    </div>
  </div>

  <div class="catalog-section">
    <h3>🚗 Иномарки</h3>
    <div class="about-section">
      <p>Иностранные автомобили с историей</p>
      <p>Данная техника является эксклюзивной, её выбирают истинные любители</p>
    </div>

    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else class="products">
      <div v-for="product in foreignProducts" :key="product.id" class="product-card">
        <h4>{{ product.name }}</h4>
        <p>{{ product.description }}</p>
        <img :src="getImageUrl(product.image_url)" :alt="product.name">
        <div class="price">{{ formatPrice(product.price) }} ₽</div>
        <div class="year">Год: {{ product.year }}</div>
        <button class="buy-btn">Подробнее</button>
      </div>
    </div>
  </div>
</template>

<script>
import { productService } from '@/services/api'

export default {
  name: 'CatalogView',
  data() {
    return {
      loading: false,
      russianProducts: [],
      foreignProducts: []
    }
  },
  async mounted() {
    await this.loadProducts()
  },
  methods: {
    async loadProducts() {
      this.loading = true
      try {
        // Загружаем российскую технику
        const russianResponse = await productService.getProductsByCategoryType('russian')
        this.russianProducts = russianResponse.data

        // Загружаем иномарки
        const foreignResponse = await productService.getProductsByCategoryType('foreign')
        this.foreignProducts = foreignResponse.data
      } catch (error) {
        console.error('Ошибка загрузки продуктов:', error)
        // Fallback на статические данные
        this.loadStaticData()
      } finally {
        this.loading = false
      }
    },

    getImageUrl(imageUrl) {
      if (imageUrl) {
        return imageUrl.startsWith('http') ? imageUrl : `http://localhost:8000${imageUrl}`
      }
      return '/src/assets/img/placeholder.jpg'
    },

    formatPrice(price) {
      return new Intl.NumberFormat('ru-RU').format(price)
    },

    loadStaticData() {
      // Fallback данные, если API недоступно
      this.russianProducts = [
        {
          id: 1,
          name: 'ВАЗ 2101 "Копейка"',
          description: 'Легендарный автомобиль советской эпохи...',
          price: 450000,
          year: 1973,
          image_url: '/src/assets/img/2101.png'
        }
        // ... остальные статические данные
      ]
    }
  }
}
</script>

<style>
.catalog-section {
  margin: 10px 0;
}

.catalog-section h3 {
  color: #ee5a24;
  font-size: 2rem;
  margin-bottom: 20px;
  text-align: center;
}

.products {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 20px;
}

.product-card {
  background: white;
  border-radius: 15px;
  padding: 15px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
  text-align: center;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.product-card h4 {
  color: #D836C4;
  margin-bottom: 10px;
  font-size: 1.3rem;
}

.product-card p {
  color: #666;
  margin-bottom: 10px;
}

.product-card img {
  max-width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
  margin-top: 10px;
}

.price {
  font-size: 1.5rem;
  font-weight: bold;
  color: #ee5a24;
  margin: 10px;
}

.buy-btn {
  background: linear-gradient(135deg, #D836C4, #ee5a24);
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease;
}

.buy-btn:hover {
  transform: scale(1.05);
}
</style>