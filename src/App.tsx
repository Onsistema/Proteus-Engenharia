import { useEffect, useRef, useState } from 'react';
import { 
  Shield, 
  Camera, 
  Zap, 
  Network, 
  Phone, 
  Lock, 
  CheckCircle2, 
  ArrowRight, 
  Star,
  MapPin,
  MessageCircle,
  Cpu,
  HardDrive,
  Menu,
  X
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const services = [
  {
    title: "Instalações Elétricas",
    desc: "Projetos e execuções residenciais, comerciais e industriais com rigor técnico e segurança.",
    icon: <Zap className="w-8 h-8 text-accent" />,
    img: "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=1000&auto=format&fit=crop"
  },
  {
    title: "Projetos & Laudos",
    desc: "Elaboração de projetos elétricos, laudos de SPDA e inspeções técnicas por engenheiros.",
    icon: <Cpu className="w-8 h-8 text-accent" />,
    img: "https://images.unsplash.com/photo-1581092160562-40aa08e78837?q=80&w=1000&auto=format&fit=crop"
  },
  {
    title: "Manutenção Preventiva",
    desc: "Redução de custos e aumento da vida útil de equipamentos através de revisões periódicas.",
    icon: <HardDrive className="w-8 h-8 text-accent" />,
    img: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1000&auto=format&fit=crop"
  },
  {
    title: "Segurança & Automação",
    desc: "Integração de sistemas de câmeras, alarmes e controle de acesso inteligente.",
    icon: <Shield className="w-8 h-8 text-accent" />,
    img: "https://images.unsplash.com/photo-1557597774-9d273605dfa9?q=80&w=1000&auto=format&fit=crop"
  }
];

const partners = [
  "Intelbras", "Schneider", "Siemens", "WEG", "Prysmian", "Steck", "Legrand", "Furukawa"
];

export default function App() {
  const headerRef = useRef<HTMLElement>(null);
  const heroRef = useRef<HTMLDivElement>(null);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [logoError, setLogoError] = useState(false);

  useEffect(() => {
    const ctx = gsap.context(() => {
      // Header Animation
      gsap.to(headerRef.current, {
        backgroundColor: "rgba(5, 5, 5, 0.9)",
        backdropFilter: "blur(12px)",
        borderBottom: "1px solid rgba(255, 255, 255, 0.1)",
        duration: 0.3,
        scrollTrigger: {
          trigger: "body",
          start: "top -50",
          toggleActions: "play none none reverse"
        }
      });

      // Hero Entrance
      gsap.from(".hero-title", {
        y: 100,
        opacity: 0,
        duration: 1.2,
        ease: "power4.out",
        stagger: 0.2
      });
      gsap.from(".hero-sub", {
        y: 50,
        opacity: 0,
        duration: 1,
        delay: 0.5,
        ease: "power3.out"
      });
      gsap.from(".hero-btn", {
        scale: 0.8,
        opacity: 0,
        duration: 0.8,
        delay: 0.8,
        ease: "back.out(1.7)"
      });

      // Scroll Reveal for sections
      const sections = document.querySelectorAll('.reveal');
      sections.forEach((section) => {
        gsap.from(section, {
          y: 40,
          opacity: 0,
          duration: 1,
          ease: "power2.out",
          scrollTrigger: {
            trigger: section,
            start: "top 90%",
            toggleActions: "play none none reverse",
          }
        });
      });
    });

    const timer = setTimeout(() => {
      ScrollTrigger.refresh();
    }, 500);

    return () => {
      ctx.revert();
      clearTimeout(timer);
    };
  }, []);

  const navLinks = [
    { name: "Serviços", href: "#servicos" },
    { name: "Sobre", href: "#sobre" },
    { name: "Depoimentos", href: "#depoimentos" },
    { name: "Contato", href: "#contato" },
  ];

  return (
    <div className="min-h-screen bg-dark text-white selection:bg-accent selection:text-white">
      {/* Header */}
      <header 
        ref={headerRef}
        className="fixed top-0 left-0 w-full z-50 transition-all duration-300 py-4 px-4 md:px-12 flex items-center justify-between"
      >
        <div className="flex items-center gap-3">
          <div className={`relative h-10 w-10 md:h-12 md:w-12 flex items-center justify-center ${logoError ? 'bg-accent rounded-lg' : ''}`}>
            {!logoError ? (
              <img 
                src="/logo.png" 
                alt="Proteus Logo" 
                className="h-full w-full object-contain"
                onError={() => setLogoError(true)}
                referrerPolicy="no-referrer"
              />
            ) : (
              <Zap className="w-6 h-6 text-white fill-white" />
            )}
          </div>
          <span className="font-display text-lg md:text-xl tracking-tighter uppercase font-bold">Proteus</span>
        </div>
        
        <nav className="hidden lg:flex items-center gap-8 text-sm font-medium uppercase tracking-widest text-white/70">
          {navLinks.map((link) => (
            <a key={link.name} href={link.href} className="hover:text-accent transition-colors">
              {link.name}
            </a>
          ))}
        </nav>

        <div className="flex items-center gap-4">
          <a 
            href="https://wa.me/5519971418256" 
            target="_blank"
            className="hidden sm:block bg-white text-dark px-6 py-2.5 rounded-full text-sm font-bold hover:bg-accent hover:text-white transition-all duration-300"
          >
            Orçamento Grátis
          </a>
          
          <button 
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="lg:hidden p-2 text-white hover:text-accent transition-colors"
          >
            {isMenuOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>
      </header>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="fixed inset-0 z-40 bg-dark/95 backdrop-blur-xl pt-24 px-6 lg:hidden"
          >
            <nav className="flex flex-col gap-8 text-center">
              {navLinks.map((link) => (
                <a 
                  key={link.name} 
                  href={link.href} 
                  onClick={() => setIsMenuOpen(false)}
                  className="text-3xl font-display uppercase tracking-tighter hover:text-accent transition-colors"
                >
                  {link.name}
                </a>
              ))}
              <a 
                href="https://wa.me/5519971418256" 
                target="_blank"
                className="mt-4 bg-accent text-white py-5 rounded-2xl text-xl font-bold"
              >
                Orçamento Grátis
              </a>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Hero Section */}
      <section 
        ref={heroRef}
        className="relative min-h-screen flex items-center justify-center overflow-hidden pt-20"
      >
        <div className="absolute inset-0 z-0">
          <img 
            src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=2070&auto=format&fit=crop" 
            alt="Engenharia Elétrica"
            className="w-full h-full object-cover opacity-30 scale-110"
            referrerPolicy="no-referrer"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-dark via-dark/80 to-dark"></div>
        </div>

        <div className="relative z-10 container mx-auto px-6 text-center">
          <motion.div 
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-full glass mb-8 text-[10px] md:text-xs font-bold uppercase tracking-widest text-accent border-accent/20"
          >
            <Zap className="w-3 h-3 fill-accent" />
            Engenharia Elétrica de Alta Performance
          </motion.div>
          
          <h1 className="hero-title font-display text-4xl sm:text-7xl md:text-8xl lg:text-9xl leading-[0.9] tracking-tighter mb-6 text-balance">
            ENERGIA <br />
            <span className="text-accent italic">COM PRECISÃO</span>
          </h1>
          
          <p className="hero-sub max-w-2xl mx-auto text-base md:text-xl text-white/60 mb-10 text-balance leading-relaxed">
            Especialistas em instalações elétricas, projetos e manutenção industrial. Segurança e eficiência energética para o seu negócio em Campinas e região.
          </p>

          <div className="hero-btn flex flex-col sm:flex-row items-center justify-center gap-4">
            <a 
              href="https://wa.me/5519971418256"
              className="w-full sm:w-auto group relative bg-accent text-white px-10 py-5 rounded-full text-lg font-bold overflow-hidden transition-all hover:scale-105 active:scale-95 text-center"
            >
              <span className="relative z-10 flex items-center justify-center gap-2">
                Solicitar Orçamento <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </span>
              <div className="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
            </a>
            <a 
              href="#servicos"
              className="w-full sm:w-auto px-10 py-5 rounded-full text-lg font-bold border border-white/10 hover:bg-white/5 transition-all text-center"
            >
              Nossos Serviços
            </a>
          </div>
        </div>

        {/* Scroll Indicator */}
        <div className="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-30">
          <span className="text-[10px] uppercase tracking-[0.3em]">Scroll</span>
          <div className="w-px h-12 bg-gradient-to-b from-white to-transparent"></div>
        </div>
      </section>

      {/* Authority Marquee */}
      <section className="py-8 md:py-12 border-y border-white/5 bg-white/[0.02] overflow-hidden">
        <div className="animate-marquee whitespace-nowrap">
          {[...partners, ...partners].map((partner, i) => (
            <div key={i} className="inline-flex mx-6 md:mx-12 items-center gap-4 grayscale opacity-40 hover:grayscale-0 hover:opacity-100 transition-all cursor-default">
              <span className="text-xl md:text-2xl font-display uppercase tracking-tighter">{partner}</span>
            </div>
          ))}
        </div>
      </section>

      {/* Differentials - Bento Grid */}
      <section id="servicos" className="py-16 md:py-24 px-4 md:px-12">
        <div className="container mx-auto">
          <div className="reveal mb-12 md:mb-16 text-center md:text-left">
            <h2 className="font-display text-4xl md:text-6xl tracking-tighter mb-4">
              ENGENHARIA <span className="text-accent">ELÉTRICA</span>
            </h2>
            <p className="text-white/50 max-w-xl mx-auto md:mx-0">
              Soluções completas em infraestrutura elétrica, desde o projeto inicial até a manutenção preventiva e corretiva.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-12 gap-4 md:gap-6 auto-rows-min md:auto-rows-[300px]">
            {/* Bento Item 1 */}
            <div className="reveal md:col-span-8 bento-card flex flex-col justify-end relative overflow-hidden group p-6 md:p-10 min-h-[300px]">
              <img 
                src={services[0].img} 
                className="absolute inset-0 w-full h-full object-cover opacity-20 group-hover:scale-110 transition-transform duration-700" 
                alt={services[0].title}
                referrerPolicy="no-referrer"
              />
              <div className="relative z-10">
                <Zap className="w-10 h-10 md:w-12 md:h-12 text-accent mb-4" />
                <h3 className="text-2xl md:text-3xl font-display mb-2">{services[0].title}</h3>
                <p className="text-white/60 max-w-md text-sm md:text-base">{services[0].desc}</p>
              </div>
            </div>

            {/* Bento Item 2 */}
            <div className="reveal md:col-span-4 bento-card flex flex-col items-center justify-center text-center bg-accent/10 border-accent/20 p-6 min-h-[200px]">
              <Cpu className="w-12 h-12 md:w-16 md:h-16 text-accent mb-6 animate-pulse" />
              <h3 className="text-xl md:text-2xl font-display mb-2">Projetos & Laudos</h3>
              <p className="text-white/60 text-xs md:text-sm">Conformidade e Segurança</p>
            </div>

            {/* Bento Item 3 */}
            <div className="reveal md:col-span-4 bento-card flex flex-col justify-between p-6 min-h-[200px]">
              <div className="flex justify-between items-start">
                <HardDrive className="w-8 h-8 md:w-10 md:h-10 text-accent" />
                <span className="text-[8px] md:text-[10px] font-bold uppercase tracking-widest glass px-3 py-1 rounded-full">Manutenção</span>
              </div>
              <div>
                <h3 className="text-xl md:text-2xl font-display mb-2">Preventiva</h3>
                <p className="text-white/60 text-xs md:text-sm">Redução de custos e aumento da eficiência energética.</p>
              </div>
            </div>

            {/* Bento Item 4 */}
            <div className="reveal md:col-span-8 bento-card relative overflow-hidden group flex items-end p-6 md:p-10 min-h-[300px]">
              <img 
                src={services[3].img} 
                className="absolute inset-0 w-full h-full object-cover opacity-20 group-hover:scale-110 transition-transform duration-700" 
                alt={services[3].title}
                referrerPolicy="no-referrer"
              />
              <div className="relative z-10 w-full flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div>
                  <h3 className="text-2xl md:text-3xl font-display mb-2">{services[3].title}</h3>
                  <p className="text-white/60 max-w-sm text-sm md:text-base">Integração de sistemas de segurança e automação predial.</p>
                </div>
                <div className="glass p-3 md:p-4 rounded-2xl">
                  <Shield className="w-6 h-6 md:w-8 md:h-8 text-accent" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="sobre" className="py-16 md:py-24 bg-white/[0.01] relative overflow-hidden">
        <div className="container mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-12 md:gap-16 items-center">
          <div className="reveal relative order-2 lg:order-1">
            <div className="aspect-square rounded-3xl overflow-hidden border border-white/10">
              <img 
                src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=2070&auto=format&fit=crop" 
                alt="Equipe Proteus"
                className="w-full h-full object-cover"
                referrerPolicy="no-referrer"
              />
            </div>
            <div className="absolute -bottom-4 -right-4 md:-bottom-6 -right-6 glass p-4 md:p-8 rounded-2xl md:rounded-3xl">
              <p className="text-2xl md:text-4xl font-display text-accent mb-1">2019</p>
              <p className="text-[8px] md:text-xs uppercase tracking-widest font-bold">Desde Abril</p>
            </div>
          </div>

          <div className="reveal order-1 lg:order-2">
            <span className="text-accent font-bold uppercase tracking-[0.3em] text-[10px] md:text-xs mb-4 block">Nossa Expertise</span>
            <h2 className="font-display text-3xl md:text-6xl tracking-tighter mb-6 md:mb-8 leading-tight">
              ENGENHARIA QUE <br />
              <span className="italic">ILUMINA O FUTURO</span>
            </h2>
            <p className="text-white/60 text-base md:text-lg leading-relaxed mb-6 md:mb-8">
              A Proteus Engenharia Elétrica é referência em soluções de infraestrutura e manutenção. Com uma equipe liderada por engenheiros experientes, entregamos projetos que priorizam a segurança, a eficiência energética e a conformidade com as normas técnicas (NBR-5410).
            </p>
            
            <ul className="space-y-3 md:space-y-4 mb-8 md:mb-10">
              {[
                "Projetos Elétricos e Laudos de SPDA",
                "Instalações Industriais e Comerciais",
                "Manutenção de Quadros e Painéis",
                "Eficiência Energética e Automação"
              ].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-white/80 text-sm md:text-base">
                  <CheckCircle2 className="w-4 h-4 md:w-5 md:h-5 text-accent" />
                  {item}
                </li>
              ))}
            </ul>

            <div className="flex items-center gap-4 md:gap-6">
              <div className="flex -space-x-3 md:-space-x-4">
                {[1,2,3,4].map(i => (
                  <div key={i} className="w-10 h-10 md:w-12 md:h-12 rounded-full border-2 border-dark overflow-hidden">
                    <img src={`https://i.pravatar.cc/100?img=${i+10}`} alt="Client" referrerPolicy="no-referrer" />
                  </div>
                ))}
              </div>
              <div>
                <p className="font-bold text-xs md:text-sm">4.8/5.0</p>
                <p className="text-[10px] md:text-xs text-white/40">Excelência Técnica</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section id="depoimentos" className="py-16 md:py-24 px-4 md:px-6">
        <div className="container mx-auto">
          <div className="reveal text-center mb-12 md:mb-16">
            <h2 className="font-display text-3xl md:text-6xl tracking-tighter mb-4 uppercase">O QUE DIZEM <span className="text-accent italic">NOSSOS CLIENTES</span></h2>
            <div className="flex justify-center gap-1 mb-4">
              {[1,2,3,4,5].map(i => <Star key={i} className="w-4 h-4 md:w-5 md:h-5 fill-accent text-accent" />)}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
            {[
              {
                name: "Ricardo Silva",
                role: "Gerente Industrial",
                text: "A manutenção preventiva realizada pela Proteus reduziu drasticamente nossas paradas não programadas. Profissionais de altíssimo nível."
              },
              {
                name: "Ana Paula",
                role: "Administradora de Condomínio",
                text: "O projeto de iluminação e a reforma do quadro elétrico do condomínio foram executados com perfeição e dentro do prazo."
              },
              {
                name: "Marcos Oliveira",
                role: "Proprietário Comercial",
                text: "Instalação elétrica rápida e limpa. O engenheiro foi muito atencioso e resolveu um problema antigo na rede que ninguém achava."
              }
            ].map((testimonial, i) => (
              <div key={i} className="reveal bento-card flex flex-col justify-between p-6 md:p-8">
                <p className="text-white/70 italic mb-6 md:mb-8 text-sm md:text-base leading-relaxed">"{testimonial.text}"</p>
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-full bg-accent/20 flex items-center justify-center font-bold text-accent text-sm">
                    {testimonial.name[0]}
                  </div>
                  <div>
                    <p className="font-bold text-xs md:text-sm">{testimonial.name}</p>
                    <p className="text-[10px] md:text-xs text-white/40">{testimonial.role}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact / CTA */}
      <section id="contato" className="py-16 md:py-24 px-4 md:px-6 relative overflow-hidden">
        <div className="absolute inset-0 bg-accent/5 -z-10"></div>
        <div className="container mx-auto max-w-5xl glass rounded-[2rem] md:rounded-[3rem] p-6 md:p-20 text-center relative overflow-hidden">
          <div className="absolute top-0 right-0 w-48 h-48 md:w-64 md:h-64 bg-accent/20 blur-[80px] md:blur-[120px] -translate-y-1/2 translate-x-1/2"></div>
          
          <div className="reveal">
            <h2 className="font-display text-3xl md:text-7xl tracking-tighter mb-6 md:mb-8 text-balance uppercase">
              SOLICITE SEU <span className="text-accent">PROJETO</span> AGORA
            </h2>
            <p className="text-white/60 text-base md:text-lg mb-8 md:mb-12 max-w-2xl mx-auto">
              Fale com um engenheiro e receba um orçamento personalizado para sua residência ou empresa.
            </p>
            
            <div className="flex flex-col lg:flex-row items-center justify-center gap-4 md:gap-6 mb-8 md:mb-12">
              <a 
                href="https://wa.me/5519971418256"
                className="w-full lg:w-auto flex items-center justify-center gap-3 bg-accent text-white px-8 md:px-12 py-4 md:py-6 rounded-full text-lg md:text-xl font-bold hover:scale-105 transition-transform"
              >
                <MessageCircle className="w-6 h-6" /> WhatsApp Agora
              </a>
              <div className="flex flex-col items-start gap-3 md:gap-4 text-left glass p-4 md:p-6 rounded-2xl md:rounded-3xl w-full lg:w-auto">
                <div className="flex items-center gap-3">
                  <Phone className="w-4 h-4 md:w-5 md:h-5 text-accent" />
                  <span className="font-bold text-sm md:text-base">(19) 97141-8256</span>
                </div>
                <div className="flex items-center gap-3">
                  <MapPin className="w-4 h-4 md:w-5 md:h-5 text-accent" />
                  <span className="text-[10px] md:text-sm text-white/60">Campinas e Região</span>
                </div>
              </div>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-8 pt-8 md:pt-12 border-t border-white/10">
              <div>
                <p className="text-2xl md:text-3xl font-display text-accent mb-1">4.8</p>
                <p className="text-[8px] md:text-[10px] uppercase tracking-widest font-bold text-white/40">Google Rating</p>
              </div>
              <div>
                <p className="text-2xl md:text-3xl font-display text-accent mb-1">150+</p>
                <p className="text-[8px] md:text-[10px] uppercase tracking-widest font-bold text-white/40">Projetos</p>
              </div>
              <div>
                <p className="text-2xl md:text-3xl font-display text-accent mb-1">2019</p>
                <p className="text-[8px] md:text-[10px] uppercase tracking-widest font-bold text-white/40">Fundação</p>
              </div>
              <div>
                <p className="text-2xl md:text-3xl font-display text-accent mb-1">100%</p>
                <p className="text-[8px] md:text-[10px] uppercase tracking-widest font-bold text-white/40">Segurança</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-6 border-t border-white/5">
        <div className="container mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
          <div className="flex items-center gap-3">
            <div className="h-10 w-10 bg-accent rounded-lg flex items-center justify-center">
              {logoError ? (
                <Zap className="text-white w-6 h-6 fill-white" />
              ) : (
                <img 
                  src="/logo.png" 
                  alt="Proteus Logo" 
                  className="h-full w-full object-contain p-1"
                  onError={() => setLogoError(true)}
                />
              )}
            </div>
            <span className="font-display text-lg tracking-tighter uppercase font-bold">Proteus</span>
          </div>
          
          <p className="text-white/30 text-[10px] uppercase tracking-widest text-center">
            © 2026 Proteus Engenharia Elétrica • Todos os direitos reservados
          </p>

          <div className="flex items-center gap-6">
            <a href="https://www.instagram.com/proteus_engenharia/" target="_blank" className="text-white/40 hover:text-accent transition-colors text-xs uppercase tracking-widest">
              Instagram
            </a>
          </div>
        </div>
      </footer>

      {/* Floating WhatsApp */}
      <a 
        href="https://wa.me/5519971418256" 
        target="_blank"
        className="fixed bottom-6 right-6 md:bottom-8 md:right-8 z-50 w-14 h-14 md:w-16 md:h-16 bg-[#25D366] rounded-full flex items-center justify-center shadow-2xl hover:scale-110 transition-transform active:scale-95"
      >
        <MessageCircle className="w-7 h-7 md:w-8 md:h-8 text-white fill-white" />
        <span className="absolute -top-1 -left-1 flex h-4 w-4 md:h-5 md:w-5">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
          <span className="relative inline-flex rounded-full h-4 w-4 md:h-5 md:w-5 bg-white text-[10px] items-center justify-center text-[#25D366] font-bold">1</span>
        </span>
      </a>
    </div>
  );
}
