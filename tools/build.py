# -*- coding: utf-8 -*-
"""Gera o site estático da Proteus na pasta /site.
Uso: python3 tools/build.py
"""
import json, os, re, html, shutil
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
TOOLS = ROOT / "tools"
import sys; sys.path.insert(0, str(TOOLS))
from content import *          # noqa
from posts import POSTS        # noqa
try:
    from photos import PHOTOS, WORKS   # fotos reais (Instagram)
except ImportError:
    PHOTOS, WORKS = {}, []

E = html.escape
YEAR = "2026"

# ---------- dados ----------
services = json.load(open(TOOLS / "data/services.json", encoding="utf-8")) + NEW_SERVICES
for s in services:
    g, short_name, blurb = SERVICE_META[s["slug"]]
    s["group"], s["short"], s["blurb"] = g, short_name, blurb
order = list(SERVICE_META.keys())
services.sort(key=lambda s: order.index(s["slug"]))
SV = {s["slug"]: s for s in services}
codes = {}
for g, _, letter in GROUPS:
    for i, s in enumerate([x for x in services if x["group"] == g], 1):
        codes[s["slug"]] = f"{letter}{i}"
AR = {a["slug"]: a for a in AREAS}
PO = {p["slug"]: p for p in POSTS}
POSTS_SORTED = sorted(POSTS, key=lambda p: p["date"], reverse=True)

IMG = {  # fotos de alta resolução (Pexels, uso livre) em site/img
    "instalacoes-eletricas": "cove2", "manutencao-eletrica": "cove", "engenharia-eletrica": "projeto",
    "carregador-veicular": "ev", "instalacao-de-aparelhos-eletricos": "cove2", "cameras-de-seguranca": "casa",
    "controle-de-acesso": "hero2", "cerca-eletrica": "muro", "alarmes-de-incendio": "alarme",
    "automacao-residencial": "painel", "som-ambiente": "pool2",
    "area:campinas": "hero", "area:cambui": "cove2", "area:barao-geraldo": "casa", "area:taquaral": "cove",
    "area:valinhos": "pool", "area:paulinia": "projeto2", "area:vinhedo": "pool2", "area:sumare": "muro",
    "area:hortolandia": "projeto2", "area:indaiatuba": "hero2",
}
ALTS = {"hero": "Fachada de casa moderna iluminada à noite", "hero2": "Entrada de residência contemporânea com iluminação embutida",
    "cove": "Sala com iluminação indireta embutida no forro", "cove2": "Ambiente integrado com sanca de LED",
    "muro": "Fachada de casa moderna com muro e portão de madeira", "ev": "Carro elétrico carregando em wallbox residencial",
    "ev2": "Wallbox instalado na parede da garagem", "pool": "Casa contemporânea com piscina iluminada ao entardecer",
    "pool2": "Residência com área externa e iluminação de paisagismo", "painel": "Painel touch de automação residencial",
    "alarme": "Central de alarme instalada na parede", "projeto": "Planta de projeto sobre a mesa", "projeto2": "Arquitetos revisando projeto no escritório",
    "casa": "Casa moderna iluminada ao anoitecer"}

def hi(key):
    n = IMG.get(key, key)
    return {"src": f"/img/{n}.jpg", "alt": ALTS.get(n, ""), "real": False}

def photo(key, fallback_slug=None):
    """Foto de alta resolução se houver; senão foto real; senão a ilustrativa."""
    if key in IMG:
        return hi(key)
    if key in PHOTOS:
        return PHOTOS[key]
    slug = fallback_slug or key
    if slug == "carregador-veicular":
        slug = "instalacoes-eletricas"
    return {"src": f"/imagens/{slug}-servico-ilustrativo.jpg", "alt": "Imagem ilustrativa", "real": False}

def wa(text):
    return f"https://wa.me/{WA}?text={quote(text)}"

# ---------- ícones ----------
I = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
 "chev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".5" fill="currentColor"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1l-.9 1.2c-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4ZM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8Zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.8L.1 24l6.3-1.7A11.8 11.8 0 0 0 24 12c0-3.2-1.2-6.1-3.5-8.4Z"/></svg>',
}

def wires(cls, w, h, paths):
    ps = "".join(f'<path class="{c}" d="{d}"/>' for c, d in paths)
    return f'<svg class="wires draw {cls}" viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true">{ps}</svg>'

def hero_wires():
    # três condutores (fase, neutro, terra) correndo pela base do hero
    return wires("", 1400, 120, [
        ("w-r", "M0 40 H520 Q560 40 560 70 V80 Q560 98 590 98 H1400"),
        ("w-b", "M0 58 H500 Q540 58 540 86 V92 Q540 110 570 110 H1400"),
        ("w-g", "M0 76 H480 Q500 76 506 96 Q512 118 540 118 H1400"),
        ("w-y", "M0 76 H480 Q500 76 506 96 Q512 118 540 118 H1400"),
    ])

def small_wires():
    return wires("", 1400, 90, [
        ("w-r", "M0 30 H900 Q930 30 930 55 Q930 74 960 74 H1400"),
        ("w-b", "M0 46 H880 Q910 46 910 66 Q910 84 940 84 H1400"),
        ("w-g", "M0 62 H860 Q880 62 886 76 Q892 88 920 88 H1400"),
        ("w-y", "M0 62 H860 Q880 62 886 76 Q892 88 920 88 H1400"),
    ])

# ---------- schema ----------
def org():
    return {
        "@context": "https://schema.org", "@type": "Electrician", "@id": BASE + "/#empresa",
        "name": "Proteus Instalações e Projetos", "url": BASE + "/",
        "logo": BASE + "/assets/mark.svg", "image": BASE + "/assets/og.jpg",
        "telephone": PHONE_E164, "foundingDate": "2019-04",
        "description": "Engenharia elétrica, instalações, câmeras de segurança, controle de acesso, cerca elétrica, redes e carregadores para carro elétrico em Campinas e região.",
        "address": {"@type": "PostalAddress", "addressLocality": "Campinas", "addressRegion": "SP", "addressCountry": "BR"},
        "areaServed": [{"@type": "City", "name": n} for n in ["Campinas", "Valinhos", "Vinhedo", "Paulínia", "Sumaré", "Hortolândia", "Indaiatuba"]] +
                      [{"@type": "Place", "name": f"{n}, Campinas"} for n in ["Cambuí", "Barão Geraldo", "Taquaral"]],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:00", "closes": "19:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "12:00"}],
        "sameAs": [INSTAGRAM, FACEBOOK],
        "knowsAbout": [s["name"] for s in services],
    }

def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(items)]}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faqs]}

# ---------- layout ----------
def head(title, desc, path, image=None, schemas=(), og_type="website", body=""):
    url = BASE + path
    img = image if image and image.startswith("http") else BASE + (image or "/assets/og.jpg")
    js = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta name="theme-color" content="#141518"><meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{og_type}"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Proteus Instalações e Projetos">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Instrument+Serif&display=swap">
<link rel="stylesheet" href="/assets/site.css?v=6">{js}</head><body class="{body}">
<a class="skip" href="#conteudo">Pular para o conteúdo</a>'''

def header(active=""):
    cols = ""
    for g, label, _ in GROUPS:
        links = "".join(f'<a href="/servicos/{s["slug"]}/">{E(s["short"])}</a>' for s in services if s["group"] == g)
        cols += f'<div><h4>{label}</h4>{links}</div>'
    cur = lambda k: ' aria-current="page"' if active == k else ""
    return f'''<header class="top"><div class="wrap top-row">
<a class="brand" href="/" aria-label="Proteus Instalações e Projetos, página inicial"><img src="/assets/mark.svg" alt="" width="40" height="44"><span><b>Proteus</b><small>Instalações e Projetos</small></span></a>
<nav class="nav" id="nav" aria-label="Principal">
<div class="drop"><button type="button" aria-expanded="false" aria-controls="mega">Serviços {I["chev"]}</button><div class="mega" id="mega">{cols}<a class="all" href="/servicos/">Ver todos os serviços</a></div></div>
<a href="/trabalhos/"{cur("trabalhos")}>Obras</a>
<a href="/#arquitetos">Arquitetos</a>
<a href="/atendimento/"{cur("atendimento")}>Onde atendemos</a>
<a href="/blog/"{cur("blog")}>Blog</a>
<a href="/#contato">Contato</a>
<a class="btn wa mobile-cta" style="display:none" href="{wa("Olá, Proteus! Gostaria de um orçamento.")}" target="_blank" rel="noopener">{I["wa"]}Chamar no WhatsApp</a>
</nav>
<a class="btn" href="{wa("Olá, Proteus! Gostaria de um orçamento.")}" target="_blank" rel="noopener">Solicitar orçamento</a>
<button class="menu-btn" type="button" aria-label="Abrir menu" aria-controls="nav" aria-expanded="false"><span></span></button>
</div></header><main id="conteudo">'''

def footer():
    svc = "".join(f'<a href="/servicos/{s["slug"]}/">{E(s["short"])}</a>' for s in services[:8])
    ar = "".join(f'<a href="/atendimento/{a["slug"]}/">{E(a["name"])}</a>' for a in AREAS)
    return f'''</main><footer class="foot"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="/"><img src="/assets/mark.svg" alt="" width="40" height="44"><span><b>Proteus</b><small>Instalações e Projetos</small></span></a>
<p>Engenharia elétrica, segurança eletrônica e redes em Campinas e região, desde 2019. Atendimento no endereço do cliente.</p></div>
<div><b>Serviços</b>{svc}<a href="/servicos/">Todos os serviços</a></div>
<div><b>Onde atendemos</b>{ar}</div>
<div><b>Contato</b><a href="{wa("Olá, Proteus!")}" target="_blank" rel="noopener">WhatsApp {PHONE}</a><a href="tel:{PHONE_E164}">Ligar</a>
<a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a>
<span style="display:block;padding:4px 0">Seg a sex, 7h às 19h<br>Sáb, 9h às 12h</span></div>
</div>
<div class="foot-bottom"><span>© {YEAR} Proteus Instalações e Projetos · Campinas, SP</span><span><a href="/blog/">Blog</a> · <a href="/sitemap.xml">Mapa do site</a></span></div>
</div></footer>
<a class="wa-float" href="{wa("Olá, Proteus! Encontrei vocês pelo site e gostaria de um orçamento.")}" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">{I["wa"]}<span>WhatsApp</span></a>
<script src="/assets/site.js?v=4" defer></script></body></html>'''

def faq_block(faqs):
    return '<div class="faq">' + "".join(
        f'<details><summary>{E(f["q"])}<i aria-hidden="true"></i></summary><p>{E(f["a"])}</p></details>' for f in faqs) + "</div>"

def contact_section(preset=""):
    opts = "".join(f'<option{" selected" if s["name"] == preset else ""}>{E(s["name"])}</option>' for s in services) + "<option>Outro serviço</option>"
    return f'''<section class="sec contact on-dark" id="contato"><div class="wrap contact-grid">
<div><span class="label">Contato</span><h2>Vamos conversar sobre o seu projeto.</h2>
<p class="lead">A gente responde pelo WhatsApp com as próximas etapas: perguntas, fotos que ajudam ou uma visita, se for o caso.</p>
<div class="contact-lines">
<a href="{wa("Olá, Proteus!")}" target="_blank" rel="noopener">{I["wa"]}{PHONE} (WhatsApp)</a>
<span>{I["pin"]}Campinas, Valinhos, Vinhedo, Paulínia, Sumaré, Hortolândia, Indaiatuba e região</span>
<span>{I["clock"]}Seg a sex, 7h às 19h · Sáb, 9h às 12h</span>
</div></div>
<form class="form" id="quote-form" novalidate>
<h3>Pedir orçamento</h3>
<div class="row"><label>Seu nome<input name="name" required autocomplete="name"></label>
<label>Cidade ou bairro<input name="city" autocomplete="address-level2" placeholder="Ex.: Cambuí"></label></div>
<label>Serviço<select name="service" required><option value="">Escolha um serviço</option>{opts}</select></label>
<label>Tipo de imóvel<select name="property"><option value="">Opcional</option><option>Casa</option><option>Apartamento</option><option>Condomínio</option><option>Comércio</option><option>Empresa ou indústria</option></select></label>
<label>Detalhes<textarea name="details" placeholder="O que precisa ser feito, quantidade, urgência..."></textarea></label>
<button class="btn wa" type="submit">{I["wa"]}Enviar pelo WhatsApp</button>
<p class="note">O formulário só monta a mensagem. Nada é salvo no site: você revisa e envia no seu WhatsApp.</p>
</form></div>
</section>'''

def breadcrumb_html(items):
    parts = []
    for i, (n, u) in enumerate(items):
        parts.append(f'<span>{E(n)}</span>' if i == len(items) - 1 else f'<a href="{u}">{E(n)}</a><span aria-hidden="true">/</span>')
    return '<nav class="crumbs" aria-label="Você está em">' + "".join(parts) + "</nav>"

def img_tag(p, cls="", eager=False, w=800, h=600):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="{p["src"]}" alt="{E(p["alt"])}" width="{w}" height="{h}" {load}{" class=%s" % cls if cls else ""}>'

def write(path, content):
    out = SITE / path.strip("/") / "index.html" if not path.endswith(".xml") and not path.endswith(".txt") else SITE / path.strip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")

# ---------- markdown mínimo ----------
def md(text):
    out, lst = [], None
    def inline(t):
        t = E(t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', t)
        return t
    def close():
        nonlocal lst
        if lst: out.append(f"</{lst}>"); lst = None
    for line in text.strip().split("\n"):
        s = line.strip()
        if not s: close(); continue
        if s.startswith("### "): close(); out.append(f"<h3>{inline(s[4:])}</h3>")
        elif s.startswith("## "): close(); h = s[3:]; out.append(f'<h2 id="{slugify(h)}">{inline(h)}</h2>')
        elif s.startswith("> "): close(); out.append(f"<blockquote><p>{inline(s[2:])}</p></blockquote>")
        elif s.startswith("- "):
            if lst != "ul": close(); out.append("<ul>"); lst = "ul"
            out.append(f"<li>{inline(s[2:])}</li>")
        elif re.match(r"\d+\. ", s):
            if lst != "ol": close(); out.append("<ol>"); lst = "ol"
            out.append(f"<li>{inline(re.sub(r'^\d+\. ', '', s))}</li>")
        else: close(); out.append(f"<p>{inline(s)}</p>")
    close()
    return "\n".join(out)

def slugify(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

# ---------- blocos reutilizáveis ----------
def discipline_cards(subset=None, img_keys=None):
    blurbs = {"ele": "Projeto, instalação e manutenção com dimensionamento correto, quadros organizados e infraestrutura pronta para o futuro.",
              "seg": "Cerca elétrica, câmeras e controle de acesso planejados para proteger sem poluir a fachada.",
              "tec": "Rede que alcança todos os ambientes, automação, iluminação de cena e som ambiente."}
    imgs = img_keys or {"ele": "cove2", "seg": "muro", "tec": "painel"}
    titles = {"ele": "Elétrica e iluminação", "seg": "Segurança", "tec": "Tecnologia e automação"}
    out = ""
    for g, _, _ in GROUPS:
        items = [s for s in services if s["group"] == g and (subset is None or s["slug"] in subset)]
        if not items: continue
        li = "".join(f'<li><a href="/servicos/{s["slug"]}/">{E(s["short"])}{I["arrow"]}</a></li>' for s in items)
        out += f'''<div class="discipline"><div class="ph">{img_tag(hi(imgs[g]), w=800, h=1000)}</div>
<h3>{titles[g]}</h3><p>{blurbs[g]}</p><ul>{li}</ul></div>'''
    return f'<div class="disciplines">{out}</div>'

panel_html = lambda subset=None: discipline_cards(subset)

def post_cards(posts):
    out = ""
    for p in posts:
        ph = photo(p["cover"])
        out += f'''<a class="post" href="/blog/{p["slug"]}/"><div class="ph">{img_tag(ph, w=720, h=480)}</div>
<small>{p["cat"]} · {p["read"]} min de leitura</small><h3>{E(p["title"])}</h3><p>{E(p["desc"])}</p></a>'''
    return f'<div class="posts">{out}</div>'

def area_cards(slugs):
    out = ""
    for s in slugs:
        a = AR[s]
        sub = {"cidade": "Cidade", "bairro": "Bairro de Campinas", "distrito": "Distrito de Campinas"}[a["kind"]]
        out += f'<a class="area" href="/atendimento/{s}/"><span>{E(a["name"])}<small>{sub}</small></span>{I["arrow"]}</a>'
    return out

def works_grid(limit=None, cls="works"):
    items = WORKS[:limit] if limit else WORKS
    if not items: return ""
    return f'<div class="{cls}">' + "".join(f'<figure>{img_tag(w, w=600, h=800)}<figcaption>{E(w["caption"])}</figcaption></figure>' for w in items) + '</div>'

def reel(codes):
    items = [w for c in codes for w in WORKS if w["src"].endswith(c + ".jpg")]
    return '<div class="reel">' + "".join(f'<figure>{img_tag(w, w=600, h=800)}<figcaption>{E(w["caption"])}</figcaption></figure>' for w in items) + '</div>'

def page_hero(items, title, lead, img=None, cta=None):
    bg = f'<div class="bg">{img_tag(img, eager=True, w=1800, h=900)}</div>' if img else ""
    cls = "page-hero" + ("" if img else " plain")
    ctah = f'<div class="hero-cta">{cta}</div>' if cta else ""
    return f'''<section class="{cls}">{bg}<div class="in"><div class="wrap">{breadcrumb_html(items)}
<h1>{E(title)}</h1><p class="lead">{lead}</p>{ctah}</div></div></section>'''

def page_home():
    home_faqs = [
        {"q": "Vocês trabalham junto com arquitetos e construtoras?", "a": "Sim. Recebemos o projeto, compatibilizamos elétrica, iluminação, rede e segurança com o arquitetônico e seguimos o cronograma da obra até a entrega."},
        {"q": "Vocês atendem residências, condomínios e empresas?", "a": "Sim. Casas, apartamentos, condomínios, lojas, clínicas, escritórios e indústrias em Campinas e região."},
        {"q": "Como funciona o orçamento?", "a": "Você conta o que precisa pelo WhatsApp, de preferência com fotos ou com o projeto. Para serviços maiores, fazemos visita técnica antes de fechar o escopo."},
        {"q": "Cerca elétrica precisa de manutenção?", "a": "Sim. Vegetação encostando, isoladores quebrados e fios frouxos causam alarmes falsos e perda de eficiência. Uma revisão periódica mantém a cerca funcionando e dentro das normas."},
        {"q": "A Proteus tem loja ou endereço para visita?", "a": "Não. Todo atendimento é feito no endereço do cliente ou na obra, com horário combinado."},
    ]
    schemas = [org(), faq_schema(home_faqs), {"@context": "https://schema.org", "@type": "WebSite", "name": "Proteus Instalações e Projetos", "url": BASE + "/"}]
    W = wa("Olá, Proteus! Gostaria de um orçamento.")
    body = head("Engenharia elétrica, cerca elétrica e segurança em Campinas | Proteus",
                "Engenharia elétrica, iluminação, cerca elétrica, câmeras, controle de acesso, automação e carregador para carro elétrico em Campinas e região. Parceira de arquitetos e construtoras.",
                "/", schemas=schemas, body="home") + header()
    body += f'''<section class="hero"><div class="hero-bg">{img_tag(hi("hero"), eager=True, w=2000, h=1333)}</div>
<div class="hero-in"><div class="wrap">
<span class="label" style="color:var(--brass-l)">Campinas e região, desde {SINCE}</span>
<h1>A infraestrutura que a arquitetura não deixa aparecer.</h1>
<p class="lead">Elétrica, iluminação, segurança e automação para residências de alto padrão, condomínios e empresas. Projeto com engenheiro responsável e acabamento à altura do seu projeto.</p>
<div class="hero-cta"><a class="btn brass" href="{W}" target="_blank" rel="noopener">Solicitar orçamento</a><a class="btn line-light" href="#arquitetos">Para arquitetos</a></div>
<div class="hero-foot"><span><span class="stars" aria-hidden="true">★★★★★</span> <b>{RATING}</b> no Google, {REVIEWS} avaliações</span><span>Engenheiro responsável em cada obra</span><span>Campinas, Valinhos, Vinhedo, Indaiatuba e região</span></div>
</div></div></section>

<section class="sec"><div class="wrap intro">
<div><span class="label">A Proteus</span><h2>Quando a elétrica é bem feita, ninguém repara. Só sente o conforto, a segurança e a luz no lugar certo.</h2></div>
<div class="intro-side"><p class="lead">Somos uma empresa de engenharia elétrica e sistemas de Campinas. Cuidamos de tudo o que passa pela parede: energia, iluminação, rede, câmeras, cerca elétrica, controle de acesso e automação.</p>
<p style="margin-top:18px">Trabalhamos com critério técnico e cuidado com o acabamento: cabos dimensionados, quadros identificados, infraestrutura embutida e nada de fio aparente estragando o projeto.</p>
<div class="facts"><div><b>{SINCE}</b><span>atendendo Campinas e região</span></div><div><b>{RATING}</b><span>nota no Google, {REVIEWS} avaliações</span></div><div><b>{len(services)}</b><span>especialidades sob um só responsável</span></div></div>
</div></div></section>

<section class="sec stone" id="servicos"><div class="wrap">
<div class="sec-head"><div><span class="label">Especialidades</span><h2>Três disciplinas, um único responsável técnico.</h2></div><p>Planejar elétrica, segurança e tecnologia juntas evita retrabalho, economiza na obra e deixa o resultado mais limpo.</p></div>
{discipline_cards()}
</div></section>

<section class="feature"><div class="feature-ph">{img_tag(hi("muro"), w=1400, h=934)}</div>
<div class="feature-tx"><span class="label">Segurança perimetral</span><h2>Cerca elétrica instalada com técnica e discrição.</h2>
<p class="lead">A primeira barreira da casa precisa funcionar todos os dias e combinar com a fachada. Instalamos, integramos ao alarme e mantemos a cerca dentro das normas.</p>
<ul class="ticks"><li>Central certificada, aterramento próprio e placas de advertência conforme a Lei 13.477/2017</li><li>Integração com alarme, sirene e aviso no celular</li><li>Hastes e fios alinhados ao desenho do muro</li><li>Manutenção preventiva: poda, isoladores, tensão e aterramento</li></ul>
<div class="row"><a class="btn" href="/servicos/cerca-eletrica/">Conhecer o serviço</a><a class="btn line" href="{wa("Olá, Proteus! Gostaria de orçamento para cerca elétrica.")}" target="_blank" rel="noopener">Orçar cerca elétrica</a></div></div></section>

<section class="feature rev on-dark"><div class="feature-ph">{img_tag(hi("ev"), w=1400, h=933)}</div>
<div class="feature-tx"><span class="label">Mobilidade elétrica</span><h2>Carregador para carro elétrico em casa ou no condomínio.</h2>
<p class="lead">Avaliamos o padrão de entrada e o quadro, dimensionamos o circuito e instalamos o wallbox de qualquer marca, com proteção completa.</p>
<ul class="ticks"><li>BYD, Volvo, Porsche, GWM e outras marcas</li><li>Circuito exclusivo com disjuntor e DR</li><li>Apoio na aprovação junto ao condomínio</li></ul>
<div class="row"><a class="btn brass" href="/servicos/carregador-veicular/">Saiba mais</a></div></div></section>

<section class="feature" id="arquitetos"><div class="feature-ph">{img_tag(hi("projeto2"), w=1400, h=933)}</div>
<div class="feature-tx"><span class="label">Para arquitetos e construtoras</span><h2>Um parceiro técnico que respeita o seu projeto.</h2>
<p class="lead">Entramos cedo na obra para que elétrica, luminotécnica, rede e segurança cheguem prontas para o acabamento, sem improviso e sem surpresa para o seu cliente.</p>
<ul class="ticks"><li>Compatibilização com o projeto arquitetônico e luminotécnico</li><li>Infraestrutura embutida para automação, som, câmeras e wallbox</li><li>Cronograma alinhado às outras frentes da obra</li><li>Comunicação direta com o engenheiro responsável</li></ul>
<div class="row"><a class="btn" href="{wa("Olá, Proteus! Sou arquiteto(a) e gostaria de conversar sobre um projeto.")}" target="_blank" rel="noopener">Falar sobre um projeto</a></div></div></section>

<section class="sec dark on-dark" id="trabalhos"><div class="wrap">
<div class="sec-head"><div><span class="label">Do canteiro</span><h2>Obras recentes.</h2></div><p>Registros feitos pela equipe durante as instalações. Mais no nosso Instagram.</p></div>
{reel(["C2FuAUQx2uC", "CdbsR9lglt2", "B2xC8ibFQ1Y", "C2P3LykAl_z", "Cvvu8NbsRw1", "CSFSiO5FNCY"])}
<div class="reel-foot"><a class="textlink" href="/trabalhos/">Ver todas as obras</a><a class="textlink" href="{INSTAGRAM}" target="_blank" rel="noopener">@proteus_engenharia</a></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="sec-head"><div><span class="label">Como trabalhamos</span><h2>Do primeiro contato à entrega.</h2></div></div>
<div class="steps">
<div class="step"><em>Primeiro</em><h3>Entendimento</h3><p>Você envia fotos, plantas ou o projeto. Tiramos as dúvidas e definimos se é preciso uma visita técnica.</p></div>
<div class="step"><em>Depois</em><h3>Escopo e proposta</h3><p>Você recebe o que será feito, materiais, prazo e valor, antes de qualquer obra começar.</p></div>
<div class="step"><em>Por fim</em><h3>Execução e entrega</h3><p>Instalação limpa e testada. Explicamos o funcionamento e deixamos tudo identificado.</p></div>
</div></div></section>

<section class="sec stone"><div class="wrap">
<div class="sec-head"><div><span class="label">Atendimento</span><h2>Onde atendemos.</h2></div><p>Sempre no endereço do cliente ou na obra.</p></div>
<div class="areas">{area_cards([a["slug"] for a in AREAS])}</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="sec-head"><div><span class="label">Blog</span><h2>Para decidir com segurança.</h2></div><p><a class="textlink" href="/blog/">Todos os artigos</a></p></div>
{post_cards(POSTS_SORTED[:3])}
</div></section>

<section class="sec stone"><div class="wrap">
<div class="sec-head"><div><span class="label">Dúvidas</span><h2>Perguntas frequentes.</h2></div></div>{faq_block(home_faqs)}
</div></section>
{contact_section()}'''
    write("/", body + footer())

def page_service(s):
    path = f'/servicos/{s["slug"]}/'
    p = photo(s["slug"])
    items = [("Início", "/"), ("Serviços", "/servicos/"), (s["short"], path)]
    faqs = s["faqs"] + [{"q": t["q"], "a": t["a"]} for t in s["topics"] if t["q"].endswith("?")][:2]
    schemas = [org(), {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"], "description": s["desc"],
               "provider": {"@id": BASE + "/#empresa"}, "areaServed": org()["areaServed"], "url": BASE + path},
               crumbs_schema(items), faq_schema(faqs)]
    gallery = [w for w in WORKS if s["slug"] in w.get("services", [])][:6]
    gal_html = ('<h2>Registros de obra</h2><div class="gallery">' + "".join(f'<figure>{img_tag(w, w=400, h=400)}</figure>' for w in gallery) + '</div>') if gallery else ""
    topics = "".join(f'<h3>{E(t["q"])}</h3><p>{E(t["a"])}</p>' for t in s["topics"])
    rel_posts = [x for x in POSTS_SORTED if s["slug"] in x["services"]][:3]
    rel_posts_html = ('<div class="box"><h3>Leia também</h3><ul>' + "".join(f'<li><a href="/blog/{x["slug"]}/">{E(x["title"])}</a></li>' for x in rel_posts) + '</ul></div>') if rel_posts else ""
    same = [x for x in services if x["group"] == s["group"] and x["slug"] != s["slug"]][:5]
    same_html = '<div class="box"><h3>Outros serviços</h3><ul>' + "".join(f'<li><a href="/servicos/{x["slug"]}/">{E(x["short"])}</a></li>' for x in same) + '</ul></div>'
    areas_links = ", ".join(f'<a href="/atendimento/{a["slug"]}/">{E(a["name"])}</a>' for a in AREAS)
    W = wa(f"Olá, Proteus! Gostaria de orçamento para {s['name']}.")
    hero_img = p if p["src"].startswith("/img/") else (p if p.get("real") else dict(p, alt=s["img_alt"]))
    body = head(s["title"], s["desc"], path, image=hero_img["src"], schemas=schemas) + header()
    body += page_hero(items, s["h1"], E(s["lead"]), hero_img, f'<a class="btn brass" href="{W}" target="_blank" rel="noopener">Solicitar orçamento</a><a class="btn line-light" href="#detalhes">Entender o serviço</a>')
    body += f'''<section class="sec" id="detalhes"><div class="wrap layout">
<article class="prose">
<h2>{E(s["h2"])}</h2>{"".join(f"<p>{E(x)}</p>" for x in s["intro"])}
<h3>O que entra no serviço</h3><ul class="checks">{"".join(f"<li>{I['check']}<span>{E(c)}</span></li>" for c in s["checks"])}</ul>
<h3>Onde costuma ser necessário</h3><div class="tags">{"".join(f"<span>{E(t)}</span>" for t in s["tags"])}</div>
{gal_html}
<h2>{E(s["guide_h2"])}</h2><p>{E(s["guide_intro"])}</p>{topics}
<h2>Perguntas frequentes</h2>{faq_block(s["faqs"])}
<p style="margin-top:28px">Atendemos em {areas_links} e região.</p>
</article>
<aside class="aside">
<div class="box dark"><h3>Vamos conversar?</h3><p>Envie fotos, plantas ou uma descrição rápida. Respondemos com as próximas etapas.</p>
<a class="btn wa" href="{W}" target="_blank" rel="noopener">{I["wa"]}Falar no WhatsApp</a></div>
{rel_posts_html}{same_html}
</aside></div></section>
{contact_section(s["name"])}'''
    write(path, body + footer())

def page_services_index():
    items = [("Início", "/"), ("Serviços", "/servicos/")]
    body = head("Serviços de engenharia elétrica, segurança e automação em Campinas | Proteus",
                "Instalações e manutenção elétrica, iluminação, carregador veicular, cerca elétrica, câmeras, controle de acesso, alarme de incêndio, redes e automação em Campinas e região.",
                "/servicos/", schemas=[org(), crumbs_schema(items)]) + header()
    body += page_hero(items, "Especialidades.", f"{len(services)} serviços em três disciplinas, planejados para funcionar juntos.")
    body += f'<section class="sec"><div class="wrap">{discipline_cards()}</div></section>{contact_section()}'
    write("/servicos/", body + footer())

def page_area(a):
    path = f'/atendimento/{a["slug"]}/'
    items = [("Início", "/"), ("Onde atendemos", "/atendimento/"), (a["name"], path)]
    schemas = [org(), crumbs_schema(items), faq_schema(a["faqs"]),
               {"@context": "https://schema.org", "@type": "Service", "name": f"Instalações elétricas e segurança eletrônica em {a['name']}",
                "provider": {"@id": BASE + "/#empresa"}, "areaServed": {"@type": "Place", "name": a["name"]}, "url": BASE + path}]
    W = wa(f"Olá, Proteus! Estou em {a['name']} e gostaria de um orçamento.")
    body = head(a["title"], a["desc"], path, schemas=schemas) + header("atendimento")
    body += page_hero(items, a["h1"], E(a["lead"]), photo("area:" + a["slug"]), f'<a class="btn brass" href="{W}" target="_blank" rel="noopener">Orçamento em {E(a["name"])}</a>')
    body += f'''<section class="sec"><div class="wrap layout"><article class="prose">
<h2>Atendimento em {E(a["name"])}</h2>{"".join(f"<p>{E(x)}</p>" for x in a["body"])}
</article><aside class="aside"><div class="box dark"><h3>No seu endereço</h3><p>Seg a sex, 7h às 19h. Sáb, 9h às 12h. Envie fotos pelo WhatsApp para adiantar o orçamento.</p>
<a class="btn wa" href="{W}" target="_blank" rel="noopener">{I["wa"]}{PHONE}</a></div></aside></div></section>
<section class="sec stone"><div class="wrap"><div class="sec-head"><div><span class="label">Em {E(a["name"])}</span><h2>Serviços mais procurados.</h2></div></div>{discipline_cards(a["focus"])}</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="label">Dúvidas</span><h2>Perguntas sobre {E(a["name"])}.</h2></div></div>{faq_block(a["faqs"])}
<div style="margin-top:80px"><span class="label">Também atendemos</span><div class="areas">{area_cards(a["near"])}</div></div></div></section>
{contact_section()}'''
    write(path, body + footer())

def page_areas_index():
    items = [("Início", "/"), ("Onde atendemos", "/atendimento/")]
    body = head("Onde a Proteus atende: Campinas, Valinhos, Vinhedo, Sumaré, Hortolândia, Indaiatuba e região",
                "A Proteus atende no endereço do cliente em Campinas (Cambuí, Barão Geraldo, Taquaral e demais bairros), Valinhos, Vinhedo, Paulínia, Sumaré, Hortolândia e Indaiatuba.",
                "/atendimento/", schemas=[org(), crumbs_schema(items)]) + header("atendimento")
    body += page_hero(items, "Onde atendemos.", "Todo atendimento é feito no endereço do cliente ou na obra.", hi("pool"))
    body += f'''<section class="sec"><div class="wrap"><div class="areas">{area_cards([a["slug"] for a in AREAS])}</div>
<p style="margin-top:32px;color:var(--ink-3)">Também atendemos outros bairros de Campinas, como Centro, Jardim das Paineiras, Chácara da Barra, Jardim Flamboyant, Botafogo, Jardim Guanabara e Jardim do Trevo. Está em outra cidade da região? Pergunte pelo WhatsApp.</p></div></section>
{contact_section()}'''
    write("/atendimento/", body + footer())

def page_blog_index():
    items = [("Início", "/"), ("Blog", "/blog/")]
    schema = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog da Proteus", "url": BASE + "/blog/",
              "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": BASE + f'/blog/{p["slug"]}/', "datePublished": p["date"]} for p in POSTS_SORTED]}
    body = head("Blog da Proteus: elétrica, segurança eletrônica e automação",
                "Guias práticos sobre instalação elétrica, cerca elétrica, câmeras, controle de acesso, carregador de carro elétrico e redes, escritos por engenheiro eletricista.",
                "/blog/", schemas=[org(), crumbs_schema(items), schema]) + header("blog")
    body += page_hero(items, "Blog.", "Guias práticos para decidir melhor antes de contratar: preço, normas, tecnologia e manutenção.")
    body += f'<section class="sec"><div class="wrap">{post_cards(POSTS_SORTED)}</div></section>{contact_section()}'
    write("/blog/", body + footer())

def page_post(p):
    path = f'/blog/{p["slug"]}/'
    items = [("Início", "/"), ("Blog", "/blog/"), (p["title"], path)]
    cover = photo(p["cover"])
    content = md(p["body"])
    toc = re.findall(r'<h2 id="(.+?)">(.+?)</h2>', content)
    toc_html = '<div class="box toc"><h3>Neste artigo</h3>' + "".join(f'<a href="#{i}">{re.sub("<.+?>","",t)}</a>' for i, t in toc) + '</div>'
    svc_html = '<div class="box"><h3>Serviços relacionados</h3><ul>' + "".join(f'<li><a href="/servicos/{x}/">{E(SV[x]["short"])}</a></li>' for x in p["services"]) + '</ul></div>'
    from datetime import date
    d = date.fromisoformat(p["date"])
    months = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    dtxt = f"{d.day} de {months[d.month-1]} de {d.year}"
    schema = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["desc"],
              "datePublished": p["date"], "dateModified": p["date"], "inLanguage": "pt-BR", "mainEntityOfPage": BASE + path,
              "image": BASE + cover["src"], "author": {"@type": "Organization", "name": "Proteus Instalações e Projetos", "url": BASE + "/"},
              "publisher": {"@id": BASE + "/#empresa"}}
    others = [x for x in POSTS_SORTED if x["slug"] != p["slug"]][:3]
    body = head(p["title"] + " | Proteus", p["desc"], path, image=cover["src"], schemas=[org(), crumbs_schema(items), schema], og_type="article") + header("blog")
    body += f'''<header class="article-head"><div class="wrap">{breadcrumb_html(items)}
<h1>{E(p["title"])}</h1><div class="meta"><span>{p["cat"]}</span><span>{dtxt}</span><span>{p["read"]} min de leitura</span><span>Por Proteus Instalações e Projetos</span></div></div></header>
<figure class="article-cover">{img_tag(cover, eager=True, w=1800, h=686)}</figure>
<section class="sec" style="padding-top:72px"><div class="wrap layout"><article class="prose">{content}
<div class="cta-band"><div><h2>Quer ajuda com isso?</h2><p>Envie fotos ou o projeto pelo WhatsApp. Respondemos com as próximas etapas.</p></div>
<a class="btn brass" href="{wa("Olá, Proteus! Li o artigo: " + p["title"])}" target="_blank" rel="noopener">Falar com a Proteus</a></div>
</article><aside class="aside">{toc_html}{svc_html}</aside></div></section>
<section class="sec stone"><div class="wrap"><div class="sec-head"><div><span class="label">Blog</span><h2>Continue lendo.</h2></div></div>{post_cards(others)}</div></section>'''
    write(path, body + footer())

def page_works():
    if not WORKS: return False
    items = [("Início", "/"), ("Obras", "/trabalhos/")]
    body = head("Obras e instalações da Proteus em Campinas e região",
                "Registros de instalações feitas pela Proteus: carregadores de carro elétrico, câmeras, controle de acesso, automação, iluminação, alarmes e elétrica em Campinas e região.",
                "/trabalhos/", schemas=[org(), crumbs_schema(items)]) + header("trabalhos")
    body += page_hero(items, "Obras.", f'Registros feitos pela equipe durante as instalações. Tem mais no nosso <a class="textlink" href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>.')
    body += f'<section class="sec"><div class="wrap">{works_grid()}</div></section>{contact_section()}'
    write("/trabalhos/", body + footer())
    return True

def sitemap(has_works):
    urls = [("/", "1.0"), ("/servicos/", "0.9")] + [(f'/servicos/{s["slug"]}/', "0.9") for s in services] + \
           [("/atendimento/", "0.7")] + [(f'/atendimento/{a["slug"]}/', "0.8") for a in AREAS] + \
           [("/blog/", "0.7")] + [(f'/blog/{p["slug"]}/', "0.6") for p in POSTS_SORTED]
    if has_works: urls.insert(2, ("/trabalhos/", "0.7"))
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
          "".join(f"<url><loc>{BASE}{u}</loc><lastmod>2026-11-21</lastmod><priority>{pr}</priority></url>\n" for u, pr in urls) + "</urlset>\n"
    (SITE / "sitemap.xml").write_text(xml, encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    return len(urls)

if __name__ == "__main__":
    page_home(); page_services_index(); page_areas_index(); page_blog_index()
    for s in services: page_service(s)
    for a in AREAS: page_area(a)
    for p in POSTS: page_post(p)
    hw = page_works()
    n = sitemap(hw)
    print(f"ok: {n} páginas")
