# Troubleshooting

## Regra principal

Localize a camada da falha antes de corrigir.

Fluxo:

```text
Cliente
  |
DNS
  |
Lightsail Firewall
  |
Nginx
  |
Aplicação
  |
Prisma
  |
PostgreSQL
```

## Site não responde

1. DNS:

```bash
dig A <domain>
```

2. Nginx:

```bash
sudo nginx -t
systemctl status nginx
curl -v http://127.0.0.1
```

3. Portas:

```bash
ss -lntup
```

4. Aplicações:

```bash
systemctl status <frontend-service>
systemctl status <backend-service>
```

## 502 Bad Gateway

Verifique primeiro o upstream:

```bash
curl -v http://127.0.0.1:<port>
ss -lntp | grep <port>
journalctl -u <service> --since "30 minutes ago"
```

Somente depois revise a configuração Nginx.

## 504 Gateway Timeout

Investigue:

- aplicação bloqueada;
- consulta lenta;
- dependência externa;
- timeout inadequado;
- pressão de CPU/RAM;
- banco lento.

Não aumente timeout como primeira correção.

## Processo reiniciando

```bash
systemctl status <service>
journalctl -u <service> -n 200 --no-pager
```

Procure:

- variável ausente;
- porta ocupada;
- permissão;
- arquivo ausente;
- incompatibilidade Node;
- build incorreto;
- conexão ao banco.

## OOM / memória

```bash
free -h
dmesg -T | grep -i -E 'oom|killed process'
journalctl -k --since "1 hour ago"
```

Se o kernel matou Node/PostgreSQL, trate dimensionamento ou consumo antes de reiniciar repetidamente.

## Disco cheio

```bash
df -h
df -i
du -xh /var/log | sort -h | tail
journalctl --disk-usage
```

Não apague arquivos de banco manualmente.

## PostgreSQL

```bash
pg_isready
systemctl status postgresql
journalctl -u postgresql --since "30 minutes ago"
```

## Prisma

```bash
npx prisma -v
npx prisma validate
npx prisma migrate status
```

## TLS

```bash
curl -Iv https://<domain>
openssl s_client -connect <domain>:443 -servername <domain>
```

Cheque DNS antes de reemitir certificado.

## Regra de encerramento

Depois da correção, registre:

- causa raiz;
- evidência;
- mudança realizada;
- validação;
- rollback disponível;
- prevenção.
