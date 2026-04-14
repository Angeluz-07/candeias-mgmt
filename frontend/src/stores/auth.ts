import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const user = ref<any>(null)
  const token = ref<string | null>(null)
  const isAuthenticated = computed(() => !!token?.value)

  function setToken(newToken: string) {
    token.value = newToken
  }
  function setUser(newUser: any) {
    user.value = newUser
  }

  function logout() {
    user.value = null
    token.value = null
  }

  return { user, token, isAuthenticated, setToken, setUser, logout }
}, 
{
  persist: true // <--- Con esto, Pinia se encarga de todo el LocalStorage por ti
})