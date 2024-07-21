<template>
  <el-card class="info-card" shadow="hover">
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
    <slot></slot>
  </el-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    }
  }
})
</script>

<style scoped>
.info-card {
  margin: 20px;
  padding: 20px;
  border-radius: 8px;
}
</style>
