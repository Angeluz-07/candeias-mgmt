<script setup lang="ts">
import { useAuth } from '../composables/useAuth'

const { login, loading, error } = useAuth()

const handleSubmit = (e: Event) => {
  const target = e.target as HTMLFormElement
  const formData = new FormData(target)
  const data = Object.fromEntries(formData)
  login(data)
}
</script>

<template>
  <div class="min-h-screen bg-black flex flex-col items-center justify-center p-6 text-white">
    <div class="w-full max-w-[360px] space-y-10">
      
      <div class="text-center">
        <h1 class="text-6xl font-black italic tracking-tighter">
           Cande<span class="text-primary">ias</span>
        </h1>
        <p class="text-zinc-500 text-[10px] tracking-[0.3em] uppercase mt-2 font-bold">
           Guayaquil - Ecuador
        </p>
      </div>

      <div class="card bg-zinc-900/40 border border-white/5 backdrop-blur-xl rounded-2xl">
        <div class="card-body pt-8 pb-8 space-y-6">
          <form @submit.prevent="handleSubmit" class="space-y-4">
            
            <div class="form-control w-full space-y-1.5">
              <label class="text-[10px] uppercase font-bold text-zinc-500 ml-1">Usuario</label>
              <input 
                name="email" 
                type="email"
                placeholder="email" 
                class="input input-bordered w-full h-14 bg-zinc-800/50 border-none text-white rounded-xl focus:outline-primary" 
              />
            </div>

            <div class="form-control w-full space-y-1.5">
              <label class="text-[10px] uppercase font-bold text-zinc-500 ml-1">Contraseña</label>
              <input 
                name="password" 
                type="password" 
                placeholder="••••••••" 
                class="input input-bordered w-full h-14 bg-zinc-800/50 border-none text-white rounded-xl focus:outline-primary" 
              />
            </div>
            
            <p v-if="error" class="text-error text-xs text-center font-bold animate-pulse">
              {{ error }}
            </p>

            <button 
              type="submit"
              :disabled="loading" 
              class="btn btn-primary w-full h-16 text-black font-black text-xl rounded-xl transition-transform active:scale-95 border-none"
            >
              {{ loading ? "Cargando..." : "Entrar" }}
            </button>
            
          </form>
        </div>
      </div>
      
    </div>
  </div>
</template>