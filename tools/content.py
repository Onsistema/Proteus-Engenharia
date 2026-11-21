# -*- coding: utf-8 -*-
"""Conteúdo do site da Proteus. Edite aqui e rode `python3 tools/build.py`."""

BASE = "https://proteus-engenharia.vercel.app"  # trocar pelo domínio próprio quando estiver ativo
PHONE = "(19) 97141-8256"
PHONE_E164 = "+5519971418256"
WA = "5519971418256"
INSTAGRAM = "https://www.instagram.com/proteus_engenharia/"
FACEBOOK = "https://www.facebook.com/ProteusIeP"
RATING = "4,8"
REVIEWS = "30"
SINCE = "2019"

GROUPS = [
    ("ele", "Elétrica", "E"),
    ("seg", "Segurança", "S"),
    ("tec", "Tecnologia e redes", "T"),
]

# ordem, grupo e chamada curta de cada serviço
SERVICE_META = {
    "instalacoes-eletricas": ("ele", "Instalações elétricas", "Pontos, circuitos e quadros para casas, lojas e escritórios."),
    "manutencao-eletrica": ("ele", "Manutenção elétrica", "Disjuntor desarmando, ponto sem energia, fiação antiga."),
    "engenharia-eletrica": ("ele", "Engenharia elétrica", "Projeto, dimensionamento e adequação com engenheiro."),
    "carregador-veicular": ("ele", "Carregador para carro elétrico", "Wallbox em casa e em condomínio, de qualquer marca."),
    "instalacao-de-aparelhos-eletricos": ("ele", "Instalação de aparelhos", "Circuito e ponto certo para cada equipamento."),
    "eletricista-industrial": ("ele", "Eletricista industrial", "Painéis, alimentação e manutenção em galpões."),
    "cameras-de-seguranca": ("seg", "Câmeras e CFTV", "Projeto, instalação e manutenção de câmeras."),
    "controle-de-acesso": ("seg", "Controle de acesso", "Facial, biometria, tag, senha e fechaduras digitais."),
    "cerca-eletrica": ("seg", "Cerca elétrica", "Proteção de perímetro com central e alarme."),
    "alarmes-de-incendio": ("seg", "Alarme de incêndio", "Centrais, detectores e acionadores endereçáveis."),
    "redes-de-internet": ("tec", "Redes e cabeamento", "Cabeamento estruturado, racks e Wi-Fi que alcança tudo."),
    "automacao-residencial": ("tec", "Automação e iluminação", "Casa inteligente, LED e cenas de iluminação."),
    "telecomunicacoes": ("tec", "Telecomunicações", "Telefonia, PABX e infraestrutura de comunicação."),
    "som-ambiente": ("tec", "Som ambiente", "Áudio distribuído em casas, lojas e recepções."),
    "manutencao-de-computadores": ("tec", "Manutenção de computadores", "Suporte a estações de trabalho de empresas."),
}

# Serviço novo (não existia no site antigo; aparece no Instagram da Proteus)
NEW_SERVICES = [{
    "slug": "carregador-veicular",
    "name": "Carregador para carro elétrico",
    "title": "Instalação de carregador para carro elétrico em Campinas | Proteus",
    "desc": "Instalação de carregador veicular (wallbox) em casas e condomínios de Campinas e região. BYD, Volvo, Porsche, GWM e outras marcas. Avaliação do quadro e do circuito.",
    "h1": "Instalação de carregador para carro elétrico em Campinas.",
    "lead": "Carregar em casa é o jeito mais prático e barato de usar um carro elétrico. Para isso, o wallbox precisa de um circuito próprio, proteção correta e uma instalação que aguente horas de carga todos os dias.",
    "h2": "Carregador veicular instalado do jeito certo, em casa ou no condomínio.",
    "intro": [
        "A Proteus instala carregadores de todas as marcas do mercado em residências e condomínios de Campinas e região. Antes de instalar, avaliamos o padrão de entrada, o quadro de distribuição e a distância até a vaga, para dimensionar cabo e proteções.",
        "Em condomínios, a instalação também envolve a autorização do síndico, o caminho do cabo pelas áreas comuns e a forma de medir o consumo de cada unidade. Ajudamos a organizar essas definições antes da obra."
    ],
    "checks": [
        "Avaliação do padrão de entrada e da carga disponível",
        "Circuito exclusivo com disjuntor e proteção DR",
        "Infraestrutura até a vaga com eletroduto e cabos dimensionados",
        "Configuração e teste do carregador com o carro",
    ],
    "tags": ["Casas e sobrados", "Vagas em condomínio", "Empresas e estacionamentos"],
    "guide_h2": "Como funciona a instalação de carregador veicular em Campinas",
    "guide_intro": "Antes de comprar ou instalar o wallbox, vale entender o que define o custo e o prazo da instalação.",
    "topics": [
        {"q": "Minha casa aguenta um carregador de carro elétrico?",
         "a": "Depende do padrão de entrada da concessionária e do que já está ligado no imóvel. Carregadores residenciais costumam trabalhar entre 3,7 kW e 7,4 kW em monofásico ou bifásico, e até 11 kW ou 22 kW em trifásico. Em alguns casos é preciso pedir aumento de carga à CPFL antes da instalação."},
        {"q": "O que entra na instalação do wallbox?",
         "a": "Circuito exclusivo saindo do quadro, disjuntor e proteção diferencial-residual (DR) adequados ao carregador, cabos dimensionados para a distância até a vaga, eletroduto ou canaleta, fixação do equipamento e teste de carga com o veículo."},
        {"q": "Carregador em condomínio: o que precisa?",
         "a": "Autorização do condomínio, definição do ponto de alimentação (medidor da unidade ou quadro das áreas comuns) e um caminho seguro para o cabo até a vaga. Em prédios com vários carros elétricos, vale planejar uma infraestrutura coletiva para não sobrecarregar a entrada de energia."},
        {"q": "Instalo o carregador que veio com o carro ou compro outro?",
         "a": "Muitas montadoras entregam um carregador portátil e um wallbox opcional. Instalamos o modelo que você já tem ou ajudamos a escolher um compatível com o carro e com a potência disponível no imóvel."},
    ],
    "faqs": [
        {"q": "Vocês instalam carregador de qualquer marca?", "a": "Sim. Já instalamos carregadores BYD, de carros de luxo como Porsche e de outras marcas. O que muda é a potência e o tipo de ligação, não a marca."},
        {"q": "Quanto tempo leva a instalação?", "a": "Em casas com quadro em boas condições, normalmente um dia de trabalho. Condomínios e casos que exigem aumento de carga levam mais tempo por causa das autorizações."},
        {"q": "Preciso de aumento de carga na CPFL?", "a": "Só se a potência disponível não for suficiente. Avaliamos o padrão e o consumo do imóvel antes e dizemos se é necessário."},
    ],
    "img_alt": "Carregador de carro elétrico instalado em garagem residencial",
}]

# Regiões atendidas (as que aparecem no Perfil da Empresa no Google)
AREAS = [
    {"slug": "campinas", "name": "Campinas", "kind": "cidade",
     "title": "Eletricista, câmeras e segurança eletrônica em Campinas | Proteus",
     "desc": "Engenheiro eletricista em Campinas: instalações elétricas, câmeras de segurança, controle de acesso, cerca elétrica, redes e carregador veicular. Atendimento no local.",
     "h1": "Instalações elétricas e segurança eletrônica em Campinas.",
     "lead": "A Proteus atende Campinas desde 2019, no endereço do cliente: casas, apartamentos, condomínios, lojas, clínicas e empresas.",
     "body": [
        "Campinas tem de tudo: prédios antigos no Centro e no Cambuí com fiação que já passou da hora de revisar, condomínios horizontais em Barão Geraldo e no Taquaral que precisam de câmeras e controle de acesso, e empresas espalhadas pelos distritos industriais que dependem de energia e rede funcionando o dia inteiro.",
        "Como o atendimento é feito no local, combinamos a visita conforme o bairro e a urgência. Para orçamentos simples, fotos e uma descrição pelo WhatsApp já resolvem boa parte da avaliação.",
     ],
     "focus": ["instalacoes-eletricas", "cameras-de-seguranca", "controle-de-acesso", "carregador-veicular", "manutencao-eletrica", "redes-de-internet"],
     "near": ["cambui", "barao-geraldo", "taquaral", "valinhos", "paulinia"],
     "faqs": [
        {"q": "Quais bairros de Campinas vocês atendem?", "a": "Todos. Entre os mais frequentes estão Cambuí, Centro, Taquaral, Barão Geraldo, Jardim das Paineiras, Chácara da Barra, Jardim Flamboyant, Botafogo, Jardim Guanabara e Jardim do Trevo."},
        {"q": "Vocês fazem visita para orçamento em Campinas?", "a": "Sim, quando o serviço exige. Em muitos casos, fotos e medidas enviadas pelo WhatsApp permitem adiantar o orçamento."},
     ]},
    {"slug": "cambui", "name": "Cambuí", "kind": "bairro",
     "title": "Eletricista e câmeras no Cambuí, Campinas | Proteus",
     "desc": "Eletricista, câmeras de segurança, controle de acesso e redes no Cambuí, em Campinas. Atendimento para apartamentos, escritórios, clínicas e lojas.",
     "h1": "Eletricista e segurança eletrônica no Cambuí.",
     "lead": "Apartamentos, consultórios, escritórios e lojas: o Cambuí concentra imóveis que precisam de instalação limpa, sem quebra-quebra e com pouca interrupção.",
     "body": [
        "Boa parte dos prédios do Cambuí tem algumas décadas. É comum encontrar quadros sem proteção DR, circuitos sobrecarregados por ar-condicionado e cozinha elétrica, e tomadas sem aterramento. Uma revisão elétrica antes da reforma evita surpresas depois.",
        "Para clínicas e escritórios, trabalhamos com rede cabeada, Wi-Fi para todos os ambientes, controle de acesso na recepção e câmeras. Para condomínios, fazemos a troca de sistemas antigos de CFTV e de interfonia por soluções atuais.",
     ],
     "focus": ["manutencao-eletrica", "instalacoes-eletricas", "redes-de-internet", "controle-de-acesso", "cameras-de-seguranca", "automacao-residencial"],
     "near": ["campinas", "taquaral", "barao-geraldo"],
     "faqs": [
        {"q": "Vocês trabalham em apartamento com regras de horário do condomínio?", "a": "Sim. Planejamos o serviço dentro dos horários permitidos pelo prédio e organizamos a obra para fazer menos barulho e sujeira."},
        {"q": "Dá para instalar rede e Wi-Fi em consultório sem quebrar parede?", "a": "Na maioria dos casos, sim, usando canaletas discretas, forro ou eletrodutos existentes. Avaliamos o melhor caminho antes."},
     ]},
    {"slug": "barao-geraldo", "name": "Barão Geraldo", "kind": "distrito",
     "title": "Eletricista, câmeras e cerca elétrica em Barão Geraldo | Proteus",
     "desc": "Instalações elétricas, câmeras de segurança, cerca elétrica, controle de acesso e carregador veicular em Barão Geraldo, Campinas.",
     "h1": "Instalações elétricas e segurança em Barão Geraldo.",
     "lead": "Casas com quintal, condomínios horizontais e chácaras: em Barão Geraldo, proteger o perímetro e manter a elétrica em dia é prioridade.",
     "body": [
        "Em casas e condomínios de Barão Geraldo, os pedidos mais comuns são câmeras cobrindo frente e fundos, cerca elétrica em muros longos, motor de portão e controle de acesso. Planejamos tudo junto para que câmeras, alarme e cerca funcionem como um só sistema.",
        "Também instalamos carregadores para carros elétricos em casas e condomínios do distrito, com avaliação do padrão de entrada antes de começar.",
     ],
     "focus": ["cameras-de-seguranca", "cerca-eletrica", "controle-de-acesso", "carregador-veicular", "instalacoes-eletricas", "automacao-residencial"],
     "near": ["campinas", "paulinia", "taquaral"],
     "faqs": [
        {"q": "Vocês atendem chácaras e casas grandes em Barão Geraldo?", "a": "Sim. Para áreas grandes, combinamos câmeras com boa visão noturna, cerca elétrica e rede bem distribuída para chegar sinal em todos os pontos."},
        {"q": "Atendem condomínios do distrito?", "a": "Sim, tanto as casas quanto as áreas comuns: portaria, controle de acesso e câmeras."},
     ]},
    {"slug": "taquaral", "name": "Taquaral", "kind": "bairro",
     "title": "Eletricista e câmeras de segurança no Taquaral, Campinas | Proteus",
     "desc": "Eletricista, câmeras, controle de acesso, automação e carregador de carro elétrico no Taquaral e região, em Campinas.",
     "h1": "Eletricista e segurança eletrônica no Taquaral.",
     "lead": "Casas, sobrados e prédios ao redor da Lagoa do Taquaral: atendemos reformas, manutenção e sistemas de segurança no bairro e arredores.",
     "body": [
        "No Taquaral, muitas casas passam por reforma e ampliação. É o momento certo para refazer circuitos, trocar o quadro, prever pontos de rede e deixar a infraestrutura pronta para câmeras, automação e carregador de carro elétrico.",
        "Em prédios do bairro, atendemos tanto o morador quanto o condomínio: manutenção elétrica, troca de câmeras e modernização do controle de acesso.",
     ],
     "focus": ["instalacoes-eletricas", "automacao-residencial", "cameras-de-seguranca", "carregador-veicular", "controle-de-acesso", "som-ambiente"],
     "near": ["campinas", "cambui", "barao-geraldo"],
     "faqs": [
        {"q": "Vocês acompanham reforma junto com o arquiteto?", "a": "Sim. Trabalhamos com arquitetos e engenheiros da obra para definir pontos elétricos, iluminação, rede e segurança antes do acabamento."},
        {"q": "Fazem automação de iluminação em casa já pronta?", "a": "Sim. Existem módulos que entram na caixa do interruptor e não exigem quebrar parede."},
     ]},
    {"slug": "valinhos", "name": "Valinhos", "kind": "cidade",
     "title": "Eletricista, câmeras e carregador veicular em Valinhos | Proteus",
     "desc": "Instalações elétricas, câmeras de segurança, cerca elétrica, controle de acesso e carregador para carro elétrico em Valinhos (SP).",
     "h1": "Instalações elétricas e segurança eletrônica em Valinhos.",
     "lead": "Valinhos tem muitos condomínios fechados e casas de alto padrão. Atendemos moradores, síndicos e empresas da cidade com o mesmo cuidado de Campinas.",
     "body": [
        "Em condomínios de Valinhos, fazemos desde a elétrica da casa até o carregador de carro elétrico na garagem, câmeras, automação e som ambiente. Para as áreas comuns, atendemos portaria com controle de acesso facial, câmeras e alarme de incêndio.",
        "Para empresas e comércios da cidade, fazemos manutenção elétrica, cabeamento de rede e segurança eletrônica.",
     ],
     "focus": ["carregador-veicular", "cameras-de-seguranca", "automacao-residencial", "controle-de-acesso", "instalacoes-eletricas", "cerca-eletrica"],
     "near": ["campinas", "taquaral", "barao-geraldo"],
     "faqs": [
        {"q": "Vocês cobram deslocamento para Valinhos?", "a": "Valinhos faz parte da nossa área de atendimento. Informamos qualquer condição no orçamento, antes de agendar."},
        {"q": "Atendem condomínios fechados em Valinhos?", "a": "Sim, tanto as casas quanto a administração do condomínio."},
     ]},
    {"slug": "paulinia", "name": "Paulínia", "kind": "cidade",
     "title": "Eletricista industrial, câmeras e redes em Paulínia | Proteus",
     "desc": "Eletricista industrial, instalações elétricas, câmeras, controle de acesso e cabeamento de rede em Paulínia (SP). Atendimento para empresas, casas e condomínios.",
     "h1": "Instalações elétricas, segurança e redes em Paulínia.",
     "lead": "Paulínia combina polo industrial e bairros residenciais em crescimento. Atendemos as duas frentes: empresas e galpões, casas e condomínios.",
     "body": [
        "Para empresas e prestadores do polo industrial de Paulínia, fazemos manutenção elétrica, adequação de painéis e alimentação de equipamentos, cabeamento estruturado e câmeras para galpões e pátios.",
        "Nos bairros residenciais e condomínios da cidade, instalamos câmeras, cerca elétrica, controle de acesso e carregadores de carro elétrico.",
     ],
     "focus": ["eletricista-industrial", "manutencao-eletrica", "redes-de-internet", "cameras-de-seguranca", "controle-de-acesso", "carregador-veicular"],
     "near": ["campinas", "barao-geraldo"],
     "faqs": [
        {"q": "Vocês atendem empresas em Paulínia?", "a": "Sim. Envie a descrição do serviço, fotos do painel ou do local e a urgência para avaliarmos."},
        {"q": "Fazem câmeras para galpão e pátio?", "a": "Sim, com câmeras adequadas para áreas grandes e externas e gravação centralizada."},
     ]},
]
