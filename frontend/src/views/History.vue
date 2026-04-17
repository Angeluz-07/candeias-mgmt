<script setup>
import { ref, onMounted } from "vue";
import MarkdownIt from "markdown-it";
import { Card, CardContent } from "@/components/ui/card";

// 1. Importación de archivos Markdown (Vite Raw)
import historiaGrupoCandeiasMD from "@/data/historiaGrupoCandeias.md?raw";
import sistemaDeGraduacionMD from "@/data/sistemaDeGraduacion.md?raw";
import personajesDeLaCapoeiraMD from "@/data/personajesDeLaCapoeira.md?raw";
import personajesDelGrupoCandeiasMD from "@/data/personajesDelGrupoCandeias.md?raw";
import historiaDeLaCapoeiraMD from "@/data/historiaDeLaCapoeira.md?raw";

import { ListIcon } from "lucide-vue-next"; // Asegúrate de tener lucide-vue-next
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";

const isSheetOpen = ref(false);

// 2. Configuración de Markdown-it
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
});

// 3. Lista de secciones (Datos estructurados)
const secciones = [
  {
    id: "historiaCandeias",
    titulo: "Historia del Grupo Candeias",
    año: "1990",
    contenido: historiaGrupoCandeiasMD,
  },
  {
    id: "sistemaGraduacion",
    titulo: "Sistema de Graduación",
    año: "2005",
    contenido: sistemaDeGraduacionMD,
  },
  {
    id: "personajesCapoeira",
    titulo: "Personajes de la Capoeira",
    año: "2005",
    contenido: personajesDeLaCapoeiraMD,
  },
  {
    id: "personajesCandeais",
    titulo: "Personajes del grupo Candeias",
    año: "2005",
    contenido: personajesDelGrupoCandeiasMD,
  },
  {
    id: "historiaCapoeira",
    titulo: "Historia de la Capoeira",
    año: "1990",
    contenido: historiaDeLaCapoeiraMD,
  }
];

const activeSection = ref(secciones[0].id);

// Función para renderizar el texto
const renderMD = (content) => md.render(content);
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
            :class="
              activeSection === sec.id
                ? 'border-[#FF6B00] text-[#FF6B00] font-bold'
                : 'border-transparent text-zinc-400 hover:text-white hover:border-zinc-700'
            "
          >
            {{ sec.titulo }}
          </a>
        </div>
      </aside>

      <div class="md:hidden fixed bottom-6 right-6 z-50">
        <Sheet v-model:open="isSheetOpen">
          <SheetTrigger asChild>
            <Button
              size="icon"
              class="h-14 w-14 rounded-full bg-[#FF6B00] shadow-lg border-none active:scale-95 transition-transform"
            >
              <ListIcon class="h-6 w-6 text-white" />
            </Button>
          </SheetTrigger>

          <SheetContent
            side="bottom"
            class="bg-black border-white/10 rounded-t-3xl max-h-[70vh] min-h-[300px] p-0 flex flex-col outline-none"
          >
            <div
              class="h-1 bg-zinc-800 w-12 mx-auto mt-3 rounded-full shrink-0"
            ></div>

            <SheetHeader class="px-6 pt-4 pb-2 text-left shrink-0">
              <SheetTitle
                class="text-zinc-500 text-xs uppercase tracking-[0.2em] font-bold"
              >
                Ir a sección
              </SheetTitle>
            </SheetHeader>

            <div class="flex-1 overflow-y-auto px-6 custom-scrollbar">
              <div class="flex flex-col mt-2 pb-20">
                <a
                  v-for="sec in secciones"
                  :key="sec.id"
                  :href="`#${sec.id}`"
                  @click="
                    () => {
                      activeSection = sec.id;
                      isSheetOpen = false;
                    }
                  "
                  class="py-5 text-xl transition-colors border-b border-white/5 last:border-none block outline-none"
                  :class="
                    activeSection === sec.id
                      ? 'text-[#FF6B00] font-black tracking-tighter'
                      : 'text-zinc-400 font-medium'
                  "
                >
                  {{ sec.titulo }}
                </a>
              </div>
            </div>
          </SheetContent>
        </Sheet>
      </div>
      <main class="flex-1 space-y-24">
        <!--header class="mb-10">
          <h1 class="text-5xl font-black italic tracking-tighter uppercase">
            Nuestra <span class="text-[#FF6B00]">Historia</span>
          </h1>
          <p class="text-zinc-500 mt-2 font-medium">Trayectoria y valores de nuestro club.</p>
        </header-->

        <section
          v-for="sec in secciones"
          :key="sec.id"
          :id="sec.id"
          class="scroll-mt-28"
        >
          <Card class="bg-zinc-950 border-white/10 overflow-hidden shadow-2xl">
            <div class="h-1.5 bg-[#FF6B00] w-20"></div>

            <CardContent class="px-8 md:px-12">
              <article
                class="prose prose-invert max-w-none prose-p:text-zinc-300 prose-p:text-lg prose-p:leading-relaxed prose-headings:text-white prose-headings:font-black prose-headings:italic prose-headings:uppercase prose-strong:text-[#FF6B00] prose-li:text-zinc-300 prose-img:rounded-2xl prose-img:border prose-img:border-white/10"
                v-html="renderMD(sec.contenido)"
              ></article>
            </CardContent>
          </Card>
        </section>
      </main>
    </div>
  </div>
</template>

<style scoped>
/* Tailwind 4 Reference */
@reference "tailwindcss";

html {
  scroll-behavior: smooth;
}

/* Ajustes finos para el contenido inyectado */
:deep(.prose h1) {
  @apply text-4xl mb-8 tracking-tighter border-b border-white/5 pb-4;
}

:deep(.prose h2) {
  @apply text-2xl mt-12 mb-4 text-white/90;
}

:deep(.prose img) {
  @apply shadow-2xl my-12 w-full object-cover max-h-[500px];
}

/* Estilo para las listas en el contenido largo */
:deep(.prose ul) {
  @apply list-disc space-y-3 my-6;
}
/* Evita que el body se scrollee cuando el menu está abierto (opcional) */
:deep([data-state="open"]) {
  overflow: hidden;
}
</style>
