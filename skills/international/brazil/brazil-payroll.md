---
name: brazil-payroll
description: Use esta skill sempre que perguntarem sobre processamento de folha de pagamento brasileira, cálculo de salários, IRRF (Imposto de Renda Retido na Fonte), contribuições ao INSS, depósitos de FGTS, 13º salário (décimo terceiro), custo do empregador, conversões de líquido para bruto ou de bruto para líquido, estrutura de holerite/contracheque, eventos do eSocial, ou qualquer questão sobre cálculo de remuneração, deduções ou obrigações do empregador no Brasil. Acione com frases como "folha de pagamento brasileira", "folha de pagamento", "INSS", "IRRF", "FGTS", "13º salário", "décimo terceiro", "férias", "salário líquido", "holerite", "eSocial", "DCTF Web", "custo do empregador Brasil", "CLT", "rescisão", "aviso prévio", ou "salário mínimo Brasil". / Use this skill whenever asked about Brazilian payroll processing, employee salary calculations, IRRF, INSS contributions, FGTS deposits, 13th salary, employer cost, gross-to-net or net-to-gross conversions, Brazilian payslip structure, eSocial filings, or any question about computing wages, deductions, or employer obligations in Brazil.
version: 1.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ariane Marrocos
review_status: current
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil Payroll

## Brasil — Folha de Pagamento (INSS, FGTS, IRRF) — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ariane Marrocos** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Folha de Pagamento

- **Salário mínimo 2025** — R$ 1.518,00/mês  _(Decreto nº 12.342/2024)_
- **Salário mínimo 2026** — R$ 1.630,00/mês  _(Decreto Federal do Salário Mínimo 2026)_
- **IRRF isenção** — R$ 2.428,80 — Isento  _(Lei nº 11.482/2007)_
- **IRRF faixa de R$ 2.428,81 a R$ 2.826,65** — 7,5% - parcela R$ 182,16  _(Lei nº 11.482/2007)_
- **IRRF faixa R$ 2.826,66 – R$ 3.751,05** — 15% - parcela R$ 394,16  _(Lei nº 11.482/2007)_
- **IRRF faixa R$ 3.751,06 – R$ 4.664,68** — 22,5% - parcela R$ 675,49  _(Lei nº 11.482/2007)_
- **IRRF Acima de R$ 4.664,68** — 27,5% - parcela R$ 908,73  _(Lei nº 11.482/2007)_
- **Dedução por dependente** — R$ 189,59/mês  _(Lei nº 9.250/1995)_
- **INSS faixa Até R$ 1.621,00** — Até R$ 1.630,00  _(Lei nº 8.212/1991 Portaria Interministerial MPS/MF nº 13/2026)_
- **INSS faixa R$ 1.621,01 – R$ 2.902,84** — R$ 1.630,01 – R$ 2.902,84  _(Lei nº 8.212/1991 Portaria Interministerial MPS/MF nº 13/2026)_
- **INSS faixa R$ 2.902,85 – R$ 4.354,27** — 12%  _(Lei nº 8.212/1991 Portaria Interministerial MPS/MF nº 13/2026)_
- **INSS faixa R$ 4.354,28 – R$ 8.475,55 (teto)** — 14%  _(Lei nº 8.212/1991 Portaria Interministerial MPS/MF nº 13/2026)_
- **INSS patronal básico** — 20% da folha total (sem teto)  _(Lei 8.212/1991)_
- **RAT/SAT** — 1%, 2% ou 3% (conforme CNAE)  _(Lei 8.212/1991)_
- **Ajuste FAP** — 0,5× a 2,0× sobre o RAT  _(Lei 10.666/2003)_
- **Terceiros** — ~5,8% (SENAI, SESI, SEBRAE, etc.)  _(Leis específicas)_
- **Total típico INSS patronal** — ~26,8% – 28,8%  _(Lei 8.212/1991)_
- **Alíquota FGTS** — 8% do bruto mensal (empregador)  _(Lei 8.036/1990)_
- **Prazo depósito FGTS** — Até dia 20 do mês seguinte (FGTS Digital)  _(Lei 8.036/1990)_
- **Multa rescisória (sem justa causa)** — 40% do saldo total do FGTS  _(Lei 8.036/1990)_
- **Estimativa acima do bruto** — ~60-70% (INSS+FGTS+13º+férias+encargos)  _(Consolidado)_
- **Jornada semanal padrão** — 44 horas  _(CLT Art. 58)_
- **Hora extra (dias úteis)** — Mínimo 50%  _(CF/88 Art. 7º XVI)_
- **Hora extra (domingos/feriados)** — Geralmente 100%, conforme legislação e convenção coletiva  _(Lei 605/1949)_
- **Adicional noturno (22h-5h)** — Mínimo 20%  _(CLT Art. 73)_
- **Insalubridade** — 10%, 20% ou 40% do salário mínimo  _(CLT Art. 192)_
- **Periculosidade** — 30% do salário-base  _(CLT Art. 193)_
- **13º salário** — 1 salário integral (duas parcelas)  _(Lei 4.090/1962)_
- **Férias** — 30 dias + 1/3 constitucional  _(CF Art. 7º XVII; CLT)_
- **Vale-transporte** — Empregado contribui com até 6% do salário básico; empregador paga o excedente.  _(Lei 7.418/1985)_
- **Licença-maternidade** — 120 dias (180 dias no Programa Empresa Cidadã)  _(CF Art. 7º XVIII)_
- **Licença-paternidade** — 5 dias (20 dias no Programa Empresa Cidadã)  _(ADCT Art. 10 §1º)_

## Seção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Brasil (República Federativa do Brasil) |
| Moeda | BRL (Real Brasileiro) |
| Periodicidade da folha | Mensal (pagamento até o 5º dia útil do mês seguinte) |
| Ano-calendário fiscal | Ano civil (1º de janeiro — 31 de dezembro) |
| Legislação principal | CLT (Consolidação das Leis do Trabalho, Decreto-Lei 5.452/1943); Lei 8.212/1991 (INSS); Lei 8.036/1990 (FGTS); Regulamento do IR (Decreto 9.580/2018) |
| Autoridade tributária | Receita Federal do Brasil (RFB) |
| Autoridade trabalhista | Ministério do Trabalho e Emprego (MTE) |
| Autoridade do FGTS | Caixa Econômica Federal (CEF) |
| INSS do empregado | Progressivo: 7,5% — 14% (teto BRL 8.475,55/mês) |
| INSS patronal | 20% + RAT (1-3%) + Terceiros (~5,8%) |
| FGTS | 8% do salário bruto (depósito exclusivo do empregador) |
| IRRF | Progressivo: 0% — 27,5% |
| Salário mínimo | BRL 1.621/mês (2026) |
| Eventos do eSocial | Mensais, até o dia 15 do mês seguinte |
| FGTS Digital | Depósito mensal até o dia 20 do mês seguinte |
| Versão da skill | 1.1 |

- **Reforma Tributária 2026 e folha** — A Reforma Tributária 2026 (EC 132/2023, LC 214/2025) é sobre tributos sobre consumo (CBS/IBS substituindo PIS/Cofins/ICMS/ISS/IPI). Folha de pagamento — INSS, FGTS, IRRF, salário-família, salário-maternidade — não é afetada.

## Seção 2 — Retenção de Imposto de Renda (IRRF)

### Tabela Mensal do IRRF (2026)

**Tabela Mensal do IRRF (2026)**

| Base de Cálculo Mensal (BRL) | Alíquota | Parcela a deduzir (BRL) |
| --- | --- | --- |
| Até 2.259,20 | 0% (isento) | — |
| 2.259,21 — 2.826,65 | 7,5% | 169,44 |
| 2.826,66 — 3.751,05 | 15% | 381,44 |
| 3.751,06 — 4.664,68 | 22,5% | 662,77 |
| Acima de 4.664,68 | 27,5% | 896,00 |

### Método de Cálculo do IRRF

**Método de Cálculo do IRRF**

| Etapa | Detalhe |
| --- | --- |
| 1. Partir do salário bruto | Toda remuneração tributável do mês |
| 2. Deduzir INSS (empregado) | Contribuição previdenciária progressiva |
| 3. Deduzir dependentes | BRL 189,59 por dependente (2026) |
| 4. Deduzir pensão alimentícia | Pagamentos determinados judicialmente |
| 5. Deduzir previdência privada (PGBL) | Até 12% da renda bruta anual |
| 6. Aplicar tabela do IRRF | Alíquota × base tributável − parcela a deduzir = IRRF |

### Regras Especiais do IRRF

**Regras Especiais do IRRF**

| Situação | Tratamento |
| --- | --- |
| 13º salário | IRRF calculado separadamente (não agregado ao salário mensal) |
| Férias | IRRF calculado sobre férias + 1/3 constitucional separadamente |
| Participação nos lucros (PLR) | Tabela progressiva específica (anual) |
| Verbas indenizatórias na rescisão | Geralmente isentas de IRRF |
| Horas extras, bônus, comissões | Somados ao bruto mensal para cálculo do IRRF |

## Seção 3 — Previdência Social: Deduções do Empregado (INSS)

### Tabela Progressiva do INSS (2026)

**Tabela Progressiva do INSS (2026)**

| Salário Mensal (BRL) | Alíquota |
| --- | --- |
| Até 1.621,00 | 7,5% |
| 1.621,01 — 2.902,84 | 9% |
| 2.902,85 — 4.354,27 | 12% |
| 4.354,28 — 8.475,55 (teto) | 14% |

### Regras Principais do INSS

- Progressiva (fatiada): cada faixa aplica-se somente à parcela contida no respectivo intervalo
- Contribuição mensal máxima: ~BRL 951,64 (no teto)
- Teto: BRL 8.475,55/mês (2026)
- INSS sobre 13º salário calculado separadamente (não somado ao salário mensal)
- Múltiplos vínculos: os salários são somados para determinação da faixa; contribuições alocadas proporcionalmente
- O INSS é dedutível na base de cálculo do IRRF

### Exemplo de Cálculo do INSS (Salário BRL 5.000)

```
Faixa 1: 1.621,00 × 7,5%             =  121,58
Faixa 2: (2.902,84 − 1.621,00) × 9%  =  115,37
Faixa 3: (4.354,27 − 2.902,84) × 12% =  174,17
Faixa 4: (5.000,00 − 4.354,27) × 14% =   90,40
Total INSS:                          =  501,52
```

## Seção 4 — Previdência Social: Contribuições do Empregador

### INSS Patronal (Contribuição Patronal)

**INSS Patronal (Contribuição Patronal)**

| Componente | Alíquota | Base |
| --- | --- | --- |
| INSS patronal básico | 20% | Folha total (sem teto) |
| RAT/SAT (acidente de trabalho) | 1%, 2% ou 3% | Conforme classificação de risco do CNAE |
| Ajuste FAP | 0,5× a 2,0× | Multiplicador aplicado ao RAT (específico por empresa) |
| Terceiros (entidades terceiras) | ~5,8% | SENAI, SESI, SEBRAE, INCRA, Salário-Educação, FNDE |
| **Total típico do INSS patronal** | **~26,8% — 28,8%** | Sobre o total da folha |

### FGTS (Fundo de Garantia do Tempo de Serviço)

**FGTS (Fundo de Garantia do Tempo de Serviço)**

| Parâmetro | Detalhe |
| --- | --- |
| Alíquota | 8% da remuneração mensal bruta |
| Pago por | Apenas pelo empregador (NÃO deduzido do empregado) |
| Base | Toda remuneração: salário, horas extras, bônus, 13º, férias |
| Teto | Nenhum (aplica-se ao salário integral) |
| Prazo de depósito | Até o dia 20 do mês seguinte (FGTS Digital) |
| Plataforma | FGTS Digital (via integração com eSocial) |
| Rescisão sem justa causa | Empregador paga multa de 40% sobre o saldo total do FGTS |

### Encargo Total do Empregador (Aproximado)

**Encargo Total do Empregador (Aproximado)**

| Componente | Alíquota |
| --- | --- |
| INSS patronal + RAT + Terceiros | ~28,8% |
| FGTS | 8% |
| Provisão de 13º salário (1/12) | 8,33% |
| Provisão de férias + 1/3 (1/12) | 11,11% |
| Subtotal das provisões | 19,44% |
| FGTS/INSS sobre provisões | ~7% |
| **Custo total aproximado do empregador acima do bruto** | **~60-70%** |

## Seção 5 — Salário Mínimo e Horas Extras

### Salário Mínimo Nacional

**Salário Mínimo Nacional**

| Ano | Mensal (BRL) | Diário (BRL) | Hora (BRL) |
| --- | --- | --- | --- |
| 2026 | 1.621,00 | 54,04 | 7,37 |
| 2025 | 1.518,00 | 50,60 | 6,91 |

- Definido pelo Decreto nº 12.797/2025 (vigência a partir de 1º de janeiro de 2026)
- Baseado em 220 horas/mês (44 horas/semana × 5 semanas)
- Pisos estaduais/regionais podem ser superiores (ex.: São Paulo, Rio de Janeiro, Paraná)
- Pisos salariais (categorias profissionais) por convenções podem superar o mínimo nacional

### Jornada de Trabalho e Horas Extras

**Jornada de Trabalho e Horas Extras**

| Parâmetro | Padrão |
| --- | --- |
| Jornada semanal padrão | 44 horas (8h/dia seg-sex + 4h sábado) |
| Alternativa comum | 40 horas (acordo coletivo) |
| Jornada diária máxima | 10 horas (8 + 2 de hora extra) |
| Adicional de hora extra (dias úteis) | Mínimo de 50% |
| Adicional de hora extra (domingos/feriados) | 100% |
| Adicional noturno (22h-5h) | Mínimo de 20% |
| Duração da hora noturna | 52 minutos e 30 segundos (hora reduzida) |
| Banco de horas | Permitido via acordo coletivo (compensação em 6-12 meses) |

### Insalubridade / Periculosidade

**Insalubridade / Periculosidade**

| Tipo | Adicional |
| --- | --- |
| Insalubridade (condições insalubres) | 10%, 20% ou 40% do salário mínimo |
| Periculosidade (condições perigosas) | 30% do salário-base |
| Não acumuláveis | Empregado escolhe a opção mais vantajosa |

## Seção 6 — Benefícios Obrigatórios

**Benefícios Obrigatórios**

| Benefício | Detalhe |
| --- | --- |
| 13º salário (gratificação natalina) | Um salário mensal integral, pago em duas parcelas |
| Férias | 30 dias corridos + 1/3 constitucional |
| Vale-transporte | Obrigatório; empregador arca com o custo que exceder 6% do salário-base |
| FGTS | Depósito mensal de 8% (custeado pelo empregador) |
| Seguro-desemprego | 3 a 5 meses (pago pelo governo na rescisão sem justa causa) |
| Salário-família | Para empregados de baixa renda com filhos menores de 14 anos |
| Licença-maternidade | 120 dias (180 dias para participantes do Empresa Cidadã) |
| Licença-paternidade | 5 dias (20 para Empresa Cidadã) |
| Seguro de acidentes de trabalho (SAT/RAT) | Coberto via contribuição patronal ao INSS |

### 13º Salário (Décimo Terceiro)

**13º Salário (Décimo Terceiro)**

| Parcela | Valor | Prazo | Deduções |
| --- | --- | --- | --- |
| 1ª parcela | 50% do salário do mês anterior | Até 30 de novembro | Sem desconto de INSS/IRRF |
| 2ª parcela | 50% restantes | Até 20 de dezembro | INSS + IRRF sobre o 13º integral |
| FGTS | 8% sobre cada parcela | Junto ao depósito mensal de FGTS | N/A |
| Proporcional | 1/12 por mês trabalhado (se < 12 meses) | Proporcional | Mesmas regras |

### Férias

**Férias**

| Parâmetro | Detalhe |
| --- | --- |
| Direito | 30 dias corridos após 12 meses (período aquisitivo) |
| Pagamento | Salário + 1/3 constitucional (terço de férias) |
| Prazo de pagamento | Até 2 dias úteis antes do início das férias |
| Abono pecuniário | Empregado pode vender até 10 dias (1/3 das férias) |
| INSS | Incide sobre o pagamento de férias |
| IRRF | Calculado separadamente sobre as férias |
| FGTS | 8% sobre as férias (incluindo 1/3) |
| Férias coletivas | Empregador pode conceder (mínimo de 10 dias consecutivos) |

### Vale-Transporte

**Vale-Transporte**

| Parâmetro | Detalhe |
| --- | --- |
| Obrigatório | Sim, para todos os empregados CLT que solicitarem |
| Contribuição do empregado | Até 6% do salário-base |
| Empregador arca com | Custo total menos a dedução de 6% do empregado |
| Isento de | INSS, FGTS, IRRF (não considerado salário) |
| Forma | Cartão de transporte pré-pago ou equivalente |

## Seção 7 — Requisitos do Holerite

Os empregadores brasileiros DEVEM emitir holerite/contracheque a cada pagamento de salário. Elementos exigidos pelo art. 464 da CLT:

**Elementos do Holerite**  _(art. 464 da CLT)_

| Elemento | Obrigatório |
| --- | --- |
| Nome do empregador, CNPJ, endereço | Sim |
| Nome do empregado, CPF, registro em CTPS | Sim |
| Cargo e departamento | Sim |
| Período de competência | Sim |
| Salário-base | Sim |
| Horas extras e respectivo valor | Sim (se aplicável) |
| Adicional noturno | Sim (se aplicável) |
| Insalubridade/periculosidade | Sim (se aplicável) |
| Comissões, bônus, gratificações | Sim |
| Remuneração bruta | Sim |
| Dedução de INSS do empregado | Sim |
| Dedução de IRRF | Sim |
| Dedução de vale-transporte (6%) | Sim (se aplicável) |
| Outras deduções (adiantamentos, benefícios, sindical) | Sim |
| Salário líquido | Sim |
| Depósito de FGTS (empregador, informativo) | Sim |
| Base de FGTS e INSS | Recomendado |

### Guarda de Documentos

- **Registros de folha de pagamento** — mínimo de 5 anos  _(CLT)_
- **Registros de FGTS** — 30 anos
- **Registros fiscais (IRRF)** — 5 anos a partir da entrega da declaração

## Seção 8 — Obrigações Acessórias

**Obrigações Acessórias**

| Declaração | Periodicidade | Prazo | Autoridade |
| --- | --- | --- | --- |
| Eventos periódicos do eSocial (S-1200 remuneração) | Mensal | Dia 15 do mês seguinte | RFB/MTE |
| Fechamento do eSocial (S-1299) | Mensal | Dia 15 do mês seguinte | RFB/MTE |
| DCTFWeb (declaração tributária) | Mensal | Dia 15 do mês seguinte (após fechamento do eSocial) | Receita Federal |
| Depósito do FGTS Digital | Mensal | Dia 20 do mês seguinte | Caixa Econômica Federal |
| Pagamento de IRRF (DARF) | Mensal | Dia 20 do mês seguinte | Receita Federal |
| 13º salário — 1ª parcela | Anual | 30 de novembro | Ao empregado |
| 13º salário — 2ª parcela | Anual | 20 de dezembro | Ao empregado |
| DIRF (Declaração anual de retenção) | Anual | Último dia útil de fevereiro | Receita Federal |
| RAIS (Relação Anual de Informações Sociais) | Anual | Março (em substituição pelos dados do eSocial) | MTE |

### Eventos do eSocial (Principais Eventos de Folha)

**Eventos do eSocial (Principais Eventos de Folha)**

| Evento | Descrição | Prazo |
| --- | --- | --- |
| S-1200 | Remuneração do trabalhador (mensal) | Dia 15 do mês seguinte |
| S-1210 | Pagamentos realizados (datas e valores) | Dia 15 do mês seguinte |
| S-1299 | Fechamento dos eventos periódicos | Dia 15 do mês seguinte |
| S-2200 | Cadastramento de empregado (admissão) | Véspera da data de início |
| S-2206 | Alteração contratual (mudança salarial) | Até o processamento da folha |
| S-2299 | Desligamento | 10 dias a contar da rescisão |
| S-2500 | Processo trabalhista | Por evento |
| S-1200 (13º) | Evento anual do 13º salário | 20 de dezembro |

### FGTS Digital

**FGTS Digital**

| Parâmetro | Detalhe |
| --- | --- |
| Substituiu | SEFIP/GFIP (sistema legado) |
| Integração | Automática a partir dos eventos do eSocial |
| Pagamento | Via portal do FGTS Digital (gera guia) |
| Prazo | Dia 20 do mês seguinte |
| Processos trabalhistas | Via FGTS Digital a partir de 1º de maio de 2026 (para novas sentenças) |

### Penalidades

**Penalidades**

| Infração | Penalidade |
| --- | --- |
| FGTS em atraso | Juros (TR + 3% ao ano) + multa (5% no primeiro mês, 10% a partir do segundo) |
| INSS em atraso | Multa de 20% + juros SELIC |
| IRRF em atraso | Multa de 0,33%/dia (máx. 20%) + juros SELIC |
| Falta de eventos do eSocial | Multa variável; pode gerar fiscalização/autuação |
| Não pagamento do 13º | Multa por empregado + possível reclamação trabalhista |
| Pagamento atrasado de férias | Pagamento em dobro (jurisprudência do TST) |

## Seção 9 — Padrões Comuns de Folha de Pagamento

### Padrão 1: Salário Mensal Padrão (BRL 5.000, Solteiro, Sem Dependentes)

```
Salário bruto:                        BRL 5.000,00
− INSS (progressivo):              − BRL    501,52
= Base de cálculo do IRRF:            BRL 4.498,48
− IRRF (22,5% − 662,77):           − BRL    349,39
− Vale-transporte (6% da base):    − BRL    300,00
= Salário líquido:                    BRL 3.849,09

Custo do empregador:
  Salário bruto:                      BRL 5.000,00
+ INSS patronal (20%):              + BRL 1.000,00
+ RAT (2%):                         + BRL   100,00
+ Terceiros (5,8%):                 + BRL   290,00
+ FGTS (8%):                        + BRL   400,00
= Custo mensal do empregador (excl. provisões): BRL 6.790,00

Provisões anuais:
+ 13º salário + encargos:           ~BRL 6.500/ano
+ Férias + 1/3 + encargos:          ~BRL 8.700/ano
```

### Padrão 2: Trabalhador com Salário Mínimo (BRL 1.621)

```
Salário bruto:                        BRL 1.621,00
− INSS (7,5%):                     − BRL    121,58
= Base de cálculo do IRRF:            BRL 1.499,42
− IRRF:                            − BRL      0,00 (abaixo do limite de isenção)
= Salário líquido (antes do VT):      BRL 1.499,42
− Vale-transporte (6%):            − BRL     97,26
= Líquido recebido:                   BRL 1.402,16

Custo mensal do empregador:
  Salário + INSS patronal + RAT + Terceiros + FGTS ≈ BRL 2.200
  Total anual (com 13º, férias, encargos) ≈ BRL 31.000
```

### Padrão 3: Cálculo do 13º Salário (Ano Completo, Salário BRL 5.000)

```
1ª parcela (até 30 de novembro):
  50% × 5.000 = BRL 2.500,00
  Sem desconto de INSS ou IRRF
  FGTS: 8% × 2.500 = BRL 200,00 (depósito do empregador)

2ª parcela (até 20 de dezembro):
  Restante: BRL 2.500,00
  INSS sobre o 13º integral (5.000): − BRL 501,52
  IRRF sobre (5.000 − 501,52) = 4.498,48: − BRL 349,39
  Líquido da 2ª parcela: BRL 2.500 − 501,52 − 349,39 = BRL 1.649,09
  FGTS: 8% × 2.500 = BRL 200,00
```

### Padrão 4: Rescisão Sem Justa Causa

**Padrão 4: Rescisão Sem Justa Causa**

| Componente | Cálculo |
| --- | --- |
| Saldo de salário | Dias trabalhados / 30 × salário mensal |
| 13º proporcional | Meses trabalhados / 12 × salário |
| Férias proporcionais + 1/3 | Meses desde o último período aquisitivo / 12 × salário × 4/3 |
| Férias vencidas + 1/3 (se houver) | Salário integral × 4/3 |
| Aviso prévio | 30 dias + 3 por ano de serviço (máx. 90 dias) |
| Multa de 40% do FGTS | 40% do saldo total do FGTS (empregador deposita na conta de FGTS do empregado) |
| FGTS sobre verbas rescisórias | 8% sobre todos os valores rescisórios |

## Seção 10 — Interação com Outras Skills

**Interação com Outras Skills**

| Skill | Interação |
| --- | --- |
| brazil-einvoice | Sem interação direta (NF-e é para mercadorias/serviços; folha utiliza eSocial) |
| payroll-workflow-base | Fluxo geral de processamento de folha; especificidades do Brasil tratadas nesta skill |

### Particularidades da Folha no Brasil

- **Regime CLT**: Todos os empregados formais (celetistas) são regidos pela CLT. Trabalhadores informais (MEI, autônomos, PJ) têm regras de contribuição inteiramente distintas.
- **eSocial é obrigatório**: TODOS os eventos da folha devem fluir pelo eSocial. Não há método alternativo de transmissão para empregadores CLT.
- **Transição para o FGTS Digital**: Entre 2024-2025, os depósitos de FGTS migraram para o FGTS Digital (integrado ao eSocial). SEFIP/GFIP somente para acertos de períodos anteriores.
- **Irredutibilidade salarial**: Pela CLT, o salário nominal não pode ser reduzido (princípio da irredutibilidade salarial), nem mesmo por acordo individual, salvo via negociação coletiva.
- **Contribuição sindical**: Desde a Reforma Trabalhista de 2017, a contribuição sindical é facultativa. O empregado deve autorizar expressamente.
- **Convenções e acordos coletivos**: Convenções coletivas e acordos coletivos podem estabelecer pisos, benefícios adicionais e banco de horas. SEMPRE verifique a convenção aplicável por CNAE/sindicato.
- **Férias fracionadas**: Após a Reforma Trabalhista de 2017, as férias podem ser fracionadas em até 3 períodos (mínimo de 14 dias para um deles, 5 dias para os demais).
- **Simples Nacional**: Microempresas e empresas de pequeno porte no Simples Nacional possuem regras distintas de INSS patronal (incluído no DAS unificado).
- **RAT/FAP**: A alíquota efetiva de acidente de trabalho depende do histórico de acidentes da própria empresa (multiplicador FAP publicado anualmente pelo governo). Sempre verifique o FAP vigente antes de calcular o INSS patronal.

## Aviso Legal

Esta skill e seus resultados são fornecidos exclusivamente para fins informativos e de cálculo e não constituem assessoria tributária, jurídica ou financeira. A Open Accountants e seus colaboradores não se responsabilizam por erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e validados por um profissional habilitado antes de qualquer entrega ou tomada de decisão.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com).

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
