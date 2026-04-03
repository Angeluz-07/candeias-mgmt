import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api, { useAuthStore } from '../api/client';

export const useAuthLogic = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const { setAuth } = useAuthStore();
  const navigate = useNavigate();

  const login = async (credentials: any) => {
    setLoading(true);
    setError(null);
    try {
      // 1. Login
      const res = await api.post('/login', credentials);
      const token = res.data.access_token;
      
      // 2. Get User (El interceptor ya tiene el token porque Zustand es reactivo)
      const userRes = await api.get('/me', { headers: { Authorization: `Bearer ${token}` }});
      
      setAuth(userRes.data, token);
      navigate('/home');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error de autenticación');
    } finally {
      setLoading(false);
    }
  };

  return { login, loading, error };
};