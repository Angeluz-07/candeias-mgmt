import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const user = ref<any>(null)
  const token = ref<string | null>(null)
  const isAuthenticated = computed(() => !!token?.value)

  function setAuth(newUser: any, newToken: string) {
    user.value = newUser
    token.value = newToken
  }

  function logout() {
    user.value = null
    token.value = null
  }

  return { user, token, isAuthenticated, setAuth, logout }
}, 
{
  persist: true // <--- Con esto, Pinia se encarga de todo el LocalStorage por ti
})