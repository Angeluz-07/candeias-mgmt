import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import { useAuthStore } from "@/stores/auth";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "home", component: Home },
    {
      path: "/historia",
      name: "history",
      component: () => import("../views/History.vue"),
    },
    {
      path: "/nosotros",
      name: "aboutUs",
      component: () => import("../views/AboutUs.vue"),
    },
    {
      path: "/contacto",
      name: "contacto",
      component: () => import("../views/Contact.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/Login.vue"),
    },
    {
      path: "/payments",
      name: "payments",
      component: () => import("../views/Payments.vue"),
      meta: { requiresAuth: true },
    },
  ],
});

router.beforeEach(async (to) => {
  const authStore = useAuthStore();
  const isAuthenticated = authStore.isAuthenticated;
  const routeRequiresAuth = to.meta.requiresAuth;

  // CASO: La ruta requiere auth y el usuario NO está logueado
  if (routeRequiresAuth && !isAuthenticated) {
    return { name: "home" };
  }
  // CASO: El usuario está logueado e intenta ir al LOGIN
  if (to.name === "login" && isAuthenticated) {
    // Lo mandamos al home. IMPORTANTE: return evita que el código siga ejecutándose
    return { name: "home" };
  }

  // CASO: Ruta desconocida
  if (!to.name) {
    return { name: "home" };
  }

  // 3. CASO: Todo lo demás (dejar pasar)
  return true;
});
export default router;
