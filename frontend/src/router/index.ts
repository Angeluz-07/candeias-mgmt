import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue' // Adjust paths based on your folder structure
import Home from '../views/Home.vue'
import { useAuthStore } from '@/stores/auth'

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

router.beforeEach(async (to) => {
  const authStore = useAuthStore();
  const isAuthenticated = !!authStore.user;
  const routeRequiresAuth = to.meta.requiresAuth;

  // CASO: La ruta requiere auth y el usuario NO está logueado
  if (routeRequiresAuth && !isAuthenticated) {
    return { name: 'login' };
  }
  // CASO: El usuario está logueado e intenta ir al LOGIN
  if (to.name === 'login' && isAuthenticated) {
    // Lo mandamos al home. IMPORTANTE: return evita que el código siga ejecutándose
    return { name: 'home' }; 
  }

  // CASO: Ruta desconocida
  if (!to.name) {
    if (isAuthenticated) {
      return { name: 'home' };
    } else {
      return { name: 'login' };
    }
  }

  // 3. CASO: Todo lo demás (dejar pasar)
  return true;
});
export default router