import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const productService = {
    // Получить все продукты
    getAllProducts: () => api.get('/products'),

    // Получить продукты по типу категории
    getProductsByCategoryType: (type) => api.get(`/products/by_category_type/?type=${type}`),

    // Получить продукт по ID
    getProduct: (id) => api.get(`/products/${id}`),
};

export const categoryService = {
    // Получить все категории
    getAllCategories: () => api.get('/categories'),
};

export const supportService = {
    // Получить контакты поддержки
    getSupportContacts: () => api.get('/support-contacts'),
};

export const teamService = {
    // Получить членов команды
    getTeamMembers: () => api.get('/team-members'),
};

export default api;