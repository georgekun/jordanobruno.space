import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import VueMeta from 'vue-meta'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import './assets/styles/main.css'

const app = createApp(App)

const vuetify = createVuetify({
    components,
    directives,
  })
  
app.use(vuetify)
app.use(router)
// app.use(VueMeta)
app.mount('#app')
