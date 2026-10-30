---
name: portugal-tax-optimization
description: "Utilize esta skill ao aconselhar sobre estratégias LEGAIS de minimização fiscal para contribuintes portugueses no ano fiscal de 2026: particulares, trabalhadores independentes (recibos verdes) e pequenos empresários. Acione com expressões como \"reduzir o meu imposto Portugal\", \"planeamento fiscal\", \"regime simplificado\", \"contabilidade organizada\", \"optimização do IRS\", \"segurança social trabalhador independente\", \"IVA\", \"recibos verdes\", \"Categoria B\", \"deduções Portugal\", ou qualquer questão sobre minimização legal do IRS ou IRC português. Cobre selecção de entidade, regime simplificado vs contabilidade organizada, tributação conjunta, IRS Jovem, deduções à coleta, amortizações, utilização de prejuízos, timing, optimização do IVA, segurança social, PPR, englobamento e linhas vermelhas (cláusula geral anti-abuso). Fora do âmbito, ver: pt-income-tax (cálculo da Categoria B), pt-irs-employees-investment (Categorias A, E, F, G, H), pt-nhr-ifici, pt-social-contributions, portugal-vat-return, pt-corporate-tax, portugal-crypto-tax. LEIA SEMPRE esta skill antes de prestar aconselhamento de optimização fiscal portuguesa. Trigger also on: \"reduce my tax Portugal\", \"tax planning\", \"regime simplificado\", \"organized accounts\", \"IRS optimization\", \"social security self-employed\", \"IVA\", \"recibos verdes\", \"Category B\", \"deductions Portugal\"."
version: 1.3
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Tax Optimization

## Portugal: Optimização Fiscal, Skill v1.3 (ano fiscal 2026)

> Source-cited draft: not reviewed by an accountant.

Esta skill reúne as alavancas legais de planeamento fiscal em Portugal para 2026. Não repete os cálculos completos: liga às skills de domínio do mesmo pacote, que mandam quando os números divergem.

- `pt-income-tax`: IRS da Categoria B (coeficientes, regra dos 15%, IRS Jovem, retenções, pagamentos por conta).
- `pt-irs-employees-investment`: Categorias A, E, F, G e H, deduções à coleta, mínimo de existência, englobamento.
- `pt-nhr-ifici`: residentes não habituais (RNH) e IFICI.
- `pt-social-contributions`: Segurança Social dos trabalhadores independentes.
- `portugal-vat-return`: IVA, isenção do art. 53.º, declarações periódicas.
- `pt-corporate-tax`: IRC, derramas, tributações autónomas, prejuízos.
- `portugal-crypto-tax`: criptoativos.

Todos os valores abaixo foram lidos no texto consolidado publicado pela AT no Portal das Finanças, ou no Guia Prático da Segurança Social, em 30 de outubro de 2026. As fontes estão na secção final.

## Rates and thresholds

### Otimização Fiscal (resumo 2026)

- **Despesas gerais familiares**: 35% das faturas com NIF, máx. €250 por sujeito passivo; famílias monoparentais 45%, máx. €335 _(CIRS art. 78.º-B, n.os 1 e 9)_
- **Saúde**: 15% das despesas, máx. €1.000 por agregado _(CIRS art. 78.º-C, n.º 1)_
- **Educação e formação**: 30% das despesas, máx. €800 por agregado _(CIRS art. 78.º-D, n.º 1)_
- **Habitação (renda da habitação própria e permanente)**: 15% das rendas, máx. €900 em 2026 _(CIRS art. 78.º-E, n.os 1 a) e 10; Decreto-Lei 97/2026, art. 15.º, n.º 1)_
- **Habitação (juros)**: 15%, máx. €296, apenas contratos celebrados até 31 de dezembro de 2011 (até €450 para rendimentos coletáveis baixos) _(CIRS art. 78.º-E, n.os 1 b) e 4)_
- **Lares**: 25% dos encargos, máx. €403,75 _(CIRS art. 84.º, n.º 1)_
- **Pensões de alimentos**: 20% dos montantes fixados por sentença ou acordo homologado _(CIRS art. 83.º-A, n.º 1)_
- **IVA em faturas**: 15% do IVA (restauração, cabeleireiros, oficinas, veterinários e outros setores da lei), máx. €250 por agregado _(CIRS art. 78.º-F, n.º 1)_
- **Depreciações**: taxas genéricas da Tabela II do Decreto Regulamentar 25/2009 (ver Secção 4; taxas por confirmar)
- **PPR, dedução IRS**: 20% das entregas, máx. €400 (menos de 35 anos), €350 (35 a 50 anos), €300 (mais de 50 anos) _(EBF art. 21.º, n.º 2)_
- **Juros de depósitos**: taxa liberatória de 28%, ou englobamento por opção _(CIRS art. 71.º, n.os 1 e 9)_
- **Dividendos (englobamento)**: só 50% incluídos no rendimento _(CIRS art. 40.º-A, n.º 1)_
- **Mais-valias mobiliárias**: taxa autónoma de 28% sobre o saldo; exclusão de 10%, 20% ou 30% para ativos detidos mais de 2, 5 ou 8 anos; perdas reportáveis 5 anos se houver englobamento _(CIRS art. 72.º, n.º 1 c); art. 43.º, n.º 5; art. 55.º, n.º 1 d))_
- **Mais-valias imobiliárias**: 50% do saldo incluído no rendimento; reinvestimento na habitação própria e permanente entre 24 meses antes e 36 meses depois da venda _(CIRS art. 43.º, n.º 2 b); art. 10.º, n.º 5)_
- **Rendas (Cat. F)**: taxa autónoma de 25% no arrendamento habitacional e 28% nos restantes casos, ou englobamento _(CIRS art. 72.º, n.os 1 e) e 2)_

## Secção 1: Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Ano fiscal | Ano civil (1 de janeiro a 31 de dezembro) |
| Legislação primária | Código do IRS (CIRS); Código do IRC (CIRC); Código do IVA (CIVA); Código dos Regimes Contributivos (Lei 110/2009); Estatuto dos Benefícios Fiscais (EBF) |
| Anti-abuso | Cláusula geral anti-abuso: art. 38.º, n.º 2, da Lei Geral Tributária (LGT); procedimento no art. 63.º do CPPT |
| Autoridade fiscal | Autoridade Tributária e Aduaneira (AT) |
| Prazo de entrega | 1 de abril a 30 de junho do ano seguinte, por via eletrónica (Modelo 3; CIRS art. 60.º, n.º 1). Rendimentos de 2026: 1 de abril a 30 de junho de 2027 |
| Taxa marginal máxima (pessoas singulares) | 48% (acima de €86.634) mais taxa adicional de solidariedade de 5% acima de €250.000, ou seja até 53% (CIRS art. 68.º e 68.º-A) |
| Taxa de IRC (sociedades) | 19% nos períodos iniciados em 2026 (Lei 64/2025, art. 3.º, n.º 2); 15% sobre os primeiros €50.000 de matéria coletável para PME e Small Mid Cap (CIRC art. 87.º, n.º 2). Ver `pt-corporate-tax` |
| Taxas de IVA | Continente 6%, 13% e 23% (CIVA art. 18.º, n.º 1). Açores 4%, 9% e 16%; Madeira 4%, 12% e 22% (ver `portugal-vat-return`) |
| Segurança social (trabalhador independente) | 21,4% (25,2% para empresários em nome individual e titulares de EIRL) sobre o rendimento relevante |
| IAS 2026 | €537,13 |

### Escalões de IRS (2026)

**Escalões de IRS (2026)**: CIRS art. 68.º, n.º 1, na redação da Lei 73-A/2025.

| Escalão | Rendimento coletável (€) | Taxa normal (A) | Taxa média (B) |
| --- | --- | --- | --- |
| 1 | Até 8.342 | 12,50% | 12,500% |
| 2 | Mais de 8.342 até 12.587 | 15,70% | 13,579% |
| 3 | Mais de 12.587 até 17.838 | 21,20% | 15,823% |
| 4 | Mais de 17.838 até 23.089 | 24,10% | 17,705% |
| 5 | Mais de 23.089 até 29.397 | 31,10% | 20,579% |
| 6 | Mais de 29.397 até 43.090 | 34,90% | 25,130% |
| 7 | Mais de 43.090 até 46.566 | 43,10% | 26,472% |
| 8 | Mais de 46.566 até 86.634 | 44,60% | 34,856% |
| 9 | Superior a 86.634 | 48,00% | (não aplicável) |

Como a AT calcula (art. 68.º, n.º 2): o limite do maior escalão que cabe no rendimento é tributado à taxa média (B) desse escalão; o excedente é tributado à taxa normal (A) do escalão seguinte. Exemplo: €35.000 = 29.397 × 20,579% + (35.000 - 29.397) × 34,90% = €8.005,06.

- **Taxa adicional de solidariedade**: 2,5% sobre a parte do rendimento coletável entre €80.000 e €250.000; 5% acima de €250.000 _(CIRS art. 68.º-A, n.os 1 e 2)_
- **Mínimo de existência (2026)**: valor de referência igual ao maior entre €12.880 e 1,5 × 14 × IAS (€11.279,73), ou seja €12.880 _(CIRS art. 70.º, n.º 1)_. Aplica-se a quem tem rendimentos sobretudo de trabalho, pensões ou atividades da tabela do art. 151.º. A fórmula completa está em `pt-irs-employees-investment`.

## Secção 2: Repartição de Rendimentos e Estruturação

### Empresário em Nome Individual (ENI) vs Sociedade (Lda)

- **Regime simplificado**: aplica-se a quem não ultrapassou €200.000 de rendimentos da Categoria B no ano anterior _(CIRS art. 28.º, n.º 2)_. Rendimento tributável = bruto × coeficiente: 0,75 para as atividades profissionais da tabela do art. 151.º; 0,35 para outras prestações de serviços; 0,15 para vendas de mercadorias e produtos, restauração, bebidas e hotelaria _(CIRS art. 31.º, n.º 1 a), b) e c))_. Outros coeficientes (0,95, 0,30, 0,10, 1 e 0,50) estão em `pt-income-tax`. Não se deduzem despesas reais além do coeficiente. Para os coeficientes 0,75 e 0,35 aplica-se a regra dos 15% (Secção 3).
- **Primeiros anos de atividade**: os coeficientes das alíneas b), c) e f) são reduzidos em 50% no ano de início e em 25% no ano seguinte, se não houver rendimentos das Categorias A ou H nesse ano; não se aplica se a atividade cessou há menos de 5 anos _(CIRS art. 31.º, n.os 10 e 11; ver `pt-income-tax`)_.
- **Contabilidade organizada**: obrigatória quando o limite de €200.000 é ultrapassado; opcional abaixo. A opção ou mudança de regime faz-se até ao fim de março do ano em que produz efeitos _(CIRS art. 28.º, n.os 4 e 5; ver `pt-income-tax`)_. Deduz despesas reais e a Segurança Social por inteiro. Requer contabilista certificado (CC). Compensa quando as despesas reais documentadas excedem a margem implícita no coeficiente (Exemplo 1).
- **Sociedade (Sociedade Unipessoal por Quotas, Lda, ou SA)**: IRC a 19% em 2026, com 15% sobre os primeiros €50.000 para PME _(CIRC art. 87.º, n.º 2; Lei 64/2025, art. 3.º)_. Acrescem derramas e tributações autónomas (ver `pt-corporate-tax`). Os lucros distribuídos a sócios residentes pagam 28% de taxa liberatória _(CIRS art. 71.º, n.º 1)_ ou, por opção de englobamento, entram em apenas 50% nos escalões progressivos _(CIRS art. 40.º-A, n.º 1)_.
- **Regra de decisão (quadro de comparação de regimes)**: Cat. B simplificado: melhor para quem tem poucas despesas reais (o coeficiente 0,75 já assume 25% de custos). Cat. B organizada: mudar quando as despesas documentadas (incluindo a Segurança Social acima de 10% do bruto) excedem essa margem e os honorários do contabilista. Lda: comparar, para o mesmo lucro, IRS + Segurança Social do ENI com IRC + derramas + 28% sobre o dividendo + custos de contabilidade, tributações autónomas e formalismos societários. Simular sempre os dois cenários com os números do cliente.

### Tributação Conjunta

Casados e unidos de facto são tributados separadamente por defeito. Podem optar pela tributação conjunta todos os anos; ambos fazem a opção na declaração _(CIRS art. 59.º; ver `pt-irs-employees-investment`)_. Na tributação conjunta as taxas aplicam-se ao rendimento coletável dividido por dois e o resultado é multiplicado por dois _(CIRS art. 69.º, n.os 1 e 3)_. A divisão por dois favorece casais com rendimentos muito desiguais (Exemplo 2). Atenção: na tributação separada os limites das deduções por agregado são divididos entre os cônjuges, e o limite global das deduções do art. 78.º, n.º 7, depende do rendimento coletável. Simular os dois cenários no Portal das Finanças.

### IRS Jovem

Quem tem até 35 anos e não é dependente pode isentar parte dos rendimentos das Categorias A e B nos primeiros 10 anos de obtenção de rendimentos, por opção na declaração _(CIRS art. 12.º-B, n.º 1)_. A isenção é de 100% no 1.º ano, 75% do 2.º ao 4.º, 50% do 5.º ao 7.º e 25% do 8.º ao 10.º, com o limite de 55 × IAS = €29.542,15 por ano em 2026 _(CIRS art. 12.º-B, n.º 5)_. Não está disponível para quem teve RNH ou IFICI. Cálculo em `pt-income-tax`.

### RNH / IFICI

Para optimização sob RNH/IFICI ver skill `pt-nhr-ifici`.

## Secção 3: Deduções que a Maioria Esquece (Optimização equivalente a PTKP)

### Deduções à Coleta: CIRS art. 78.º a 78.º-F, 83.º-A e 84.º

**Deduções à Coleta (2026)**

| Categoria | Dedução | Limite | Fonte |
| --- | --- | --- | --- |
| Despesas gerais familiares | 35% das faturas com NIF (45% em famílias monoparentais) | €250 por sujeito passivo (€335 monoparental) | Art. 78.º-B, n.os 1 e 9 |
| Saúde | 15% das despesas de saúde | €1.000 por agregado | Art. 78.º-C, n.º 1 |
| Educação e formação | 30% das despesas | €800 por agregado (mais até €300 para renda de estudante deslocado, máx. €400 de renda) | Art. 78.º-D, n.º 1 |
| Habitação: renda | 15% das rendas da habitação própria e permanente | €900 em 2026 (o novo limite de €1.000 só se aplica a partir de 2027) | Art. 78.º-E, n.os 1 a) e 10; DL 97/2026, art. 15.º, n.º 1 |
| Habitação: juros | 15% dos juros, só contratos até 31 de dezembro de 2011 | €296 (€450 para rendimento coletável até ao 1.º escalão) | Art. 78.º-E, n.os 1 b) e 4 |
| Lares | 25% dos encargos com lares e apoio domiciliário | €403,75 | Art. 84.º, n.º 1 |
| Pensão de alimentos | 20% dos montantes fixados por sentença ou acordo homologado, se o beneficiário não fizer parte do agregado | Conta para o limite global do art. 78.º, n.º 7 | Art. 83.º-A, n.º 1 |
| IVA em faturas (e-fatura) | 15% do IVA em restauração e alojamento, cabeleireiros, oficinas auto e moto, veterinários e outros setores; 100% do IVA dos passes de transportes públicos; 30% em ginásios e clubes desportivos; 35% em medicamentos veterinários | €250 por agregado | Art. 78.º-F, n.os 1, 3, 6 e 8 |
| PPR | 20% das entregas | €400 / €350 / €300 conforme a idade | EBF art. 21.º, n.º 2 |
| Donativos | Regime do EBF | Por confirmar | Ver "Not yet confirmed" |

O limite global das deduções de saúde, educação, habitação, pensões de alimentos, IVA em faturas e lares depende do rendimento coletável _(CIRS art. 78.º, n.º 7)_; as despesas gerais familiares e os dependentes ficam fora desse limite. Ver `pt-irs-employees-investment`.

As faturas comunicadas à AT até ao fim de fevereiro do ano seguinte contam para as deduções _(art. 78.º-B, n.º 5)_. A AT mostra os valores até 15 de março e o contribuinte pode reclamar até 31 de março _(art. 78.º-B, n.os 6 e 7)_. Um trabalhador independente só deduz como despesas pessoais as faturas fora da sua atividade _(art. 78.º-B, n.º 4)_.

### Deduções Específicas da Categoria B (Contabilidade Organizada)

- **Deduções Específicas da Categoria B**: em contabilidade organizada, o lucro tributável segue as regras do IRC. Deduzem-se gastos reais: renda de escritório, equipamento, serviços profissionais, deslocações, formação, telecomunicações, seguros, depreciações e a Segurança Social obrigatória. Os gastos têm de ser indispensáveis à atividade e documentados.

### Regime Simplificado: Regra de Justificação dos 15%

- **Regra de Justificação dos 15%**: para os coeficientes 0,75 e 0,35, acresce ao rendimento tributável a diferença positiva entre 15% do bruto dessas prestações de serviços e a soma de _(CIRS art. 31.º, n.º 13)_:
  - a) €4.587,09 (dedução específica da Categoria A, 8,54 × IAS) ou, se maior, as contribuições obrigatórias para a Segurança Social não deduzidas ao abrigo do art. 31.º, n.º 2;
  - b) despesas com pessoal comunicadas à AT;
  - c) rendas de imóveis afetos à atividade, em faturas comunicadas;
  - d) 1,5% do valor patrimonial tributário (VPT) dos imóveis próprios afetos à atividade (4% em hotelaria e alojamento local);
  - e) outras despesas da atividade em faturas comunicadas à AT (materiais, eletricidade, água, comunicações, deslocações e outras);
  - f) importações e aquisições intracomunitárias da atividade.
- **Uso misto**: rendas, imóveis e outras despesas só parcialmente afetos à atividade contam a 25% _(art. 31.º, n.º 14)_.
- **Afetação**: as faturas e os imóveis afetos à atividade identificam-se no Portal das Finanças até ao fim de fevereiro do ano seguinte _(art. 31.º, n.º 15)_.
- **Segurança Social**: no simplificado, com coeficientes 0,75 e 0,35, deduzem-se as contribuições obrigatórias da atividade na parte que exceda 10% do bruto, até ao rendimento líquido _(art. 31.º, n.º 2)_.

Peça sempre NIF em todas as compras profissionais. A diferença entre €4.587,09 e 15% do bruto é o valor que deve evidenciar com faturas. Exemplo: bruto de €40.000 dá 15% = €6.000; faltam €1.412,91 em despesas comunicadas para não haver acréscimo.

## Secção 4: Optimização de Amortizações

### Amortizações: Contabilidade Organizada

**Amortizações: Contabilidade Organizada** _(Decreto Regulamentar 25/2009)_

As depreciações aceites fiscalmente usam as taxas específicas da Tabela I (por setor) ou, na falta delas, as taxas genéricas da Tabela II anexas ao Decreto Regulamentar 25/2009. A cópia da AT lida hoje não reproduz as tabelas ("ver documento original"), por isso as taxas por categoria da versão anterior desta skill (edifícios, mobiliário, equipamento informático, software, viaturas, equipamento básico) passam para "Not yet confirmed". Confirmar na Tabela II do Diário da República antes de usar.

| Categoria de Ativo | Taxa |
| --- | --- |
| Edifícios (comerciais e industriais) | Tabela II do DR 25/2009 (por confirmar) |
| Mobiliário de escritório | Tabela II do DR 25/2009 (por confirmar) |
| Equipamento informático | Tabela II do DR 25/2009 (por confirmar) |
| Software | Tabela II do DR 25/2009 (por confirmar) |
| Viaturas ligeiras de passageiros | Tabela II do DR 25/2009 (por confirmar) |
| Equipamento básico | Tabela I ou II do DR 25/2009 (por confirmar) |
| Equipamentos de energia solar, fotovoltaica ou eólica (código 2250) | 8% (Tabela II, redação da Lei 82-D/2014) |

- **Limite amortização viaturas**: não são aceites as depreciações de viaturas ligeiras de passageiros ou mistas, incluindo elétricas, na parte do custo de aquisição que excede o montante fixado por portaria _(CIRC art. 34.º, n.º 1 e); DR 25/2009, art. 11.º)_. Os montantes da portaria (Portaria 467/2010, com alterações) não foram lidos hoje: ver "Not yet confirmed". As viaturas também pagam tributação autónoma (ver `pt-corporate-tax`).

### Regime Simplificado

- **Regime Simplificado**: não há depreciações autónomas. O coeficiente substitui todas as despesas. Comprar um ativo não gera dedução adicional, salvo na regra dos 15% se a fatura for de despesa da atividade.

### Reinvestimento de Mais-Valias (IRC, Sociedades)

- **Reinvestimento de Mais-Valias (IRC)**: o saldo positivo entre mais-valias e menos-valias na venda de ativos fixos tangíveis, intangíveis e biológicos não consumíveis, detidos há pelo menos um ano, conta apenas em metade, quando o valor de realização é reinvestido em ativos elegíveis no período anterior, no próprio período ou até ao fim do 2.º período seguinte _(CIRC art. 48.º, n.º 1)_. Também se aplica à Categoria B por remissão: se o reinvestimento não acontecer até ao fim do 2.º período seguinte, a diferença acresce ao rendimento desse período _(CIRS art. 31.º, n.º 6)_.

## Secção 5: Utilização de Prejuízos

### Prejuízos da Categoria B (Trabalhadores Independentes)

- **Prejuízos da Categoria B**: o resultado líquido negativo da Categoria B reporta-se aos 12 anos seguintes, apenas contra resultados positivos da Categoria B _(CIRS art. 55.º, n.º 1 a))_. No regime simplificado não se geram prejuízos, porque o coeficiente produz sempre rendimento positivo; mas prejuízos anteriores à entrada no simplificado podem ser deduzidos nesse regime _(art. 55.º, n.º 4)_.
- **Restrição-chave**: o resultado negativo de qualquer categoria só se deduz a resultados positivos da mesma categoria _(art. 55.º, n.º 1)_. Um prejuízo da Categoria B não reduz o salário (Categoria A), os rendimentos de capitais (Categoria E) nem outras categorias.

### Prejuízos da Categoria F (Rendas)

- O resultado negativo da Categoria F reporta-se aos 6 anos seguintes _(art. 55.º, n.º 1 b))_. O reporte perde-se se o imóvel não gerar rendas durante pelo menos 36 meses, seguidos ou interpolados, nos 5 anos seguintes _(art. 55.º, n.º 8)_.

### IRC (Sociedades)

- **IRC (Sociedades): Prejuízos**: os prejuízos fiscais deduzem-se aos lucros tributáveis de um ou mais períodos posteriores, sem limite de tempo, nas deduções feitas em períodos iniciados a partir de 1 de janeiro de 2023, incluindo prejuízos anteriores cujo prazo ainda corria nessa data _(CIRC art. 52.º, n.º 1; Lei 24-D/2022, art. 228.º, n.º 1)_. A dedução de cada ano não pode exceder 65% do lucro tributável desse ano; a parte não deduzida passa para os anos seguintes _(art. 52.º, n.º 2)_. O limite sobe 10 pontos (75%) quando a diferença resulta de prejuízos de 2020 e 2021 _(Lei 27-A/2020, art. 11.º, n.º 2)_. Prejuízos anteriores a 2023 de períodos abrangidos pelo REAID (art. 6.º, n.º 1, da Lei 61/2014) mantêm o prazo em vigor em 31 de dezembro de 2022 _(Lei 24-D/2022, art. 228.º, n.º 2)_. Os prejuízos perdem-se se mudar a titularidade de mais de 50% do capital ou a maioria dos direitos de voto, salvo as exceções do n.º 9 ou razões económicas válidas _(art. 52.º, n.os 8 e 9)_. Ver a skill `pt-corporate-tax`.

### Menos-Valias (Categoria G)

- **Menos-Valias mobiliárias (Categoria G)**: o saldo negativo de ações, outros valores mobiliários, derivados e criptoativos reporta-se aos 5 anos seguintes só quando o contribuinte opta pelo englobamento ou é obrigado a ele _(CIRS art. 55.º, n.º 1 d))_. Quem fica na taxa autónoma de 28% não reporta perdas.
- **Menos-valias imobiliárias**: a parte do saldo negativo incluída nos termos do art. 43.º, n.º 2, reporta-se aos 5 anos seguintes _(art. 55.º, n.º 1 c))_.

## Secção 6: Estratégias de Timing

**Estratégias de Timing**

| Estratégia | Detalhe |
| --- | --- |
| Pagamentos por conta de IRS | Quem tem rendimentos da Categoria B faz três pagamentos por conta até 20 de julho, 20 de setembro e 20 de dezembro. O total é 65% do valor da fórmula legal, e um pagamento abaixo de €50 não é exigível (CIRS art. 102.º, n.os 1 a 3). Se as retenções e pagamentos já feitos cobrirem o imposto do ano, ou a atividade parar, pode deixar de pagar; pode também reduzi-los, mas se ficar por pagar mais de 20% do normal há juros compensatórios (art. 102.º; ver `pt-income-tax`) |
| Diferir faturação para janeiro | Em regime simplificado e perto do limite de €200.000 (medido no ano anterior, art. 28.º, n.º 2), o timing decide o regime do ano seguinte. Também desloca rendimento para o ano fiscal seguinte. Só é legítimo se a prestação também ocorrer depois; a fatura segue as regras de emissão do IVA |
| Antecipar despesas antes do fim do ano | Em contabilidade organizada: adquirir equipamento, pagar serviços, regularizar faturas em aberto antes de 31 de dezembro. No simplificado, faturas de despesas da atividade ajudam a cumprir a regra dos 15% |
| Validação e-fatura | Confirmar que todas as faturas com NIF estão comunicadas e classificadas no Portal das Finanças até ao fim de fevereiro (CIRS art. 78.º-B, n.º 5; art. 31.º, n.º 15). Maximiza as deduções à coleta e a regra dos 15% |
| Tributação conjunta vs separada | Simular ambos os cenários todos os anos. Especialmente vantajosa quando um dos cônjuges não tem rendimento ou tem rendimento baixo |
| Atualização da base contributiva | A declaração trimestral à Segurança Social (até ao fim de janeiro, abril, julho e outubro) atualiza a base dos três meses seguintes. Se o rendimento descer, a base desce na declaração seguinte. Pode também ajustar a base em 25% para cima ou para baixo, em escalões de 5% (ver Secção 8) |
| Diferimento de mais-valias | Reinvestir o valor da venda em nova habitação própria e permanente entre 24 meses antes e 36 meses depois da venda (CIRS art. 10.º, n.º 5) para excluir a mais-valia |
| Prazo de detenção | Ações e fundos detidos mais de 2, 5 ou 8 anos excluem 10%, 20% ou 30% do ganho (art. 43.º, n.º 5). Criptoativos detidos 365 dias ou mais ficam fora de tributação (art. 10.º, n.º 22). Vender um pouco mais tarde muda o imposto |

## Secção 7: Optimização do IVA

**Optimização do IVA**

| Tópico | Detalhe |
| --- | --- |
| Limiar de isenção | Volume de negócios em território nacional no ano civil anterior até €15.000, sem exportações ou atividades conexas: isento ao abrigo do art. 53.º, n.º 1, do CIVA. Não liquida IVA nem deduz IVA. Rever todos os anos |
| Saída da isenção | A isenção termina no ano seguinte se o limiar for ultrapassado, e de imediato se no ano em curso o limiar for excedido em mais de 25% (€18.750) (CIVA art. 58.º, n.º 2 b) e n.º 4 b); ver `portugal-vat-return`) |
| Registo acima do limiar | Regime normal com declarações periódicas: trimestrais se o volume de negócios do ano anterior foi inferior a €650.000, mensais se igual ou superior; entrega até ao dia 20 do 2.º mês seguinte ao período (CIVA art. 41.º, n.º 1). Pode recuperar IVA em aquisições profissionais |
| Regime simplificado de IVA | Para prestadores de serviços e pequenos comerciantes, a alternativa ao regime normal é a isenção do art. 53.º. Outros regimes especiais não foram revistos hoje |
| Taxas | Continente 6%, 13% e 23% (CIVA art. 18.º, n.º 1). Açores 4%, 9% e 16%. Madeira 4%, 12% e 22% (ver `portugal-vat-return`) |
| Planeamento da dedução do IVA | No regime normal, deduzir o IVA das despesas da atividade. Bens de uso misto: método da afetação real ou pro rata (ver `portugal-vat-return`) |
| IVA em serviços transfronteiriços | Serviços B2B a sujeitos passivos com sede noutro Estado membro: o lugar da prestação é o do adquirente (regra geral do CIVA art. 6.º, n.º 6 a)). Não liquida IVA português; o cliente autoliquida no seu país. Confirmar o número no VIES |
| Declaração recapitulativa | As prestações de serviços a sujeitos passivos de outros Estados membros são indicadas na declaração recapitulativa do art. 23.º do RITI, nos prazos do art. 30.º do RITI (CIVA art. 29.º, n.º 1 i)) |

## Secção 8: Optimização da Segurança Social

### Contribuições dos Trabalhadores Independentes

- **Taxa**: 21,4% para trabalhadores independentes e respetivos cônjuges ou unidos de facto; 25,2% para empresários em nome individual e titulares de EIRL e respetivos cônjuges _(Guia Prático da Segurança Social, 2026)_
- **Cálculo do rendimento relevante**: trimestral, com base nos rendimentos do trimestre anterior: 70% das prestações de serviços; 20% das vendas de bens e dos serviços de hotelaria, restauração e bebidas declarados como tal. A base mensal é um terço do rendimento relevante do trimestre.
- **Mínimo**: sem rendimentos, ou com contribuição abaixo de €20,00, a base é fixada para dar €20,00 por mês.
- **Limite máximo**: a base de incidência mensal tem o limite de 12 × IAS = €6.445,56 (IAS 2026 = €537,13).
- **Declaração e pagamento**: declaração trimestral até ao fim de janeiro, abril, julho e outubro; pagamento todos os meses entre o dia 10 e o dia 20 do mês seguinte.
- **Contabilidade organizada**: a base é o lucro tributável do ano anterior (ver `pt-social-contributions`).

### Isenções e Reduções

**Isenções e Reduções**

| Situação | Tratamento |
| --- | --- |
| Primeiros 12 meses de atividade | Na primeira inscrição como independente, o enquadramento só produz efeitos no 1.º dia do 12.º mês após o início de atividade. Até lá não há contribuições, salvo pedido de enquadramento antecipado. Num reinício, o enquadramento começa no 1.º dia do mês do reinício |
| Meses 13 a 24 | A redução de 50% indicada na versão anterior não foi encontrada no Guia Prático lido hoje. A partir do enquadramento aplica-se a regra geral (ver "Not yet confirmed") |
| Acumulação trabalho dependente + independente | Isento como independente se o rendimento relevante médio mensal for inferior a 4 × IAS = €2.148,52 e o trabalho por conta de outrem for para outra entidade, com remuneração média de pelo menos 1 × IAS (€537,13). Acima de €2.148,52, contribui sobre o excedente |
| Pensionista | Isento se recebe pensão de invalidez ou velhice (nacional ou estrangeira), nas condições do Guia Prático |
| Cônjuge do empresário | O cônjuge ou unido de facto que trabalha com o independente fica abrangido pelo mesmo regime, à taxa de 21,4% (25,2% no caso de ENI ou EIRL). A alternativa de contratar o cônjuge como trabalhador por conta de outrem não foi revista hoje |

### Estratégias de Optimização

- **Início de atividade**: na primeira inscrição, os primeiros 12 meses não pagam contribuições. No IRS, os coeficientes também são reduzidos nos dois primeiros anos (Secção 2). Planear o arranque com estes dois efeitos.
- **Acumulação trabalho dependente + freelance**: manter um contrato de trabalho com outra entidade pode isentar o rendimento freelance até 4 × IAS de rendimento relevante médio por mês.
- **Ajuste da base**: o independente pode escolher uma base até 25% acima ou abaixo do valor apurado, em escalões de 5%, entre €20,00 e 12 × IAS. Uma base mais alta custa mais e aumenta as prestações futuras; uma mais baixa poupa hoje e reduz a proteção. Decidir com o cliente.
- **Entidades contratantes**: a empresa que recebe mais de 50% da atividade do independente paga uma contribuição própria sobre os serviços (taxas em `pt-social-contributions`). Diversificar clientes evita esse custo para o cliente, mas não pode disfarçar trabalho dependente.
- **PPR (Plano Poupança Reforma)**: dedução à coleta de 20% das entregas, com limite de €400 (menos de 35 anos), €350 (35 a 50 anos) e €300 (mais de 50 anos), por sujeito passivo; a idade conta a 1 de janeiro do ano da entrega; entregas depois da reforma não dão dedução _(EBF art. 21.º, n.os 2, 9 e 10)_.

## Secção 9: Investimento e Reforma

**Investimento e Reforma**

| Instrumento | Tratamento Fiscal |
| --- | --- |
| PPR (Plano Poupança Reforma) | Dedução à coleta de 20% das entregas, com limite por idade (EBF art. 21.º, n.º 2). No reembolso total ou parcial nas condições da lei, a matéria coletável é 2/5 do rendimento, tributado autonomamente a 20%, ou seja 8% efetivos (art. 21.º, n.º 3 b)). Reembolso fora das situações legais: a dedução é devolvida com mais 10% por cada ano decorrido, salvo após 5 anos (art. 21.º, n.º 4), e o rendimento paga 21,5% (art. 21.º, n.º 5) |
| Juros de depósitos | Taxa liberatória de 28% ou opção pelo englobamento (CIRS art. 71.º, n.os 1 e 9). Englobamento compensa se a taxa marginal for inferior a 28% |
| Dividendos (sociedades portuguesas) | Taxa liberatória de 28%. Se optar pelo englobamento, apenas 50% entram no rendimento (art. 40.º-A, n.º 1): no escalão máximo, 50% × 48% = 24%, antes da taxa de solidariedade |
| Mais-valias: valores mobiliários | Taxa autónoma de 28% sobre o saldo (art. 72.º, n.º 1 c)); exclusão de 10%, 20% ou 30% do ganho para títulos e fundos detidos mais de 2, 5 ou 8 anos (art. 43.º, n.º 5). Englobamento opcional (art. 72.º, n.º 13); obrigatório para ganhos de ativos detidos menos de 365 dias quando o rendimento coletável, incluindo o ganho, atinge o último escalão (art. 72.º, n.º 14). Menos-valias: Secção 5 |
| Mais-valias: imóveis | 50% do saldo incluído no rendimento e tributado às taxas progressivas (art. 43.º, n.º 2 b)). Exclusão por reinvestimento em habitação própria e permanente (art. 10.º, n.º 5). Se o valor declarado for inferior ao valor considerado para IMT, prevalece este (art. 44.º, n.º 2) |
| Rendimentos prediais (Categoria F) | Taxa autónoma de 25% no arrendamento habitacional, 28% nos outros (art. 72.º, n.os 1 e) e 2); taxas reduzidas para contratos longos em `pt-irs-employees-investment`. Deduzem-se os gastos suportados para obter as rendas, como IMI, condomínio, seguros e conservação, mas não gastos financeiros, depreciações, mobiliário e eletrodomésticos, nem o AIMI (art. 41.º, n.º 1). Não há amortização do edifício na Categoria F |
| Criptoativos | Ganhos de criptoativos detidos menos de 365 dias: 28% (art. 72.º, n.º 1 c)). Detidos 365 dias ou mais: ganhos e perdas excluídos (art. 10.º, n.º 22). Ver `portugal-crypto-tax` |

### Estratégia de Englobamento

- **Estratégia de Englobamento**: optar pelo englobamento (inclusão nos escalões progressivos) reduz o imposto sobre rendimentos de capitais, rendas ou mais-valias quando a taxa marginal é inferior à taxa autónoma (28%, ou 25% nas rendas habitacionais). Mas o englobamento é tudo ou nada por categoria: quem engloba um rendimento engloba todos os da mesma categoria _(CIRS art. 22.º, n.º 5)_. O englobamento também aumenta o rendimento coletável, o que reduz o limite global das deduções e pode afastar o mínimo de existência. Modelar antes de optar.

### Reinvestimento em Habitação Própria Permanente

- **Reinvestimento em Habitação Própria Permanente**: o ganho na venda da habitação própria e permanente é excluído se o valor de realização, deduzido do empréstimo amortizado, for reinvestido noutra habitação própria e permanente (ou terreno e construção, ampliação ou melhoramento) entre os 24 meses anteriores e os 36 meses posteriores à venda, e se a intenção de reinvestir for declarada na declaração do ano da venda _(CIRS art. 10.º, n.º 5)_. Reinvestimento parcial: exclusão proporcional _(art. 10.º, n.º 12)_. Condições sobre a localização (Portugal ou UE/EEE), o uso como domicílio fiscal e a regra de 2026 a 2029 para reinvestimento em habitação arrendada: ver `pt-irs-employees-investment`.

## Secção 10: Linhas Vermelhas (Cláusula Anti-Abuso e Riscos de Inspeção)

### Cláusula Geral Anti-Abuso

- **Cláusula geral anti-abuso**: são desconsideradas para efeitos tributários as construções que, tendo como finalidade principal ou uma das finalidades principais obter uma vantagem fiscal que frustre o objeto do direito fiscal, sejam realizadas com abuso das formas jurídicas ou não sejam genuínas. A tributação faz-se pelas normas aplicáveis à realidade económica _(LGT art. 38.º, n.º 2)_. A aplicação exige audição prévia do contribuinte, que tem 30 dias para responder, e autorização prévia do dirigente máximo do serviço _(CPPT art. 63.º, n.os 5 e 7)_.

### Gatilhos de Inspeção da AT

**Gatilhos de Inspeção da AT** (riscos práticos; a base legal está indicada quando existe)

| Gatilho | Risco |
| --- | --- |
| Inconsistência entre rendimento declarado e e-fatura | A AT recebe as faturas emitidas (Decreto-Lei 198/2012) e cruza-as com o rendimento declarado |
| Regime simplificado com rendimento perto de €200.000 | Dividir a mesma atividade por vários NIF ou atividades para ficar abaixo do limite cai na cláusula anti-abuso (LGT art. 38.º, n.º 2) |
| Falha na justificação dos 15% de despesas (regime simplificado) | A diferença acresce automaticamente ao rendimento tributável (CIRS art. 31.º, n.º 13) |
| Dupla atividade: serviços não declarados | A AT compara movimentos bancários com receitas declaradas |
| Falsos recibos verdes (relação laboral disfarçada de prestação de serviços) | O trabalho é requalificado como dependente; a entidade suporta contribuições e coimas. A base no Código do Trabalho não foi revista hoje |
| Transmissões imobiliárias abaixo do valor para IMT | Para as mais-valias prevalece o valor considerado para IMT, se maior (CIRS art. 44.º, n.º 2) |
| Estruturas offshore sem substância | Lucros de entidades não residentes com regime fiscal claramente mais favorável são imputados aos sócios residentes (CIRC art. 66.º) |
| Fuga a contribuições à Segurança Social | A Segurança Social recebe da AT os dados de início de atividade; contribuições em atraso pagam juros e coimas (ver `pt-social-contributions`) |
| Pedidos de reembolso de IVA de montante elevado | Revisão e inspeção antes do reembolso |

### Proibições Absolutas

- **Proibições Absolutas**: NUNCA aconselhar emissão de recibos verdes para trabalho que constitua relação laboral dependente; NUNCA aconselhar omissão de rendimento quando as faturas são comunicadas via e-fatura; NUNCA aconselhar declarar transmissões imobiliárias abaixo do valor real; NUNCA aconselhar fragmentação artificial de rendimento para se manter abaixo do limite de €200.000 do regime simplificado; NUNCA aconselhar a não inscrição em IVA quando acima do limiar de isenção; NUNCA aconselhar evitar a inscrição na Segurança Social quando legalmente exigida.

## Secção 11: Calendário Anual de Planeamento Fiscal

**Calendário Anual de Planeamento Fiscal (2026, com a declaração de 2027)**

| Quando | Ação |
| --- | --- |
| Janeiro | Declaração trimestral à Segurança Social até ao fim do mês. Contribuição mensal entre os dias 10 e 20. Rever as faturas do ano anterior no e-fatura |
| Fevereiro | Até ao fim do mês: faturas do ano anterior comunicadas contam para as deduções (art. 78.º-B, n.º 5); identificar faturas e imóveis afetos à atividade para a regra dos 15% (art. 31.º, n.º 15) |
| Março | Até 15 de março a AT mostra as deduções à coleta; reclamação até 31 de março (art. 78.º-B, n.os 6 e 7). Até ao fim de março: opção por contabilidade organizada para o ano (art. 28.º) |
| Abril | Abertura da entrega do IRS (1 de abril). Declaração trimestral à Segurança Social. Simular tributação conjunta vs separada e englobamento |
| Maio | Continuação da entrega do IRS. Simular o imposto do ano em curso |
| 30 de junho | Prazo final da Modelo 3 (art. 60.º, n.º 1). Anexo B (Categoria B), Anexo H (benefícios e deduções), Anexo J (rendimentos do estrangeiro), conforme o caso |
| Julho | 1.º pagamento por conta até 20 de julho (art. 102.º). Declaração trimestral à Segurança Social |
| Setembro | 2.º pagamento por conta até 20 de setembro. Revisão fiscal a meio do ano |
| Outubro | Declaração trimestral à Segurança Social. Rever rendimentos de capitais para a decisão de englobamento |
| Novembro | Planear entregas para PPR do fim do ano. Rever prazos de reinvestimento de vendas de imóveis (24 meses antes, 36 meses depois) |
| Dezembro | 3.º pagamento por conta até 20 de dezembro. **Mês crítico:** entregas para PPR e donativos. Garantir que as faturas da atividade têm NIF. Antecipar despesas em contabilidade organizada |

## Secção 12: Exemplos de Impacto Financeiro

Os exemplos usam os escalões de 2026 e o método do art. 68.º, n.º 2 (taxa média do escalão completo mais taxa normal sobre o excedente). Não incluem deduções à coleta nem o mínimo de existência, salvo indicação.

### Exemplo 1: Regime Simplificado vs Contabilidade Organizada (Freelancer)

**Freelancer de uma atividade da tabela do art. 151.º, residente, sem outros rendimentos, rendimentos brutos de €50.000 em 2026. Outras despesas reais da atividade (sem a Segurança Social): €8.000, todas em faturas comunicadas. Não está nos dois primeiros anos de atividade.**

1. **Segurança Social** (igual nos dois cenários, para comparar): 70% × 50.000 × 21,4% = €7.490 no ano. A base mensal (35.000 / 12 = €2.916,67) está abaixo do limite de €6.445,56. Em contabilidade organizada a base seria o lucro do ano anterior; o exemplo assume o mesmo valor.
2. **Regime simplificado:** 50.000 × 0,75 = €37.500. A Segurança Social acima de 10% do bruto deduz-se: 7.490 - 5.000 = €2.490 (art. 31.º, n.º 2). Rendimento tributável €35.010. Regra dos 15%: 15% × 50.000 = €7.500; justificado = 5.000 (maior entre €4.587,09 e a Segurança Social não deduzida de €5.000) + 8.000 = €13.000. Não há acréscimo. IRS: 29.397 × 20,579% + (35.010 - 29.397) × 34,90% = €8.008,55.
3. **Contabilidade organizada:** 50.000 - 8.000 - 7.490 = €34.510. IRS: 29.397 × 20,579% + (34.510 - 29.397) × 34,90% = €7.834,05.
4. **Resultado:** a contabilidade organizada poupa €174,50 de IRS antes dos honorários do contabilista certificado. Se os honorários forem superiores, o simplificado ganha. Com Segurança Social acima de 10% do bruto, a contabilidade organizada só baixa o IRS quando as outras despesas reais excedem 15% do bruto (aqui €7.500).

```oa-check
name: PT freelancer art. 151, gross 50,000, simplified vs organised accounts, 2026 bands
inputs:
  gross: 50000
  expenses: 8000
  ss_share: 0.70
  ss_rate: 0.214
  coef: 0.75
  specific_deduction: 4587.09
  band5_top: 29397
  band5_avg: 0.20579
  band6_rate: 0.349
steps:
  - ss: gross * ss_share * ss_rate
  - ss_deductible: max(0, ss - 0.10 * gross)
  - simplified_taxable: gross * coef - ss_deductible
  - justified: max(specific_deduction, ss - ss_deductible) + expenses
  - addback: max(0, 0.15 * gross - justified)
  - simplified_tax: round(band5_top * band5_avg + (simplified_taxable + addback - band5_top) * band6_rate, 2)
  - organised_taxable: gross - expenses - ss
  - organised_tax: round(band5_top * band5_avg + (organised_taxable - band5_top) * band6_rate, 2)
  - saving_organised: simplified_tax - organised_tax
expected:
  ss: 7490.00
  simplified_taxable: 35010.00
  addback: 0
  simplified_tax: 8008.55
  organised_taxable: 34510.00
  organised_tax: 7834.05
  saving_organised: 174.50
```

### Exemplo 2: Tributação Conjunta vs Separada

**Casal casado. Rendimento coletável do Cônjuge A: €60.000. Cônjuge B: €10.000 (segundo cenário: €0).**

1. **Separada:** A: 46.566 × 26,472% + (60.000 - 46.566) × 44,60% = €18.318,52. B: 8.342 × 12,50% + (10.000 - 8.342) × 15,70% = €1.303,06. Total €19.621,58.
2. **Conjunta:** 70.000 / 2 = €35.000. Imposto sobre metade: 29.397 × 20,579% + (35.000 - 29.397) × 34,90% = €8.005,06. Vezes dois: €16.010,12. **A tributação conjunta poupa €3.611,46** neste caso.
3. **Se o Cônjuge B aufere €0:** conjunta: 60.000 / 2 = €30.000; 29.397 × 20,579% + 603 × 34,90% = €6.260,06; vezes dois €12.520,12. Separada: €18.318,52. **A tributação conjunta poupa €5.798,40.**
4. Antes de optar, refazer a comparação com as deduções à coleta: na tributação separada cada cônjuge tem os seus limites, e o limite global do art. 78.º, n.º 7, muda com o rendimento coletável.

```oa-check
name: PT couple 60,000 and 10,000 taxable, joint vs separate, 2026 bands
inputs:
  a_income: 60000
  b_income: 10000
  band1_top: 8342
  band1_rate: 0.125
  band2_rate: 0.157
  band5_top: 29397
  band5_avg: 0.20579
  band6_rate: 0.349
  band7_top: 46566
  band7_avg: 0.26472
  band8_rate: 0.446
steps:
  - tax_a: round(band7_top * band7_avg + (a_income - band7_top) * band8_rate, 2)
  - tax_b: round(band1_top * band1_rate + (b_income - band1_top) * band2_rate, 2)
  - separate: tax_a + tax_b
  - half: (a_income + b_income) / 2
  - joint: 2 * round(band5_top * band5_avg + (half - band5_top) * band6_rate, 2)
  - saving_joint: separate - joint
  - joint_b_zero: 2 * round(band5_top * band5_avg + (a_income / 2 - band5_top) * band6_rate, 2)
  - saving_b_zero: tax_a - joint_b_zero
expected:
  tax_a: 18318.52
  tax_b: 1303.06
  separate: 19621.58
  joint: 16010.12
  saving_joint: 3611.46
  joint_b_zero: 12520.12
  saving_b_zero: 5798.40
```

### Exemplo 3: Criptoativos Detidos Mais de 365 Dias

**Comprou BTC por €10.000 em janeiro de 2025. Vendeu por €25.000 em março de 2026 (mais de 365 dias). Não é atividade empresarial.**

Imposto: **€0**. Os ganhos de criptoativos detidos 365 dias ou mais são excluídos de tributação (CIRS art. 10.º, n.º 22).

Se vendido antes de 365 dias: (25.000 - 10.000) × 28% = €4.200 de imposto à taxa autónoma (art. 72.º, n.º 1 c)), salvo opção pelo englobamento.

```oa-check
name: PT crypto gain 15,000, held under vs over 365 days, 2026
inputs:
  cost: 10000
  proceeds: 25000
  rate: 0.28
  held_over_365: 1
steps:
  - gain: proceeds - cost
  - tax_short: gain * rate
  - tax_long: gain * rate * (1 - held_over_365)
expected:
  gain: 15000
  tax_short: 4200.00
  tax_long: 0
```

### Exemplo 4: Reinvestimento em Habitação Própria Permanente

**Venda em 2026 da habitação própria e permanente por €300.000, comprada em 2025 por €200.000 e usada como domicílio fiscal desde a compra. Sem empréstimo. Outro rendimento coletável do vendedor: €30.000. Sem correção monetária (detida menos de 24 meses).**

1. Mais-valia €100.000; 50% incluído = €50.000 (art. 43.º, n.º 2 b)). Rendimento coletável passa de €30.000 para €80.000.
2. IRS sobre €30.000: €6.260,06. IRS sobre €80.000: 46.566 × 26,472% + (80.000 - 46.566) × 44,60% = €27.238,52. Imposto adicional da venda: **€20.978,46**. (Sem taxa de solidariedade: aplica-se só acima de €80.000.)
3. Reinvestir os €300.000 em nova habitação própria e permanente dentro do prazo e declarar a intenção: **€0 de imposto** sobre a venda (art. 10.º, n.º 5).
4. Reinvestimento parcial de €200.000 (2/3 do valor de realização): exclui-se a parte proporcional (art. 10.º, n.º 12). Fica tributado 1/3 do ganho: 100.000 / 3 × 50% = €16.666,67 incluídos. IRS sobre €46.666,67: 46.566 × 26,472% + 100,67 × 44,60% = €12.371,85; imposto adicional **€6.111,79**.

```oa-check
name: PT main home sale gain 100,000, other income 30,000, full and two-thirds reinvestment, 2026 bands
inputs:
  sale: 300000
  cost: 200000
  other_income: 30000
  reinvested: 200000
  inclusion: 0.50
  band5_top: 29397
  band5_avg: 0.20579
  band6_rate: 0.349
  band7_top: 46566
  band7_avg: 0.26472
  band8_rate: 0.446
steps:
  - gain: sale - cost
  - included: gain * inclusion
  - tax_base: round(band5_top * band5_avg + (other_income - band5_top) * band6_rate, 2)
  - tax_with_sale: round(band7_top * band7_avg + (other_income + included - band7_top) * band8_rate, 2)
  - extra_no_reinvest: tax_with_sale - tax_base
  - included_partial: round(gain * (1 - reinvested / sale) * inclusion, 2)
  - taxable_partial: other_income + included_partial
  - tax_partial: round(band7_top * band7_avg + (taxable_partial - band7_top) * band8_rate, 2)
  - extra_partial: tax_partial - tax_base
expected:
  included: 50000
  tax_base: 6260.06
  tax_with_sale: 27238.52
  extra_no_reinvest: 20978.46
  included_partial: 16666.67
  tax_partial: 12371.85
  extra_partial: 6111.79
```

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 68, IRS bands 2026 (wording of Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-30 |
| CIRS art. 68-A, solidarity surcharge | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx | 2026-10-30 |
| CIRS art. 69, joint taxation divisor | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs69.aspx | 2026-10-30 |
| CIRS art. 59, joint taxation option | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs59.aspx | 2026-10-30 |
| CIRS art. 70, minimum existence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs70.aspx | 2026-10-30 |
| CIRS art. 12-B, IRS Jovem | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx | 2026-10-30 |
| CIRS art. 22, aggregation of a whole category | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx | 2026-10-30 |
| CIRS art. 25, specific deduction 8.54 x IAS | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx | 2026-10-30 |
| CIRS art. 28, simplified regime limit | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx | 2026-10-30 |
| CIRS art. 31, coefficients, 10% and 15% rules | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-10-30 |
| CIRS art. 10, capital gains, main home reinvestment, crypto 365 days | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx | 2026-10-30 |
| CIRS art. 40-A, 50% of dividends | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs40a.aspx | 2026-10-30 |
| CIRS art. 41, Category F deductions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs41.aspx | 2026-10-30 |
| CIRS art. 43, 50% inclusion and holding-period exclusions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs43.aspx | 2026-10-30 |
| CIRS art. 44, value for IMT prevails | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs44.aspx | 2026-10-30 |
| CIRS art. 55, losses | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs55.aspx | 2026-10-30 |
| CIRS art. 60, filing period | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-30 |
| CIRS art. 71, 28% final withholding and option | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx | 2026-10-30 |
| CIRS art. 72, autonomous rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx | 2026-10-30 |
| CIRS art. 78, overall cap on deductions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78.aspx | 2026-10-30 |
| CIRS art. 78-B, general family expenses and e-fatura dates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78b.aspx | 2026-10-30 |
| CIRS art. 78-C, health | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78c.aspx | 2026-10-30 |
| CIRS art. 78-D, education | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78d.aspx | 2026-10-30 |
| CIRS art. 78-E, housing (with Decreto-Lei 97/2026 art. 15 transitional rule) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78e.aspx | 2026-10-30 |
| CIRS art. 78-F, VAT on invoices | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78f.aspx | 2026-10-30 |
| CIRS art. 83-A, alimony | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs83a.aspx | 2026-10-30 |
| CIRS art. 84, care homes | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs84.aspx | 2026-10-30 |
| CIRS art. 102, payments on account | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs102.aspx | 2026-10-30 |
| CIRC art. 87, IRC rates, with Lei 64/2025 art. 3 transitional rule (19% in 2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-30 |
| CIRC art. 52, tax losses, with Lei 24-D/2022 art. 228 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx | 2026-10-30 |
| Lei 27-A/2020, art. 11(2), +10 points for 2020 and 2021 losses | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei_27_A_2020.pdf | 2026-10-30 |
| CIRC art. 48, reinvestment of gains | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc48.aspx | 2026-10-30 |
| CIRC art. 34, car depreciation cap | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc34.aspx | 2026-10-30 |
| CIRC art. 66, controlled foreign companies | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc66.aspx | 2026-10-30 |
| Decreto Regulamentar 25/2009 (AT copy; tables not reproduced) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/outros_diplomas/Documents/Dec_Regulamentar25_2009.pdf | 2026-10-30 |
| CIVA art. 53, small-business exemption EUR 15,000 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx | 2026-10-30 |
| CIVA art. 58, end of exemption, 25% margin | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva58.aspx | 2026-10-30 |
| CIVA art. 18, mainland VAT rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx | 2026-10-30 |
| CIVA art. 6, place of supply of services | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva6.aspx | 2026-10-30 |
| CIVA art. 29, recapitulative statement | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva29.aspx | 2026-10-30 |
| CIVA art. 41, periodic return deadlines, EUR 650,000 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva41.aspx | 2026-10-30 |
| EBF art. 21, PPR | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf-artigo-21-ordm-.aspx | 2026-10-30 |
| LGT art. 38, general anti-abuse clause | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt38.aspx | 2026-10-30 |
| CPPT art. 63, anti-abuse procedure | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cppt/Pages/cppt63.aspx | 2026-10-30 |
| Segurança Social, Guia Prático, Trabalhadores Independentes (2026: IAS EUR 537.13, 21.4%, 25.2%, 70%/20%, EUR 20 minimum, ceiling EUR 6,445.56, 4 x IAS exemption, 12-month start, payment 10th to 20th, 25% option) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-30 |

Not yet confirmed: the depreciation rates by asset class in Tabela II of Decreto Regulamentar 25/2009 (the old version gave commercial buildings 2%, industrial buildings 5%, office furniture 12.5%, computer equipment 33.33%, software 33.33%, light passenger cars 25%, basic equipment 10% to 20%; AT's copy read today does not reproduce the tables); the car cost caps of Portaria 467/2010 as amended (the old version gave EUR 62,500 for electric and EUR 37,500 for other cars; not read); the "50% reduction in months 13 to 24" of self-employed contributions (not found in the Guia Prático read today); hiring a spouse as an employee as an alternative to the spouse cover (not reviewed); the donations deduction in the EBF (the old version said "up to 15% of the tax"; not read); the deadline for reporting household composition to AT (the old version said March; not read); the Código do Trabalho rules on false self-employment; the rule-of-thumb that incorporation pays above about EUR 60,000 to 80,000 of profit (no official source; replaced by a method); Azores and Madeira VAT rates are taken from `portugal-vat-return` and were not re-read today; the IRC derrama and autonomous taxation figures are in `pt-corporate-tax` and were not re-read today.

## Aviso Legal

Esta skill e os seus resultados são fornecidos apenas para fins informativos e computacionais e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuintes não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado (como um Contabilista Certificado, consultor fiscal ou profissional licenciado equivalente na sua jurisdição) antes da entrega ou atuação.

A versão mais atualizada desta skill é mantida em [openaccountants.com](https://openaccountants.com).

> Contributed by Ryan Duguid.

> Contributed by Michael Cutajar.

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
