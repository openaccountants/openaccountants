---
name: portugal-tax-optimization
description: "Utilize esta skill ao aconselhar sobre estratégias LEGAIS de minimização fiscal para contribuintes portugueses — particulares, trabalhadores independentes (recibos verdes) e pequenos empresários. Acione com expressões como \"reduzir o meu imposto Portugal\", \"planeamento fiscal\", \"regime simplificado\", \"contabilidade organizada\", \"optimização do IRS\", \"segurança social trabalhador independente\", \"IVA\", \"recibos verdes\", \"Categoria B\", \"deduções Portugal\", ou qualquer questão sobre minimização legal do IRS ou IRC português. Cobre selecção de entidade, regime simplificado vs contabilidade organizada, estratégias de dedução, amortizações, utilização de prejuízos, timing, optimização do IVA, segurança social e linhas vermelhas. LEIA SEMPRE esta skill antes de prestar aconselhamento de optimização fiscal portuguesa. Trigger also on: \"reduce my tax Portugal\", \"tax planning\", \"regime simplificado\", \"organized accounts\", \"IRS optimization\", \"social security self-employed\", \"IVA\", \"recibos verdes\", \"Category B\", \"deductions Portugal\"."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mário Jorge da costa Vale
review_status: current
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Tax Optimization

## Portugal — Optimização Fiscal — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mário Jorge da costa Vale** on 2026-06-04.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Otimização Fiscal

- **Despesas gerais familiares** — 35% com NIF, máx €250/contribuinte  _(CIRS)_
- **Saúde** — 15% das despesas, máx €1.000  _(CIRS)_
- **Educação** — 30% das despesas, máx €800  _(CIRS)_
- **Habitação (renda)** — 15%, máx €502  _(CIRS)_
- **Habitação (juros)** — 15%, máx €296  _(CIRS)_
- **Lares** — 25%, máx €403,75  _(CIRS)_
- **IVA/fatura** — 15% do IVA (restauração, cabeleireiros, etc.), máx €250  _(CIRS)_
- **Edifícios comerciais** — Edifícios comerciais - 2% ; Edifícios industriais - 5%  _(DR 25/2009)_
- **Mobiliário de escritório** — 12,5%  _(Decreto Regulamentar n.º 25/2009)_
- **Equipamento informático** — 33,33%  _(Decreto Regulamentar n.º 25/2009)_
- **Software** — 33,33%  _(Decreto Regulamentar n.º 25/2009)_
- **Viaturas ligeiras de passageiros** — 25%  _(Decreto Regulamentar n.º 25/2009)_
- **PPR — dedução IRS** — 20% das contribuições (limite por idade)  _(CIRS)_
- **Juros depósitos** — 28% taxa autónoma (ou englobamento)  _(CIRS)_
- **Dividendos (englobamento)** — 50% incluído no rendimento (efetivo máx 24%)  _(CIRS)_
- **Mais-valias mobiliárias** — 28% taxa autónoma; perdas compensáveis 5 anos  _(CIRS)_
- **Mais-valias imobiliárias** — 50% do ganho incluído no rendimento; reinvestimento HPP 36 meses  _(CIRS Art. 10.º n.º 5)_
- **Rendas (Cat. F)** — taxa autónoma 25% para habitação própria e permanente e 28% outros casos, ou englobamento  _(CIRS artº 72º)_

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Ano fiscal | Ano civil (1 de Janeiro – 31 de Dezembro) |
| Legislação primária | Código do IRS (CIRS); Código do IRC; Código do IVA; Código Contributivo da Segurança Social |
| Anti-abuso | CGAA: Cláusula Geral Anti-Abuso (Art 38.º, n.º 2 da Lei Geral Tributária, LGT) |
| Autoridade fiscal | Autoridade Tributária e Aduaneira (AT) |
| Prazo de entrega | 1 de Abril – 30 de Junho do ano seguinte (Modelo 3 IRS) |
| Taxa marginal máxima (pessoas singulares) | 48% + taxa adicional de solidariedade de 5% (acima de €250.000) = até 53% |
| Taxa de IRC (sociedades) | 21% taxa normal; 17% sobre os primeiros €50.000 para PMEs |
| Taxa normal de IVA | 23% (continente); 22% Madeira; 16% Açores |
| Segurança social (trabalhador independente) | 21,4% sobre a base calculada |

### Escalões de IRS (2026)

**Escalões de IRS (2026)**

| Escalão | Rendimento Tributável (€) | Taxa Marginal | Parcela a Abater |
| --- | --- | --- | --- |
| 1 | 0 – 8.342 | 12,5% | €0 |
| 2 | 8.342 – 12.587 | 15,7% | €266,94 |
| 3 | 12.587 – 17.838 | 21,2% | €959,23 |
| 4 | 17.838 – 23.089 | 24,1% | €1.476,53 |
| 5 | 23.089 – 29.397 | 31,1% | €3.092,76 |
| 6 | 29.397 – 43.090 | 34,9% | €4.209,85 |
| 7 | 43.090 – 46.566 | 43,1% | €7.743,23 |
| 8 | 46.566 – 86.634 | 44,6% | €8.441,72 |
| 9 | Acima de 86.634 | 48,0% | €11.387,28 |

- **Taxa adicional de solidariedade** — 2,5% sobre rendimento tributável entre €80.000 e €250.000; 5% acima de €250.000  _(Art 68.º-A CIRS)_
- **Mínimo de Existência (2026)** — €12.880 — garante que o rendimento líquido após imposto de nenhum contribuinte cai abaixo deste limiar

## Secção 2 — Repartição de Rendimentos e Estruturação

### Empresário em Nome Individual (ENI) vs Sociedade (Lda)

- **Regime simplificado** — rendimentos brutos ≤€200.000. Rendimento tributável = bruto × coeficiente (ex.: 0,75 para serviços profissionais listados no Art 151.º CIRS; 0,35 para outros serviços; 0,15 para venda de bens). Não pode deduzir despesas adicionais para além do coeficiente — é um pacote fechado. Tem de justificar 15% do bruto como despesas profissionais (facturas com NIF).  _(Art 151.º CIRS)_
- **Contabilidade organizada** — obrigatória se rendimentos brutos >€200.000, opcional abaixo. Deduz despesas profissionais reais. Requer contabilista certificado (CC). Mais vantajosa quando as despesas reais excedem significativamente a dedução implícita no coeficiente.
- **Sociedade (Sociedade Unipessoal por Quotas, Lda, ou SA)** — IRC a 21% (17% sobre os primeiros €50.000 para PMEs). Lucros distribuídos como dividendos tributados a 28% (taxa liberatória) ou incluídos no IRS por englobamento a taxas progressivas (exclusão de 50% para sócios residentes — tributação por englobamento). Carga administrativa superior.
- **Regra de decisão (quadro de comparação de regimes)** — Cat B simplificado: óptimo para freelancers com baixas despesas reais (o coeficiente já implica 25%+ de despesas automaticamente). Cat B organizada: mudar quando as despesas documentadas excedam a margem implícita do coeficiente. Lda (Sociedade): ponderar incorporação quando o lucro consistentemente excede ~€60.000–€80.000, pesando os custos adicionais de contabilidade, derrama, tributações autónomas e formalismos societários.

### Tributação Conjunta

Casais casados ou unidos de facto podem optar pela tributação conjunta. O rendimento tributável é dividido por dois, o imposto calculado sobre metade, e depois duplicado. Vantajosa quando os rendimentos são significativamente desiguais — puxa o cônjuge com rendimento mais elevado para um escalão inferior.

### RNH / IFICI

Para optimização sob RNH/IFICI ver skill pt-nhr-ifici.

## Secção 3 — Deduções que a Maioria Esquece (Optimização equivalente a PTKP)

### Deduções à Colecta — Art 78.º CIRS

**Deduções à Colecta — Art 78.º CIRS**  _(Art 78.º CIRS)_

| Categoria | Dedução | Limite |
| --- | --- | --- |
| Despesas gerais familiares | 35% das despesas com NIF | €250/contribuinte (€500 casal) |
| Saúde | 15% das despesas de saúde (IVA 6% ou isento) | €1.000 |
| Educação | 30% das despesas de educação | €800 |
| Habitação | 15% de rendas ou juros de empréstimo | €502 (renda) / €296 (juros) |
| Lares | 25% das despesas | €403,75 |
| Pensão de alimentos | 20% dos pagamentos fixados judicialmente | Sem limite |
| IVA em facturas (e-fatura) | 15% do IVA em restaurantes, cabeleireiros, oficinas auto, veterinários, ginásios, etc. | €250 (via e-fatura) |
| Donativos | Vários | Até 15% da colecta |

### Deduções Específicas da Categoria B (Contabilidade Organizada)

- **Deduções Específicas da Categoria B** — Em contabilidade organizada, deduzem-se despesas profissionais reais: renda de escritório, equipamento, serviços profissionais, deslocações, formação, telecomunicações, seguros e amortizações. Sujeito ao princípio da indispensabilidade.

### Regime Simplificado — Regra de Justificação dos 15%

- **Regra de Justificação dos 15%** — Para coeficientes 0,75 e 0,35, tem de justificar despesas equivalentes a 15% dos rendimentos brutos. Se não totalmente justificadas, o défice é acrescido ao rendimento tributável. Fontes de justificação: Dedução específica: €4.587,09 aplicada automaticamente (ou total das contribuições para segurança social, se superior, até 10% do bruto); Facturas profissionais com o seu NIF (utilities, telecomunicações, serviços profissionais, deslocações, etc.); IMI e juros de empréstimo sobre imóvel afecto à actividade.

peça sempre NIF em todas as compras profissionais. A diferença entre €4.587,09 e 15% do bruto é o valor que deve evidenciar por facturas.

## Secção 4 — Optimização de Amortizações

### Amortizações — Contabilidade Organizada

**Amortizações — Contabilidade Organizada**  _(Decreto Regulamentar n.º 25/2009)_

| Categoria de Activo | Taxa |
| --- | --- |
| Edifícios (comerciais) | 2%–5% |
| Mobiliário de escritório | 12,5% |
| Equipamento informático | 33,33% |
| Software | 33,33% |
| Viaturas ligeiras de passageiros | 25% |
| Equipamento básico | 10%–20% |

- **Limite amortização viaturas** — A amortização de viaturas está limitada a viaturas com custo ≤€62.500 (eléctricas) ou ≤€37.500 (outras). O excesso de custo é não amortizável.

### Regime Simplificado

- **Regime Simplificado** — Não há amortizações autónomas — o coeficiente subsume todas as despesas. A aquisição de activos não gera deduções adicionais.

### Reinvestimento de Mais-Valias (IRC — Sociedades)

- **Reinvestimento de Mais-Valias (IRC)** — Reinvestimento de mais-valias de activos fixos em novos activos elegíveis dentro do prazo de reinvestimento: exclusão de 50% da mais-valia. Oportunidade de planeamento na alienação de instalações ou equipamento.  _(Art 48.º CIRC)_

## Secção 5 — Utilização de Prejuízos

### Prejuízos da Categoria B (Trabalhadores Independentes)

- **Prejuízos da Categoria B** — Em contabilidade organizada, os prejuízos da Categoria B podem compensar outros rendimentos da Categoria B no mesmo ano e reportar-se por 12 anos. Os prejuízos no regime simplificado NÃO são gerados — a metodologia do coeficiente produz sempre rendimento tributável positivo.  _(Art 55.º CIRS)_
- **Restrição-chave** — os prejuízos da Categoria B não podem compensar outras categorias de rendimento (Categoria A trabalho dependente, Categoria E rendimentos de capitais, etc.) — apenas outros rendimentos da Categoria B.

### IRC (Sociedades)

- **IRC (Sociedades) — Prejuízos** — Os prejuízos fiscais reportam-se por 12 anos. Podem compensar até 65% do lucro tributável em cada ano subsequente. Sujeito à manutenção de >50% de continuidade na titularidade.  _(Art 52.º CIRC)_

### Menos-Valias (Categoria G)

- **Menos-Valias (Categoria G)** — As menos-valias mobiliárias reportam-se por 5 anos, apenas contra mais-valias. As menos-valias imobiliárias compensam mais-valias imobiliárias.  _(Art 55.º, n.º 5 CIRS)_

## Secção 6 — Estratégias de Timing

**Estratégias de Timing**

| Estratégia | Detalhe |
| --- | --- |
| Pagamentos por conta de IRS | Trabalhadores independentes com IRS do ano anterior >€301 devem efectuar 3 pagamentos por conta (Julho, Setembro, Dezembro). Se o rendimento descer, solicitar redução (Art 107.º CIRS) |
| Diferir facturação para Janeiro | Em regime simplificado e próximo do limiar de €200.000, o timing é decisivo. Também desloca rendimento para o ano fiscal seguinte |
| Antecipar despesas antes do fim do ano | Em contabilidade organizada: adquirir equipamento, pré-pagar serviços, regularizar facturas em aberto antes de 31 de Dezembro |
| Validação e-fatura | Confirmar que todas as facturas com NIF estão validadas no Portal das Finanças até meados de Fevereiro (prazo para correcções). Maximiza a dedução de IVA e despesas gerais |
| Tributação conjunta vs separada | Simular ambos os cenários anualmente. Especialmente vantajoso quando um dos cônjuges não tem rendimento ou tem rendimento baixo |
| Actualização da base contributiva | Declaração trimestral actualiza a base contributiva. Se o rendimento descer, declarar prontamente para reduzir os pagamentos trimestrais à SS |
| Diferimento de mais-valias | Reinvestir o produto da venda em nova habitação própria permanente no prazo de 36 meses (Art 10.º, n.º 5 CIRS) para excluir a mais-valia |

## Secção 7 — Optimização do IVA

**Optimização do IVA**

| Tópico | Detalhe |
| --- | --- |
| Limiar de isenção | Volume de negócios ≤€14.500 (2026): isento de IVA ao abrigo do Art 53.º CIVA. Não liquida IVA, não tem direito a dedução. Rever anualmente, dado que o limiar pode mudar |
| Registo acima do limiar | Registo obrigatório e declarações periódicas trimestrais de IVA. Pode recuperar IVA em aquisições profissionais |
| Regime simplificado de IVA | Não existe regime simplificado autónomo para além da isenção do Art 53.º. Pequenas empresas aplicam o regime normal acima do limiar |
| Taxas | 23% normal (continente); 13% intermédia; 6% reduzida. Açores: 16%/9%/4%. Madeira: 22%/12%/5% |
| Planeamento da dedução do IVA | Em contabilidade organizada, deduzir totalmente o IVA em despesas profissionais. Bens de uso misto: método pro rata (pro rata de dedução) |
| IVA em serviços transfronteiriços | Serviços B2B intra-UE: aplica-se a regra de inversão do sujeito passivo (Art 6.º, n.º 6 a) CIVA). Não liquida IVA português; o cliente autoliquida no seu país. Registar no VIES |
| Declaração recapitulativa | Declaração trimestral de operações intracomunitárias quando há prestações de serviços intra-UE |

## Secção 8 — Optimização da Segurança Social

### Contribuições dos Trabalhadores Independentes

- **Taxa** — 21,4% sobre o rendimento relevante
- **Cálculo do rendimento relevante** — trimestral, com base nos rendimentos brutos do trimestre anterior × coeficiente (tipicamente 70% para serviços, 20% para venda de bens)
- **Limite máximo anual** — 12 × IAS (Indexante dos Apoios Sociais). IAS 2026 = €522,50 → limite ~€75.240/ano
- **Pagamentos trimestrais** — Janeiro, Abril, Julho, Outubro

### Isenções e Reduções

**Isenções e Reduções**

| Situação | Tratamento |
| --- | --- |
| Primeiros 12 meses de actividade | Isenção total (apenas para primeira inscrição como trabalhador independente) |
| Meses 13–24 | Redução de 50% |
| Acumulação trabalho dependente + independente | Se for trabalhador por conta de outrem com descontos para SS e o rendimento do trabalho independente for <4× IAS (~€2.090/mês), pode estar dispensado de contribuições como independente |
| Cônjuge do empresário | Se genuinamente trabalha no negócio, pode ser registado como trabalhador por conta de outrem com contribuições do empregador |

### Estratégias de Optimização

- **Rendimento inicial baixo** — aproveitar a isenção de 12 meses + redução de 50% nos 12 meses seguintes = 2 anos de SS reduzida
- **Acumulação trabalho dependente + freelance** — manter contrato de trabalho para potencialmente isentar o rendimento freelance de contribuições à SS
- **Contribuições voluntárias superiores** — geralmente não vantajosas — os benefícios (pensão) são modestos face ao custo adicional. Focar em poupança privada para reforma (PPR)
- **PPR (Plano Poupança Reforma)** — investimento em plano aprovado → dedução à colecta de 20% das contribuições, com limite de €400 (até 35 anos), €350 (35–50 anos), €300 (50+). Por contribuinte.

## Secção 9 — Investimento e Reforma

**Investimento e Reforma**

| Instrumento | Tratamento Fiscal |
| --- | --- |
| PPR (Plano Poupança Reforma) | Dedução à colecta de IRS de 20% das contribuições (limite dependente da idade). Penalização de levantamento antecipado fora dos eventos qualificantes. Mais-valias tributadas a 8% (após 8+ anos) |
| Juros de depósitos | Taxa liberatória de 28% ou opção pelo englobamento (taxas progressivas). Englobamento vantajoso se a taxa marginal for <28% |
| Dividendos (sociedades portuguesas) | Taxa liberatória de 28%. Se optar por englobamento, apenas 50% incluídos no rendimento tributável (efectivo máximo de 24%) |
| Mais-valias — valores mobiliários | Taxa liberatória de 28% sobre o saldo. Englobamento opcional. Menos-valias compensam mais-valias do mesmo ano e reportam-se por 5 anos |
| Mais-valias — imóveis | 50% do saldo incluído no rendimento tributável (taxas progressivas). Exclusão por reinvestimento em habitação própria permanente em 36 meses (Art 10.º, n.º 5 CIRS) |
| Rendimentos prediais (Categoria F) | Taxa liberatória de 28% ou englobamento. Despesas dedutíveis: IMI, condomínio, seguros, manutenção, gestão. Amortização de 2% para edifícios |
| Criptoactivos | 28% sobre mais-valias de criptoactivos detidos <365 dias. Isentas se detidos ≥365 dias (Art 10.º, n.º 17 CIRS) |

### Estratégia de Englobamento

- **Estratégia de Englobamento** — Optar pelo englobamento (inclusão nos escalões progressivos do IRS) pode reduzir o imposto sobre rendimentos de capitais se a sua taxa marginal for inferior a 28%. Contudo, o englobamento é tudo-ou-nada por categoria — não pode escolher rubricas individuais. Modelar cuidadosamente antes de optar.

### Reinvestimento em Habitação Própria Permanente

- **Reinvestimento em Habitação Própria Permanente** — A mais-valia líquida da venda da habitação própria permanente é excluída de tributação se o produto for reinvestido em nova habitação própria permanente (UE/EEE) no prazo de 36 meses após a venda ou 24 meses antes. Reinvestimento parcial → exclusão parcial.

## Secção 10 — Linhas Vermelhas (CGAA e Riscos de Inspecção)

### CGAA (Cláusula Geral Anti-Abuso)

- **CGAA** — A AT pode desconsiderar ou requalificar operações que sejam artificiais, sem substância económica e essencialmente motivadas por evasão fiscal. Requer parecer prévio do Centro de Estudos Fiscais.  _(Art 38.º, n.º 2 da Lei Geral Tributária (LGT))_

### Gatilhos de Inspecção da AT

**Gatilhos de Inspecção da AT**

| Gatilho | Risco |
| --- | --- |
| Inconsistência entre rendimento declarado e e-fatura | A AT cruza facturas emitidas com rendimento declarado. Sinalização automática |
| Regime simplificado com rendimento próximo de €200.000 | A AT verifica fragmentação de rendimento por vários NIFs/actividades |
| Falha na justificação dos 15% de despesas (regime simplificado) | Défice automaticamente acrescido ao rendimento tributável |
| Dupla actividade — serviços não declarados | A AT monitoriza depósitos bancários vs receitas declaradas |
| Falsos recibos verdes (relação laboral dependente disfarçada de freelance) | Empregador é multado; trabalhador é reclassificado. ACT e AT articulam |
| Transmissões imobiliárias abaixo do VPT (Valor Patrimonial Tributário) | A AT aplica o maior entre preço de venda e VPT para mais-valias e IMT |
| Estruturas offshore sem substância | Regras CFC (Art 66.º CIRC) e obrigações declarativas |
| Fuga a contribuições à Segurança Social | A Segurança Social cruza dados com a AT. Coimas + contribuições em atraso |
| Pedidos de reembolso de IVA de montante elevado | Revisão manual e inspecção |

### Proibições Absolutas

- **Proibições Absolutas** — NUNCA aconselhar emissão de recibos verdes para trabalho que constitua relação laboral dependente; NUNCA aconselhar omissão de rendimento quando as facturas são rastreadas via e-fatura; NUNCA aconselhar declarar transmissões imobiliárias abaixo do VPT; NUNCA aconselhar fragmentação artificial de rendimento para se manter abaixo do limiar de €200.000 do regime simplificado; NUNCA aconselhar a não inscrição em IVA quando acima do limiar de isenção; NUNCA aconselhar evitar a inscrição na Segurança Social quando legalmente exigida.

## Secção 11 — Calendário Anual de Planeamento Fiscal

**Calendário Anual de Planeamento Fiscal**

| Quando | Acção |
| --- | --- |
| Janeiro | Contribuição trimestral à SS. Primeira oportunidade de pagamento por conta de IRS. Rever e-fatura do ano anterior — iniciar correcções |
| Fevereiro | Prazo de validação no e-fatura (tipicamente meados de Fevereiro). Garantir que todas as facturas com NIF estão correctamente categorizadas |
| Março | Prazo para comunicar a composição do agregado familiar à AT. Confirmar deduções de IRS no Portal das Finanças |
| Abril | Abertura do período de entrega do IRS (1 de Abril). Entrega antecipada para declarações simples. Reavaliar tributação conjunta vs separada |
| Maio | Continuação da entrega do IRS. Contribuição trimestral à SS (Abril). Simular imposto do ano |
| 30 de Junho | Prazo final de entrega do IRS. Garantir submissão do Modelo 3. Entregar Anexo B (Categoria B), Anexo H (deduções), Anexo J (rendimentos do estrangeiro) |
| Julho | Primeiro pagamento por conta de IRS. Rever base contributiva da SS para o trimestre seguinte |
| Setembro | Segundo pagamento por conta de IRS. Revisão fiscal de meio do ano |
| Outubro | Contribuição trimestral à SS. Rever rendimentos de capitais para decisão sobre englobamento |
| Novembro | Planear contribuições para PPR de fim de ano. Rever transmissões imobiliárias quanto a prazos de reinvestimento |
| Dezembro | Terceiro pagamento por conta de IRS. **Mês crítico:** efectuar contribuições para PPR, donativos. Garantir que todas as facturas profissionais foram emitidas com NIF. Última contribuição à SS do ano. Prazo para opções relativas ao IVA |

## Secção 12 — Exemplos de Impacto Financeiro

### Exemplo 1 — Regime Simplificado vs Contabilidade Organizada (Freelancer)

**Freelancer (profissional do Art 151.º), rendimentos brutos €50.000. Despesas reais: €8.000.**

**Regime simplificado:** Tributável = €50.000 × 0,75 = €37.500 (assumindo 15% de despesas justificadas). IRS: €37.500 × 34,9% – €4.209,85 (escalão 6) = €8.877,65. Acresce SS: 21,4% × (€50.000 × 0,70 / 3 × base 12 meses) ≈ €7.490. **Total imposto + SS: ~€16.368.**

**Contabilidade organizada:** Tributável = €50.000 – €8.000 = €42.000. IRS: €42.000 × 34,9% – €4.209,85 = €10.448,15. SS: igual ~€7.490. Acrescem honorários de contabilista ~€1.500. **Total: ~€19.438.**

**O regime simplificado poupa ~€3.070.** A contabilidade organizada só compensa se as despesas reais excederem €12.500 (25% do bruto).

### Exemplo 2 — Tributação Conjunta vs Separada

**Casal: Cônjuge A aufere €60.000, Cônjuge B aufere €10.000.**

**Separada:** A: IRS ~€14.527. B: IRS ~€460. Total: ~€14.987.

**Conjunta:** Combinado €70.000 ÷ 2 = €35.000 cada. IRS por metade: ~€8.012 × 2 = ~€16.024. **A tributação separada poupa ~€1.037** neste caso.

**Se o Cônjuge B aufere €0:** Conjunta: €60.000 ÷ 2 = €30.000 cada. IRS: ~€6.215 × 2 = €12.430. Separada: €14.527. **A tributação conjunta poupa ~€2.097.**

### Exemplo 3 — Criptoactivos Detidos Mais de 365 Dias

**Comprou BTC por €10.000 em Janeiro de 2025. Vendeu por €25.000 em Março de 2026 (>365 dias).**

Imposto: **€0** — as mais-valias de criptoactivos detidos ≥365 dias são isentas (Art 10.º, n.º 17 CIRS).

Se vendido em menos de 365 dias: (€25.000 – €10.000) × 28% = €4.200 de imposto.

### Exemplo 4 — Reinvestimento em Habitação Própria Permanente

Venda da habitação própria permanente por €300.000 (aquisição por €200.000). Mais-valia: €100.000. 50% incluído = €50.000 tributados à taxa marginal (~34,9%) = €13.341.

Reinvestir os €300.000 totais em nova habitação própria permanente em 36 meses: **€0 de imposto.** Reinvestimento parcial (€200.000 de €300.000 = 66,7%): 66,7% excluído → imposto sobre 33,3% × €50.000 = ~€4.450.

## Aviso Legal

Esta skill e os seus resultados são fornecidos apenas para fins informativos e computacionais e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuintes não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado (como um Contabilista Certificado, consultor fiscal ou profissional licenciado equivalente na sua jurisdição) antes da entrega ou actuação.

A versão mais actualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
