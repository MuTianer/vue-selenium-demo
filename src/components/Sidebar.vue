<template>
  <el-menu class="el-menu-vertical-demo" unique-opened>
    <el-sub-menu index="1">
      <template #title><i class="el-icon-message"></i>Messages</template>
      <el-menu-item index="1-1">Inbox</el-menu-item>
      <el-menu-item index="1-2">Sent</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="2">
      <template #title><i class="el-icon-menu"></i>Other</template>
      <el-menu-item index="2-1">Option 1</el-menu-item>
      <el-menu-item index="2-2">Option 2</el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style scoped>
.el-menu-vertical-demo {
  width: 200px;
  min-height: 100vh;
  border-right: 1px solid #eaeaea;
}
</style>
