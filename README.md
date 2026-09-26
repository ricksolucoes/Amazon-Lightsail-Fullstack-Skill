# amazon-lightsail-fullstack

Skill especializada em Amazon Lightsail + Ubuntu Server para a stack aprovada do projeto.

## Stack congelada pela skill

- TypeScript 7.0.x
- Next.js 16.3.x
- React 19.3.x
- Tailwind CSS 4.3.x
- shadcn/ui compatível com React 19/Tailwind v4
- NestJS 12.1.x
- REST + Swagger/OpenAPI
- PostgreSQL 18.x
- Prisma 7.10.x
- JWT + Refresh Token + Argon2
- Zod
- class-validator
- Jest + Playwright
- Git + GitHub
- Ubuntu Server nativo
- sem Docker

## Pacotes

- `standalone/amazon-lightsail-fullstack`: Agent Skill direta.
- `plugin/amazon-lightsail-fullstack`: pacote portátil com `plugin.json`.

## Princípios

A skill não altera tecnologias ou versões sem solicitação explícita. Ela prioriza inspeção do estado real, comandos verificáveis, rollback, menor privilégio, banco não exposto publicamente e deploy supervisionado por systemd/Nginx.


## Pipeline comportamental v2

CTO -> Arquiteto de Soluções -> Engenheiro de Redes -> SysAdmin/DevOps -> Auditoria Técnica.


## Revisão v3

Correções aplicadas após auditoria independente:

- correção de erro textual no `SKILL.md`;
- `preflight.sh` tornado não interativo para consulta do UFW;
- criação de `references/deployment-sequence.md` como fonte normativa única;
- harmonização de `native-deployment.md` e `behavioral-pipeline.md`;
- inclusão de `tests/activation-cases.md` com casos de ativação, não ativação, transição e regressão.


## Revisão v4

Correções implementadas após a auditoria independente final:

- `description` restringida ao domínio real de infraestrutura/deploy/operação;
- adicionados casos negativos para Prisma local, PostgreSQL local e GitHub Actions isolado;
- criado `tests/activation-cases.json`;
- criado `scripts/validate_activation.py`;
- validação local da política de ativação executada com casos positivos e negativos;
- mantida distinção entre validação interna da skill e o roteador proprietário do host.


## Revisão v5

- política de ativação consolidada em `references/activation-policy.md`;
- `description` alinhada ao escopo;
- Ubuntu genérico e outras stacks fora do escopo;
- adicionados casos limítrofes;
- removido o classificador que simulava o roteador;
- `router-eval-cases.json` destinado ao evaluation harness real;
- `validate_skill_contract.py` valida somente consistência interna.


## Revisão v6

Correção final solicitada pelo revisor:

- removida a dependência de `PyYAML` de `scripts/validate_skill_contract.py`;
- o validador agora usa somente a biblioteca padrão do Python;
- o parser interno é limitado ao subconjunto de front matter utilizado por esta skill;
- a validação é executada também com `python3 -S`, desabilitando `site-packages`, para comprovar que não depende de pacote externo.
