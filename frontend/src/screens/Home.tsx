import { useAuthStore } from "../api/client";
import { Button } from "@/components/ui/button";
import { LogOut, Dumbbell, Flame, User, Calendar, Activity } from "lucide-react";

export default function Home() {
  const { user, logout } = useAuthStore();

  return (
    <div className="min-h-screen bg-[#0A0A0A] text-white flex flex-col">
      {/* --- NAVBAR MOBILE-FIRST --- */}
      <nav className="w-full border-b border-zinc-800 bg-zinc-950/50 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Flame className="text-[#FF6B00] w-8 h-8"/>
            <span className="font-black italic text-2xl tracking-tighter">
              CANDE<span className="text-[#FF6B00]">IAS</span>
            </span>
          </div>
          
          <Button 
            variant="ghost" 
            onClick={logout}
            className="text-zinc-400 hover:text-[#FF6B00] hover:bg-zinc-900 transition-colors"
          >
            <LogOut className="w-5 h-5 mr-2" />
            <span className="hidden sm:inline">Cerrar Sesión</span>
          </Button>
        </div>
      </nav>

      {/* --- CONTENIDO PRINCIPAL --- */}
      <main className="flex-1 p-6 space-y-8 max-w-lg mx-auto w-full">
        
        {/* Mensaje de Bienvenida */}
        <section className="mt-4">
          <h2 className="text-zinc-500 uppercase tracking-widest text-[10px] font-bold">Panel de Control</h2>
          <h1 className="text-4xl font-black mt-2 leading-tight">
            BIENVENIDO, <br />
            <span className="text-[#FF6B00] uppercase italic">{user?.name || 'ATLETA'}</span>
          </h1>
          <p className="text-zinc-400 text-sm mt-2">
            Tu progreso de hoy está listo para ser registrado.
          </p>
        </section>

        {/* --- DUMMY CARDS (Presentation Info) --- */}
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-zinc-900/50 p-4 rounded-2xl border border-zinc-800 space-y-3">
            <Activity className="text-[#FF6B00] w-6 h-6" />
            <div>
              <p className="text-[10px] uppercase text-zinc-500 font-bold">Calorías</p>
              <p className="text-2xl font-black italic">1,240</p>
            </div>
          </div>
          
          <div className="bg-zinc-900/50 p-4 rounded-2xl border border-zinc-800 space-y-3">
            <Calendar className="text-[#FF6B00] w-6 h-6" />
            <div>
              <p className="text-[10px] uppercase text-zinc-500 font-bold">Racha</p>
              <p className="text-2xl font-black italic">12 DÍAS</p>
            </div>
          </div>
        </div>

        {/* Sección Informativa Dummy */}
        <div className="bg-gradient-to-br from-zinc-900 to-black p-6 rounded-3xl border border-zinc-800 relative overflow-hidden group">
          <div className="relative z-10">
            <h3 className="font-bold text-lg">Entrenamiento del día</h3>
            <p className="text-zinc-400 text-sm mt-1">Pierna y Core - Intensidad Alta</p>
            <Button className="mt-4 bg-white text-black hover:bg-zinc-200 font-bold rounded-full px-6">
              EMPEZAR AHORA
            </Button>
          </div>
          <Dumbbell className="absolute -right-4 -bottom-4 w-32 h-32 text-white/5 rotate-12 group-hover:scale-110 transition-transform" />
        </div>

      </main>

      {/* --- BOTTOM TAB BAR (Mobile Standard) --- */}
      <footer className="md:hidden border-t border-zinc-800 bg-zinc-950 px-8 py-4 flex justify-between items-center sticky bottom-0">
        <Activity className="w-6 h-6 text-[#FF6B00]" />
        <Calendar className="w-6 h-6 text-zinc-600" />
        <div className="bg-[#FF6B00] p-3 rounded-full -mt-10 border-4 border-[#0A0A0A] shadow-lg">
          <Dumbbell className="w-6 h-6 text-black" />
        </div>
        <User className="w-6 h-6 text-zinc-600" />
        <LogOut onClick={logout} className="w-6 h-6 text-zinc-600" />
      </footer>
    </div>
  );
}