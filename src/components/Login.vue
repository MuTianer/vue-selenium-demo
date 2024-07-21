<template>
  <el-card class="login-card" shadow="hover">
    <h2 class="login-title">Login</h2>
    <el-form @submit.native.prevent="handleLogin" label-width="auto">
      <el-form-item label="Username" :error="usernameError">
        <el-input v-model="username" placeholder="Enter your username" />
      </el-form-item>
      <el-form-item label="Password" :error="passwordError">
        <el-input v-model="password" type="password" placeholder="Enter your password" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleLogin">Login</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useUserStore } from '../store'
import { useRouter } from 'vue-router'

export default defineComponent({
  setup() {
    const userStore = useUserStore()
    const router = useRouter()
    const username = ref('')
    const password = ref('')
    const usernameError = ref('')
    const passwordError = ref('')

    const validateInputs = () => {
      let valid = true
      if (!username.value) {
        usernameError.value = 'Username is required'
        valid = false
      } else {
        usernameError.value = ''
      }
      if (!password.value) {
        passwordError.value = 'Password is required'
        valid = false
      } else {
        passwordError.value = ''
      }
      return valid
    }

    const handleLogin = () => {
      if (validateInputs()) {
        userStore.login(username.value)
        router.push('/home')
      }
    }

    return {
      username,
      password,
      usernameError,
      passwordError,
      handleLogin
    }
  }
})
</script>

<style scoped>
.login-card {
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.login-title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: bold;
}
</style>
