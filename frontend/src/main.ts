import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate' // <--- Importar
import App from './App.vue'
import './style.css' 
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate) // <--- Registrar
app.use(router)
app.use(pinia)
app.mount('#app')