<script setup lang="ts">
import Navbar from './views/Navbar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="min-h-screen bg-black"> <Navbar />
    
    <main>
      <RouterView />
    </main>
  </div>
</template>