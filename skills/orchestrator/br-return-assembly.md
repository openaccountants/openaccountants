---
name: br-return-assembly
description: Final orchestrator skill that assembles the complete Brazil filing package for Brazil-resident self-employed individuals (MEI, Simples Nacional, autônomo/pessoa física). Consumes outputs from all Brazil content skills (br-irpf for Declaração de Ajuste Anual, br-simples for DAS/DASN reconciliation, br-inss for INSS contributions, br-iss for ISS municipal) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Brazil content skills listed above. Brazil full-year residents only. Self-employed individuals only.
version: 1.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BR Return Assembly

## Brasil — Montagem do Working Paper Tributário — Skill v1.1

## DIRETRIZ CRÍTICA DE EXECUÇÃO -- LEIA PRIMEIRO

**Quando este skill é invocado, você já passou pela etapa de intake. O usuário consentiu com o workflow completo. Execute todos os passos sem pausar para pedir permissão.**

Especificamente:

- **NÃO pergunte ao usuário "até que profundidade você quer que eu vá"** ou "você quer o pacote completo" ou qualquer variação. O usuário pediu suas declarações. Ele quer suas declarações. Produza-as.
- **NÃO anuncie quantos tokens ou chamadas de ferramenta isso vai consumir.** Execute.
- **NÃO pergunte quais entregáveis devem ser priorizados.** Produza todos os entregáveis listados na Seção 4. Se ficar sem contexto no meio da execução, finalize primeiro o trabalho de cálculo (números, posições, flags), depois produza os outputs formatados possíveis, e ao final declare claramente quais entregáveis não foram produzidos e por quê.
- **NÃO revalide o escopo que o intake já validou.** Se o `br-freelance-intake` produziu um pacote de intake, confie nele. Você pode conferir números específicos durante a reconciliação, mas não re-interrogue o usuário sobre residência, tipo de atividade, ou qualquer outro item que o intake já capturou.
- **NÃO pause entre content skills para checar com o usuário.** Rode-os na ordem de dependência (Seção 2) sem mensagens de status entre cada um. Uma única mensagem de status no final é aceitável.
- **Self-checks são metas, não bloqueios.** Se um self-check falhar, anote-o na seção de open flags do reviewer brief e continue. NÃO interrompa o workflow inteiro porque um self-check teve resposta ambígua.
- **Citações de fonte primária vão no reviewer brief final, não nos passos intermediários de cálculo.**

**O usuário já foi informado (pelo intake skill) que o pacote final exige assinatura de contador antes do envio. Declare isso uma vez no output final e siga em frente.**

**Modo de falha a evitar:** o skill para no meio da execução e faz uma meta-pergunta sobre ritmo de workflow. Se sentir vontade de perguntar "como devo proceder", a ação correta é escolher o caminho mais defensável e prosseguir, sinalizando a decisão no reviewer brief para que o revisor possa contestá-la.

## O que é este arquivo

O skill capstone final para declarações de autônomos no Brasil. Cada content skill do Brasil alimenta este. O output é o pacote completo de revisão que um contador pode revisar, assinar e entregar ao cliente junto com as instruções de envio.

Este skill coordena a execução dos content skills, verifica a consistência cross-skill e monta o entregável final.

## Seção 1 -- Escopo

- **Escopo do pacote** — Residentes no Brasil ano-inteiro; Autônomos e pequenos empresários: MEI, Simples Nacional (ME/EPP), autônomo/pessoa física; Ano-calendário 2025 (exercício 2026); Envio da IRPF Declaração de Ajuste Anual, DASN-SIMEI (MEI), reconciliação de DAS (Simples), reconciliação de carnê-leão (autônomo), reconciliação de INSS, reconciliação de ISS (se aplicável)  _(Seção 1)_

## Seção 2 -- Ordem de execução e cadeia de dependências

O skill faz o roteamento com base no tipo de atividade estabelecido no intake e impõe a ordem de execução:

### Rota A: MEI

0. **br-simples (modo MEI)** — declaração anual DASN-SIMEI + reconciliação de pagamentos DAS. Verificar faturamento bruto contra o limite de R$81.000. Reconciliar 12 pagamentos mensais de DAS (R$75,90 base para serviços 2025, ajustado pelo componente ICMS/ISS). Calcular a parcela isenta (32% serviços, 8% comércio, 8% indústria, 16% transporte). Output: valores da DASN-SIMEI, parcela isenta, parcela tributável para o IRPF.
0. **br-irpf** — Declaração de Ajuste Anual (se obrigado). Parcela tributável MEI entra como rendimentos tributáveis. Parcela isenta MEI entra como rendimentos isentos e não tributáveis. Outras fontes de renda consolidadas. Output: IRPF completo com todas as fichas.
0. **br-inss** — reconciliação do INSS. O INSS do MEI está incluído no DAS (5% do salário mínimo para aposentadoria por idade). Se houver complementação (15% adicional para aposentadoria por tempo de contribuição), reconciliar. Output: resumo das contribuições do INSS, meses contribuídos.

### Rota B: Simples Nacional

0. **br-simples (modo Simples)** — reconciliação do DAS. Determinar o Anexo correto (I-V) com base no CNAE. Calcular o fator R (folha de pagamento / receita bruta 12 meses) para a migração Anexo V -> III. Reconciliar pagamentos mensais de DAS contra o faturamento. Verificar sublimite estadual para ICMS/ISS, se aplicável. Output: reconciliação do DAS, alíquota efetiva, total pago vs devido.
0. **br-irpf** — Declaração de Ajuste Anual. Pró-labore como rendimentos tributáveis (com INSS 11% deduzido). Distribuição de lucros isentos (lucro - impostos Simples, limitado à presunção ou contabilidade). Outras fontes de renda consolidadas. Output: IRPF completo com todas as fichas.
0. **br-inss** — reconciliação do INSS. INSS sobre pró-labore: 11% retido (empresa) + CPP dentro do DAS. Verificar o teto previdenciário (R$7.786,02 em 2025). Output: resumo das contribuições do INSS.
0. **br-iss** — reconciliação do ISS (se atividade de serviços). ISS incluído no DAS para o Simples Nacional (exceto atividades do Anexo IV). Para Anexo IV (advocacia, vigilância, limpeza): ISS pago separadamente ao município. Output: reconciliação do ISS.

### Rota C: Autônomo / Pessoa Física

0. **br-iss** — reconciliação do ISS (se atividade de serviços em município que exija). Alíquota de ISS por município (tipicamente 2-5%). Reconciliar ISS pago ou retido. Output: valores de ISS, montante dedutível.
0. **Reconciliação do carnê-leão (embutido no br-irpf)** — Cálculo mensal dos rendimentos PF, deduções do livro-caixa, INSS, dependentes. Aplicação mensal da tabela progressiva do IRPF. Reconciliar DARFs pagos (código 0190) contra o imposto devido mensal. Output: cronograma mensal do carnê-leão, total pago, qualquer diferença com exposição a multa/juros.
0. **br-irpf** — Declaração de Ajuste Anual. Todos os rendimentos tributáveis (PF via carnê-leão + PJ com IRRF). Deduções do livro-caixa. INSS pago como dedução. Deduções legais (médicas, educação, PGBL, dependentes, pensão). Bens e direitos / dívidas e ônus atualizados. Output: IRPF completo com todas as fichas.
0. **br-inss** — reconciliação do INSS. Contribuinte individual: 20% sobre remuneração (até o teto de R$7.786,02). Ou plano simplificado: 11% sobre o salário mínimo. Reconciliar pagamentos de GPS. Output: resumo das contribuições do INSS, meses contribuídos.

- **Falha de skill upstream** — Se algum content skill upstream não produzir output validado, o skill de montagem anota a falha no reviewer brief e continua com os dados disponíveis, em vez de interromper totalmente.  _(Seção 2)_

## Seção 3 -- Reconciliação cross-skill

### Verificação 1: reconciliação de receita entre obrigações

**Verificação 1: reconciliação de receita entre obrigações**  _(Seção 3)_

| Fonte | IRPF | Simples/MEI | Carnê-leão | Regra |
| --- | --- | --- | --- | --- |
| Notas fiscais emitidas | Rendimentos tributáveis (ficha Rendimentos Recebidos de PJ) | Faturamento bruto (PGDAS-D / DASN-SIMEI) | Rendimentos recebidos de PF (mensal) | Tudo deve reconciliar com depósitos bancários dentro de R$100 |
| Depósitos bancários | Soma de todas as fontes de renda | Faturamento total | Recebimentos PF mensais | Diferenças de timing (competência vs caixa) são comuns |

**Se houver divergência:** sinalizar para o revisor. Causas comuns: notas fiscais não emitidas para todos os recebimentos, timing entre emissão e pagamento, devoluções/cancelamentos.

### Verificação 2: contribuições do INSS vs dedução no IRPF

**Verificação 2: contribuições do INSS vs dedução no IRPF**  _(Seção 3)_

| Fonte do INSS | Tratamento no IRPF | Regra |
| --- | --- | --- |
| Autônomo GPS (20% ou 11%) | Dedução na ficha Pagamentos Efetuados (código 36) | Valor efetivamente pago, não valor devido |
| MEI DAS (componente INSS) | Não dedutível separadamente (incluído no cálculo da parcela isenta) | Não contar em duplicidade |
| INSS sobre pró-labore Simples (11%) | Dedução do rendimento tributável na ficha Rendimentos Recebidos de PJ | Retido pela empresa, reduz o rendimento tributável |

**Se houver divergência:** verificar se o caminho do INSS corresponde ao tipo de atividade. Contar INSS em duplicidade é um erro comum.

### Verificação 3: alinhamento carnê-leão vs ajuste anual (somente autônomo)

**Verificação 3: alinhamento carnê-leão vs ajuste anual (somente autônomo)**  _(Seção 3)_

| Carnê-leão (mensal) | Ajuste Anual | Regra |
| --- | --- | --- |
| Rendimentos de PF mensais | Mesmos valores na ficha Rendimentos Recebidos de PF | Totais mensais devem somar o anual |
| Deduções de livro-caixa mensais | Total do livro-caixa no ajuste anual | Mensal não pode exceder a receita mensal |
| Imposto pago (DARFs 0190) | Imposto pago / retido (ficha Imposto Pago/Retido código 1) | Creditado contra a obrigação anual |

**Se houver divergência:** carnê-leão não calculado/pago mensalmente corretamente resulta em multa (0,33%/dia até 20%) + juros SELIC. Sinalizar a exposição no reviewer brief.

### Verificação 4: emissão de notas fiscais

**Verificação 4: emissão de notas fiscais**  _(Seção 3)_

| Item | Verificação | Regra |
| --- | --- | --- |
| Total de notas fiscais emitidas | Deve igualar ou exceder os rendimentos declarados | Art. 1 LC 116/2003 (serviços), legislação do ICMS (comércio) |
| ISS retido nas notas | Deve igualar o valor de ISS pago/retido | Alíquotas municipais conforme LC 116/2003 |
| IRRF retido nas notas (serviços PJ) | Deve coincidir com o informe de rendimentos de cada PJ | 1,5% padrão para serviços (Art. 647 RIR/2018) |

**Se houver inconsistência:** notas fiscais faltantes representam risco de conformidade. Sinalizar para o revisor.

### Verificação 5: consistência de bens e direitos

**Verificação 5: consistência de bens e direitos**  _(Seção 3)_

| Ano anterior | Ano corrente | Regra |
| --- | --- | --- |
| Bens e direitos 31/12/2024 | Bens e direitos 31/12/2025 | Alterações devem ser explicadas (aquisições, vendas, depreciação) |
| Dívidas e ônus 31/12/2024 | Dívidas e ônus 31/12/2025 | Alterações devem ser explicadas (nova dívida, pagamentos) |

**Se houver inconsistência:** aumentos inexplicados em bens sem renda correspondente é um red flag para malha fina. Sinalizar.

## Seção 4 -- Reconciliação CBS/IBS 2026

A partir de 2026, contribuintes fora do Simples Nacional precisam reconciliar CBS e IBS emitidos nas notas com os créditos recebidos. Esta seção define como o working paper deve tratar a transição da reforma tributária do consumo (EC 132/2023 e LC 214/2025).

### Cronograma da transição

- **2026 (fase de teste)** — valores de CBS 0,9% + IBS 0,1% destacados nas notas, com pagamento simbólico — a obrigação pode ser suspensa por 3 meses sem multa após a regulamentação, desde que o contribuinte cumpra as obrigações acessórias (emissão correta da nota com os campos de CBS/IBS preenchidos).  _(EC 132/2023 e LC 214/2025, Seção 4)_
- **2027** — CBS pleno entra em vigor; o working paper deve substituir a reconciliação PIS/Cofins pela reconciliação CBS. PIS e Cofins são extintos para a maioria das atividades.  _(EC 132/2023 e LC 214/2025, Seção 4)_
- **2029** — IBS passa a ser cobrado de forma gradual, com alíquota crescente a cada ano-calendário até 2032.  _(EC 132/2023 e LC 214/2025, Seção 4)_
- **2033** — ICMS e ISS são extintos do working paper. A reconciliação cross-skill da Seção 3 deve ser ajustada para remover a Verificação 4 (ISS retido em notas) na sua forma atual.  _(EC 132/2023 e LC 214/2025, Seção 4)_

### Estrutura obrigatória do working paper (a partir de 2026)

- **Estrutura obrigatória do working paper** — O working paper deve listar separadamente, em sheets ou seções dedicadas: 1. Créditos de CBS — CBS destacado em notas fiscais de entrada (aquisições de bens e serviços com direito a crédito), por fornecedor e por período de apuração. 2. Créditos de IBS — IBS destacado em notas fiscais de entrada, por fornecedor e por período de apuração. 3. Débitos de CBS — CBS destacado em notas fiscais de saída emitidas pelo contribuinte, por cliente e por período. 4. Débitos de IBS — IBS destacado em notas fiscais de saída, por cliente e por período. 5. Saldo — diferença entre débitos e créditos, por tributo, com indicação de saldo a recolher ou saldo credor a transportar para o período seguinte.  _(Seção 4)_

### Observações para 2026 (fase de teste)

- Mesmo com pagamento simbólico ou suspenso, a reconciliação precisa ser feita para validar a emissão correta das notas e a apuração dos créditos.
- Contribuintes do Simples Nacional permanecem fora desta reconciliação em 2026 — o CBS/IBS está embutido no DAS, salvo opção pelo regime regular híbrido prevista em regulamentação específica.
- Notas fiscais emitidas sem os campos de CBS/IBS preenchidos corretamente expõem o contribuinte a autuação a partir do fim do período de suspensão.

### Referências cruzadas

- Para emissão correta da nota fiscal eletrônica com campos de CBS/IBS, consultar **brazil-einvoice**.
- Para impacto sobre o IRPF e distribuição de lucros, consultar **br-income-tax** (br-irpf).
- Para tratamento no Simples Nacional, consultar **br-simples-nacional**.

## Seção 5 -- Conteúdo do pacote final de revisão

### Documentos

1. Sumário executivo -- visão geral de uma página: tipo de atividade, rendimentos, imposto devido, imposto pago, restituição/saldo a pagar
2. Working paper do IRPF -- ficha a ficha com fórmulas (todas as fichas relevantes para o autônomo)
3. Cronograma do carnê-leão (autônomo) OU reconciliação do DAS (MEI/Simples) -- detalhamento mensal
4. Resumo do livro-caixa (autônomo) -- receita mensal e despesas dedutíveis
5. Reconciliação do INSS -- tipo de contribuição, pagamentos mensais, total, verificação do teto
6. Reconciliação do ISS (se aplicável) -- alíquotas municipais, valores pagos, alinhamento com notas
7. Reconciliação CBS/IBS (a partir de 2026) -- créditos e débitos de CBS e IBS, saldo apurado
8. Cronograma de bens e direitos / dívidas e ônus -- declaração completa de ativos e passivos
9. Resumo das reconciliações cross-skill -- todas as cinco verificações com pass/fail e notas
10. Reviewer brief -- narrativa abrangente com posições, citações, flags e resultados dos self-checks
11. Lista de ações para o cliente -- o que o cliente precisa fazer, com datas e valores

### Conteúdo do reviewer brief

# Pacote Completo de Declaração: [Nome do Cliente] -- Ano-calendário 2025 / Exercício 2026

## Sumário Executivo
- Situação: [Solteiro / Casado / União estável]
- Residência: Brasil (ano inteiro), [município] - [UF]
- Tipo de atividade: MEI / Simples Nacional (Anexo [X]) / Autônomo PF
- CNPJ: [número] (ou somente CPF para autônomo)
- Total rendimentos tributáveis: R$ X
- Total deduções: R$ X
- Base de cálculo IRPF: R$ X
- Imposto devido: R$ X
- IRRF retido na fonte: R$ X
- Carnê-leão pago: R$ X (somente autônomo)
- Imposto a restituir / saldo a pagar: R$ X
- INSS total contribuído: R$ X
- DAS total pago: R$ X (somente MEI/Simples)

## IRPF -- Declaração de Ajuste Anual
[Conteúdo do output do br-irpf]

### Rendimentos Tributáveis
- Rendimentos recebidos de PJ: R$ X
  - [Detalhamento por cliente com IRRF retido por PJ]
- Rendimentos recebidos de PF (carnê-leão): R$ X
- Pró-labore (Simples): R$ X

### Rendimentos Isentos e Não Tributáveis
- Parcela isenta MEI: R$ X (32% serviços / 8% comércio)
- Distribuição de lucros isentos (Simples): R$ X
- Rendimentos de poupança: R$ X
- Outros isentos: R$ X

### Rendimentos Sujeitos à Tributação Exclusiva/Definitiva
- Aplicações financeiras: R$ X
- 13º salário: R$ X (se CLT)

### Deduções Legais (modelo completa)
- INSS: R$ X
- Dependentes: R$ X (R$2.275,08 x [n])
- Despesas médicas: R$ X (sem limite)
- Despesas de educação: R$ X (limite R$3.561,50 por pessoa)
- PGBL: R$ X (limite 12% rendimentos tributáveis)
- Pensão alimentícia: R$ X
- Livro-caixa: R$ X

### Desconto Simplificado (modelo simplificada)
- 20% dos rendimentos tributáveis: R$ X
- Limite: R$16.754,34
- Modelo mais vantajoso: [completa / simplificada] -- economia de R$ X

### Cálculo do Imposto
- Base de cálculo: R$ X
- Tabela progressiva 2025 (ano-calendário 2025 / exercício 2026):
  - Até R$2.428,80/mês desde maio de 2025 (R$28.467,20/ano): isento
  - R$2.428,81 - R$2.826,65: 7,5%
  - R$2.826,66 - R$3.751,05: 15%
  - R$3.751,06 - R$4.664,68: 22,5%
  - Acima de R$4.664,68: 27,5%
- Imposto devido: R$ X
- Dedução do imposto: R$ X
- Imposto líquido: R$ X

### Imposto Pago / Retido
- IRRF retido na fonte (PJ): R$ X
- Carnê-leão pago (DARFs 0190): R$ X
- Imposto complementar pago: R$ X
- Total creditado: R$ X
- Restituição / saldo a pagar: R$ X

## Carnê-Leão (somente Autônomo)
[Cronograma mensal]
- Mês | Rendimento PF | Livro-caixa | INSS | Dependentes | Base | Imposto | DARF pago | Diferença
- Detalhamento jan-dez
- Total anual: imposto devido R$ X, pago R$ X, diferença R$ X
- Exposição a multa/juros se houve subpagamento: [cálculo ou "nenhuma"]

## DAS / DASN-SIMEI (somente MEI)
[Conteúdo do output do br-simples]
- Faturamento bruto 2025: R$ X
- vs limite R$81.000: [dentro / excedido]
- Pagamentos mensais de DAS: R$75,90 x 12 = R$910,80 (base serviços 2025)
- DAS pago: R$ X
- DAS em atraso: R$ X (se houver)
- Parcela isenta: R$ X (32% serviços)
- Parcela tributável para IRPF: R$ X

## Reconciliação do DAS (somente Simples Nacional)
[Conteúdo do output do br-simples]
- Anexo: [I-V]
- Fator R: [valor] (migração Anexo V -> III se >= 28%)
- RBT12 (receita bruta 12 meses): R$ X
- Alíquota nominal: [taxa]%
- Parcela a deduzir: R$ X
- Alíquota efetiva: [taxa]%
- DAS mensal devido vs pago: [cronograma]
- Total de DAS devido: R$ X
- Total de DAS pago: R$ X
- Diferença: R$ X

## INSS
[Conteúdo do output do br-inss]
- Tipo de contribuição: [contribuinte individual 20% / plano simplificado 11% / MEI 5%]
- Base mensal: R$ X
- Teto previdenciário: R$7.786,02 (2025)
- INSS mensal devido: R$ X
- Mensal pago: [cronograma]
- Total devido: R$ X
- Total pago: R$ X
- Meses contribuídos: [quantidade]/12

## ISS (se aplicável)
[Conteúdo do output do br-iss]
- Município: [nome]
- Alíquota ISS: [taxa]%
- ISS devido: R$ X
- ISS pago/retido: R$ X
- Alinhamento com notas fiscais: [pass/fail]

## CBS/IBS (a partir de 2026)
- Fase do cronograma: [teste 2026 / CBS pleno 2027 / IBS gradual 2029+]
- Créditos de CBS no período: R$ X
- Créditos de IBS no período: R$ X
- Débitos de CBS no período: R$ X
- Débitos de IBS no período: R$ X
- Saldo CBS (a recolher / credor): R$ X
- Saldo IBS (a recolher / credor): R$ X

## Bens e Direitos / Dívidas e Ônus
- Bens e direitos 31/12/2025: R$ X total
  - [Lista de itens com código, descrição, situação 31/12/2024, situação 31/12/2025]
- Dívidas e ônus 31/12/2025: R$ X total
  - [Lista de itens]
- Variações ano a ano explicadas: [lista]

## Reconciliação Cross-skill
- Receita entre obrigações: [pass/fail]
- INSS vs dedução no IRPF: [pass/fail]
- Carnê-leão vs ajuste anual: [pass/fail]
- Emissão de notas fiscais: [pass/fail]
- Consistência de bens e direitos: [pass/fail]

## Flags de Atenção para o Revisor
[Agregadas de todos os skills upstream]
- Itens T2 que exigem confirmação do contador
- Exposição a subpagamento de carnê-leão (multa + juros SELIC)
- Faturamento MEI se aproximando do limite de R$81.000
- Faturamento Simples Nacional se aproximando do sublimite ou do limite de R$4,8 mi
- Cálculo do fator R para migração Anexo V -> III
- Deduções de livro-caixa excedendo a receita mensal
- Variações ano a ano em bens e direitos sem explicação por renda
- PGBL excedendo o limite de 12%
- Indicadores de risco de malha fina

## Posições Adotadas
[Lista com citações de legislação]
- Ex.: "Deduções de livro-caixa: R$24.000 -- Art. 75-78 RIR/2018 (Decreto 9.580/2018)"
- Ex.: "Parcela isenta MEI 32% serviços -- Art. 15 Lei 9.249/1995 c/c Art. 26 §1° LC 123/2006"
- Ex.: "Dedução de PGBL R$9.600 (dentro do limite de 12%) -- Art. 11 Lei 9.532/1997"
- Ex.: "Despesas médicas R$8.400 (dedução integral, sem limite) -- Art. 80 RIR/2018"

## Notas de Planejamento para 2026
- Carnê-leão mensal: obrigatório se rendimentos de PF excederem a faixa de isenção
- Limite MEI R$81.000: trajetória atual do faturamento para 2026
- INSS: verificar adequação do plano de contribuição para os objetivos de aposentadoria
- Calendário de pagamento do DAS (MEI/Simples): dia 20 de cada mês
- CBS/IBS: iniciar reconciliação a partir de 2026 (fase de teste); preparar substituição da reconciliação PIS/Cofins por CBS em 2027
- Mudanças legislativas: verificar tabela progressiva do IRPF 2026, salário mínimo, teto do INSS, regulamentação infralegal da reforma tributária (LC 214/2025)
- Obrigações acessórias: DCTFWeb, ECF, ECD, EFD-ICMS/IPI, EFD-Reinf, EFD-Contribuições, eSocial

## Lista de Ações do Cliente

### Imediato (antes do último dia útil de maio de 2026 -- prazo do IRPF):
1. Revisar este pacote de declaração com seu contador
2. Enviar a Declaração de Ajuste Anual do IRPF pelo programa IRPF 2026 (Receita Federal)
3. Pagar o saldo a pagar R$ X (ou a 1ª quota de até 8 parcelas -- mínimo R$50 via DARF código 0211)
4. Enviar a DASN-SIMEI (MEI) -- prazo 31 de maio de 2026
5. Verificar se todos os DAS 2025 estão pagos (regularizar atrasados com juros + multa)

### Obrigações mensais (2026):
- Pagamento do DAS (MEI/Simples): dia 20 de cada mês
- Carnê-leão (autônomo recebendo de PF): último dia útil do mês seguinte ao recebimento
- INSS GPS (autônomo): dia 15 do mês seguinte
- ISS (se fora do Simples): conforme calendário municipal
- CBS/IBS (a partir de 2026): apuração mensal e reconciliação de créditos/débitos

### Pagamentos por quota do IRPF (se parcelamento):
- 1ª quota: último dia útil de maio de 2026
- 2ª quota: último dia útil de junho de 2026 (+ SELIC)
- Até a 8ª quota: último dia útil de dezembro de 2026 (+ SELIC acumulada)

### Obrigações acessórias anuais (calendário 2026):
- DCTFWeb: mensal, até o dia 15 do mês seguinte
- ECF: prazo final em julho de 2026 (referente ao ano-calendário 2025)
- ECD: prazo final no último dia útil de maio de 2026
- EFD-ICMS/IPI: mensal, conforme calendário SPED
- EFD-Reinf: mensal, até o dia 15 do mês seguinte
- EFD-Contribuições: mensal, até o 10º dia útil do 2º mês seguinte

### Contínuas:
1. Emitir nota fiscal para todos os serviços/produtos (obrigatório -- LC 116/2003, legislação do ICMS) — a partir de 2026, com campos de CBS/IBS preenchidos
2. Manter o livro-caixa mensalmente (autônomo) -- Art. 75 RIR/2018
3. Guardar todos os recibos e notas por 5 anos (Art. 195 CTN -- decadência)
4. Calcular e pagar o carnê-leão mensalmente se receber de PF
5. Monitorar o faturamento MEI contra o limite de R$81.000 / Simples contra R$4,8 mi
6. Atualizar o registro de bens e direitos para quaisquer aquisições/alienações
7. Pagar o INSS mensalmente para manter a contagem de contribuições para aposentadoria
8. Manter reconciliação CBS/IBS a partir de 2026 (créditos, débitos e saldo)

## Seção 6 -- Recusas

- **R-BR-1** — Skill upstream não rodou. Nomear o skill específico. Observação: este é um aviso, não um hard stop. Continuar com os dados disponíveis e sinalizar a lacuna.  _(Seção 6)_
- **R-BR-2** — Self-check upstream falhou. Nomear o check específico e anotá-lo no reviewer brief. Continuar.  _(Seção 6)_
- **R-BR-3** — Reconciliação cross-skill falhou. Nomear a reconciliação específica e descrever a discrepância. Sinalizar para o revisor mas continuar.  _(Seção 6)_
- **R-BR-4** — Intake incompleto. Itens específicos faltantes do intake impedem o cálculo. Listar o que está faltando e pedir ao usuário o dado específico.  _(Seção 6)_
- **R-BR-5** — Item fora do escopo descoberto durante a montagem. Ex.: ganhos de capital (GCAP), rendimentos do exterior exigindo carnê-leão sobre fonte estrangeira, ou rendimentos de aluguel exigindo DARF separado. Sinalizar e excluir do cálculo.  _(Seção 6)_

## Seção 7 -- Self-checks

- **Check BR1** — Todos os skills upstream foram executados. br-irpf, br-inss e o caminho aplicável de br-simples ou carnê-leão produziram output.  _(Seção 7)_
- **Check BR2** — Reconciliação de receita passou. Total de rendimentos entre IRPF, DAS/carnê-leão e notas fiscais alinhados dentro de R$100.  _(Seção 7)_
- **Check BR3** — INSS corretamente classificado e deduzido. O caminho do INSS corresponde ao tipo de atividade. Sem dupla contagem entre componente do DAS e GPS separado.  _(Seção 7)_
- **Check BR4** — Carnê-leão alinha com ajuste anual (autônomo). Totais mensais somam o anual. DARFs pagos creditados corretamente.  _(Seção 7)_
- **Check BR5** — Parcela isenta MEI calculada corretamente. Percentual correto (32% serviços, 8% comércio, 8% indústria, 16% transporte) aplicado ao faturamento.  _(Seção 7)_
- **Check BR6** — Anexo do Simples determinado corretamente. CNAE mapeia para o Anexo correto. Fator R calculado se atividade do Anexo V.  _(Seção 7)_
- **Check BR7** — Modelo de IRPF (completa vs simplificada) otimizado. Os dois modelos calculados, escolhido o mais vantajoso.  _(Seção 7)_
- **Check BR8** — Bens e direitos completos e consistentes. Todos os ativos > R$5.000 declarados. Variações ano a ano explicadas.  _(Seção 7)_
- **Check BR9** — Deduções legais dentro dos limites. Limite de educação por pessoa R$3.561,50. Limite de PGBL 12%. Dependentes R$2.275,08 cada.  _(Seção 7)_
- **Check BR10** — Calendário de envios está completo. Prazo do IRPF, prazo da DASN-SIMEI, DAS mensal, carnê-leão mensal, INSS mensal, todos listados; obrigações acessórias (DCTFWeb, ECF, ECD, EFD-ICMS/IPI, EFD-Reinf, EFD-Contribuições) listadas.  _(Seção 7)_
- **Check BR11** — Sem números de formulário em mensagens voltadas ao usuário. Notas internas podem referenciar fichas e artigos; mensagens ao usuário usam português comum sempre que possível.  _(Seção 7)_
- **Check BR12** — Reviewer brief contém citações de legislação. Toda posição cita artigos específicos do RIR/2018, LC 123/2006, Lei 9.249/1995, CTN, EC 132/2023, LC 214/2025 ou outra legislação aplicável.  _(Seção 7)_
- **Check BR13** — Reconciliação CBS/IBS executada (a partir de 2026). Créditos e débitos de CBS e IBS listados separadamente, com saldo apurado e flag para fase do cronograma de transição.  _(Seção 7)_

## Seção 8 -- Arquivos de saída

O output final consiste em três arquivos:

1. `[client_slug]_2025_br_master.xlsx` -- workbook master único contendo todas as planilhas. Abas incluem: Capa, Resumo do IRPF (todas as fichas), Cronograma Mensal do Carnê-Leão (autônomo) ou Reconciliação do DAS (MEI/Simples), Livro-Caixa (autônomo), Reconciliação do INSS, Reconciliação do ISS, Reconciliação CBS/IBS (a partir de 2026), Bens e Direitos, Dívidas e Ônus, Resumo Cross-Check. Usar fórmulas vivas sempre que possível -- ex.: rendimentos do IRPF referenciam as abas de carnê-leão/DAS; dedução do INSS referencia a aba do INSS; tabela progressiva é fórmula. Verificar que não há erros `#REF!`. Verificar que os valores calculados batem dentro de R$1 antes de entregar.

2. `reviewer_brief.md` -- arquivo único em markdown cobrindo todas as seções da Seção 5 acima: sumário executivo, IRPF, carnê-leão/DAS, INSS, ISS, CBS/IBS, bens e direitos, reconciliação cross-skill, flags, posições, notas de planejamento.

3. `client_action_list.md` -- arquivo único em markdown com ações passo a passo: envios e pagamentos imediatos, calendário mensal de DAS/carnê-leão/INSS/CBS-IBS para 2026, lembretes de conformidade contínuos.

**Se a execução ficar sem contexto no meio da construção:** produzir o que estiver completo, e ao final declarar quais dos três arquivos não foram produzidos ou estão parciais.

**Todos os arquivos são colocados em `/mnt/user-data/outputs/` e apresentados ao usuário via a ferramenta `present_files` ao final.**

## Seção 9 -- Referências cruzadas entre skills

**Inputs:**
- `br-freelance-intake` -- pacote de intake estruturado (JSON)
- `br-income-tax` (br-irpf) -- output do cálculo da Declaração de Ajuste Anual do IRPF
- `br-simples-nacional` (br-simples) -- output da reconciliação de DAS/DASN (MEI ou Simples)
- `br-inss` -- output da reconciliação de contribuições do INSS
- `br-iss` -- output da reconciliação de ISS (se aplicável)
- `brazil-einvoice` -- emissão de nota fiscal eletrônica com campos de CBS/IBS (a partir de 2026)

**Outputs:** o pacote final de revisão. Sem skill downstream.

## Seção 10 -- Lacunas conhecidas

1. O preenchimento de formulários PDF não é automatizado. O revisor usa as planilhas para preencher o IRPF via o programa da Receita Federal.
2. O envio eletrônico é feito pelo revisor via programa IRPF ou portal e-CAC, não por este skill.
3. A execução do pagamento é responsabilidade do cliente; o skill apenas fornece instruções, DARFs e valores.
4. Ganhos de capital (GCAP) em venda de ativos exigem DARF separado e estão fora do escopo.
5. Rendimentos do exterior (rendimentos do exterior) com carnê-leão sobre fonte estrangeira estão fora do escopo.
6. Rendimentos de aluguel (aluguéis) exigindo tratamento separado de carnê-leão estão fora do escopo.
7. Declarações de espólio estão fora do escopo.
8. O pacote está completo somente para o ano-calendário 2025; 2026 aparece apenas como planejamento prospectivo.
9. Retificadora só é suportada se a declaração original foi feita neste workflow.
10. Obrigações de empregador DIRF/EFD-Reinf para Simples com funcionários estão fora do escopo amplo (a Seção 5 lista os prazos, mas a apuração detalhada é tratada em skill próprio).
11. A reconciliação CBS/IBS (Seção 4) cobre apenas a fase de teste 2026 e o cronograma de transição. A apuração detalhada por NCM, regimes específicos (zona franca, ZPE) e split payment estão fora do escopo desta versão.

### Change log

- **v1.0 (maio de 2026):** rascunho inicial. Modelado a partir do mt-return-assembly v0.1 adaptado para a jurisdição do Brasil com quatro content skills (IRPF, Simples/DAS, INSS, ISS).
- **v1.1 (maio de 2026):** tradução completa para português brasileiro; adicionada Seção 4 -- Reconciliação CBS/IBS 2026 cobrindo o cronograma da reforma tributária (EC 132/2023, LC 214/2025); estrutura obrigatória do working paper para créditos/débitos de CBS e IBS; novo Check BR13; integração com obrigações acessórias (DCTFWeb, ECF, ECD, EFD-ICMS/IPI, EFD-Reinf, EFD-Contribuições) na lista de ações e nos self-checks; referência cruzada para brazil-einvoice.

## Fim do skill

## Aviso legal

Este skill e seus outputs são fornecidos apenas para fins informativos e de cálculo e não constituem aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus colaboradores não aceitam responsabilidade por quaisquer erros, omissões ou resultados decorrentes do uso deste skill. Todos os outputs devem ser revisados e assinados por um profissional qualificado (como contador registrado no CRC, advogado tributarista ou prático licenciado equivalente em sua jurisdição) antes do envio ou da tomada de ação.

A versão mais atualizada e verificada deste skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar revisão profissional por um contador licenciado e acompanhar atualizações conforme a legislação tributária mudar.

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
