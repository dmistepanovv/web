const { spawn } = require('child_process');
const fs = require('fs');

console.log('Установка зависимостей фронтенда...');

// Проверяем наличие node_modules
if (!fs.existsSync('node_modules')) {
  console.log('Устанавливаем npm зависимости...');
  const install = spawn('npm', ['install'], { stdio: 'inherit' });

  install.on('close', (code) => {
    if (code === 0) {
      console.log('Запуск сервера разработки...');
      const dev = spawn('npm', ['run', 'dev'], { stdio: 'inherit' });
    } else {
      console.error('Ошибка установки зависимостей');
    }
  });
} else {
  console.log('Запуск сервера разработки...');
  const dev = spawn('npm', ['run', 'dev'], { stdio: 'inherit' });
}