
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { VueQueryPlugin } from '@tanstack/vue-query'
import App from '@/App.vue'
import router from './router/index'
import VueCookies from 'vue3-cookies';
import './assets/index.css'
import { setupInterceptors } from './lib/axios'

const app = createApp(App)

app.use(router)
app.use(createPinia())
app.use(VueQueryPlugin)
app.use(VueCookies)

router.isReady().then(setupInterceptors)

app.use(VueCookies, {
  expireTimes: "7d",
  path: "/",
  domain: "",
  secure: true,
  sameSite: "strict",
});


app.mount('#app')
