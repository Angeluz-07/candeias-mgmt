<script setup lang="ts">
import { ref, onMounted } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import { StudentService } from '@/composables/studentService';

const students = ref([]);
const loading = ref(true);
const totalRecords = ref(0);
const rows = ref(10); // Registros por página
const first = ref(0); // Índice del primer registro

const loadLazyData = async (event?: any) => {
    loading.value = true;

    // 'event' contiene la información de paginación y orden de PrimeVue
    const params = {
        page: event ? event.page : 0,
        rows: event ? event.rows : rows.value,
        sortField: event?.sortField,
        sortOrder: event?.sortOrder,
    };

    try {
        const response = await StudentService.getStudents(params);
        students.value = response.data;
        totalRecords.value = response.totalRecords;
    } finally {
        loading.value = false;
    }
};

onMounted(() => {
    loadLazyData();
});
</script>

<template>
  <div class="card">
    <DataTable 
      v-model:first="first"
      :value="students" 
      lazy 
      paginator 
      :rows="rows" 
      :totalRecords="totalRecords" 
      :loading="loading" 
      @page="loadLazyData"
      @sort="loadLazyData"
      filterDisplay="menu"
      responsiveLayout="scroll"
      class="p-datatable-sm"
    >
      <Column field="id" header="ID" sortable />
      <Column field="name" header="Nombre del Producto" sortable />
      <Column field="price" header="Precio">
        <template #body="slotProps">
          {{ new Intl.NumberFormat('es-EC', { style: 'currency', currency: 'USD' }).format(slotProps.data.price) }}
        </template>
      </Column>
      <Column field="stock" header="Inventario" />
    </DataTable>
  </div>
</template>