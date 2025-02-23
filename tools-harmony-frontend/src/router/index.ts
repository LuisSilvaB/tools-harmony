import { isAuthenticated } from '@/views/auth/login/services/login.service'
import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/dashboard/DashboardView.vue'
import HomeView from '@/views/home/HomeView.vue'
import LoginView from '@/views/auth/login/LoginView.vue'
import RegisterView from '@/views/auth/register/RegisterView.vue'
import ConvertFile from '@/views/dashboard/ConvertFile/ConvertFile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/auth/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/auth/register',
      name: 'register',
      component: RegisterView,
      meta: {
        requiresAuth: false,
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta: {
        requiresAuth: true,
      },
      children: [
        {
          path: 'convert-file',
          name: 'convert-file',
          component: ConvertFile,
          meta: {
            requiresAuth: true,
          }
        },
      ]
    }
  ],
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated()) {
      next({ path: '/auth/login' })
    } else {
      next()
    }
  } else if ((to.path === '/auth/login' && isAuthenticated()) || (to.path === '/auth/register' && isAuthenticated())) {
    next({ path: '/dashboard' })
  } else {
    next()
  }
})

export default router
