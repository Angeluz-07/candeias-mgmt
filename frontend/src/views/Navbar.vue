<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router"; // Importante
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Menu } from "lucide-vue-next";
import { Flame } from "lucide-vue-next";
import { useAuthStore } from "@/stores/auth";

const menuItems = [
  { name: "Inicio", to: "/" },
  { name: "Historia", to: "/historia" },
  { name: "Quienes Somos", to: "/nosotros" },
  { name: "Contacto", to: "/contacto" },
];

const isOpen = ref(false);
const useAuth = useAuthStore();
const handleLogout = () => {
  useAuth.logout()
}
</script>

<template>
  <nav class="bg-black border-b border-white/10 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        
        <div class="md:hidden">
          <Sheet v-model:open="isOpen">
            <SheetTrigger asChild>
              <Button variant="ghost" class="text-white"><Menu /></Button>
            </SheetTrigger>
            <SheetContent side="left" class="bg-black border-white/10">
              <div class="flex flex-col space-y-6 mt-10">
                <RouterLink
                  v-for="item in menuItems"
                  :key="item.name"
                  :to="item.to"
                  @click="isOpen = false"
                  class="text-gray-300 hover:text-[#FF6B00] text-lg"
                  active-class="text-[#FF6B00]"
                >
                  {{ item.name }}
                </RouterLink>
                <Button
                  asChild
                  @click="isOpen = false"
                  class="bg-[#FF6B00] w-full"
                >
                  <RouterLink to="/login">Login</RouterLink>
                </Button>
              </div>
            </SheetContent>
          </Sheet>
        </div>
        
        <RouterLink to="/" class="text-white">
          <div class="flex items-center gap-2">
            <Flame class="text-[#FF6B00] w-8 h-8" />
            <span class="font-black italic text-2xl tracking-tighter">
              Cande<span class="text-[#FF6B00]">ias</span>
            </span>
          </div>
        </RouterLink>

        <div class="hidden md:flex items-center space-x-8">
          <RouterLink
            v-for="item in menuItems"
            :key="item.name"
            :to="item.to"
            class="text-gray-300 hover:text-[#FF6B00] transition-colors text-sm font-medium"
            active-class="text-[#FF6B00]"
          >
            {{ item.name }}
          </RouterLink>

        <Button
          v-if="useAuth.isAuthenticated"
          variant="ghost"
          @click="handleLogout"
          class="text-zinc-400 hover:text-[#FF6B00] hover:bg-zinc-900 transition-colors"
        >
          <LogOut class="w-5 h-5 mr-2" />
          <span class="hidden sm:inline">Cerrar Sesión</span>
        </Button>

        <Button v-else asChild class="bg-[#FF6B00] hover:bg-orange-600 text-white">
          <RouterLink to="/login">Login</RouterLink>
        </Button>
        </div>

      </div>
    </div>
  </nav>
</template>
