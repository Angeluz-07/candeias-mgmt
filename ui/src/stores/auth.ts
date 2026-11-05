import { defineStore } from 'pinia'
import { computed } from 'vue'
import { useAuth, useUser } from '@clerk/vue'

export const useAuthStore = defineStore('auth', () => {
  // Extraemos las herramientas oficiales de Clerk
  const { getToken, isLoaded, isSignedIn, signOut } = useAuth()
  const { user } = useUser()

  // Propiedades computadas limpias expuestas para toda la app
  const isAuthenticated = computed(() => !!isSignedIn.value)
  const currentUser = computed(() => user.value)
  const loading = computed(() => !isLoaded.value)

  // Método centralizado para obtener el token JWT para la API / Axios
  const getAuthToken = async () => {
    try {
      if (getToken.value) {
        return await getToken.value()
      }
      return null
    } catch (error) {
      console.error('Error al obtener el token en el store:', error)
      return null
    }
  }

  // Método centralizado para cerrar sesión
  const logout = async () => {
    try {
      await signOut.value()
    } catch (error) {
      console.error('Error al cerrar sesión:', error)
    }
  }

  return {
    isAuthenticated,
    currentUser,
    loading,
    getAuthToken,
    logout
  }
})