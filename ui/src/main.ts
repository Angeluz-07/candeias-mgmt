import { createApp } from "vue";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate"; // <--- Importar
import App from "./App.vue";
import "./style.css";
import router from "./router";
import PrimeVue from "primevue/config";
import Aura from "@primeuix/themes/aura";
import { clerkPlugin } from "@clerk/vue";

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;

if (!PUBLISHABLE_KEY) {
  throw new Error("Add your Clerk Publishable Key to the .env file");
}

const app = createApp(App);
app.use(clerkPlugin, { publishableKey: PUBLISHABLE_KEY });

app.use(router);

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate); // <--- Registrar
app.use(pinia);

app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
});
app.mount("#app");
