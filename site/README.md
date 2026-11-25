# Proteus Instalações e Projetos — site

Site estático publicado na Vercel (projeto **proteus-engenharia**, pasta raiz `site`). Cada push na `main` publica automaticamente.

## Como editar

As páginas são geradas por `tools/build.py`. Não edite os HTML à mão: edite o conteúdo e gere de novo.

- `tools/content.py`: dados da empresa, domínio (`BASE`), serviços novos e regiões atendidas.
- `tools/data/services.json`: textos das páginas de serviço.
- `tools/posts.py`: artigos do blog (markdown simples).
- `tools/photos.py`: fotos reais (Instagram) e onde cada uma aparece. Arquivos em `site/fotos/`.
- `site/assets/site.css` e `site/assets/site.js`: visual e comportamento.

Depois de editar: `python3 tools/build.py` e faça commit da pasta `site`.

## Domínio próprio

Domínio ativo: proteusengenharia.com.br (DNS na Hostinger, registro A 76.76.21.21). Para mudar, troque `BASE` em `tools/content.py`, rode o build e configure o domínio na Vercel com redirecionamento do endereço `.vercel.app`.
