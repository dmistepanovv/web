import { defineStore } from 'pinia'; // для создания хранилища состояния
import { authService, authStorage } from '@/services/api';


// Создание хранилища данных, доступные из любого компонента
export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: authStorage.getUser(),
        isAuthenticated: !!authStorage.getAccessToken(),
        loading: false,
        error: null
    }),

    actions: { // Методы хранилища
        async register(userData) {
            this.loading = true;
            this.error = null;

            try {
                // Отправляем запрос на сервер
                const response = await authService.register(userData);

                // Получаем данные ответа
                const { user, access, refresh } = response.data;

                // Сохраняем в localStorage
                authStorage.setTokens(access, refresh);
                authStorage.setUser(user);

                // Обновляем состояние хранилища
                this.user = user;
                this.isAuthenticated = true;
                this.loading = false;

                return { success: true, user };
            } catch (error) {
                this.loading = false;
                this.error = error.response?.data || { error: 'Registration failed' };
                return { success: false, error: this.error };
            }
        },

        // Такая же логика как выше, толь не создание, а вход
        async login(credentials) {
            this.loading = true;
            this.error = null;

            try {
                const response = await authService.login(credentials);
                const { user, access, refresh } = response.data;

                authStorage.setTokens(access, refresh);
                authStorage.setUser(user);

                this.user = user;
                this.isAuthenticated = true;
                this.loading = false;

                return { success: true, user };
            } catch (error) {
                this.loading = false;
                this.error = error.response?.data || { error: 'Login failed' };
                return { success: false, error: this.error };
            }
        },

        async logout() {
            try {
                const refreshToken = authStorage.getRefreshToken();
                if (refreshToken) {
                    await authService.logout(refreshToken);
                }
            } catch (error) {
                console.error('Logout error:', error);
            } finally {
                authStorage.clearTokens();
                this.user = null;
                this.isAuthenticated = false;
            }
        },

        async checkAuth() { // Проверка токена на авторизацию
            if (authStorage.getAccessToken()) {
                try {
                    const response = await authService.getProfile();
                    this.user = response.data;
                    this.isAuthenticated = true;
                } catch (error) {
                    this.logout();
                }
            }
        },

        clearError() {
            this.error = null;
        }
    },

    getters: { // геттеры вычисляют значения на основе state
        getUser: (state) => state.user,
        isLoggedIn: (state) => state.isAuthenticated,
        isLoading: (state) => state.loading,
        getError: (state) => state.error
    }
});