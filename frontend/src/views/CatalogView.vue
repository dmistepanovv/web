<template>
  <div class="catalog-section">
    <h3>🪆 Российская техника</h3>

    <div class="about-section">
      <p>Легендарные автомобили и мотоциклы советской и российской эпохи</p>
      <p>Данная техника пользуется большим спросом во всех странах СНГ</p>
      <p></p>
    </div>
    <div class="products">
      <div class="product-card">
        <h4>ВАЗ 2101 "Копейка"</h4>
        <p>Легендарный автомобиль советской эпохи 1973 года выпуска. Полностью восстановлен, оригинальный двигатель. Отличное техническое состояние, все документы в порядке.</p>
        <img src="@/assets/img/2101.png" alt="ВАЗ 2101">
        <div class="price">450 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>

      <div class="product-card">
        <h4>ИЖ Планета-4</h4>
        <p>Культовый советский мотоцикл 1985 года. Надежный двигатель 350cc, классический дизайн. Полностью оригинальные детали, полная комплектация.</p>
        <img src="@/assets/img/IJ4.png" alt="ИЖ Планета-4">
        <div class="price">85 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>

      <div class="product-card">
        <h4>УАЗ-469</h4>
        <p>Внедорожник 1990 года. Легенда бездорожья. Полный привод, усиленная подвеска. Идеален для охоты и рыбалки.</p>
        <img src="@/assets/img/uaz469.jpg" alt="УАЗ-469">
        <div class="price">320 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>

      <div class="product-card">
        <h4>Москвич-412</h4>
        <p>Советский седан 1978 года. Редкий экземпляр в отличном состоянии. Полностью оригинальный салон.</p>
        <img src="@/assets/img/moskvich412.jpg" alt="Москвич-412">
        <div class="price">280 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>
      <div class="product-card">
        <h4>Лада (ВАЗ) 2110</h4>
        <p>Первая "иномарка", выпущенная на просторах России. Экономичность, неплохая динамика. Такая есть даже у нашего администратора!</p>
        <img src="@/assets/img/vaz2110.jpg" alt="Лада (ВАЗ) 2110">
        <div class="price">480 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>
      <div class="product-card">
        <h4>Лада Аура</h4>
        <p>Флагман российского автомобилестроения. Комфорт и эргономичность это про неё.</p>
        <img src="@/assets/img/vazaura.jpg" alt="Лада Аура">
        <div class="price">2 780 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>
    </div>
  </div>

  <div class="catalog-section">

    <h3>🚗 Иномарки</h3>
    <div class="about-section">
      <p>Иностранные автомобили с историей</p>
      <p>Данная техника является эксклюзивной, её выбирают истинные любители </p>
    </div>

    <div class="products">
      <div class="product-card">
        <h4>Volkswagen Golf II</h4>
        <p>Немецкий хэтчбек 1990 года. Культовая модель в отличном состоянии.</p>
        <img src="@/assets/img/golf2.jpg" alt="Volkswagen Golf II">
        <div class="price">350 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>

      <div class="product-card">
        <h4>Ford Mustang 1968</h4>
        <p>Американская легенда. V8 двигатель, полностью восстановлен.</p>
        <img src="@/assets/img/mustang68.jpg" alt="Ford Mustang 1968">
        <div class="price">2 500 000 ₽</div>
        <button class="buy-btn">Подробнее</button>
      </div>
    </div>
  </div>
</template>

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