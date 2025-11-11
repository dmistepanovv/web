import { defineStore } from 'pinia';
import { authService, authStorage } from '@/services/api';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: authStorage.getUser(),
        isAuthenticated: !!authStorage.getAccessToken(),
        loading: false,
        error: null
    }),

    actions: {
        async register(userData) {
            this.loading = true;
            this.error = null;

            try {
                const response = await authService.register(userData);
                const { user, access, refresh } = response.data;

                authStorage.setTokens(access, refresh);
                authStorage.setUser(user);

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

        async checkAuth() {
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

    getters: {
        getUser: (state) => state.user,
        isLoggedIn: (state) => state.isAuthenticated,
        isLoading: (state) => state.loading,
        getError: (state) => state.error
    }
});