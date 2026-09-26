# Amazon Lightsail — arquitetura e provisionamento

## Objetivo

Orientar a criação de uma instância Lightsail para uma aplicação Next.js + NestJS + PostgreSQL executada nativamente no Ubuntu Server.

## Provisionamento

Antes de criar a instância, determine:

- região AWS;
- latência esperada;
- público principal;
- tamanho inicial;
- necessidade de IPv6;
- política de snapshots;
- domínio;
- estratégia de crescimento.

Não escolha plano apenas pelo menor preço. Dimensione considerando simultaneamente:

- build do Next.js;
- build do NestJS;
- Node.js em produção;
- PostgreSQL;
- Nginx;
- testes eventualmente executados no servidor;
- margem para atualizações e picos.

## IP estático

O IP público dinâmico de uma instância Lightsail pode mudar quando a instância é parada/iniciada.

Para servidor publicado:

1. criar Static IP;
2. anexar à instância;
3. validar acesso;
4. somente então configurar DNS.

## Firewall Lightsail

Trate regras IPv4 e IPv6 separadamente.

Exposição pública típica:

```text
TCP 22   SSH
TCP 80   HTTP
TCP 443  HTTPS
```

SSH deve ser restrito por origem quando operacionalmente possível.

Não publicar:

```text
3000     exemplo Next.js
3001     exemplo NestJS
5432     PostgreSQL
```

As portas reais da aplicação devem ser confirmadas no projeto.

## DNS

Sequência:

1. Static IP anexado;
2. aplicação/Nginx respondendo;
3. registro A apontando para Static IP;
4. AAAA somente se IPv6 estiver corretamente configurado;
5. aguardar resolução;
6. validar com `dig`;
7. emitir TLS.

Comandos úteis:

```bash
dig A example.com
dig AAAA example.com
getent ahosts example.com
```

## Snapshots

Antes de mudanças relevantes:

- snapshot da instância;
- backup lógico do PostgreSQL quando a mudança envolver banco.

Snapshot não substitui estratégia de backup consistente do banco.

## Crescimento

Uma única instância é válida como arquitetura inicial, mas monitore:

- RAM;
- CPU;
- disco;
- I/O;
- conexões PostgreSQL;
- tempo de resposta;
- uso durante builds.

Se os recursos se tornarem concorrentes, avalie separar banco e aplicação ou migrar componentes. Não faça essa mudança sem demanda e análise.
