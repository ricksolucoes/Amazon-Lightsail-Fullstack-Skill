# Deploy nativo — Next.js 16.3.x + NestJS 12.1.x

## Princípio

Sem Docker.

Fluxo esperado:

Consulte `deployment-sequence.md`. A sequência normativa é:

```text
preflight
-> backup/snapshot quando aplicável
-> atualização do código
-> install dependencies
-> test
-> build
-> validar migrations
-> backup do banco quando necessário
-> migration
-> restart systemd
-> teste localhost
-> Nginx
-> health check
-> logs
-> auditoria
```

## Node.js

Não fixe uma versão arbitrária dentro da skill.

Antes do provisionamento, confira os requisitos oficiais simultaneamente para:

- Next.js 16.3.x;
- NestJS 12.1.x;
- Prisma 7.10.x.

Escolha uma versão Node suportada pelos três.

Registre a versão no projeto para tornar builds reproduzíveis.

## Dependências

Use o package manager já definido pelo repositório.

Nunca misture npm, pnpm, yarn ou bun sem solicitação.

Preserve o lockfile.

Para npm, quando apropriado:

```bash
npm ci
```

## Next.js

Fluxo conceitual:

```bash
npm ci
npm run build
npm run start
```

Não assuma porta. Descubra no projeto/configuração.

Em produção, deixe Nginx falar com Next.js via loopback.

## NestJS

Fluxo conceitual:

```bash
npm ci
npm run build
node dist/main.js
```

O comando real deve ser obtido do `package.json`.

Não invente layout do `dist`.

## systemd

Exemplo conceitual:

```ini
[Unit]
Description=Application Backend
After=network.target postgresql.service

[Service]
Type=simple
User=<deploy-user>
WorkingDirectory=<backend-directory>
EnvironmentFile=<backend-env-file>
ExecStart=<node-path> <entrypoint>
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Substitua placeholders apenas por valores confirmados.

Após criar/modificar:

```bash
sudo systemctl daemon-reload
sudo systemctl enable <service>
sudo systemctl restart <service>
sudo systemctl status <service>
```

## Nginx

Padrão:

- TLS termina no Nginx;
- Nginx encaminha para serviços em `127.0.0.1`;
- preserve headers relevantes;
- configure limites/timeouts somente quando houver necessidade.

Sempre validar:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

## Segredos

Produção:

- não versionar `.env`;
- segredos com permissão restrita;
- JWT access secret e refresh secret devem ser distintos quando o projeto assim define;
- nunca imprimir segredos em logs;
- nunca colar segredo real na documentação da skill.

## Deploy seguro

Antes:

```text
[ ] working tree/revisão confirmada
[ ] backup quando necessário
[ ] migrations revisadas
[ ] espaço em disco
[ ] memória disponível
```

Depois:

```text
[ ] systemd active
[ ] localhost frontend responde
[ ] localhost API responde
[ ] Nginx responde
[ ] health endpoint responde
[ ] logs sem erro novo
```

## Rollback

Rollback deve considerar separadamente:

- código;
- dependências;
- build;
- migration de banco.

Reverter Git não desfaz automaticamente uma migration incompatível.
