# Activation Policy — Fonte Normativa

## Objetivo

Este arquivo define o escopo de ativação da skill `amazon-lightsail-fullstack`.

A `description` do `SKILL.md` deve ser uma síntese fiel desta política.

## Regra de ativação

A skill deve ser considerada aplicável em somente dois grupos de contexto.

### Grupo A — Amazon Lightsail explícito

Ative quando a solicitação mencionar explicitamente Amazon Lightsail e tratar de provisionamento, dimensionamento, Ubuntu no Lightsail, deploy, infraestrutura, Nginx, systemd, firewall, DNS, TLS/SSL, SSH, PostgreSQL, Prisma em produção, backup, snapshots, observabilidade, troubleshooting, capacidade ou operação do servidor.

### Grupo B — Ubuntu Server + stack aprovada

Ative quando a solicitação:

1. envolver Ubuntu Server, infraestrutura, deploy ou operação de servidor; e
2. envolver ao menos um componente da stack aprovada: Next.js, NestJS, PostgreSQL ou Prisma.

## Não ativar

Não use para:

- Ubuntu genérico sem a stack aprovada;
- Samba no Ubuntu;
- Nginx para aplicação Python;
- systemd para Django;
- UFW genérico;
- PostgreSQL para Java;
- desenvolvimento isolado de React/Next/Nest/Prisma;
- Prisma local sem contexto de servidor/deploy;
- Git/GitHub isolado;
- outros serviços AWS sem Lightsail.

## Prioridade de interpretação

1. Procure referência explícita a Lightsail.
2. Sem Lightsail, exija contexto de infraestrutura/deploy/operação em Ubuntu.
3. Exija ao menos um componente da stack aprovada.
4. Se não atender, não considere a skill aplicável.

## Testes

Use `tests/router-eval-cases.json` em um evaluation harness real do host.

`scripts/validate_skill_contract.py` não simula o roteador. Ele valida somente consistência interna da skill.

## Regra final

Não mantenha um classificador paralelo hardcoded para tentar reproduzir a ativação semântica do host.

A fonte de verdade é:

```text
activation-policy.md
        ↓
SKILL.md description
        ↓
host skill router
```
