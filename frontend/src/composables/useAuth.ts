import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { UserService } from "@/services/userService"; // Importas tus servicios
import { AuthService } from "@/services/authService";

export function useAuth() {
  const store = useAuthStore();
  const router = useRouter();
  const loading = ref(false);
  const error = ref(null);

  const login = async (credentials) => {
    loading.value = true;
    error.value = null;

    try {
      // 1. Llamada limpia al servicio
      const { data } = await AuthService.login(credentials);

      // Guardamos el token primero para que el interceptor lo use en la siguiente llamada
      store.setToken(data.access_token);

      // 2. Fetch "Me" (El interceptor ya pone el Bearer token solo)
      const userResponse = await UserService.getMe();

      // 3. Update Store completo
      store.setUser(userResponse.data);

      router.push("/payments");
    } catch (err) {
      error.value = err.response?.data?.detail || "Error al iniciar sesión";
    } finally {
      loading.value = false;
    }
  };

  return { login, loading, error };
}
