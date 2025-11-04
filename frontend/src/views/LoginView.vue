<template>
  <div id="login-page" class="page">
    <h2 class="page-title">Вход в систему</h2>

    <form class="login-form">
      <div class="form-group">
        <label for="username">Имя пользователя или Email:</label>
        <input type="text" id="username" name="username" required placeholder="Введите ваш логин">
      </div>

      <div class="form-group">
        <label for="password">Пароль:</label>
        <input type="password" id="password" name="password" required placeholder="Введите ваш пароль">
      </div>

      <button type="submit" class="btn">Войти</button>
      <div class="register-link">
        <p>Еще нет аккаунта? <a href="#">Зарегистрироваться</a></p>
      </div>
    </form>
  </div>
</template>

<style>
.page-title {
  font-size: 1.8rem;
  margin: 10px 0;
  text-align: center;
}

.login-form {
  max-width: 200px;
  margin: 0 auto 20px;
  background-color: lightsalmon;
  border: #D836C4 solid 2px;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #2c2c2c;
}

.form-group input {
  width: 100%;
  padding: 4px;
  border: 2px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.btn {
  background-color: #ff6b6b;
  color: white;
  padding: 12px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
  width: 100%;
}

.btn:hover {
  background-color: #ee5a24;
}

.register-link {
  text-align: center;
  margin-top: 10px;
  color: #666;
}
</style>