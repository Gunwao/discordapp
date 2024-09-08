import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

const app = createApp(App)

// Globally configure Axios
app.config.globalProperties.$http = axios

// Mount the app to the DOM
app.mount('#app')
