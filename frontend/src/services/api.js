import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

// Создаем экземпляр axios
const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Перехватчик для добавления токена к запросам
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Перехватчик для обработки ошибок авторизации
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshToken = localStorage.getItem('refreshToken');
                if (refreshToken) {
                    const response = await axios.post(`${API_BASE_URL}/auth/token/refresh/`, {
                        refresh: refreshToken
                    });

                    const { access } = response.data;
                    localStorage.setItem('accessToken', access);
                    originalRequest.headers.Authorization = `Bearer ${access}`;
                    return api(originalRequest);
                }
            } catch (refreshError) {
                console.error('Token refresh failed:', refreshError);
                localStorage.removeItem('accessToken');
                localStorage.removeItem('refreshToken');
                localStorage.removeItem('user');
                window.location.href = '/login';
            }
        }

        return Promise.reject(error);
    }
);

export const authService = {
    register: (userData) => api.post('/auth/register/', userData),
    login: (credentials) => api.post('/auth/login/', credentials),
    logout: (refreshToken) => api.post('/auth/logout/', { refresh_token: refreshToken }),
    getProfile: () => api.get('/auth/profile/'),
    refreshToken: (refresh) => api.post('/auth/token/refresh/', { refresh }),
};

export const productService = {
    // Получить все продукты
    getAllProducts: () => api.get('/products'),

    // Получить продукты по типу категории
    getProductsByCategoryType: (type) => api.get(`/products/by_category_type/?type=${type}`),

    // Получить продукт по ID
    getProduct: (id) => api.get(`/products/${id}`),
};

// Получить все категории
export const categoryService = {
    getAllCategories: () => api.get('/categories'),
};

// Получить контакты поддержки
export const supportService = {
    getSupportContacts: () => api.get('/support-contacts'),
};

// Получить членов команды
export const teamService = {
    getTeamMembers: () => api.get('/team-members'),
};

// Получить сообщения отзывов
export const feedbackService = {
    createFeedback: (data) => api.post('/feedback/', data),
    getFeedback: () => api.get('/feedback/'),
};

// Функции для работы с localStorage
export const authStorage = {
    setTokens: (access, refresh) => {
        localStorage.setItem('accessToken', access);
        localStorage.setItem('refreshToken', refresh);
    },
    getAccessToken: () => localStorage.getItem('accessToken'),
    getRefreshToken: () => localStorage.getItem('refreshToken'),
    clearTokens: () => {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        localStorage.removeItem('user');
    },
    setUser: (user) => localStorage.setItem('user', JSON.stringify(user)),
    getUser: () => {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    }
};

export default api;