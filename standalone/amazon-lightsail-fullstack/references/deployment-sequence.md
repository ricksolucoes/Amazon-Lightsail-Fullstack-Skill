# Deployment Sequence — Fonte Normativa

## Autoridade

Este arquivo define a ordem normativa de deploy para produção.

Se qualquer outro arquivo da skill apresentar ordem diferente, este arquivo prevalece.

## Sequência padrão

```text
1. Preflight e estado atual
2. Backup/snapshot quando aplicável
3. Atualização controlada do código
4. Instalação reproduzível de dependências
5. Testes automatizados pertinentes
6. Build do frontend e backend
7. Validação de configuração e variáveis de ambiente
8. Validação do banco e estado das migrations
9. Backup lógico do PostgreSQL quando a migration tiver risco relevante
10. Aplicação de migrations de produção
11. Restart controlado dos serviços systemd
12. Teste local dos serviços
13. Validação do Nginx
14. Validação HTTP/HTTPS
15. Health checks
16. Smoke tests
17. Verificação de logs
18. Reboot controlado quando fizer parte da mudança
19. Auditoria final
```

## Regra para migrations

A migration deve ocorrer **depois do build e antes do restart dos serviços que dependem do novo schema**, salvo quando a estratégia de compatibilidade do projeto exigir uma implantação em múltiplas fases.

Fluxo padrão:

```text
build
-> validate migration status
-> backup quando necessário
-> prisma migrate deploy
-> restart systemd
-> health check
```

## Exceção: migration em múltiplas fases

Se uma alteração de schema exigir compatibilidade temporária entre versão antiga e nova da aplicação:

1. classifique a mudança como expand/contract;
2. aplique primeiro apenas mudanças retrocompatíveis;
3. publique a aplicação;
4. valide;
5. remova estruturas antigas somente em implantação posterior.

Não use esse fluxo por padrão. Aplique apenas quando o schema e o código realmente exigirem.

## Proibições em produção

Nunca executar por padrão:

```bash
npx prisma migrate reset
npx prisma db push --force-reset
```

## Falha de migration

Se a migration falhar:

1. não reinicie serviços para a nova versão;
2. preserve logs;
3. verifique estado com `npx prisma migrate status`;
4. avalie impacto parcial;
5. restaure somente com plano de recuperação validado;
6. não improvise reversão destrutiva.

## Rollback

Rollback de código e rollback de banco são problemas distintos.

Nunca trate `git checkout <versão-anterior>` como rollback suficiente quando o schema já foi alterado.

## Regra final

A skill deve apresentar uma única sequência normativa.

Arquivos auxiliares podem detalhar etapas, mas não redefinir a ordem.
