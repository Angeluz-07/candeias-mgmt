<script setup lang="ts">
// Assuming your auth logic is in a composable (like a hook)
import { useAuth } from '../composables/useAuth'
import { Card, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'

const { login, loading, error } = useAuth()

const handleSubmit = (e: Event) => {
  const target = e.target as HTMLFormElement
  const formData = new FormData(target)
  const data = Object.fromEntries(formData)
  
  // In Vue, we don't need to manually prevent default if we use 
  // the @submit.prevent modifier in the template (see below)
  login(data)
}
</script>

<template>
  <div class="min-h-screen bg-[#0A0A0A] flex flex-col items-center justify-center p-6 text-white">
    <div class="w-full max-w-[360px] space-y-10">
      
      <div class="text-center">
        <h1 class="text-6xl font-black italic tracking-tighter uppercase">
          FIT<span class="text-[#FF6B00]">CLUB</span>
        </h1>
        <p class="text-zinc-500 text-[10px] tracking-[0.3em] uppercase mt-2 font-bold">
          Guayaquil Edition
        </p>
      </div>

      <Card class="bg-zinc-900/40 border-zinc-800 backdrop-blur-xl rounded-2xl">
        <CardContent class="pt-8 pb-8 space-y-6">
          <form @submit.prevent="handleSubmit" class="space-y-4">
            
            <div class="space-y-1.5">
              <label class="text-[10px] uppercase font-bold text-zinc-500 ml-1">Usuario</label>
              <Input 
                name="email" 
                placeholder="email" 
                class="h-14 bg-zinc-800/50 border-none text-white rounded-xl focus:ring-[#FF6B00]" 
              />
            </div>

            <div class="space-y-1.5">
              <label class="text-[10px] uppercase font-bold text-zinc-500 ml-1">Contraseña</label>
              <Input 
                name="password" 
                type="password" 
                placeholder="••••••••" 
                class="h-14 bg-zinc-800/50 border-none text-white rounded-xl focus:ring-[#FF6B00]" 
              />
            </div>
            
            <p v-if="error" class="text-red-500 text-xs text-center font-bold animate-pulse">
              {{ error }}
            </p>

            <Button 
              type="submit"
              :disabled="loading" 
              class="w-full h-16 bg-[#FF6B00] hover:bg-[#e66000] text-black font-black text-xl rounded-xl transition-transform active:scale-95 shadow-[0_0_20px_rgba(255,107,0,0.3)]"
            >
              {{ loading ? "CARGANDO..." : "ENTRAR" }}
            </Button>
            
          </form>
        </CardContent>
      </Card>
      
    </div>
  </div>
</template>