import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue' // Adjust paths based on your folder structure
import Home from '../views/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login,
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      // You can add a "meta" field here for your Auth Guard later
      meta: { requiresAuth: true }
    },
  ],
})

export default router