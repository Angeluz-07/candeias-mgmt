import axios from 'axios';
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

// --- STORE INTEGRADO PARA SIMPLICIDAD ---
interface AuthState {
  user: any | null;
  token: string | null;
  setAuth: (user: any, token: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null, token: null,
      setAuth: (user, token) => set({ user, token }),
      logout: () => { set({ user: null, token: null }); localStorage.clear(); },
    }),
    { name: 'fit-auth' }
  )
);

// --- CLIENTE AXIOS ---
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
});

api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token;
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;