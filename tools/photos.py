# -*- coding: utf-8 -*-
"""Fotos reais da Proteus (Instagram @proteus_engenharia). Arquivos em site/fotos/<codigo>.jpg."""
from pathlib import Path
_DIR = Path(__file__).resolve().parent.parent / "site" / "fotos"

# código do post: (legenda, texto alternativo, serviços relacionados)
_ALL = [
    ("C2FuAUQx2uC", "Carregador veicular instalado com quadro de proteção próprio", "Wallbox instalado em parede com quadro de proteção dedicado", ["carregador-veicular"]),
    ("B2xC8ibFQ1Y", "Quadro de distribuição montado e organizado", "Quadro de distribuição com disjuntores e cabos organizados", ["instalacoes-eletricas", "manutencao-eletrica", "engenharia-eletrica"]),
    ("CdbsR9lglt2", "Reconhecimento facial na entrada de condomínio", "Leitor de reconhecimento facial instalado na entrada de condomínio", ["controle-de-acesso"]),
    ("Cvvu8NbsRw1", "Rack de rede organizado", "Rack de rede com patch panel e cabos organizados", ["redes-de-internet", "telecomunicacoes"]),
    ("C2P3LykAl_z", "Iluminação LED em tabica com perfil de silicone", "Fita de LED embutida em tabica no teto", ["automacao-residencial"]),
    ("C2mZDIJIY0c", "Alarme de incêndio endereçável", "Acionador manual de alarme de incêndio instalado", ["alarmes-de-incendio"]),
    ("B3KN1xJl8cf", "Câmera dome em área comum", "Câmera dome fixada em parede", ["cameras-de-seguranca"]),
    ("Cdi2paEAS-j", "Câmera com infraestrutura nova, sem fio aparente", "Câmera de segurança fixada sob viga com cabeamento embutido", ["cameras-de-seguranca"]),
    ("C1-J2q2p63m", "Instalação de carregador BYD", "Eletricista instalando carregador veicular junto ao quadro", ["carregador-veicular"]),
    ("CvvutW-skcY", "Cabeamento estruturado com switch", "Cabos de rede azuis conectados a switch", ["redes-de-internet"]),
    ("CSFSiO5FNCY", "Fechaduras digitais Intelbras", "Caixas de fechaduras digitais Intelbras com senha e biometria", ["controle-de-acesso"]),
    ("C2Yb2hYpIgA", "Interruptor inteligente para casa automatizada", "Interruptor touch de automação residencial instalado na parede", ["automacao-residencial"]),
    ("Cde3EEqo_nc", "Troca do sistema de câmeras em condomínio", "Câmera nova instalada em muro de condomínio", ["cameras-de-seguranca"]),
    ("Ce2XwFqoNHB", "Rack com patch panels e organizadores", "Rack de telecomunicações com patch panels", ["redes-de-internet", "telecomunicacoes"]),
    ("B6MKZrKF8Nw", "Controle de acesso com leitor e interfone", "Interfone e leitor de acesso instalados na parede", ["controle-de-acesso"]),
    ("CwTnCmPJFl_", "Teste e certificação de cabos de rede", "Testador de cabos de rede em uso", ["redes-de-internet"]),
    ("B5HDKSKFLdR", "Eletroduto e acionador de alarme de incêndio", "Eletroduto aparente e acionador de incêndio em parede", ["alarmes-de-incendio", "instalacoes-eletricas"]),
    ("C2UZLBput4e", "Iluminação embutida com automação", "Spots de iluminação embutidos em teto de gesso", ["automacao-residencial"]),
    ("B3MkFydlqd3", "Vídeo porteiro instalado", "Vídeo porteiro instalado em parede", ["controle-de-acesso", "telecomunicacoes"]),
    ("CSMpmWVgg-x", "Infraestrutura para iluminação e som ambiente", "Parede de tijolos com eletroduto e caixas de passagem", ["som-ambiente", "instalacoes-eletricas"]),
    ("CdeXhC_gixj", "Instalação de motor e acionamento de portão", "Equipamento de acionamento instalado em parede", ["controle-de-acesso"]),
    ("C3DU5_KgomZ", "Carregador BYD pronto para instalar", "Carregador veicular BYD antes da instalação", ["carregador-veicular"]),
    ("BpsJMyAg8ts", "Leitor de acesso em porta", "Leitor de controle de acesso ao lado de porta", ["controle-de-acesso"]),
    ("B4DLAiCFo7y", "Organização de cabeamento em caixa de passagem", "Cabos organizados dentro de caixa de passagem", ["redes-de-internet", "telecomunicacoes"]),
]
PHOTOS, WORKS = {}, []
_have = lambda c: (_DIR / f"{c}.jpg").exists()
for code, cap, alt, svcs in _ALL:
    if not _have(code):
        continue
    item = {"src": f"/fotos/{code}.jpg", "alt": alt, "caption": cap, "services": svcs, "real": True}
    WORKS.append(item)
    for s in svcs:  # primeira foto encontrada vira a foto do serviço
        PHOTOS.setdefault(s, item)

def _pick(key, code):
    if _have(code):
        PHOTOS[key] = next(w for w in WORKS if w["src"].endswith(code + ".jpg"))

_pick("home:1", "CdbsR9lglt2")
_pick("home:2", "C2FuAUQx2uC")
_pick("home:3", "Cvvu8NbsRw1")
_pick("home:about", "B2xC8ibFQ1Y")
for svc_slug in ["som-ambiente", "manutencao-de-computadores", "eletricista-industrial", "instalacao-de-aparelhos-eletricos"]:
    pass  # sem foto real específica: usam a ilustrativa
