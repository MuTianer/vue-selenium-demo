<template>
  <div>
    <h1>Welcome, {{ userStore.user?.username }}</h1>
    <el-button type="primary" @click="handleLogout">Logout</el-button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useUserStore } from '../store'

export default defineComponent({
  setup() {
    const userStore = useUserStore()

    const handleLogout = () => {
      userStore.logout()
    }

    return {
      userStore,
      handleLogout
    }
  }
})
</script>
