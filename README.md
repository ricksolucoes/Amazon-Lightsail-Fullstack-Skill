<div align="center">

# ☁️ Amazon Lightsail Full Stack Skill

### Agent Skill para arquitetura, provisionamento, segurança, deploy e operação de aplicações modernas no Amazon Lightsail

[![Amazon Lightsail](https://img.shields.io/badge/Amazon%20Lightsail-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/lightsail/)
[![Ubuntu Server](https://img.shields.io/badge/Ubuntu%20Server-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/server)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-OpenAI-000000?style=for-the-badge&logo=openai&logoColor=white)](https://agentskills.io/)
[![License MIT](https://img.shields.io/github/license/ricksolucoes/amazon-lightsail-fullstack-skill?style=for-the-badge)](LICENSE)


</div>



## 📌 Sobre o projeto

**Amazon Lightsail Full Stack Skill** é uma Agent Skill especializada em transformar uma IA em um profissional de infraestrutura capaz de **planejar, configurar, publicar, proteger, validar e diagnosticar** aplicações full stack executadas no **Amazon Lightsail com Ubuntu Server**.

A skill não atua apenas como um gerador de comandos.

Ela organiza o raciocínio da IA em diferentes responsabilidades técnicas para impedir que uma instalação comece antes de requisitos, arquitetura, custos, rede e segurança estarem suficientemente definidos.

O comportamento segue este fluxo:

```text
CTO
 ↓
Arquiteto de Soluções
 ↓
Engenheiro de Redes
 ↓
SysAdmin / DevOps
 ↓
Auditoria Técnica
```

O resultado é uma abordagem orientada a:

- 🎯 contexto antes da execução;
- 💰 custo-benefício;
- 🧩 compatibilidade entre tecnologias;
- 🔐 segurança por padrão;
- 🛡️ menor exposição de serviços;
- 🔎 inspeção antes de alterações;
- 🧪 validação depois de cada etapa;
- ↩️ rollback quando houver risco;
- 📋 auditoria técnica antes de considerar a implantação concluída.



## 🎯 Para que serve

A skill foi criada para auxiliar uma IA em tarefas como:

- criar e dimensionar uma instância Amazon Lightsail;
- preparar Ubuntu Server para produção;
- configurar Static IP;
- planejar DNS;
- revisar IPv4 e IPv6;
- configurar Lightsail Firewall e UFW;
- proteger SSH;
- instalar e validar runtime Node.js;
- publicar Next.js;
- publicar NestJS;
- instalar e proteger PostgreSQL;
- configurar Prisma em produção;
- executar migrations com segurança;
- configurar Nginx como reverse proxy;
- configurar HTTPS/TLS;
- criar serviços `systemd`;
- organizar variáveis de ambiente;
- diagnosticar `502`, `504`, OOM e disco cheio;
- revisar portas expostas;
- planejar snapshot e backup;
- estruturar deploy via Git/GitHub;
- validar o servidor antes e depois de mudanças.



## 🧠 The Tech Brain

A IA alterna entre quatro comportamentos principais e uma etapa final de auditoria.

### 👔 CTO — Comportamento Executivo

Responsável por transformar a necessidade do usuário em requisitos técnicos.

Analisa:

- orçamento;
- ambiente;
- criticidade;
- crescimento;
- disponibilidade;
- RPO/RTO;
- necessidade de backup;
- custo-benefício.

O CTO evita dimensionamento exagerado e também impede uma infraestrutura abaixo da necessidade real.



### 🏗️ Arquiteto de Soluções — Comportamento Analítico

Responsável por transformar o escopo aprovado em arquitetura.

Analisa:

- compatibilidade da stack;
- runtime;
- CPU;
- memória;
- armazenamento;
- topologia;
- serviços;
- portas internas;
- diretórios;
- build;
- migrations;
- logs;
- observabilidade.

Produz a **Bill of Infrastructure** da solução.



### 🌐 Engenheiro de Redes — Comportamento Tático

Responsável por conectividade, exposição e segurança.

Analisa:

- Static IP;
- DNS;
- IPv4;
- IPv6;
- SSH;
- Lightsail Firewall;
- UFW;
- portas públicas;
- portas privadas;
- reverse proxy;
- TLS.

A regra principal é:

> Expor publicamente apenas o que realmente precisa estar público.



### ⚙️ SysAdmin / DevOps — Comportamento Operacional

Responsável pela execução.

Transforma as decisões anteriores em:

- comandos;
- scripts;
- arquivos de configuração;
- serviços `systemd`;
- Nginx;
- PostgreSQL;
- Prisma;
- deploy;
- validações;
- rollback.

Cada alteração operacional deve seguir:

```text
1. Objetivo
2. Pré-condição
3. Comando
4. Resultado esperado
5. Validação
6. Rollback
7. Próxima etapa
```



### 🔍 Auditoria Técnica

Depois da implantação, a IA revisa o ambiente.

Entre os itens auditados:

- stack preservada;
- serviços sem `root`;
- segredos fora do Git;
- portas internas privadas;
- PostgreSQL protegido;
- HTTPS válido;
- `systemd` habilitado;
- serviços recuperáveis após reboot;
- logs disponíveis;
- backup definido;
- rollback documentado;
- ausência de `chmod 777`;
- ausência de mudanças fora do escopo.

Se houver não conformidade, a tarefa retorna para o especialista responsável.



## 🧱 Stack tecnológica suportada

A skill foi desenhada para trabalhar com esta linha tecnológica:

| Camada | Tecnologia |
|---|---|
| 🟦 Linguagem | TypeScript 7.0.x |
| ▲ Frontend | Next.js 16.3.x |
| ⚛️ UI | React 19.3.x |
| 🎨 CSS | Tailwind CSS 4.3.x |
| 🧩 Componentes | shadcn/ui compatível com React 19 / Tailwind v4 |
| 🐈 Backend | NestJS 12.1.x |
| 🔌 API | REST + Swagger/OpenAPI |
| 🐘 Banco | PostgreSQL 18.x |
| 🔺 ORM | Prisma 7.10.x |
| 🔐 Auth | JWT + Refresh Token + Argon2 |
| ✅ Frontend validation | Zod |
| ✅ Backend validation | class-validator |
| 🧪 Testes | Jest + Playwright |
| 🌿 Versionamento | Git + GitHub |
| 🐧 Servidor | Ubuntu Server |
| 📦 Deploy | Nativo |
| 🐳 Docker | Não utilizado no deploy inicial |

> A skill trata essa stack como contrato técnico e não troca tecnologias ou versões silenciosamente.



## 🏛️ Arquitetura padrão

A topologia inicial esperada é:

```text
                      Internet
                         │
                         ▼
                Lightsail Firewall
                         │
                         ▼
                     Static IP
                         │
                         ▼
                  Nginx :80/:443
                    /         \
                   /           \
                  ▼             ▼
              Next.js         NestJS
            127.0.0.1       127.0.0.1
                                  │
                                  ▼
                                Prisma
                                  │
                                  ▼
                             PostgreSQL
                           localhost:5432
```

Por padrão:

| Serviço | Exposição |
|---|---|
| SSH | Restrita |
| HTTP 80 | Pública |
| HTTPS 443 | Pública |
| Next.js | Privada |
| NestJS | Privada |
| PostgreSQL | Privada |




## 🔐 Segurança por padrão

A skill possui regras que impedem recomendações operacionais inseguras.

Ela não deve:

- ❌ usar `chmod 777`;
- ❌ executar aplicações como `root`;
- ❌ colocar segredos no Git;
- ❌ expor PostgreSQL publicamente por padrão;
- ❌ abrir portas internas do Next.js/NestJS sem necessidade;
- ❌ alterar SSH antes de validar acesso alternativo;
- ❌ destruir banco, snapshot, certificado ou instância sem confirmação;
- ❌ usar `prisma migrate reset` em produção;
- ❌ usar `prisma db push --force-reset` em produção;
- ❌ inventar IP, senha, domínio, região ou credencial.



## 🚦 Quando a skill deve ser usada

A política completa está em:

[`references/activation-policy.md`](standalone/amazon-lightsail-fullstack/references/activation-policy.md)

### ✅ Deve ativar

Exemplos:

```text
Quero montar um servidor no Amazon Lightsail para publicar
meu Next.js e NestJS com PostgreSQL.
```

```text
Meu NestJS no Lightsail está retornando 502 no Nginx.
```

```text
Preciso publicar Next.js em um Ubuntu Server usando Nginx e systemd.
```

```text
Preciso aplicar Prisma migrations em produção no Ubuntu Server
da minha API NestJS.
```

### ❌ Não deve ativar

Exemplos:

```text
Como instalar Samba no Ubuntu?
```

```text
Como configurar Nginx para Flask?
```

```text
Como criar um serviço systemd para Django?
```

```text
Como instalar PostgreSQL para uma aplicação Java?
```

```text
Como criar um componente React com shadcn/ui?
```



## 📂 Estrutura do repositório

```text
amazon-lightsail-fullstack-skill/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── standalone/
│   └── amazon-lightsail-fullstack/
│       │
│       ├── SKILL.md
│       │
│       ├── agents/
│       │   └── openai.yaml
│       │
│       ├── references/
│       │   ├── activation-policy.md
│       │   ├── behavioral-pipeline.md
│       │   ├── deployment-sequence.md
│       │   ├── lightsail-architecture.md
│       │   ├── native-deployment.md
│       │   ├── postgresql-prisma.md
│       │   ├── troubleshooting.md
│       │   └── ubuntu-hardening.md
│       │
│       ├── scripts/
│       │   ├── preflight.sh
│       │   └── validate_skill_contract.py
│       │
│       └── tests/
│           ├── activation-cases.md
│           └── router-eval-cases.json
│
└── plugin/
    └── amazon-lightsail-fullstack/
        ├── plugin.json
        └── skills/
            └── amazon-lightsail-fullstack/
                └── ...
```



## 📦 Formatos disponíveis

O repositório disponibiliza a skill em dois formatos.

### 🧠 Agent Skill standalone

Use:

```text
standalone/amazon-lightsail-fullstack/
```

Esse diretório contém:

- `SKILL.md`;
- referências;
- scripts;
- testes;
- metadados OpenAI.

### 🔌 Plugin portátil

Use:

```text
plugin/amazon-lightsail-fullstack/
```

O plugin contém:

```text
plugin.json
skills/
```

A skill interna é mantida equivalente à standalone.



## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/ricksolucoes/amazon-lightsail-fullstack-skill.git
cd amazon-lightsail-fullstack-skill
```

### 2. Escolha o formato

Para trabalhar diretamente com a Agent Skill:

```text
standalone/amazon-lightsail-fullstack
```

Para utilizar o pacote portátil:

```text
plugin/amazon-lightsail-fullstack
```

### 3. Disponibilize a skill no host compatível

Instale ou registre o diretório conforme o mecanismo de Agent Skills suportado pelo host utilizado.

A ativação implícita está habilitada em:

```text
agents/openai.yaml
```



## 💬 Exemplos de uso

### Planejamento completo

```text
Quero publicar um sistema com Next.js, NestJS, Prisma e PostgreSQL
no Amazon Lightsail.

Ainda não escolhi a máquina.

Analise o cenário e me conduza desde o dimensionamento até o deploy.
```

A skill deve começar pelo comportamento **CTO**, e não diretamente por comandos.



### Troubleshooting

```text
Meu backend NestJS está funcionando em localhost,
mas o domínio retorna 502 pelo Nginx no Lightsail.

Analise sem alterar nada até identificar a camada do problema.
```

A skill deve coletar evidências antes de recomendar alterações.



### Revisão de segurança

```text
Revise as portas, firewall, SSH, Nginx e PostgreSQL
do meu servidor Lightsail e me diga o que está exposto indevidamente.
```



### Deploy em produção

```text
Tenho o build aprovado.

Me conduza pelo deploy de produção seguindo a ordem segura
de migrations, restart dos serviços, health check e rollback.
```



## 🔄 Sequência normativa de deploy

A fonte oficial da ordem de implantação é:

[`references/deployment-sequence.md`](standalone/amazon-lightsail-fullstack/references/deployment-sequence.md)

Resumo:

```text
Preflight
   ↓
Backup / Snapshot
   ↓
Atualização do código
   ↓
Dependências
   ↓
Testes
   ↓
Build
   ↓
Validar migrations
   ↓
Backup do banco
   ↓
Prisma migrate deploy
   ↓
Restart systemd
   ↓
Teste localhost
   ↓
Nginx
   ↓
Health Check
   ↓
Logs
   ↓
Auditoria
```



## 🩺 Preflight do servidor

A skill inclui um script de inspeção não destrutivo:

```bash
bash standalone/amazon-lightsail-fullstack/scripts/preflight.sh
```

Ele verifica:

- sistema operacional;
- arquitetura;
- uptime;
- memória;
- disco;
- inodes;
- rede;
- portas;
- serviços com falha;
- Node.js;
- npm/pnpm/yarn;
- Git;
- Nginx;
- PostgreSQL;
- UFW.

O script evita prompt interativo de `sudo`.



## ✅ Validar o contrato da skill

Execute:

```bash
python3 standalone/amazon-lightsail-fullstack/scripts/validate_skill_contract.py
```

O validador utiliza **somente a biblioteca padrão do Python**.

Também pode ser executado sem carregar `site-packages`:

```bash
python3 -S standalone/amazon-lightsail-fullstack/scripts/validate_skill_contract.py
```

Saída esperada:

```text
Skill contract validation: PASS
External Python dependencies: NONE
Host semantic routing was NOT simulated.
```

> Esse script valida a consistência interna da skill.  
> Ele não tenta reproduzir o roteador semântico do host.



## 🧪 Casos de ativação

O dataset de avaliação está em:

```text
standalone/amazon-lightsail-fullstack/tests/router-eval-cases.json
```

Atualmente ele cobre:

```text
6 casos positivos
10 casos negativos
```

Incluindo fronteiras como:

- Lightsail vs outros serviços AWS;
- Ubuntu da stack vs Ubuntu genérico;
- Prisma em produção vs Prisma local;
- Nginx/NestJS vs Nginx/Flask;
- PostgreSQL da stack vs PostgreSQL/Java.



## 📚 Documentação interna

| Documento | Responsabilidade |
|||
| [`SKILL.md`](standalone/amazon-lightsail-fullstack/SKILL.md) | Comportamento principal da skill |
| [`activation-policy.md`](standalone/amazon-lightsail-fullstack/references/activation-policy.md) | Regras de ativação |
| [`behavioral-pipeline.md`](standalone/amazon-lightsail-fullstack/references/behavioral-pipeline.md) | Estados CTO → Auditoria |
| [`deployment-sequence.md`](standalone/amazon-lightsail-fullstack/references/deployment-sequence.md) | Ordem normativa do deploy |
| [`lightsail-architecture.md`](standalone/amazon-lightsail-fullstack/references/lightsail-architecture.md) | Arquitetura Lightsail |
| [`ubuntu-hardening.md`](standalone/amazon-lightsail-fullstack/references/ubuntu-hardening.md) | Segurança do Ubuntu |
| [`native-deployment.md`](standalone/amazon-lightsail-fullstack/references/native-deployment.md) | Deploy nativo |
| [`postgresql-prisma.md`](standalone/amazon-lightsail-fullstack/references/postgresql-prisma.md) | PostgreSQL + Prisma |
| [`troubleshooting.md`](standalone/amazon-lightsail-fullstack/references/troubleshooting.md) | Diagnóstico operacional |



## 🤝 Contribuindo

Contribuições são bem-vindas.

Ao propor alterações:

1. preserve o escopo da skill;
2. não altere silenciosamente a stack;
3. mantenha standalone e plugin equivalentes;
4. não introduza segredos ou dados reais;
5. atualize casos de teste quando alterar regras de ativação;
6. preserve a sequência normativa de deploy;
7. valide o contrato antes de enviar a alteração.



## 📜 Licença

Distribuído sob a licença **MIT**.

Veja [`LICENSE`](LICENSE).



<div align="center">

### ☁️ Amazon Lightsail Full Stack Skill

**Arquitetura antes da execução. Segurança antes da exposição. Validação antes da conclusão.**

Desenvolvido por **Rick Soluções**

</div>
