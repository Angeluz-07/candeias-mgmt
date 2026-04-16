<!--script setup lang="ts"></script>

<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white flex flex-col font-sans">
    <main class="flex-1 p-6 space-y-1 max-w-lg mx-auto w-full">
      Welcome to history of Candeias group :)
      
    </main>
  </div>
</template-->

<script setup>
import { ref } from 'vue'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@/components/ui/accordion'
import { ScrollArea } from '@/components/ui/scroll-area'

// Ejemplo de las 8 secciones
const secciones = [
  { id: 'fundacion', titulo: 'La Fundación', año: '1990' },
  { id: 'primeros-pasos', titulo: 'Primeros Pasos', año: '1995' },
  { id: 'crecimiento', titulo: 'Era de Crecimiento', año: '2000' },
  { id: 'crisis', titulo: 'Desafíos Superados', año: '2005' },
  { id: 'exito', titulo: 'Éxito Regional', año: '2010' },
  { id: 'modernizacion', titulo: 'Modernización', año: '2015' },
  { id: 'actualidad', titulo: 'Actualidad', año: '2020' },
  { id: 'futuro', titulo: 'Visión al Futuro', año: '2025' },
]

const activeSection = ref('fundacion')
</script>

<template>
  <div class="min-h-screen bg-black text-white p-4 md:p-8">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row gap-10">
      
      <aside class="hidden md:block w-64 sticky top-24 h-[calc(100vh-120px)]">
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

      <main class="flex-1 space-y-16">
        <header class="mb-10">
          <h1 class="text-4xl font-black italic tracking-tighter uppercase">
            Nuestra <span class="text-[#FF6B00]">Historia</span>
          </h1>
          <p class="text-zinc-400 mt-2">Un recorrido por los hitos que forjaron Candeias.</p>
        </header>

        <section 
          v-for="sec in secciones" 
          :key="sec.id" 
          :id="sec.id" 
          class="scroll-mt-24"
        >
          <Card class="bg-zinc-950 border-white/10 overflow-hidden">
            <div class="h-1 bg-[#FF6B00] w-20"></div> <CardHeader class="pb-2">
              <div class="text-[#FF6B00] font-mono text-sm mb-1">{{ sec.año }}</div>
              <CardTitle class="text-2xl font-bold text-white uppercase tracking-tight">
                {{ sec.titulo }}
              </CardTitle>
            </CardHeader>

            <CardContent class="space-y-4">
              <p class="text-zinc-300 leading-relaxed">
                Aquí va la narrativa principal de esta sección. Puedes describir los eventos clave, 
                las personas involucradas y la importancia de esta era para el club.
              </p>

              <Accordion type="single" collapsible class="w-full border-t border-white/5 pt-4">
                <AccordionItem value="detalles" class="border-none">
                  <AccordionTrigger class="text-zinc-400 hover:text-[#FF6B00] py-2">
                    Ver hitos específicos y estadísticas
                  </AccordionTrigger>
                  <AccordionContent class="text-zinc-500 bg-black/40 p-4 rounded-lg mt-2">
                    <ul class="list-disc list-inside space-y-2">
                      <li>Logro o sub-evento importante número uno.</li>
                      <li>Inauguración de nuevas instalaciones.</li>
                      <li>Premios o reconocimientos obtenidos.</li>
                    </ul>
                    </AccordionContent>
                </AccordionItem>
              </Accordion>
            </CardContent>
          </Card>
        </section>
      </main>
    </div>
  </div>
</template>

<style scoped>
/* Suaviza el salto de los anclajes */
html {
  scroll-behavior: smooth;
}

/* Estilos personalizados para el Accordion de Shadcn para que encaje con el tema oscuro */
:deep(.AccordionTrigger) {
  text-decoration: none !important;
}
</style>