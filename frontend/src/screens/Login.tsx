import { useAuthLogic } from "../hooks/use-auth-logic";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";

export default function Login() {
  const { login, loading, error } = useAuthLogic();

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.currentTarget));
    login(data);
  };

  return (
    <div className="min-h-screen bg-[#0A0A0A] flex flex-col items-center justify-center p-6 text-white">
      <div className="w-full max-w-[360px] space-y-10">
        <div className="text-center">
          <h1 className="text-6xl font-black italic tracking-tighter uppercase">
            FIT<span className="text-[#FF6B00]">CLUB</span>
          </h1>
          <p className="text-zinc-500 text-[10px] tracking-[0.3em] uppercase mt-2 font-bold">Guayaquil Edition</p>
        </div>

        <Card className="bg-zinc-900/40 border-zinc-800 backdrop-blur-xl rounded-2xl">
          <CardContent className="pt-8 pb-8 space-y-6">
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-1.5">
                <label className="text-[10px] uppercase font-bold text-zinc-500 ml-1">Usuario</label>
                <Input name="email" placeholder="email" className="h-14 bg-zinc-800/50 border-none text-white rounded-xl" />
              </div>
              <div className="space-y-1.5">
                <label className="text-[10px] uppercase font-bold text-zinc-500 ml-1">Contraseña</label>
                <Input name="password" type="password" placeholder="••••••••" className="h-14 bg-zinc-800/50 border-none text-white rounded-xl" />
              </div>
              
              {error && <p className="text-red-500 text-xs text-center font-bold animate-pulse">{error}</p>}

              <Button 
                disabled={loading} 
                className="w-full h-16 bg-[#FF6B00] hover:bg-[#e66000] text-black font-black text-xl rounded-xl transition-transform active:scale-95 shadow-[0_0_20px_rgba(255,107,0,0.3)]"
              >
                {loading ? "CARGANDO..." : "ENTRAR"}
              </Button>
            </form>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}