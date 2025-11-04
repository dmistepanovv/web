<template>
  <header>
    <div class="header-content">
      <div class="logo">
        <img src="@/assets/img/logo.png" alt="Логотип Strawberries"/>
        <h1> StrawBerries </h1>
      </div>
    </div>
  </header>
  <nav>
    <div class="nav-content">
      <a><RouterLink to="/">Главная страница</RouterLink></a>
      <a><RouterLink to="/login">Авторизация</RouterLink></a>
      <a><RouterLink to="/catalog">Каталог</RouterLink></a>
      <a><RouterLink to="/support">Поддержка</RouterLink></a>
    </div>
  </nav>
  <hr>
  <main>
    <router-view />
  </main>

  <footer>
    <div class="footer-content">
      <p>© 2025 StrawBerries. Народный маркетплейс</p>
      <p>Все права защищены</p>
    </div>
  </footer>
</template>

<style>
  /* общие настройки*/
  * {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
  }

  a {
    text-decoration: none;
  }

  img {
    max-width: 25%;
  }

  body {
    background-color: #f8f9fa;
    line-height: 160%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  /* Шапка сайта */
  header {
    background: linear-gradient(135deg, #D836C4, #ee5a24);
    color: white;
    padding: 0.5rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
  }

  .header-content {
    padding: 1% 2%;
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 15px;
  }

  .logo img {
    max-width: 10%;
    border-radius: 10px;
  }

  .logo h1 {
    font-size: 1.5rem;
    font-weight: bold;
  }

  /* Навигация */
  .nav-content {
    margin: 1%;
    padding: 0.5% 0;
    display: flex;
    gap: 2%;
  }

  nav a {
    padding: 10px 15px;
    border-radius: 5px;
  }

  .router-link-active {
    background-color: lightpink;
  }

  nav a:hover {
    background-color: #ff6b6b;
    transform: translateY(-2px);
  }

  main {
    max-width: 1920px;
    margin: 2% auto;
    padding: 2% 2%;
    width: 90%;
  }

  hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, #D836C4, transparent);
  }

  /* Подвал */
  footer {
    background-color: #D836C4;
    color: white;
    text-align: left;
    padding: 10px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
  }

  .footer-content {
    padding: 10px 20px;
  }
</style>
<script setup lang="ts">
</script>