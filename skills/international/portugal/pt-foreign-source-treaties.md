---
name: pt-foreign-source-treaties
description: "Utilizar esta skill sempre que estejam em causa rendimentos estrangeiros declarados em Portugal ou a aplicação de uma Convenção de Dupla Tributação celebrada por Portugal. Acionar com frases como \"CDT Portugal\", \"Convenção de Dupla Tributação\", \"rendimentos estrangeiros Portugal\", \"isenção dividendos estrangeiros Portugal\", \"pensão estrangeira Portugal\", \"tax credit Portugal\", \"crédito de imposto por dupla tributação internacional\", \"MLI Portugal\", \"Instrumento Multilateral\", \"Anexo J IRS\", \"Modelo 3 Anexo J\", \"imputação ordinária Portugal\", \"método de isenção CDT\", \"RNH rendimento estrangeiro\", \"IFICI rendimento estrangeiro\". Também ativar para: \"Portugal double tax treaty\", \"Portugal DTA matrix\", \"foreign income Portugal taxation\", \"Portugal MLI\", \"Portugal tax treaty network\", \"Portugal withholding tax relief\". LER SEMPRE esta skill antes de tratar de qualquer rendimento estrangeiro declarado em Portugal por residente fiscal português, ou antes de aplicar uma CDT a um caso concreto. Cobre a rede de ~80 CDTs em vigor, o método de imputação ordinária do art.º 81.º CIRS, as especificidades do RNH legado e do IFICI quanto ao método de isenção, o MLI e a cláusula PPT, o preenchimento do Anexo J do Modelo 3 e a documentação probatória exigida pela AT."
jurisdiction: PT
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# pt-foreign-source-treaties

## Portugal — Convenções de Dupla Tributação e Rendimentos Estrangeiros — Skill v1.0

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Imposto base | IRS — Imposto sobre o Rendimento das Pessoas Singulares |
| Moeda | EUR (rendimentos estrangeiros convertidos ao câmbio do dia do recebimento ou câmbio médio do período, conforme art.º 23.º CIRS) |
| Ano fiscal | Ano civil (1 de janeiro – 31 de dezembro) |
| Autoridade tributária | Autoridade Tributária e Aduaneira (AT) |
| Portal | Portal das Finanças (portaldasfinancas.gov.pt) |
| Diploma base | Código do IRS (Decreto-Lei n.º 442-A/88), em especial art.º 15.º (residentes), art.º 22.º (englobamento), art.º 81.º (eliminação da dupla tributação internacional) |
| Modelo de CDT | Modelo OCDE com adaptações; ~80 CDTs em vigor |
| Instrumento multilateral | MLI / Convenção Multilateral OCDE — ratificada por Portugal em 28 de fevereiro de 2020; entrada em vigor a 1 de junho de 2020 |
| Método principal de eliminação | Imputação ordinária (crédito de imposto) — art.º 81.º, n.º 1 CIRS |
| Formulário de declaração | Modelo 3 IRS, Anexo J (rendimentos obtidos no estrangeiro) |
| Prazo de entrega | 1 de abril a 30 de junho do ano seguinte ao do rendimento |
| Validado por | Pendente — requer validação por contabilista certificado ou advogado tributarista português |
| Versão da skill | 1.0 |

### Lista das 20 CDTs mais relevantes em vigor

**Lista das 20 CDTs mais relevantes em vigor**

| País contraparte | Em vigor desde | Observações |
| --- | --- | --- |
| Espanha | 1995 | Vizinho — trabalhadores transfronteiriços |
| França | 1972 (revista) | Protocolo de revisão em discussão |
| Reino Unido | 1969 | Mais antiga em vigor; CDT pós-Brexit mantém-se |
| Alemanha | 1982 | Forte fluxo de pensionistas |
| Itália | 1984 | — |
| Países Baixos | 2000 | Cláusula LOB importante |
| Bélgica | 1971 (revista 1995) | — |
| Luxemburgo | 2000 | Holding/financeiro |
| Irlanda | 1995 | — |
| Áustria | 1972 | — |
| Suíça | 1976 (revista) | Pensionistas; troca de informações ativa |
| EUA | 1996 | Cláusula LOB (Limitation On Benefits) |
| Brasil | 2001 | Comunidade lusófona; dividendos máx. 15% |
| China | 2000 | — |
| Cabo Verde | 2000 | CPLP |
| Moçambique | 1993 (revista) | CPLP |
| Angola | 2019 | CPLP — em vigor 22 ago 2019 |
| Canadá | 2001 | — |
| Suécia | DENUNCIADA em jun 2022 — efeitos 1 jan 2024 | Sem CDT em 2025 |
| Noruega | 2012 | Substituiu CDT anterior |

> **Suécia — alerta crítico:** a Suécia denunciou unilateralmente a CDT em junho de 2022, com cessação de efeitos a 1 de janeiro de 2024. Em 2025 **não existe CDT em vigor** entre Portugal e a Suécia. Pensões privadas e dividendos suecos passam a sofrer retenção na fonte sueca normal sem cap convencional, e o residente em Portugal aplica apenas a eliminação unilateral do art.º 81.º, n.º 1 CIRS.

### Defaults conservadores

**Defaults conservadores**

| Ambiguidade | Default |
| --- | --- |
| País sem CDT identificada | Aplicar apenas eliminação unilateral (art.º 81.º, n.º 1 CIRS) — imputação ordinária limitada à fração do IRS português |
| Dúvida sobre residência fiscal | PARAR — afeta tributação mundial vs por fonte |
| Documento estrangeiro não traduzido | Solicitar tradução certificada antes de aplicar CDT |
| Imposto estrangeiro sem comprovativo | Não conceder crédito — exigir certificado da autoridade fiscal estrangeira |
| Categoria de rendimento ambígua | PARAR — categoria errada gera artigo CDT errado |
| RNH/IFICI invocado sem inscrição | Verificar inscrição no Portal das Finanças antes de aplicar regime |
| MLI: dúvida sobre PPT | Tratamento conservador — assumir que PPT pode ser invocado pela AT |
| Câmbio em falta | Usar câmbio médio anual do BCE para o ano em causa |

## Secção 2 — Mecânica de Isenção vs Crédito de Imposto

### Os dois métodos de eliminação da dupla tributação internacional

**Os dois métodos de eliminação da dupla tributação internacional**

| Método | Descrição | Quem aplica |
| --- | --- | --- |
| **Método de isenção** | O Estado de residência isenta o rendimento já tributado no Estado da fonte (com ou sem progressividade) | Portugal aplica apenas em casos restritos (RNH legado; certas CDTs em categorias específicas) |
| **Método de imputação (crédito)** | O Estado de residência tributa o rendimento mundial mas concede crédito pelo imposto pago no estrangeiro | Regra geral em Portugal — art.º 81.º, n.º 1 CIRS |

### Imputação ordinária — art.º 81.º, n.º 1 CIRS

- **Imputação ordinária** — Portugal aplica imputação ordinária (não integral). O crédito de imposto está limitado ao menor dos seguintes valores: 1. Imposto efetivamente pago no estrangeiro, no limite do imposto previsto na CDT (se existir); e 2. Fração do IRS português correspondente aos rendimentos estrangeiros, calculada na proporção do rendimento líquido estrangeiro sobre o rendimento global.  _(art.º 81.º, n.º 1 CIRS)_
- **Crédito máximo** — Crédito máximo = (Rendimento líquido estrangeiro / Rendimento global líquido) × IRS apurado em Portugal  _(art.º 81.º, n.º 1 CIRS)_
- **Crédito efetivo** — O crédito efetivo = mínimo (imposto pago no estrangeiro até ao tecto da CDT; fração de IRS português).  _(art.º 81.º, n.º 1 CIRS)_

### Excesso de imposto estrangeiro

- **Excesso não reembolsado** — Se o imposto estrangeiro exceder o limite calculado, o excesso não é reembolsado nem reportado a anos futuros — perde-se. Por isso é crítico invocar a CDT junto do Estado da fonte para reduzir a retenção na fonte ao limite convencional antes de aplicar o crédito em Portugal.

### Hierarquia de aplicação

- **Passos de aplicação** — 1. Verificar se existe CDT em vigor para 2025. 2. Determinar o artigo aplicável da CDT consoante a categoria do rendimento. 3. Determinar o direito de tributação (exclusivo do Estado de residência, exclusivo da fonte, ou partilhado com cap). 4. Se partilhado: verificar a taxa máxima retida na fonte permitida pela CDT. 5. Solicitar a redução/reembolso da retenção em excesso ao Estado da fonte (formulário próprio: M-1, M-2, RFI, etc.). 6. Em Portugal: declarar no Anexo J e aplicar o art.º 81.º para crédito de imposto.

## Secção 3 — Matriz CDT por Tipo de Rendimento

> A matriz seguinte é genérica (alinhada com o Modelo OCDE). **Cada CDT específica deve ser consultada para taxas exatas e variações.**

**Matriz CDT por Tipo de Rendimento**

| Categoria | Artigo Modelo OCDE | Regra geral | Tecto típico de retenção na fonte | Categoria IRS |
| --- | --- | --- | --- | --- |
| **Rendimentos imobiliários** | Art. 6.º | Tributação no Estado da fonte (onde se situa o imóvel) | Sem cap — tributação plena na fonte | Categoria F |
| **Lucros das empresas** | Art. 7.º | Estado de residência, salvo estabelecimento estável | — | Categoria B (se EE) |
| **Dividendos** | Art. 10.º | Tributação partilhada | 5% / 10% / 15% (varia por CDT) | Categoria E |
| **Juros** | Art. 11.º | Tributação partilhada | 10% / 15% (varia por CDT) | Categoria E |
| **Royalties** | Art. 12.º | Tributação partilhada (ou exclusiva no residência em algumas CDTs) | 5% / 10% (varia por CDT) | Categoria B ou E |
| **Mais-valias mobiliárias** | Art. 13.º | Tributação no Estado de residência (regra) | 0% (normalmente) | Categoria G |
| **Mais-valias imobiliárias** | Art. 13.º, n.º 1 | Tributação no Estado da fonte | Sem cap | Categoria G |
| **Trabalho dependente** | Art. 15.º | Estado onde é exercido (regra dos 183 dias) | — | Categoria A |
| **Conselho/administradores** | Art. 16.º | Estado de residência da sociedade | — | Categoria A ou B |
| **Pensões privadas** | Art. 18.º | Tributação no Estado de residência do beneficiário | 0% no Estado da fonte (típico) | Categoria H |
| **Pensões públicas** | Art. 19.º | Tributação no Estado pagador (regra) | Variável | Categoria H |
| **Outros rendimentos** | Art. 21.º | Estado de residência | — | Vária |

### Notas práticas por categoria

- **Dividendos:** Brasil 15%; EUA 15% (5% se participação ≥ 10%); Reino Unido 10%/15%; França 15%; Alemanha 15% (5% para participações qualificadas).
- **Juros:** EUA 10%; Brasil 15%; Reino Unido 10%; Alemanha 15% (com isenção parcial em alguns instrumentos).
- **Royalties:** Brasil 15%; EUA 10%; Reino Unido 5%; Alemanha 10%.
- **Pensões privadas:** quase todas as CDTs dão tributação exclusiva ao Estado de residência (Portugal, neste caso) — é por aqui que historicamente entrou o "carrossel" do RNH legado para pensionistas estrangeiros.

## Secção 4 — CDTs Críticas para RNH e IFICI

### Estados Unidos da América (CDT 1994; em vigor desde 1996)

- Modelo OCDE com cláusula LOB (Limitation On Benefits) específica.
- Dividendos: 15% geral; 5% para participações qualificadas (≥ 10% do capital).
- Juros: 10%.
- Royalties: 10%.
- Pensões privadas: tributação exclusiva no Estado de residência (Portugal).
- **Atenção:** os EUA tributam pela cidadania — cidadãos americanos residentes em Portugal continuam sujeitos a IRS federal americano (a CDT atenua mas não elimina).

### Reino Unido (CDT 1968; em vigor desde 1969 — a mais antiga)

- Pós-Brexit mantém-se em vigor sem alterações.
- Dividendos: 10%/15%.
- Royalties: 5%.
- Pensões privadas: tributação no Estado de residência (Portugal).
- Pensões públicas britânicas: tributação no Reino Unido.

### França (CDT 1971; em vigor desde 1972)

- **Situação fluida:** existe protocolo de revisão em discussão (estado em 2025).
- Dividendos: 15%.
- Royalties: 5%.
- Pensões privadas: tributação no Estado de residência (Portugal).
- Cláusula específica para fronteiriços.

### Alemanha (CDT 1980; em vigor desde 1982)

- Dividendos: 15% (5% para participações ≥ 10%).
- Juros: 15% (com isenções específicas).
- Royalties: 10%.
- Pensões privadas: tributação no Estado de residência.

### Suécia (DENUNCIADA)

- CDT cessou efeitos a **1 de janeiro de 2024**.
- Em 2025: **sem CDT em vigor**.
- Retenções suecas aplicam-se às taxas internas plenas (SINK aplicável a não residentes; pensões privadas suecas a 25%).
- NHRs suecos que beneficiavam de isenção em Portugal e baixa retenção na Suécia perdem o duplo benefício.

### Países Baixos (CDT 1999; em vigor desde 2000)

- Cláusula LOB.
- Dividendos: 10%.
- Pensões privadas: tributação no Estado de residência, mas com regras específicas para acumulações em planos NL.

### Brasil (CDT 2000; em vigor desde 2001)

- Dividendos: **15% máximo** retenção na fonte.
- Juros: 15%.
- Royalties: 15%.
- Pensões: tributação no Estado de residência.
- Lusofonia — fluxo bidirecional muito relevante.

### China (CDT 1998; em vigor desde 2000)

- Dividendos: 10%.
- Juros: 10%.
- Royalties: 10%.

### Espanha (CDT 1993; em vigor desde 1995)

- Vizinho — relevante para trabalhadores transfronteiriços.
- Dividendos: 10%/15%.
- Pensões privadas: tributação no Estado de residência.
- Regras específicas para fronteiriços e duplicação de residência (tie-breaker do art. 4.º).

### RNH legado vs IFICI — implicações por CDT

**RNH legado vs IFICI — implicações por CDT**

| Regime | Mecânica para rendimentos estrangeiros |
| --- | --- |
| **RNH legado** (inscritos até 31 dez 2023 / certos transitórios 2024) | Aplica método de **isenção** amplo: dividendos, juros, royalties, mais-valias mobiliárias, rendimentos imobiliários, pensões — desde que **possam ser tributados** no Estado da fonte ao abrigo da CDT (não exige que sejam efetivamente tributados, salvo regra anti-paraíso). Pensões: tributação efetiva a 10% em Portugal desde a alteração de 2020 (Lei 2/2020). |
| **IFICI** (Investment Tax Incentive — sucessor do RNH; inscrições a partir de 2024) | Isenção **restrita**: aplica-se a dividendos, juros, royalties, mais-valias e rendimentos de profissões qualificadas, com requisitos mais apertados. **Pensões estrangeiras: passam a estar sujeitas a 10% (art.º 72.º-A CIRS) — perdem isenção total.** Rendimentos do trabalho em profissões altamente qualificadas: tributados a 20% em Portugal (taxa especial). |

> Ver skill **pt-nhr-ifici** para as regras detalhadas de inscrição, requisitos e profissões qualificadas.

## Secção 5 — MLI (Instrumento Multilateral)

### Estado em Portugal

- **Estado do MLI em Portugal** — Portugal assinou a Convenção Multilateral OCDE (MLI) em 7 de junho de 2017. Depositou o instrumento de ratificação em 28 de fevereiro de 2020. Entrada em vigor para Portugal: 1 de junho de 2020. Aplica-se às CDTs notificadas como Covered Tax Agreements (CTAs) com contrapartes que também ratificaram o MLI.

### Cláusula PPT — Principal Purpose Test (art. 7.º MLI)

- **PPT — Principal Purpose Test** — Sob o PPT, um benefício previsto na CDT pode ser negado se for razoável concluir, considerando todos os factos e circunstâncias, que a obtenção desse benefício foi um dos principais objetivos de qualquer estrutura ou transação que tenha resultado, direta ou indiretamente, nesse benefício. Portugal optou pela aplicação do PPT como standard mínimo BEPS Acção 6.  _(art. 7.º MLI)_

**Implicação prática:** estruturas com finalidade essencialmente fiscal (treaty shopping, holdings sem substância, etc.) podem ver-se privadas dos benefícios da CDT pela AT mesmo que formalmente cumpram os requisitos.

### Outras opções MLI relevantes feitas por Portugal

- **Opções MLI de Portugal** — - Arbitragem obrigatória vinculativa (Parte VI): aceite por Portugal — disputas MAP não resolvidas em 2 anos vão a arbitragem. - Definição alargada de estabelecimento estável (art. 12.º MLI): aceite — endereça artificial avoidance via comissionistas. - Métodos de eliminação (art. 5.º MLI): Portugal manteve o método de imputação (opção C) — não converteu CDTs de isenção em imputação por via do MLI.

### Como verificar se uma CDT está "modificada" pelo MLI

- **Passos de verificação** — 1. Verificar a lista de CTAs notificados por Portugal (publicada pelo Ministério das Finanças e pela OCDE). 2. Verificar a lista do outro Estado contratante. 3. As cláusulas MLI aplicam-se apenas quando ambos os Estados notificaram a mesma CDT e fizeram opções compatíveis. 4. Consultar as versões sintetizadas publicadas pela OCDE para o texto integrado.

## Secção 6 — Anexo J do Modelo 3

### Estrutura do Anexo J (IRS)

- **Definição Anexo J** — O Anexo J declara rendimentos obtidos no estrangeiro por residentes fiscais em Portugal.

**Estrutura do Anexo J**

| Quadro | Conteúdo |
| --- | --- |
| Quadro 3 | Identificação do sujeito passivo |
| Quadro 4 | Rendimentos da Categoria A (trabalho dependente) — país, código de rendimento, valor bruto, imposto pago no estrangeiro, contribuições sociais |
| Quadro 5 | Rendimentos da Categoria B (empresariais e profissionais) — país, atividade, valor bruto, retenção |
| Quadro 6 | Rendimentos da Categoria E (capitais) — dividendos, juros, royalties — por país e tipo |
| Quadro 7 | Rendimentos prediais Categoria F — país, identificação do imóvel, rendas brutas, imposto pago |
| Quadro 8 | Mais-valias e outros incrementos patrimoniais Categoria G — operações, valores de aquisição e realização |
| Quadro 9 | Pensões Categoria H — país pagador, tipo (privada/pública/social), valor bruto, retenção |
| Quadro 11 | Crédito de imposto por dupla tributação internacional — cálculo do art.º 81.º |

### Códigos de rendimento (exemplos frequentes)

**Códigos de rendimento**

| Código | Rendimento |
| --- | --- |
| E01 | Dividendos |
| E02 | Juros |
| E03 | Royalties |
| H01 | Pensão de velhice — regime público |
| H02 | Pensão de velhice — regime privado |
| H05 | Pensão de sobrevivência |

### Country codes

- **Códigos de país** — Usar códigos ISO 3166 alpha-2 (ex.: BR para Brasil, US para EUA, GB para Reino Unido, DE para Alemanha, FR para França).

### Articulação com outros anexos

- **Articulação com outros anexos** — - Os rendimentos do Anexo J englobam-se com os rendimentos do Anexo A, B, E, F, G, H portugueses para apuramento do rendimento global e da taxa marginal. - Algumas categorias podem optar por tributação autónoma (ex.: dividendos a 28%) — opção de não englobamento é exercida no Quadro 8 do rosto do Modelo 3. - Para RNH/IFICI: rendimentos isentos são declarados no Anexo L (Quadro 6).

## Secção 7 — Documentação Requerida

### Comprovativos obrigatórios

**Comprovativos obrigatórios**

| Documento | Finalidade | Quem emite |
| --- | --- | --- |
| Certificado de residência fiscal portuguesa | Solicitar redução de retenção na fonte estrangeira ao abrigo da CDT | AT (Portal das Finanças, "Pedir certidão de residência fiscal") |
| Certificado de imposto pago no estrangeiro | Suportar o crédito do art.º 81.º CIRS | Autoridade fiscal estrangeira ou entidade pagadora |
| Formulário CDT do país da fonte | Pedido prévio de redução de retenção | Varia: EUA usa Form 8233/W-8BEN; Alemanha usa Antrag auf Erstattung; UK usa Form DT-Individual; etc. |
| Comprovativos de inscrição RNH/IFICI | Aplicação dos regimes especiais | Portal das Finanças |
| Tradução certificada | Documentos em língua estrangeira (exceto inglês/espanhol/francês em muitos casos) | Tradutor ajuramentado |
| Comprovativos de câmbio | Conversão para EUR | BCE, Banco de Portugal ou banco do contribuinte |

### Prazos de conservação

- **Prazo de conservação de documentos** — Conservar todos os documentos de suporte por 4 anos após a entrega da declaração (regra geral CIRS) — a AT pode inspecionar e exigir prova do imposto pago no estrangeiro.  _(regra geral CIRS)_

### Erros frequentes detetados pela AT

- **Erros frequentes** — 1. Declaração do imposto bruto retido na fonte em vez do imposto líquido devido após CDT. 2. Pedido de crédito sem comprovativo emitido pela autoridade fiscal estrangeira (recibos do banco não chegam em muitos casos). 3. Não declaração de contas/rendimentos estrangeiros (Modelo 3 — risco de coima até €22.500 + crime fiscal em casos graves). 4. Erro na conversão cambial — uso de câmbios não oficiais. 5. Aplicação de método de isenção sem ter inscrição RNH/IFICI válida e ativa.

## Secção 8 — Exemplos Práticos

### Exemplo 1 — Dividendo brasileiro

**Factos:** Residente fiscal em Portugal (sem RNH/IFICI). Recebe €10.000 brutos de dividendos de empresa brasileira em 2025. A fonte pagadora brasileira reteve 15% (€1.500), em linha com a CDT Portugal-Brasil.

**Tratamento:**

1. **Categoria E** em Portugal — dividendos.
2. Tributação autónoma a **28%** (sem englobamento) ou opção por englobamento.
3. Anexo J, Quadro 6: rendimento bruto €10.000, código E01, país BR, imposto pago €1.500.
4. **Crédito art.º 81.º:** menor de
   - imposto pago no estrangeiro: €1.500
   - fração IRS portuguesa: 28% × €10.000 = €2.800 (se tributação autónoma)
5. Crédito efetivo: **€1.500**. IRS líquido a pagar em Portugal sobre estes dividendos: €2.800 − €1.500 = **€1.300**.
6. Carga total: €1.500 (BR) + €1.300 (PT) = €2.800 = 28% — neutralizada pela CDT + crédito.

### Exemplo 2 — Pensão sueca

**Factos:** Residente fiscal em Portugal desde 2018 ao abrigo do RNH (legado). Recebe pensão privada sueca de €30.000 brutos em 2025.

**Tratamento:**

1. **CDT Portugal-Suécia: DENUNCIADA — cessou efeitos a 1 jan 2024.** Em 2025 não há CDT.
2. A Suécia aplica a sua retenção interna (SINK 25% para não residentes em pensões privadas) → €7.500 retidos.
3. Em Portugal:
   - RNH legado prevê tributação de pensões estrangeiras a **10%** (desde a Lei 2/2020).
   - IRS RNH sobre pensão: 10% × €30.000 = **€3.000**.
4. **Crédito art.º 81.º (eliminação unilateral):** menor de
   - imposto pago na Suécia: €7.500
   - fração IRS portuguesa: €3.000
5. Crédito efetivo: **€3.000**. IRS líquido em Portugal: €0.
6. Excesso de imposto sueco (€4.500): **não recuperável** — perde-se. Sem CDT, não há mecanismo convencional para pedir reembolso parcial à Suécia.

> Lição: a denúncia da CDT pela Suécia torna esta situação significativamente mais cara do que antes de 2024. Recomenda-se revisão do planeamento para pensionistas suecos.

### Exemplo 3 — Royalty americano

**Factos:** Programador residente em Portugal, sem RNH/IFICI. Recebe €20.000 brutos de royalties pagos por empresa dos EUA por software licenciado em 2025. A empresa americana reteve 30% (€6.000) por falta de invocação atempada da CDT.

**Tratamento:**

1. CDT Portugal-EUA limita retenção sobre royalties a **10%** (€2.000).
2. **Acção corretiva no Estado da fonte:** pedir reembolso de €4.000 ao IRS americano via formulário 1040-NR + W-8BEN com certificado de residência português. Prazo: 3 anos.
3. Em Portugal (assumindo Categoria B — atividade profissional habitual de programador):
   - Englobamento obrigatório na taxa marginal (até 48% + sobretaxa).
   - Anexo J, Quadro 5, país US, código de atividade adequado.
4. **Crédito art.º 81.º:** limitado a €2.000 (taxa CDT), não €6.000.
   - Se o reembolso americano for obtido: €2.000 retidos efetivamente.
   - Fração IRS portuguesa (assumindo taxa marginal 35%): 35% × €20.000 = €7.000 (antes de despesas dedutíveis).
   - Crédito efetivo: menor de €2.000 e €7.000 = **€2.000**.
5. **Se reembolso americano não for solicitado:** os €4.000 em excesso de retenção **NÃO podem ser creditados em Portugal** — a CDT limita o crédito ao imposto previsto na convenção, não ao efetivamente retido em violação dela.

> Lição: invocar a CDT junto do Estado da fonte antes do pagamento ou pedir o reembolso atempadamente é essencial. Excesso retido em violação da CDT não é compensável em Portugal.

## Secção 9 — Defaults Conservadores (consolidados)

**Defaults Conservadores (consolidados)**

| Cenário | Default conservador |
| --- | --- |
| Sem CDT identificada | Eliminação unilateral art.º 81.º apenas — sem cap convencional |
| CDT existe mas categoria duvidosa | Aplicar artigo de "outros rendimentos" (art. 21.º) e flagrar para revisão |
| MLI: dúvida sobre aplicação do PPT | Documentar a substância económica da estrutura |
| RNH/IFICI sem inscrição confirmada | Regime geral — sem isenção |
| Imposto estrangeiro sem certificado oficial | Crédito recusado até obtenção de certificado |
| Câmbio em falta | Câmbio médio anual BCE |
| Pensão sueca em 2025 | Sem CDT — aplicar só art.º 81.º unilateral |
| Cidadão norte-americano residente em PT | Sinalizar dupla obrigação declarativa (Portugal + IRS federal EUA via FBAR/FATCA) |
| Mais-valias imobiliárias estrangeiras | Tributação plena na fonte + crédito em PT — verificar se imóvel está no património declarado |
| Royalty de software | Verificar se é royalty (art. 12.º) ou serviço (art. 7.º/14.º) — distinção crítica |

## Secção 10 — Fontes

### Diplomas portugueses

- **Código do IRS (CIRS)** — Decreto-Lei n.º 442-A/88, de 30 de novembro, em especial:
  - Art.º 15.º — âmbito da sujeição (residentes vs não residentes).
  - Art.º 16.º — residência fiscal.
  - Art.º 22.º — englobamento.
  - Art.º 72.º — taxas especiais.
  - Art.º 72.º-A — IFICI (introduzido pela Lei 82/2023 — OE 2024).
  - **Art.º 81.º — eliminação da dupla tributação jurídica internacional.**
- **Lei n.º 2/2020** (OE 2020) — alteração ao regime RNH: pensões estrangeiras tributadas a 10%.
- **Lei n.º 82/2023** (OE 2024) — criação do regime IFICI e revogação prospetiva do RNH.

### Instrumento multilateral

- **Convenção Multilateral OCDE (MLI)** — Resolução da Assembleia da República n.º 225/2019, de 24 de outubro; Decreto do Presidente da República n.º 92/2019.
- Lista de CTAs notificados por Portugal — publicada pela OCDE e pelo Ministério das Finanças.

### CDTs específicas (instrumentos)

- **CDT Portugal-EUA** — Aviso n.º 35/95; em vigor desde 1 jan 1996.
- **CDT Portugal-Reino Unido** — Decreto-Lei n.º 48 497, de 24 de julho de 1968.
- **CDT Portugal-França** — Decreto-Lei n.º 105/71.
- **CDT Portugal-Alemanha** — Lei n.º 12/82.
- **CDT Portugal-Brasil** — Aviso n.º 39/2002; em vigor desde 5 out 2001.
- **CDT Portugal-Espanha** — Aviso n.º 164/95.
- **CDT Portugal-Suécia** — Aviso n.º 3/2003 — **DENUNCIADA em junho de 2022**; cessão de efeitos 1 jan 2024.
- **CDT Portugal-Países Baixos** — Aviso n.º 145/2000.
- **CDT Portugal-China** — Aviso n.º 95/2000.

### Doutrina administrativa AT

- **Brochura AT — "Convenções para Evitar a Dupla Tributação"** (atualizada periodicamente).
- **Circulares e ofícios-circulados AT** sobre aplicação do art.º 81.º CIRS e procedimento de pedido de redução de retenção (formulário M-1, M-2).
- **Manual de Preenchimento do Modelo 3 — Anexo J**, publicado anualmente pela AT.

### Modelos OCDE e BEPS

- **Modelo de Convenção Fiscal OCDE** sobre o Rendimento e o Património (última atualização 2017, com comentários).
- **Plano BEPS — Acção 6** (Prevenção do abuso das convenções fiscais).
- **Convenção Multilateral OCDE (MLI)** — texto consolidado, comentários e versões sintetizadas por CDT.

### Cross-reference a outras skills

- **pt-nhr-ifici** — regras detalhadas dos regimes RNH e IFICI, requisitos de inscrição, profissões qualificadas e tratamento por categoria.
- **pt-income-tax** — regras gerais de IRS, englobamento, taxas e deduções.
- **portugal-crypto-tax** — tratamento de criptoativos estrangeiros (NFTs, exchanges não residentes).

## Skill v1.0 — pendente de validação

*Skill v1.0 — pendente de validação por contabilista certificado ou advogado tributarista português.*

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
