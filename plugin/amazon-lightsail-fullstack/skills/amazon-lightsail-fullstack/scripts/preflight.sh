#!/usr/bin/env bash
set -u

section() {
  printf '\n==== %s ====\n' "$1"
}

run() {
  printf '$ %s\n' "$*"
  "$@" 2>&1 || true
}

section "System"
run uname -a
command -v lsb_release >/dev/null 2>&1 && run lsb_release -a
run uname -m
run uptime

section "Resources"
run free -h
run df -h
run df -i
run lsblk

section "Network"
run ip -brief address
run ss -lntup

section "Services"
run systemctl --failed
for svc in nginx postgresql; do
  if systemctl list-unit-files "${svc}.service" >/dev/null 2>&1; then
    run systemctl status "${svc}" --no-pager
  fi
done

section "Toolchain"
for cmd in node npm pnpm yarn git nginx psql npx; do
  if command -v "$cmd" >/dev/null 2>&1; then
    case "$cmd" in
      nginx) run nginx -v ;;
      psql) run psql --version ;;
      *) run "$cmd" --version ;;
    esac
  else
    printf '%s: not installed or not in PATH\n' "$cmd"
  fi
done

section "Firewall"
if command -v ufw >/dev/null 2>&1; then
  if [ "$(id -u)" -eq 0 ]; then
    run ufw status verbose
  elif command -v sudo >/dev/null 2>&1 && sudo -n true 2>/dev/null; then
    run sudo -n ufw status verbose
  else
    echo "ufw: status requires elevated privileges; skipped to keep preflight non-interactive"
  fi
else
  echo "ufw: not installed"
fi

section "Listening PostgreSQL"
run sh -c "ss -lntp 2>/dev/null | grep ':5432' || true"

section "Listening Node-like ports"
run sh -c "ss -lntp 2>/dev/null | grep -E 'node|:3000|:3001|:4000|:8000|:8080' || true"

echo
echo "Preflight completed. This script performs inspection only and does not intentionally modify system state."
