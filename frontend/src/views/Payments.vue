<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import { Button } from "@/components/ui/button";
import { useRouter } from "vue-router";

import {
  LogOut,
  Dumbbell,
  Flame,
  User,
  Calendar,
  Activity,
} from "lucide-vue-next";

import StudentTable from "./StudentTable.vue";
const authStore = useAuthStore();

const router = useRouter();

// Computed or direct access works great with Pinia
const user = authStore.user;

</script>

<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white flex flex-col font-sans">


    <main class="flex-1 p-6 space-y-1 max-w-lg mx-auto w-full">
      <section class="mt-4">
        <h2
          class="text-zinc-500 uppercase tracking-widest text-[10px] font-bold"
        >
          Control Panel
        </h2>
        <h1 class="text-4xl font-black mt-2 leading-tight ">
          Bienvenido
          <span class="text-[#FF6B00] italic">{{
            user?.username || "ATLETA"
          }}</span>
        </h1>
      </section>

      <div class="p-6">
        <StudentTable />
      </div>


    </main>

    <!--footer
      class="md:hidden border-t border-zinc-800 bg-zinc-950 px-8 py-4 flex justify-between items-center sticky bottom-0"
    >
      <Activity class="w-6 h-6 text-[#FF6B00]" />
      <Calendar class="w-6 h-6 text-zinc-600" />

      <div
        class="bg-[#FF6B00] p-3 rounded-full -mt-10 border-4 border-[#0A0A0A] shadow-lg active:scale-90 transition-transform"
      >
        <Dumbbell class="w-6 h-6 text-black" />
      </div>

      <User class="w-6 h-6 text-zinc-600" />
      <LogOut
        @click="handleLogout"
        class="w-6 h-6 text-zinc-600 cursor-pointer"
      />
    </footer-->
  </div>
</template>
