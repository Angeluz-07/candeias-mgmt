import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import axios from 'axios'

// Set your base URL once - Good for Guayaquil local dev or production
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000'
})

export function useAuth() {
  const store = useAuthStore()
  const router = useRouter()
  
  const loading = ref(false)
  const error = ref<string | null>(null)

  const login = async (credentials: any) => {
    loading.value = true
    error.value = null

    try {
      // 1. Post to Login
      const { data } = await api.post('/login', credentials)
      
      // 2. Fetch "Me" data (common pattern in your previous projects)
      const userResponse = await api.get('/me', {
        headers: { Authorization: `Bearer ${data.access_token}` }
      })

      // 3. Update Store
      store.setAuth(userResponse.data, data.access_token)

      // 4. Redirect
      router.push('/home')
    } catch (err: any) {
      error.value = err.response?.data?.detail || 'Error al iniciar sesión'
    } finally {
      loading.value = false
    }
  }

  return {
    login,
    loading,
    error,
    user: store.user,
    isAuthenticated: store.isAuthenticated
  }
}