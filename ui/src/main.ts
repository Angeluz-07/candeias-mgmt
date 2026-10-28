import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate' // <--- Importar
import App from './App.vue'
import './style.css' 
import router from './router'
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';

const app = createApp(App)
app.use(router)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate) // <--- Registrar
app.use(pinia)

app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});
app.mount('#app')