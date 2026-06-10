# Skill: LGPD Review

Use esta skill para revisar qualquer sistema, fluxo, formulário, integração ou comunicação que colete, processe ou armazene dados pessoais de clientes.

**Quem usa:** technology-director, data-intelligence-lead, devops-security-agent, integration-agent, ecommerce-agent

---

## Verificações obrigatórias

### Coleta
1. Existe base legal definida para coleta de cada dado (consentimento, contrato, legítimo interesse)?
2. O formulário tem linguagem clara sobre o que está sendo coletado e para quê?
3. O consentimento é granular (marketing ≠ operacional)?
4. Dados sensíveis (saúde, biometria, origem racial) têm tratamento diferenciado?

### Armazenamento
5. Os dados são armazenados apenas pelo tempo necessário?
6. Existe política de retenção documentada?
7. Os dados estão criptografados em repouso e em trânsito?
8. Quem tem acesso está documentado (princípio do menor privilégio)?

### Terceiros
9. Os fornecedores e plataformas que recebem dados têm DPA (Data Processing Agreement)?
10. Transferência internacional de dados está coberta (cláusulas contratuais padrão)?

### Direitos do titular
11. Existe canal funcional para solicitações de acesso, correção, exclusão e portabilidade?
12. O prazo de resposta (15 dias úteis pela LGPD) está coberto operacionalmente?

## Formato de saída

```
Status: conforme / conforme com ressalvas / não conforme

Pontos críticos:
- [item] → risco: [descrição] → ação necessária: [o que fazer]

Prazo sugerido para adequação: [urgente / próximo sprint / próximo trimestre]
```

## Escalonamento

- Não conformidade crítica → bloquear deploy, acionar technology-director
- Dúvida jurídica → registrar como dependência de consultoria jurídica especializada
