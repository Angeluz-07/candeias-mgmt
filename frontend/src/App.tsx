import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Login from './screens/Login';
import Home from './screens/Home'; // Nuevo import
import { useAuthStore } from './api/client';

export default function App() {
  const isAuth = useAuthStore(s => !!s.token);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={!isAuth ? <Login /> : <Navigate to="/home" />} />
        {/* Ruta Protegida */}
        <Route path="/home" element={isAuth ? <Home /> : <Navigate to="/login" />} />
        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>
    </BrowserRouter>
  );
}