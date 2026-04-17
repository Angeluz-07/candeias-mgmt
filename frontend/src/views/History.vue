<script setup>
import { ref, onMounted } from 'vue'
import MarkdownIt from 'markdown-it'
import { Card, CardContent } from '@/components/ui/card'

// 1. Importación de archivos Markdown (Vite Raw)
import historiaGrupoCandeiasMD from '@/data/historiaGrupoCandeias.md?raw'
import sistemaDeGraduacionMD from '@/data/sistemaDeGraduacion.md?raw'
import personajesDeLaCapoeiraMD from '@/data/personajesDeLaCapoeira.md?raw'
import personajesDelGrupoCandeiasMD from '@/data/personajesDelGrupoCandeias.md?raw'
import historiaDeLaCapoeiraMD from '@/data/historiaDeLaCapoeira.md?raw'

// 2. Configuración de Markdown-it
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
})

// 3. Lista de secciones (Datos estructurados)
const secciones = [
  { 
    id: 'historiaCandeias', 
    titulo: 'Historia del Grupo Candeias', 
    año: '1990', 
    contenido: historiaGrupoCandeiasMD 
  },
  { 
    id: 'sistemaGraduacion', 
    titulo: 'Sistema de Graduación', 
    año: '2005', 
    contenido: sistemaDeGraduacionMD 
  },  
  { 
    id: 'personajesCapoeira', 
    titulo: 'Personajes de la Capoeira', 
    año: '2005', 
    contenido: personajesDeLaCapoeiraMD 
  },
  { 
    id: 'personajesCandeais', 
    titulo: 'Personajes del grupo Candeias', 
    año: '2005', 
    contenido: personajesDelGrupoCandeiasMD 
  },
  { 
    id: 'historiaCapoeira', 
    titulo: 'Historia de la Capoeira', 
    año: '1990', 
    contenido: historiaDeLaCapoeiraMD 
  },
]

const activeSection = ref(secciones[0].id)

// Función para renderizar el texto
const renderMD = (content) => md.render(content)
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
            :class="activeSection === sec.id 
              ? 'border-[#FF6B00] text-[#FF6B00] font-bold' 
              : 'border-transparent text-zinc-400 hover:text-white hover:border-zinc-700'"
          >
            {{ sec.titulo }}
          </a>
        </div>
      </aside>

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
                class="prose prose-invert max-w-none
                       prose-p:text-zinc-300 prose-p:text-lg prose-p:leading-relaxed
                       prose-headings:text-white prose-headings:font-black prose-headings:italic prose-headings:uppercase
                       prose-strong:text-[#FF6B00]
                       prose-li:text-zinc-300
                       prose-img:rounded-2xl prose-img:border prose-img:border-white/10"
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
</style>