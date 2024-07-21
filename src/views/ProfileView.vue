<template>
  <div>
    <Navbar />
    <div class="content">
      <h1 id="page-title">Profile</h1>
      <p>Profile content goes here.</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Navbar from '../components/Navbar.vue'

export default defineComponent({
  components: {
    Navbar
  }
})
</script>

<style scoped>
.content {
  padding: 20px;
}
</style>
