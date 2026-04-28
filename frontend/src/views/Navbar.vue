<script setup>
import { RouterLink } from "vue-router";
import { Menu, Flame, LogOut } from "lucide-vue-next";
import { useAuthStore } from "@/stores/auth";
import { computed } from 'vue'

const useAuth = useAuthStore();
const handleLogout = () => useAuth.logout();

const menuItems = [
  { name: "Historia", to: "/historia" },
  { name: "Quienes Somos", to: "/nosotros" },
  { name: "Contacto", to: "/contacto" },
  { name: "Pagos", to: "/payments", private: true },
];

const visibleMenuItems = computed(() => {
  return menuItems.filter(item => !item.private || useAuth.isAuthenticated);
});
</script>

<template>
  <div class="drawer z-50">
    <input id="nav-drawer" type="checkbox" class="drawer-toggle" />
    
    <div class="drawer-content flex flex-col">
      <nav class="bg-black border-b border-white/10 w-full h-16">
        <div class="max-w-7xl mx-auto px-4 h-full flex items-center justify-between">
          
          <label for="nav-drawer" class="btn btn-ghost btn-sm md:hidden text-white">
            <Menu class="w-6 h-6" />
          </label>

          <RouterLink to="/" class="text-white">
            <div class="flex items-center gap-2">
              <Flame class="text-primary w-8 h-8" />
              <span class="font-black italic text-2xl tracking-tighter">
                Cande<span class="text-primary">ias</span>
              </span>
            </div>
          </RouterLink>

          <div class="hidden md:flex items-center space-x-8">
            <RouterLink
              v-for="item in visibleMenuItems"
              :key="item.name"
              :to="item.to"
              class="text-gray-300 hover:text-primary transition-colors text-sm font-medium"
              active-class="text-primary"
            >
              {{ item.name }}
            </RouterLink>

            <button
              v-if="useAuth.isAuthenticated"
              @click="handleLogout"
              class="btn btn-ghost btn-sm text-zinc-400 hover:text-primary"
            >
              <LogOut class="w-5 h-5 mr-2" />
              Cerrar Sesión
            </button>

            <RouterLink v-else to="/login" class="btn btn-primary btn-sm text-white">
              Login
            </RouterLink>
          </div>
        </div>
      </nav>
    </div>

    <div class="drawer-side">
      <label for="nav-drawer" class="drawer-overlay"></label>
      <div class="p-4 w-80 min-h-full bg-black border-r border-white/10 flex flex-col gap-6 pt-10">
        <RouterLink
          v-for="item in visibleMenuItems"
          :key="item.name"
          :to="item.to"
          class="text-gray-300 hover:text-primary text-lg"
          active-class="text-primary"
        >
          {{ item.name }}
        </RouterLink>

        <button
          v-if="useAuth.isAuthenticated"
          @click="handleLogout"
          class="btn btn-ghost justify-start text-zinc-400 hover:text-primary"
        >
          <LogOut class="w-5 h-5 mr-2" />
          Cerrar Sesión
        </button>

        <RouterLink v-else to="/login" class="btn btn-primary w-full">
          Login
        </RouterLink>
      </div>
    </div>
  </div>
</template>