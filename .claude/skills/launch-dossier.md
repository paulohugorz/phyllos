# Skill: Launch Dossier

Use esta skill para verificar se um produto ou coleção está pronto para lançamento. É o gate final antes do go-live — nenhum produto entra no mercado sem passar por esta checklist.

**Quem usa:** product-dev-lead, launch-coordinator, brand-director, product-director

---

## Checklist de aprovação — os 6 gates

### Gate 1 — Produto físico
- [ ] Modelagem aprovada pelo fit-technical-designer
- [ ] Gradação de tamanhos completa e documentada
- [ ] Proto final aprovado pelo design-lead
- [ ] Composição do tecido verificada (ficha do fornecedor)

### Gate 2 — Materiais e certificações
- [ ] Certificações vigentes (GOTS, GRS, OEKO-TEX — com número e validade)
- [ ] Procedência documentada (origem → confecção → produto acabado)
- [ ] Fornecedores auditados pelo sourcing-agent
- [ ] Nenhum fornecedor sem rastreabilidade aprovada

### Gate 3 — Claims técnicos
- [ ] Todos os claims passaram pela skill claim-validation
- [ ] Laudos de laboratório em arquivo (UPF, compressão, secagem, etc.)
- [ ] Nenhum claim genérico sem evidência
- [ ] Limitações documentadas na ficha técnica

### Gate 4 — Testes internos
- [ ] Protocolo de teste executado pelo product-testing-agent
- [ ] Mínimo de ciclos de uso validados (6 meses internamente ou equivalente)
- [ ] Resultados de durabilidade documentados
- [ ] Defeitos encontrados foram corrigidos e retestados

### Gate 5 — Comunicação e marca
- [ ] Copy passou pelo content-voice-review
- [ ] Claims ambientais passaram pelo anti-greenwashing-check
- [ ] Brand Director aprovou comunicação pública
- [ ] Ficha técnica de produto pronta para e-commerce e atendimento

### Gate 6 — Operações e tecnologia
- [ ] SKU cadastrado no sistema
- [ ] Estoque inicial definido pelo inventory-agent
- [ ] E-commerce configurado (foto, descrição, tamanhos, preço)
- [ ] Fluxo de pós-compra testado (confirmação, rastreio, troca)
- [ ] Support agent briefado sobre o produto

## Formato de saída

```
Produto: [nome]
Data de avaliação: [data]

Status geral: APROVADO / BLOQUEADO

Gates aprovados: [lista]
Gates bloqueados: [lista com motivo e responsável]

Decisão recomendada: lançar / aguardar [prazo estimado]
```

## Regra final

Um produto bloqueado em qualquer gate não lança. O custo de lançar errado (recalls, greenwashing, claims falsos, fitting ruim) é sempre maior do que o custo de atrasar.
