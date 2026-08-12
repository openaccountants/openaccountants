---
name: portugal-bookkeeping
description: "Utilize esta skill sempre que lhe forem colocadas questões sobre contabilidade portuguesa, plano de contas, SNC, demonstrações financeiras ou normas contabilísticas em Portugal. Active perante expressões como \"contabilidade Portugal\", \"SNC\", \"código de contas\", \"Sistema de Normalização Contabilística\", \"plano de contas\", \"microentidade\", \"pequena entidade\", \"NCRF\", \"NCRF-PE\", \"NC-ME\", \"balanço\", \"demonstração de resultados\", \"IES\", \"contabilista certificado\", \"regime simplificado\", \"contabilidade organizada\", \"SAF-T(PT)\", \"CAE\", \"Categoria B\", ou qualquer questão sobre o registo de operações, relato financeiro ou regras contabilísticas para entidades portuguesas. Trigger also on: \"Portuguese bookkeeping\", \"Portugal accounting\", \"SNC chart of accounts\", \"Portuguese GAAP\", \"simplified regime Portugal\", \"organized accounting Portugal\", \"self-employed Portugal Cat B\", \"SAF-T Portugal\", \"CAE coefficients\", \"Portuguese certified accountant\"."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Bookkeeping

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Ano económico | Ano civil (1 de Janeiro a 31 de Dezembro) obrigatório para a generalidade das entidades |
| Normas contabilísticas | SNC (Sistema de Normalização Contabilística); NCRF (completas), NCRF-PE (pequenas entidades), NC-ME (microentidades) |
| Plano de contas padrão | Código de Contas SNC (Portaria n.º 218/2015) — obrigatório |
| Organismo normalizador | CNC (Comissão de Normalização Contabilística) |
| Principal legislação | Decreto-Lei n.º 158/2009 (alterado pelo DL 98/2015); Portaria 218/2015 (código de contas); Portaria 220/2015 (modelos de demonstrações financeiras) |
| Classificação de actividade | CAE (Classificação das Actividades Económicas) — Revisão 3 |
| Ficheiro normalizado | SAF-T(PT) — Standard Audit File for Tax (Portugal) — submissão mensal à AT |
| Obrigação de relato | IES (Informação Empresarial Simplificada) — submissão electrónica anual à AT/IRN/INE/BdP |
| Autoridade tributária | AT (Autoridade Tributária e Aduaneira) |
| Ordem profissional | OCC (Ordem dos Contabilistas Certificados) |
| Contabilista certificado obrigatório | Sim — todas as entidades sujeitas ao SNC devem ter um Contabilista Certificado (membro da OCC) |
| Período de conservação de documentos | 10 anos (artigo 123.º do CIRC e artigo 52.º do CIVA) |

## Secção 2 — Plano de Contas Padrão (Código de Contas SNC)

O plano de contas SNC é obrigatório e está estruturado em 8 classes. As empresas devem utilizar a estrutura de contas prescrita.

### Classe 1 — Meios Financeiros Líquidos

**Classe 1 — Meios Financeiros Líquidos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 11 | Caixa | Caixa (numerário) |
| 12 | Depósitos à ordem | Contas bancárias à ordem |
| 13 | Outros depósitos bancários | Outros depósitos bancários (a prazo) |
| 14 | Outros instrumentos financeiros | Outros instrumentos financeiros |

### Classe 2 — Contas a Receber e a Pagar

**Classe 2 — Contas a Receber e a Pagar**

| Código | Conta | Descrição |
| --- | --- | --- |
| 21 | Clientes | Clientes (contas a receber comerciais) |
| 211 | Clientes c/c | Clientes — conta corrente |
| 2111 | Clientes gerais | Clientes gerais |
| 212 | Clientes — títulos a receber | Letras a receber |
| 219 | Perdas por imparidade acumuladas | Perdas por imparidade acumuladas |
| 22 | Fornecedores | Fornecedores (contas a pagar comerciais) |
| 221 | Fornecedores c/c | Fornecedores — conta corrente |
| 23 | Pessoal | Contas do pessoal |
| 231 | Remunerações a pagar | Remunerações a pagar |
| 232 | Adiantamentos a pessoal | Adiantamentos ao pessoal |
| 24 | Estado e outros entes públicos | Estado e outros entes públicos |
| 241 | Imposto sobre o rendimento | Imposto sobre o rendimento (IRC) |
| 2411 | IRC estimado | IRC estimado |
| 2412 | IRC retido na fonte | IRC retido na fonte |
| 2413 | Pagamentos por conta | Pagamentos por conta |
| 243 | IVA | IVA |
| 2431 | IVA suportado | IVA suportado |
| 2432 | IVA dedutível | IVA dedutível |
| 2433 | IVA liquidado | IVA liquidado |
| 2434 | IVA regularizações | IVA — regularizações |
| 2435 | IVA apuramento | IVA — apuramento |
| 2436 | IVA a pagar | IVA a pagar |
| 2437 | IVA a recuperar | IVA a recuperar |
| 245 | Contrib. para Segurança Social | Contribuições para a Segurança Social |
| 25 | Financiamentos obtidos | Financiamentos obtidos (empréstimos) |
| 251 | Instituições de crédito | Empréstimos bancários |
| 26 | Acionistas/sócios | Accionistas/sócios |
| 27 | Outras contas a receber e a pagar | Outras contas a receber e a pagar |
| 271 | Fornecedores de investimentos | Fornecedores de investimentos (credores de capex) |
| 278 | Outros devedores e credores | Outros devedores e credores |

### Classe 3 — Inventários e Activos Biológicos

**Classe 3 — Inventários e Activos Biológicos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 31 | Compras | Compras |
| 311 | Mercadorias | Mercadorias para revenda |
| 312 | Matérias-primas | Matérias-primas |
| 32 | Mercadorias | Mercadorias para revenda (existências) |
| 33 | Matérias-primas | Matérias-primas (existências) |
| 34 | Produtos acabados | Produtos acabados |
| 35 | Produtos e trabalhos em curso | Produção em curso |
| 36 | Subprodutos e desperdícios | Subprodutos e desperdícios |
| 38 | Reclassificação e regularização | Reclassificação e regularização |
| 39 | Adiantamentos por conta de compras | Adiantamentos por conta de compras |

### Classe 4 — Investimentos (Activos Fixos)

**Classe 4 — Investimentos (Activos Fixos)**

| Código | Conta | Descrição |
| --- | --- | --- |
| 41 | Investimentos financeiros | Investimentos financeiros |
| 42 | Propriedades de investimento | Propriedades de investimento |
| 43 | Activos fixos tangíveis | Activos fixos tangíveis |
| 431 | Terrenos e recursos naturais | Terrenos e recursos naturais |
| 432 | Edifícios e outras construções | Edifícios e outras construções |
| 433 | Equipamento básico | Equipamento básico (maquinaria) |
| 434 | Equipamento de transporte | Equipamento de transporte (viaturas) |
| 435 | Equipamento administrativo | Equipamento administrativo (escritório/informática) |
| 436 | Equipamentos biológicos | Activos biológicos (equipamento) |
| 437 | Outros activos fixos tangíveis | Outros activos fixos tangíveis |
| 438 | Depreciações acumuladas | Depreciações acumuladas |
| 44 | Activos intangíveis | Activos intangíveis |
| 441 | Goodwill | Goodwill |
| 442 | Projectos de desenvolvimento | Projectos de desenvolvimento |
| 443 | Programas de computador | Programas de computador |
| 444 | Propriedade industrial | Propriedade industrial (patentes, marcas) |
| 446 | Outros activos intangíveis | Outros activos intangíveis |
| 448 | Amortizações acumuladas | Amortizações acumuladas |
| 45 | Investimentos em curso | Investimentos em curso |
| 46 | Activos não correntes detidos para venda | Activos não correntes detidos para venda |

### Classe 5 — Capital, Reservas e Resultados Transitados

**Classe 5 — Capital, Reservas e Resultados Transitados**

| Código | Conta | Descrição |
| --- | --- | --- |
| 51 | Capital | Capital social |
| 52 | Acções (quotas) próprias | Acções (quotas) próprias |
| 53 | Outros instrumentos de capital próprio | Outros instrumentos de capital próprio |
| 54 | Prémios de emissão | Prémios de emissão |
| 55 | Reservas | Reservas |
| 551 | Reservas legais | Reservas legais |
| 552 | Outras reservas | Outras reservas |
| 56 | Resultados transitados | Resultados transitados |
| 57 | Ajustamentos em activos financeiros | Ajustamentos em activos financeiros |
| 58 | Excedentes de revalorização | Excedentes de revalorização |
| 59 | Outras variações no capital próprio | Outras variações no capital próprio |

### Classe 6 — Gastos

**Classe 6 — Gastos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 61 | CMVMC | Custo das mercadorias vendidas e das matérias consumidas |
| 62 | Fornecimentos e serviços externos (FSE) | Fornecimentos e serviços externos |
| 6211 | Subcontratos | Subcontratos |
| 6212 | Trabalhos especializados | Trabalhos especializados (contabilidade, jurídicos, etc.) |
| 6213 | Publicidade e propaganda | Publicidade e propaganda |
| 6214 | Vigilância e segurança | Vigilância e segurança |
| 6215 | Honorários | Honorários |
| 6216 | Comissões | Comissões |
| 622 | Serviços diversos | Serviços diversos |
| 6221 | Rendas e alugueres | Rendas e alugueres |
| 6222 | Comunicação | Comunicações (telecomunicações) |
| 6223 | Seguros | Seguros |
| 6224 | Royalties | Royalties |
| 6225 | Transportes de mercadorias | Transportes de mercadorias |
| 6226 | Deslocações e estadas | Deslocações e estadas |
| 6227 | Material de escritório | Material de escritório |
| 6228 | Energia e fluidos | Energia e fluidos |
| 6229 | Manutenção e reparação | Manutenção e reparação |
| 63 | Gastos com o pessoal | Gastos com o pessoal |
| 631 | Remunerações dos órgãos sociais | Remunerações dos órgãos sociais |
| 632 | Remunerações do pessoal | Remunerações do pessoal |
| 635 | Encargos sobre remunerações | Encargos sobre remunerações (Segurança Social — entidade patronal) |
| 636 | Seguros de acidentes de trabalho | Seguros de acidentes de trabalho |
| 64 | Gastos de depreciação e amortização | Gastos de depreciação e amortização |
| 641 | Propriedades de investimento | Depreciação — propriedades de investimento |
| 642 | Activos fixos tangíveis | Depreciação — activos fixos tangíveis |
| 643 | Activos intangíveis | Amortização — activos intangíveis |
| 65 | Perdas por imparidade | Perdas por imparidade |
| 66 | Perdas por reduções de justo valor | Perdas por reduções de justo valor |
| 67 | Provisões do período | Provisões do período |
| 68 | Outros gastos e perdas | Outros gastos e perdas |
| 681 | Impostos (indirectos) | Impostos indirectos |
| 6811 | IMI e outros impostos | IMI e outros impostos locais |
| 682 | Descontos de pronto pagamento | Descontos de pronto pagamento concedidos |
| 686 | Gastos financeiros | Gastos financeiros (juros suportados) |
| 688 | Outros | Outros gastos diversos |
| 69 | Gastos e perdas de financiamento | Gastos e perdas de financiamento |
| 691 | Juros suportados | Juros suportados |

### Classe 7 — Rendimentos

**Classe 7 — Rendimentos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 71 | Vendas | Vendas de mercadorias |
| 72 | Prestações de serviços | Prestações de serviços |
| 73 | Variações nos inventários da produção | Variações nos inventários da produção |
| 74 | Trabalhos para a própria entidade | Trabalhos para a própria entidade (capitalizados) |
| 75 | Subsídios à exploração | Subsídios à exploração |
| 76 | Reversões | Reversões de imparidades/provisões |
| 78 | Outros rendimentos e ganhos | Outros rendimentos e ganhos |
| 781 | Rendimentos suplementares | Rendimentos suplementares |
| 782 | Descontos obtidos | Descontos de pronto pagamento obtidos |
| 786 | Rendimentos financeiros | Rendimentos financeiros (juros obtidos) |
| 79 | Juros e rendimentos similares | Juros e rendimentos similares |

### Classe 8 — Resultados

**Classe 8 — Resultados**

| Código | Conta | Descrição |
| --- | --- | --- |
| 81 | Resultado líquido do período | Resultado líquido do período |
| 811 | Resultado antes de impostos | Resultado antes de impostos |
| 812 | Imposto sobre o rendimento | Imposto sobre o rendimento |
| 818 | Resultado líquido | Resultado líquido |

## Secção 3 — Reconhecimento do Rédito

### Base de Caixa vs Base de Acréscimo

**Base de Caixa vs Base de Acréscimo**

| Tipo de entidade | Base | Notas |
| --- | --- | --- |
| Entidades sujeitas ao SNC | Acréscimo (obrigatória) | O SNC/NCRF exige a base de acréscimo (regime do acréscimo) |
| Microentidades (NC-ME) | Acréscimo | Regras de reconhecimento simplificadas, mas ainda em base de acréscimo |
| Trabalhadores independentes (Categoria B do IRS) | Caixa ou Acréscimo | Regime simplificado utiliza valores facturados; contabilidade organizada utiliza o regime do acréscimo |

### Regras-Chave

- **Rédito da venda de bens** — Reconhecido quando os riscos e benefícios são transferidos para o comprador (NCRF 20)  _(NCRF 20)_
- **Rédito de prestação de serviços** — Método da percentagem de acabamento se o desfecho puder ser estimado com fiabilidade; caso contrário, apenas até ao limite dos custos recuperáveis
- **NC-ME (microentidades)** — Rédito reconhecido na facturação para bens; ao longo do tempo para serviços
- **IVA — obrigação de facturação** — A obrigação nasce na data da factura (factura obrigatória no prazo de 5 dias úteis após a entrega)

### Regime Simplificado para Trabalhadores Independentes (Categoria B do IRS)

- **Limiar de volume de negócios para regime simplificado** — 200.000 EUR EUR  _(artigo 31.º do CIRS)_
- **Coeficiente 0,75 — serviços tabela art.151.º CIRS** — 0,75 (serviços previstos na tabela do artigo 151.º do CIRS (actividades profissionais, incluindo desenvolvimento de software, consultoria, design, etc.))  _(artigo 31.º do CIRS; artigo 151.º do CIRS)_
- **Coeficiente 0,15 — vendas de mercadorias e hotelaria/restauração** — 0,15 (vendas de mercadorias e produtos e prestações de serviços de actividades hoteleiras e de restauração e bebidas)  _(artigo 31.º do CIRS)_
- **Coeficiente 0,10 — outras prestações de serviços** — 0,10 (outras prestações de serviços não previstas nas alíneas anteriores)  _(artigo 31.º do CIRS)_
- **Registo no regime simplificado** — No regime simplificado não existe obrigação de contabilidade organizada — apenas o registo dos rendimentos auferidos (modelo de registo de facturas)
- **Contabilidade organizada obrigatória** — A contabilidade organizada é obrigatória acima de 200.000 EUR de volume de negócios para a Categoria B, ou por opção do sujeito passivo (mantida por um período mínimo de três anos)

Para titulares do regime de Residente Não Habitual (RNH) ou do Incentivo Fiscal à Investigação Científica e Inovação (IFICI), consulte a skill pt-nhr-ifici para o tratamento específico desses regimes

## Secção 4 — Classificação de Gastos

### Gastos Dedutíveis (IRC)

**Gastos Dedutíveis (IRC)**

| Categoria | Código SNC | Dedutibilidade |
| --- | --- | --- |
| Renda (instalações da empresa) | 6221 | 100% dedutível |
| Energia e utilidades | 6228 | 100% dedutível |
| Honorários (contabilista, advogado) | 6212/6215 | 100% dedutível |
| Seguros (de empresa) | 6223 | 100% dedutível |
| Publicidade | 6213 | 100% dedutível |
| Material de escritório | 6227 | 100% dedutível |
| Telecomunicações | 6222 | 100% dedutível (proporção empresarial) |
| Despesas bancárias | 686 | 100% dedutível |
| Gastos com o pessoal | 63x | 100% dedutível |
| Deslocações (empresariais) | 6226 | 100% dedutível mediante documentação |
| Subscrições de software | 6212 | 100% dedutível |
| Manutenção e reparação | 6229 | 100% dedutível |

### Gastos Parcial ou Totalmente Não Dedutíveis

**Gastos Parcial ou Totalmente Não Dedutíveis**

| Categoria | Limitação |
| --- | --- |
| Despesas com viaturas (ligeiros de passageiros) | Limitadas por tributação autónoma |
| Despesas de representação | Sujeitas a tributação autónoma a 10% |
| Despesas não documentadas | Não dedutíveis + 50% de tributação autónoma |
| Multas e penalidades | 0% — nunca dedutíveis |
| IRC (o próprio imposto sobre o rendimento) | 0% — nunca dedutível |
| Ajudas de custo excessivas | Não dedutíveis acima dos limites legais |
| Despesas com entidades em paraísos fiscais | Não dedutíveis salvo prova de substância comercial |

### Tributação Autónoma

**Tributação Autónoma**

| Gasto | Taxa |
| --- | --- |
| Despesas de representação | 10% |
| Encargos com viaturas (aquisição ≤ 27.500 EUR) | 10% |
| Encargos com viaturas (27.500–35.000 EUR) | 27,5% |
| Encargos com viaturas (> 35.000 EUR) | 35% |
| Despesas não documentadas | 50% (70% se entidade isenta) |
| Ajudas de custo não facturadas | 5% |
| Encargos com viaturas eléctricas (≤ 62.500 EUR) | 0% |

### Tributação Autónoma

Tributação adicional incidente sobre determinados gastos, ainda que a empresa apresente lucro:

## Secção 5 — Limiares Activo vs Gasto

### Regras de Capitalização

**Regras de Capitalização**

| Regra | Detalhe |
| --- | --- |
| Capitalização obrigatória | Todos os elementos com vida útil superior a 1 ano e custo mensurável com fiabilidade |
| Limiar de baixo valor | Não existe de minimis legal; a prática admite reconhecimento como gasto de bens < 1.000 EUR em alguns casos |
| Dispêndio subsequente | Capitalizado se prolongar a vida útil ou aumentar a capacidade; caso contrário, reconhecido como gasto |

### Taxas de Depreciação (Decreto Regulamentar n.º 25/2009 — Tabela Genérica II)

**Taxas de Depreciação (Decreto Regulamentar n.º 25/2009 — Tabela Genérica II)**  _(Decreto Regulamentar n.º 25/2009 — Tabela Genérica II)_

| Tipo de activo | Método | Taxa máxima anual | Vida útil típica |
| --- | --- | --- | --- |
| Edifícios industriais | Quotas constantes | 5% | 20 anos |
| Edifícios comerciais | Quotas constantes | 2% | 50 anos |
| Construções ligeiras | Quotas constantes | 10% | 10 anos |
| Máquinas e equipamento básico | Quotas constantes | 12,5–20% | 5–8 anos |
| Equipamento de transporte (pesado) | Quotas constantes | 20% | 5 anos |
| Viaturas ligeiras de passageiros | Quotas constantes | 25% | 4 anos |
| Hardware informático | Quotas constantes | 33,33% | 3 anos |
| Software | Quotas constantes | 33,33% | 3 anos |
| Mobiliário de escritório | Quotas constantes | 12,5% | 8 anos |
| Equipamento de escritório | Quotas constantes | 20% | 5 anos |
| Ferramentas | Quotas constantes | 25% | 4 anos |
| Goodwill | Quotas constantes | Máx. 5% ao ano (20 anos) | Conforme contrato |

### Regras-Chave

- **Método de depreciação regime regra** — O método das quotas constantes é o regime regra; o método das quotas decrescentes é admitido para activos fixos tangíveis novos (excepto edifícios, viaturas e mobiliário de escritório)
- **Depreciação anual mínima** — Depreciação anual mínima = 50% da taxa máxima (quotas mínimas)
- **Comunicação à AT se depreciação inferior à mínima** — Se for praticada depreciação inferior à mínima, é exigida comunicação escrita à AT
- **Início da depreciação** — A depreciação inicia-se a partir do mês de entrada em funcionamento (pro rata)
- **Terrenos não depreciáveis** — Os terrenos não são depreciáveis

## Secção 6 — Modelo da Demonstração de Resultados (por Naturezas)

Portugal utiliza o modelo por naturezas como demonstração de resultados padrão. O modelo por funções é facultativo.

### Por Naturezas (modelo padrão para todas as entidades sujeitas ao SNC)

**Modelo Demonstração de Resultados por Naturezas**

```
Vendas e serviços prestados (Rédito)                           xxx
Subsídios à exploração                                         xxx
Variação nos inventários da produção                           xxx
Trabalhos para a própria entidade                              xxx
CMVMC (Custo das mercadorias vendidas e matérias consumidas)  (xxx)
Fornecimentos e serviços externos (FSE)                       (xxx)
Gastos com o pessoal                                          (xxx)
Imparidade de inventários                                     (xxx)
Imparidade de dívidas a receber                               (xxx)
Provisões                                                     (xxx)
Outras imparidades / variações no justo valor                 (xxx)
Outros rendimentos e ganhos                                    xxx
Outros gastos e perdas                                        (xxx)
                                                            -------
EBITDA                                                         xxx

Gastos de depreciação e amortização                           (xxx)
                                                            -------
EBIT (Resultado operacional)                                   xxx

Juros e rendimentos similares obtidos                          xxx
Juros e gastos similares suportados                           (xxx)
                                                            -------
Resultado antes de impostos (EBT)                              xxx

Imposto sobre o rendimento do período (IRC)                   (xxx)
                                                            -------
Resultado líquido do período                                   xxx
```

## Secção 7 — Modelo do Balanço

Portugal utiliza o formato vertical com classificação corrente/não corrente.

### Modelo

**Modelo do Balanço**

```
ACTIVO

Activo não corrente
  Activos fixos tangíveis                                     xxx
  Propriedades de investimento                                xxx
  Goodwill                                                    xxx
  Activos intangíveis                                         xxx
  Investimentos financeiros                                   xxx
  Activos por impostos diferidos                              xxx
                                                           -------
  Total do activo não corrente                                xxx

Activo corrente
  Inventários                                                 xxx
  Clientes                                                    xxx
  Estado e outros entes públicos                              xxx
  Outras contas a receber                                     xxx
  Diferimentos                                                xxx
  Caixa e depósitos bancários                                 xxx
                                                           -------
  Total do activo corrente                                    xxx

TOTAL DO ACTIVO                                               xxx
                                                           =======

CAPITAL PRÓPRIO E PASSIVO

Capital próprio
  Capital realizado                                           xxx
  Reservas legais                                             xxx
  Outras reservas                                             xxx
  Resultados transitados                                      xxx
  Resultado líquido do período                                xxx
                                                           -------
  Total do capital próprio                                    xxx

Passivo não corrente
  Financiamentos obtidos                                      xxx
  Provisões                                                   xxx
  Passivos por impostos diferidos                             xxx
                                                           -------
  Total do passivo não corrente                               xxx

Passivo corrente
  Fornecedores                                                xxx
  Estado e outros entes públicos                              xxx
  Financiamentos obtidos (curto prazo)                        xxx
  Outras contas a pagar                                       xxx
  Diferimentos                                                xxx
                                                           -------
  Total do passivo corrente                                   xxx

TOTAL DO CAPITAL PRÓPRIO E PASSIVO                            xxx
                                                           =======
```

## Secção 8 — Padrões de Reconciliação Bancária

### Formatos de Extracto Bancário em Portugal

**Formatos de Extracto Bancário em Portugal**

| Banco | Formato | Campos-chave |
| --- | --- | --- |
| Millennium BCP | CSV, OFX | Data, Descrição, Montante, Saldo, Contraparte |
| Caixa Geral de Depósitos (CGD) | CSV, OFX | Data, Descrição, Valor, Saldo |
| Novo Banco | CSV | Data, Descrição, Débito, Crédito, Saldo |
| Santander Totta | CSV, OFX | Data, Descrição, Montante, Saldo |
| BPI | CSV | Data Valor, Descrição, Débito, Crédito, Saldo |
| ActivoBank | CSV | Data, Tipo, Descrição, Montante |

### Descrições Habituais de Movimentos

**Descrições Habituais de Movimentos**

| Padrão | Classificação |
| --- | --- |
| TRF, TRANSFERENCIA | Transferência (verificar sentido) |
| DD, DEBITO DIRETO | Débito directo (gasto recorrente) |
| MB, MULTIBANCO | Pagamento ATM/cartão |
| PAGAMENTO DE SERVICOS | Pagamento de serviços (utilidades, etc.) |
| AT-AUTORIDADE TRIBUTARIA | Pagamento de imposto à AT |
| SEGURANCA SOCIAL, SS | Pagamento à Segurança Social |
| COMPRA/VENDA MB WAY | Pagamento móvel |
| JUROS | Juros (verificar débito/crédito) |
| COMISSAO, DESPESA | Despesas bancárias |
| IMPOSTO SELO | Imposto do selo (sobre operações bancárias) |

## Secção 9 — Simplificações para Microentidades e Pequenos Negócios

### Categorias de Dimensão (até 2025; limiares aumentados a partir de 2026)

**Categorias de Dimensão (até 2025; limiares aumentados a partir de 2026)**

| Categoria | Total do balanço | Volume de negócios líquido | Trabalhadores |
| --- | --- | --- | --- |
| Microentidade | ≤ 350.000 EUR (450.000 EUR a partir de 2026) | ≤ 700.000 EUR (900.000 EUR a partir de 2026) | ≤ 10 |
| Pequena entidade | ≤ 4.000.000 EUR (5.000.000 EUR a partir de 2026) | ≤ 8.000.000 EUR (10.000.000 EUR a partir de 2026) | ≤ 50 |
| Média entidade | ≤ 20.000.000 EUR (25.000.000 EUR a partir de 2026) | ≤ 40.000.000 EUR (50.000.000 EUR a partir de 2026) | ≤ 250 |

- **Regra dos 2 de 3 critérios** — A entidade não pode exceder 2 dos 3 critérios no período imediatamente anterior.

### Normas Aplicáveis

**Normas Aplicáveis**

| Categoria | Norma | Principais simplificações |
| --- | --- | --- |
| Microentidade | NC-ME | Sem impostos diferidos, sem revalorizações, sem justo valor; demonstrações financeiras simplificadas (2 páginas) |
| Pequena entidade | NCRF-PE | Divulgações reduzidas; demonstração dos fluxos de caixa não exigida |
| Média/Grande | NCRF completas (28 normas) | Divulgações completas; demonstração dos fluxos de caixa; demonstração das alterações no capital próprio |

### Simplificações NC-ME (Microentidades)

- **Demonstrações financeiras** — Apenas Balanço + Demonstração de Resultados + Anexo limitado (sem fluxos de caixa, sem demonstração das alterações no capital próprio)
- **Mensuração de activos** — Todos os activos mensurados ao custo deduzido de depreciações/amortizações (sem justo valor, sem revalorização)
- **Impostos diferidos** — Não exige apuramento de impostos diferidos
- **Anexo simplificado** — Anexo simplificado com um máximo de 15 rubricas
- **Locações** — Sem distinção entre financeira e operacional; todas as locações reconhecidas como gasto

### Empresário em Nome Individual (Trabalhador Independente)

- **Limiar regime simplificado** — 200.000 EUR EUR (Categoria B do IRS)
- **Sem obrigação de contabilidade organizada no regime simplificado** — Sem obrigação de contabilidade organizada no regime simplificado — tributação por aplicação de coeficientes em função do CAE
- **Contabilidade organizada facultativa/obrigatória** — A contabilidade organizada é facultativa abaixo do limiar e obrigatória acima
- **Contabilista certificado obrigatório se contabilidade organizada** — Contabilista certificado (membro da OCC) obrigatório se for adoptada a contabilidade organizada

Para o tratamento do regime de Residente Não Habitual (RNH) e do Incentivo Fiscal à Investigação Científica e Inovação (IFICI), consulte a skill pt-nhr-ifici

## Secção 10 — Articulação com Skills Fiscais

### Imposto sobre o Rendimento das Pessoas Colectivas (IRC)

- **IES integra dados contabilísticos e fiscais** — A submissão da IES integra os dados contabilísticos e fiscais num único relato anual
- **Resultado fiscal e Quadro 07** — O resultado fiscal parte do resultado contabilístico (conta 81) com correcções fiscais no Quadro 07 da Modelo 22
- **Principais correcções fiscais** — Principais correcções: tributação autónoma, gastos não dedutíveis, benefícios fiscais (SIFIDE, RFAI, DLRR)
- **Taxa de IRC geral** — 21% (taxa geral)
- **Taxa reduzida PME primeiros 50.000 EUR** — 17% (sobre os primeiros 50.000 EUR para PME; derrama estadual sobre lucros superiores a 1.500.000 EUR)

Utilize a skill pt-income-tax para o apuramento detalhado

### IVA

- **Contas do IVA** — Contas do IVA: classe 243x do plano SNC
- **Periodicidade mensal vs trimestral** — 650.000 EUR EUR (Periodicidade mensal se o volume de negócios for superior a 650.000 EUR; caso contrário, trimestral)
- **Taxa normal IVA continente** — 23% (continente)
- **Taxa normal IVA Açores** — 16% (Açores)
- **Taxa normal IVA Madeira** — 22% (Madeira)
- **Taxas reduzidas IVA** — 6% e 13%

Utilize a skill portugal-vat-return para detalhes da submissão

### SAF-T(PT)

- **Obrigatoriedade SAF-T(PT)** — O ficheiro SAF-T(PT) (Standard Audit File for Tax — versão portuguesa) é obrigatório
- **Prazo de submissão mensal** — Submissão mensal à AT até ao dia 5 do segundo mês seguinte ao da emissão das facturas (SAF-T de facturação)
- **SAF-T de contabilidade** — SAF-T de contabilidade submetido anualmente em articulação com a IES
- **Software certificado** — Software de facturação certificado pela AT é obrigatório acima de determinados limiares de volume de negócios
- **Comunicação de facturas** — Todas as facturas devem ser emitidas por programa certificado e comunicadas à AT

### Segurança Social

- **Contribuição da entidade patronal** — 23,75% (da remuneração ilíquida)
- **Contribuição do trabalhador** — 11% (da remuneração ilíquida)
- **Trabalhador independente** — 21,4% (do rendimento relevante (25,2% no primeiro ano))
- **Registo contabilístico** — Registado na conta 245 até ao pagamento

Utilize a skill pt-social-contributions para detalhes

### Conservação de Documentos

- **Período de conservação obrigatório** — 10 anos anos  _(artigo 123.º do CIRC e artigo 52.º do CIVA)_
- **Âmbito de aplicação** — Aplicável a livros, registos contabilísticos, facturas, documentos de suporte e ficheiros SAF-T(PT)
- **Conservação electrónica** — A conservação em formato electrónico é admitida desde que seja garantida a autenticidade, integridade e legibilidade

## Aviso Legal

Esta skill e os respectivos resultados são disponibilizados apenas para fins informativos e de apoio ao cálculo e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus colaboradores não aceitam qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado (Contabilista Certificado membro da OCC) antes da submissão ou de qualquer actuação com base nos mesmos.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
