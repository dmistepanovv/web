<template>
  <div class="catalog-section">
    <!-- Поисковая строка -->
    <div class="search-container">
      <div class="search-box">
        <input
            type="text"
            v-model="searchQuery"
            placeholder="Поиск товаров по названию, описанию или категории..."
            @input="handleSearch"
            class="search-input"
        >
        <span class="search-icon">🔍</span>
      </div>
      <div class="search-results-info" v-if="searchQuery">
        Найдено товаров: {{ totalProducts }}
      </div>
    </div>

    <div class="catalog-filters">
      <button
          class="filter-btn"
          :class="{ active: activeFilter === 'all' }"
          @click="setFilter('all')"
      >
        Все товары
      </button>
      <button
          class="filter-btn"
          :class="{ active: activeFilter === 'russian' }"
          @click="setFilter('russian')"
      >
        🇷🇺 Российские
      </button>
      <button
          class="filter-btn"
          :class="{ active: activeFilter === 'foreign' }"
          @click="setFilter('foreign')"
      >
        🚗 Иномарки
      </button>
    </div>

    <div v-if="loading" class="loading">Загрузка...</div>

    <div v-else>
      <!-- Российская техника -->
      <div class="category-section" v-if="showRussian">
        <h3>🪆 Российская техника</h3>
        <div class="about-section">
          <p>Легендарные автомобили и мотоциклы советской и российской эпохи</p>
        </div>

        <div class="products">
          <div v-for="product in filteredRussianProducts" :key="product.id" class="product-card">
            <h4>{{ product.name }}</h4>
            <p>{{ product.description }}</p>
            <img :src="getImageUrl(product.image_url)" :alt="product.name" @error="handleImageError">
            <div class="price">{{ formatPrice(product.price) }} ₽</div>
            <div class="year">Год: {{ product.year }}</div>
            <button
                class="buy-btn"
                @click="$router.push({ name: 'product', params: { id: product.id } })"
            >
              Подробнее
            </button>
          </div>
        </div>
      </div>

      <!-- Иномарки -->
      <div class="category-section" v-if="showForeign">
        <h3>🚗 Иномарки</h3>
        <div class="about-section">
          <p>Иностранные автомобили с историей</p>
        </div>

        <div class="products">
          <div v-for="product in filteredForeignProducts" :key="product.id" class="product-card">
            <h4>{{ product.name }}</h4>
            <p>{{ product.description }}</p>
            <img :src="getImageUrl(product.image_url)" :alt="product.name" @error="handleImageError">
            <div class="price">{{ formatPrice(product.price) }} ₽</div>
            <div class="year">Год: {{ product.year }}</div>
            <button
                class="buy-btn"
                @click="$router.push({ name: 'product', params: { id: product.id } })"
            >
              Подробнее
            </button>
          </div>
        </div>
      </div>

      <!-- Сообщение если ничего не найдено -->
      <div v-if="!hasProducts && searchQuery" class="no-results">
        <p>По запросу "{{ searchQuery }}" ничего не найдено</p>
        <button @click="clearSearch" class="btn-secondary">Показать все товары</button>
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
      searchQuery: '',
      activeFilter: 'all',
      allProducts: [],
      searchTimeout: null
    }
  },
  computed: {
    filteredRussianProducts() {
      let products = this.allProducts.filter(p => p.category_type === 'russian')

      if (this.searchQuery) {
        products = this.filterProductsBySearch(products)
      }

      return products
    },

    filteredForeignProducts() {
      let products = this.allProducts.filter(p => p.category_type === 'foreign')

      if (this.searchQuery) {
        products = this.filterProductsBySearch(products)
      }

      return products
    },

    showRussian() {
      return (this.activeFilter === 'all' || this.activeFilter === 'russian') &&
          this.filteredRussianProducts.length > 0
    },

    showForeign() {
      return (this.activeFilter === 'all' || this.activeFilter === 'foreign') &&
          this.filteredForeignProducts.length > 0
    },

    hasProducts() {
      return this.filteredRussianProducts.length > 0 || this.filteredForeignProducts.length > 0
    },

    totalProducts() {
      return this.filteredRussianProducts.length + this.filteredForeignProducts.length
    }
  },
  async mounted() {
    await this.loadProducts()
  },
  methods: {
    async loadProducts() {
      this.loading = true
      try {
        const response = await productService.getAllProducts()
        this.allProducts = response.data
      } catch (error) {
        console.error('Ошибка загрузки продуктов:', error)
      } finally {
        this.loading = false
      }
    },

    handleSearch() {
      // Дебаунс поиска - ждем 300ms после последнего ввода
      clearTimeout(this.searchTimeout)
      this.searchTimeout = setTimeout(() => {
        this.performSearch()
      }, 300)
    },

    async performSearch() {
      if (!this.searchQuery) {
        await this.loadProducts()
        return
      }

      this.loading = true
      try {
        const response = await productService.getAllProducts()
        // Фильтруем на клиенте для простоты
        this.allProducts = response.data.filter(product =>
            product.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            product.description.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            (product.category && product.category.name.toLowerCase().includes(this.searchQuery.toLowerCase()))
        )
      } catch (error) {
        console.error('Ошибка поиска:', error)
      } finally {
        this.loading = false
      }
    },

    filterProductsBySearch(products) {
      return products.filter(product =>
          product.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          product.description.toLowerCase().includes(this.searchQuery.toLowerCase())
      )
    },

    setFilter(filter) {
      this.activeFilter = filter
    },

    clearSearch() {
      this.searchQuery = ''
      this.loadProducts()
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

    handleImageError(event) {
      event.target.src = '/src/assets/img/placeholder.jpg'
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

/* Для поиска*/
.search-container {
  margin-bottom: 30px;
}

.search-box {
  position: relative;
  max-width: 600px;
  margin: 0 auto 15px;
}

.search-input {
  width: 100%;
  padding: 15px 50px 15px 20px;
  border: 2px solid #ddd;
  border-radius: 25px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #D836C4;
  box-shadow: 0 0 0 3px rgba(216, 54, 196, 0.1);
}

.search-icon {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2rem;
}

.search-results-info {
  text-align: center;
  color: #666;
  font-style: italic;
}

.catalog-filters {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 10px 20px;
  border: 2px solid #D836C4;
  background: white;
  color: #D836C4;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: bold;
}

.filter-btn:hover {
  background: #f8f9fa;
  transform: translateY(-2px);
}

.filter-btn.active {
  background: #D836C4;
  color: white;
}

.category-section {
  margin: 40px 0;
}

.no-results {
  text-align: center;
  padding: 60px 20px;
  color: #666;
}

.no-results p {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

.loading {
  text-align: center;
  padding: 40px;
  font-size: 1.2rem;
  color: #666;
}

/* Адаптивность */
@media (max-width: 768px) {
  .search-input {
    padding: 12px 45px 12px 15px;
  }

  .catalog-filters {
    gap: 10px;
  }

  .filter-btn {
    padding: 8px 16px;
    font-size: 0.9rem;
  }
}
</style>