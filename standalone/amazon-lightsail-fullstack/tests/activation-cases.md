# Skill Tests — Router Evaluation Cases

## Objetivo

Definir casos representativos para avaliar a ativação real da skill no host.

A fonte normativa é `../references/activation-policy.md`.

## Importante

Não existe classificador local para imitar o roteador semântico do host.

`router-eval-cases.json` é um dataset para evaluation harness real.

O script `../scripts/validate_skill_contract.py` valida apenas consistência interna do pacote.

## Cobertura

Inclui casos positivos de Lightsail e Ubuntu + stack aprovada, e negativos de Ubuntu genérico, outras stacks, desenvolvimento isolado e AWS fora de Lightsail.

## Critério de aprovação

A ativação real só pode ser considerada validada quando esses casos forem executados no host alvo.
