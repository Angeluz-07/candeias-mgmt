<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { 
  LogOut, 
  Dumbbell, 
  Flame, 
  User, 
  Calendar, 
  Activity 
} from 'lucide-vue-next'

const authStore = useAuthStore()

// Computed or direct access works great with Pinia
const user = authStore.user

const handleLogout = () => {
  authStore.logout()
  // You would typically redirect here, e.g., router.push('/login')
}
</script>

<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white flex flex-col font-sans">
    
    <nav class="w-full border-b border-zinc-800 bg-zinc-950/50 backdrop-blur-md sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <Flame class="text-[#FF6B00] w-8 h-8" />
          <span class="font-black italic text-2xl tracking-tighter uppercase">
            CANDE<span class="text-[#FF6B00]">IAS</span>
          </span>
        </div>
        
        <Button 
          variant="ghost" 
          @click="handleLogout"
          class="text-zinc-400 hover:text-[#FF6B00] hover:bg-zinc-900 transition-colors"
        >
          <LogOut class="w-5 h-5 mr-2" />
          <span class="hidden sm:inline">Cerrar Sesión</span>
        </Button>
      </div>
    </nav>

    <main class="flex-1 p-6 space-y-8 max-w-lg mx-auto w-full">
      
      <section class="mt-4">
        <h2 class="text-zinc-500 uppercase tracking-widest text-[10px] font-bold">Panel de Control</h2>
        <h1 class="text-4xl font-black mt-2 leading-tight uppercase">
          BIENVENIDO, <br />
          <span class="text-[#FF6B00] italic">{{ user?.name || 'ATLETA' }}</span>
        </h1>
        <p class="text-zinc-400 text-sm mt-2">
          Tu progreso de hoy está listo para ser registrado.
        </p>
      </section>

      <div class="grid grid-cols-2 gap-4">
        <div class="bg-zinc-900/50 p-4 rounded-2xl border border-zinc-800 space-y-3">
          <Activity class="text-[#FF6B00] w-6 h-6" />
          <div>
            <p class="text-[10px] uppercase text-zinc-500 font-bold">Calorías</p>
            <p class="text-2xl font-black italic">1,240</p>
          </div>
        </div>
        
        <div class="bg-zinc-900/50 p-4 rounded-2xl border border-zinc-800 space-y-3">
          <Calendar class="text-[#FF6B00] w-6 h-6" />
          <div>
            <p class="text-[10px] uppercase text-zinc-500 font-bold">Racha</p>
            <p class="text-2xl font-black italic">12 DÍAS</p>
          </div>
        </div>
      </div>

      <div class="bg-gradient-to-br from-zinc-900 to-black p-6 rounded-3xl border border-zinc-800 relative overflow-hidden group">
        <div class="relative z-10">
          <h3 class="font-bold text-lg">Entrenamiento del día</h3>
          <p class="text-zinc-400 text-sm mt-1">Pierna y Core - Intensidad Alta</p>
          <Button class="mt-4 bg-white text-black hover:bg-zinc-200 font-bold rounded-full px-6">
            EMPEZAR AHORA
          </Button>
        </div>
        <Dumbbell class="absolute -right-4 -bottom-4 w-32 h-32 text-white/5 rotate-12 group-hover:scale-110 transition-transform duration-500" />
      </div>

    </main>

    <footer class="md:hidden border-t border-zinc-800 bg-zinc-950 px-8 py-4 flex justify-between items-center sticky bottom-0">
      <Activity class="w-6 h-6 text-[#FF6B00]" />
      <Calendar class="w-6 h-6 text-zinc-600" />
      
      <div class="bg-[#FF6B00] p-3 rounded-full -mt-10 border-4 border-[#0A0A0A] shadow-lg active:scale-90 transition-transform">
        <Dumbbell class="w-6 h-6 text-black" />
      </div>
      
      <User class="w-6 h-6 text-zinc-600" />
      <LogOut @click="handleLogout" class="w-6 h-6 text-zinc-600 cursor-pointer" />
    </footer>
  </div>
</template>