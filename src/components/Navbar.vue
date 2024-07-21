<template>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
    <el-menu-item itemid="home-menu" index="1" @click="navigateTo('/home')">Home</el-menu-item>
    <el-menu-item itemid="profile-menu" index="2" @click="navigateTo('/profile')"
      >Profile</el-menu-item
    >
    <el-menu-item itemid="settings-menu" index="3" @click="navigateTo('/settings')"
      >Settings</el-menu-item
    >
  </el-menu>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

export default defineComponent({
  setup() {
    const router = useRouter()
    const route = useRoute()
    const activeIndex = ref('1')

    watch(
      () => route.path,
      (newPath) => {
        switch (newPath) {
          case '/home':
            activeIndex.value = '1'
            break
          case '/profile':
            activeIndex.value = '2'
            break
          case '/settings':
            activeIndex.value = '3'
            break
          default:
            activeIndex.value = '1'
        }
      },
      { immediate: true }
    )

    const navigateTo = (path: string) => {
      router.push(path)
    }

    return {
      activeIndex,
      navigateTo
    }
  }
})
</script>

<style scoped>
.el-menu-demo {
  line-height: 60px;
}
</style>
