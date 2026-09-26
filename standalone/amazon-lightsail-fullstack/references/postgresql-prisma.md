# PostgreSQL 18.x + Prisma 7.10.x

## Topologia inicial

Por padrão:

```text
NestJS -> Prisma -> PostgreSQL @ localhost
```

PostgreSQL não precisa estar acessível pela internet.

## Usuários

Separe:

- superusuário administrativo;
- role da aplicação.

A role da aplicação deve possuir apenas os privilégios necessários.

Nunca use o superusuário PostgreSQL como credencial permanente da aplicação.

## Rede

Confirme:

```bash
ss -lntp | grep 5432
```

Para banco local, prefira bind local conforme arquitetura.

Não altere `listen_addresses` para `*` sem requisito explícito.

## DATABASE_URL

Trate como segredo.

Formato conceitual:

```text
postgresql://USER:PASSWORD@HOST:PORT/DATABASE?schema=public
```

Não coloque credencial real em exemplos versionados.

## Prisma

Antes de deploy:

```bash
npx prisma -v
npx prisma validate
npx prisma migrate status
```

Em produção, a estratégia típica de migrations deve usar o fluxo de deploy já aprovado pelo projeto.

Nunca em produção sem autorização explícita:

```bash
npx prisma migrate reset
npx prisma db push --force-reset
```

## Migration

Antes de uma migration relevante:

1. revisar SQL gerado quando aplicável;
2. identificar locks e operações destrutivas;
3. fazer backup;
4. confirmar janela de implantação;
5. aplicar migration;
6. validar schema;
7. executar smoke test.

## Backup lógico

Exemplo conceitual:

```bash
pg_dump --format=custom --file=<backup-file> <database>
```

A forma de autenticação e destino devem seguir a política real.

Valide backups periodicamente. Backup não testado não deve ser tratado como recuperação garantida.

## Diagnóstico

```bash
pg_isready
sudo -u postgres psql
systemctl status postgresql
journalctl -u postgresql --since "30 minutes ago"
```

No Prisma:

```bash
npx prisma migrate status
npx prisma validate
```

Diferencie:

- PostgreSQL indisponível;
- credencial inválida;
- DNS/host incorreto;
- schema divergente;
- migration pendente;
- pool/conexões esgotadas.
