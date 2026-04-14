import api from '@/api/client'

export const UserService = {
  getMe: () => api.get('/me')
}
