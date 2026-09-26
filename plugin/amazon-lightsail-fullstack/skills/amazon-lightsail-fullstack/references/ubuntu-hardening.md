# Ubuntu Server — preparação e hardening

## Atualização inicial

Inspecione versão e pacotes antes de alterar:

```bash
lsb_release -a
uname -a
apt list --upgradable
```

Aplique atualizações de forma controlada.

## Usuário operacional

Prefira um usuário dedicado para deploy/aplicação.

Não execute Next.js ou NestJS como root.

Diretórios de aplicação devem pertencer ao usuário operacional e ao grupo apropriado.

## SSH

Preferências:

- autenticação por chave;
- chave privada protegida no cliente;
- restringir origem no firewall Lightsail quando possível;
- desabilitar métodos inseguros somente depois de validar o acesso alternativo.

Nunca faça mudanças de SSH sem manter uma sessão de recuperação aberta.

## UFW

Se usar UFW além do firewall do Lightsail:

1. autorize SSH antes de habilitar;
2. autorize HTTP/HTTPS;
3. confira regras;
4. habilite;
5. teste nova conexão.

Exemplo, apenas depois de confirmar a política:

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw status verbose
```

Não exponha PostgreSQL via UFW por padrão.

## Diretórios

Exemplo conceitual:

```text
/var/www/app/
  frontend/
  backend/

/etc/app/
  frontend.env
  backend.env
```

A estrutura real deve refletir o projeto.

Proteja arquivos `.env`:

```bash
chmod 600 /etc/app/backend.env
```

Ajuste owner/group conforme o usuário de serviço.

## Atualizações automáticas

Avalie `unattended-upgrades` para patches de segurança.

Não habilite mudanças automáticas de major version para componentes críticos sem estratégia de teste.

## Timezone

Confirme:

```bash
timedatectl
```

A aplicação deve preferir UTC internamente quando apropriado, sem alterar requisitos de negócio.

## Swap

Não crie swap automaticamente.

Primeiro confirme:

```bash
free -h
swapon --show
```

Swap pode ajudar em instâncias pequenas durante build, mas não corrige dimensionamento insuficiente.
