import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from "@/views/LoginView.vue";
import CatalogView from "@/views/CatalogView.vue";
import SupportView from "@/views/SupportView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
      {
          path: '/catalog',
          name: 'catalog',
          component: CatalogView,
      },
      {
          path: '/support',
          name: 'support',
          component: SupportView,
      },
  ],
})

export default router