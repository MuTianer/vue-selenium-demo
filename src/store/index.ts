import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    isAuthenticated: false,
    user: null as { username: string } | null
  }),
  actions: {
    login(username: string) {
      this.isAuthenticated = true
      this.user = { username }
    },
    logout() {
      this.isAuthenticated = false
      this.user = null
    }
  }
})
