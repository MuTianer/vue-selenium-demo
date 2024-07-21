<template>
  <div>
    <h1>Login</h1>
    <Login />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Login from '../components/Login.vue'

export default defineComponent({
  components: {
    Login
  }
})
</script>
