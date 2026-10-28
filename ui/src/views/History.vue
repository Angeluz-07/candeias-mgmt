<script setup>
import { ref } from "vue";
import MarkdownIt from "markdown-it";
// Eliminamos todos los imports de shadcn
import { ListIcon } from "lucide-vue-next";

// Data
import historiaGrupoCandeiasMD from "@/data/historiaGrupoCandeias.md?raw";
import sistemaDeGraduacionMD from "@/data/sistemaDeGraduacion.md?raw";
import personajesDeLaCapoeiraMD from "@/data/personajesDeLaCapoeira.md?raw";
import personajesDelGrupoCandeiasMD from "@/data/personajesDelGrupoCandeias.md?raw";
import historiaDeLaCapoeiraMD from "@/data/historiaDeLaCapoeira.md?raw";

const md = new MarkdownIt({ html: true, linkify: true, typographer: true });

const secciones = [
  { id: "historiaCandeias", titulo: "Historia del Grupo Candeias", contenido: historiaGrupoCandeiasMD },
  { id: "sistemaGraduacion", titulo: "Sistema de Graduación", contenido: sistemaDeGraduacionMD },
  { id: "personajesCapoeira", titulo: "Personajes de la Capoeira", contenido: personajesDeLaCapoeiraMD },
  { id: "personajesCandeais", titulo: "Personajes del grupo Candeias", contenido: personajesDelGrupoCandeiasMD },
  { id: "historiaCapoeira", titulo: "Historia de la Capoeira", contenido: historiaDeLaCapoeiraMD }
];

const activeSection = ref(secciones[0].id);
const isDrawerOpen = ref(false); // Para el menú móvil
</script>

<template>
  <div class="min-h-screen bg-black text-white p-4 md:p-10">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row gap-12">
      
      <aside class="hidden md:block w-64 sticky top-24 h-fit">
        <div class="border-l border-white/10 ml-2 space-y-1">
          <a
            v-for="sec in secciones"
            :key="sec.id"
            :href="`#${sec.id}`"
            @click="activeSection = sec.id"
            class="block pl-4 py-2 text-sm transition-all border-l-2 -ml-[2px]"
            :class="activeSection === sec.id ? 'border-primary text-primary font-bold' : 'border-transparent text-zinc-400 hover:text-white hover:border-zinc-700'"
          >
            {{ sec.titulo }}
          </a>
        </div>
      </aside>

      <div class="drawer md:hidden z-50">
        <input id="mobile-menu" type="checkbox" class="drawer-toggle" v-model="isDrawerOpen" />
        <div class="drawer-content fixed bottom-6 right-6">
          <label for="mobile-menu" class="btn btn-primary btn-circle h-14 w-14 shadow-lg border-none active:scale-95">
            <ListIcon class="h-6 w-6 text-white" />
          </label>
        </div>
        <div class="drawer-side">
          <label for="mobile-menu" class="drawer-overlay"></label>
          <div class="p-4 w-full bg-black min-h-[300px] rounded-t-3xl border-t border-white/10">
            <div class="h-1 bg-zinc-800 w-12 mx-auto mt-2 mb-6 rounded-full"></div>
            <p class="text-zinc-500 text-xs uppercase tracking-[0.2em] font-bold px-6">Ir a sección</p>
            <div class="flex flex-col mt-4">
              <a
                v-for="sec in secciones"
                :key="sec.id"
                :href="`#${sec.id}`"
                @click="activeSection = sec.id; isDrawerOpen = false"
                class="py-5 px-6 text-xl border-b border-white/5 block"
                :class="activeSection === sec.id ? 'text-primary font-black' : 'text-zinc-400'"
              >
                {{ sec.titulo }}
              </a>
            </div>
          </div>
        </div>
      </div>

      <main class="flex-1 space-y-24">
        <section v-for="sec in secciones" :key="sec.id" :id="sec.id" class="scroll-mt-28">
          <div class="card bg-zinc-950 border border-white/10 shadow-2xl">
            <div class="h-1.5 bg-primary w-20"></div>
            <div class="card-body px-8 md:px-12">
              <article
                class="prose prose-invert max-w-none prose-headings:font-black prose-headings:italic prose-strong:text-primary prose-img:rounded-2xl"
                v-html="md.render(sec.contenido)"
              ></article>
            </div>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<style scoped>
@reference "tailwindcss";
html { scroll-behavior: smooth; }
/* Mantenemos tus estilos específicos para el contenido markdown */
:deep(.prose h1) { @apply text-4xl mb-8 tracking-tighter border-b border-white/5 pb-4; }
:deep(.prose h2) { @apply text-2xl mt-12 mb-4 text-white/90; }
:deep(.prose img) { @apply shadow-2xl my-12 w-full object-cover max-h-[500px]; }
</style>