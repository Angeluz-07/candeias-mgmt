import api from '@/api/client'

export const AuthService = {
  login: (credentials) => api.post('/login', credentials)
}