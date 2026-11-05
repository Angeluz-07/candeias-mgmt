<script setup lang="ts">
import StudentTable from "../StudentTable.vue";
import DashboardNavbar from "./DashboardNavbar.vue";
</script>

<template>
  <DashboardNavbar></DashboardNavbar>
  <div class="p-6">
    <StudentTable></StudentTable>
  </div>
</template>
