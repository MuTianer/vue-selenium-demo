import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import SettingsView from '../views/SettingsView.vue'

const routes = [
  { path: '/', component: LoginView },
  { path: '/home', component: HomeView },
  { path: '/profile', component: ProfileView },
  { path: '/settings', component: SettingsView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
