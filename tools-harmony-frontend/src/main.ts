
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { VueQueryPlugin } from '@tanstack/vue-query'
import App from '@/App.vue'
import router from './router/index'
import VueCookies from 'vue3-cookies';
import { setupInterceptors } from './lib/axios'
import Vue3Toasity, { type ToastContainerOptions } from 'vue3-toastify';
import { CIcon } from '@coreui/icons-vue';
import { ICONS } from './contants/icons'

import './assets/index.css'
import 'vue3-toastify/dist/index.css';

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

app.use(Vue3Toasity, {
  autoClose: 3000,
} as ToastContainerOptions);

app.provide('icons', ICONS)
app.component('CIcon', CIcon)

app.mount('#app')
