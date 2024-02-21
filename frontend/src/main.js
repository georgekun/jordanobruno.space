import './assets/styles/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import VueMeta from 'vue-meta'

const app = createApp(App)


app.use(router)
// app.use(VueMeta)
app.mount('#app')
