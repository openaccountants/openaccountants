---
name: portugal-bookkeeping
description: "Utilize esta skill sempre que lhe forem colocadas questões sobre contabilidade portuguesa no ano de 2026: plano de contas SNC (Portaria 218/2015), normas NCRF, NCRF-PE e NC-ME, categorias de dimensão com os novos limites de 2026 (DL 126-B/2025), demonstrações financeiras (Portaria 220/2015), regras fiscais de depreciação (DR 25/2009, CIRC 29.º a 34.º), tributação autónoma, regime simplificado da Categoria B (CIRS 28.º e 31.º), faturação com programa certificado, comunicação de faturas (dia 5), SAF-T (PT), IES até 15 de julho e conservação por 10 anos. Active perante \"contabilidade Portugal\", \"SNC\", \"código de contas\", \"microentidade\", \"NC-ME\", \"IES\", \"SAF-T(PT)\", \"contabilista certificado\", \"regime simplificado\", \"contabilidade organizada\". Trigger also on: \"Portuguese bookkeeping\", \"Portugal accounting\", \"SNC chart of accounts\", \"Portuguese GAAP\", \"SAF-T Portugal\". Fora de âmbito: cálculo do IRC (pt-corporate-tax), IRS (pt-income-tax), IVA (portugal-vat-return), Segurança Social (pt-social-contributions), demonstrações financeiras em detalhe (portugal-financial-statements), faturação eletrónica (portugal-einvoice)."
version: 1.2
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Bookkeeping

## Secção 1: Referência Rápida

**Referência Rápida** (ano de 2026)

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Período de tributação | Ano civil (CIRC art. 8.º, n.º 1). As pessoas coletivas podem adotar outro período anual, que coincida com o período de prestação de contas e se mantenha pelo menos 5 períodos (art. 8.º, n.º 2) |
| Normas contabilísticas | SNC (Sistema de Normalização Contabilística, DL 158/2009): NCRF (28 normas), NCRF-PE (pequenas entidades), NC-ME (microentidades) |
| Plano de contas padrão | Código de Contas (Portaria n.º 218/2015), de aplicação obrigatória para as entidades sujeitas ao SNC, para períodos iniciados em ou após 1 de janeiro de 2016 |
| Modelos de demonstrações financeiras | Portaria n.º 220/2015 |
| Organismo normalizador | CNC (Comissão de Normalização Contabilística) |
| Principal legislação | DL 158/2009 (republicado pelo DL 98/2015; limites de dimensão alterados pelo DL 126-B/2025 a partir de 2026); Portarias 218/2015 e 220/2015; DL 28/2019 (faturas e conservação); DL 198/2012 (comunicação de faturas e de inventários) |
| Classificação de atividade | CAE (Classificação Portuguesa das Atividades Económicas) |
| Ficheiro normalizado | SAF-T (PT) (Portaria 321-A/2007). A comunicação mensal de faturas pode fazer-se por ficheiro SAF-T (PT) de faturação. O SAF-T (PT) da contabilidade só é exigido para os períodos de 2027 e seguintes, a entregar a partir de 2028 (Lei 73-A/2025, art. 95.º, n.º 2) |
| Obrigação de relato anual | IES (Informação Empresarial Simplificada), por via eletrónica até 15 de julho (CIRC art. 121.º, n.º 2) |
| Autoridade tributária | AT (Autoridade Tributária e Aduaneira) |
| Ordem profissional | OCC (Ordem dos Contabilistas Certificados) |
| Contabilista certificado | As entidades que possuam ou devam possuir contabilidade organizada precisam de um contabilista certificado: só ele pode assumir a responsabilidade técnica e assinar as demonstrações financeiras e as declarações fiscais (Estatuto da OCC, art. 10.º, n.º 1, al. b)) |
| Atraso máximo na contabilidade | 90 dias, contados do último dia do mês a que as operações respeitam (CIRC art. 123.º, n.º 3) |
| Período de conservação de documentos | 10 anos (DL 28/2019, art. 19.º, n.º 1; CIVA art. 52.º, n.º 1) |

## Secção 2: Plano de Contas Padrão (Código de Contas SNC)

O Código de Contas da Portaria n.º 218/2015 é obrigatório para as entidades sujeitas ao SNC e está estruturado em 8 classes. As contas abaixo seguem a numeração e as designações da Portaria. Algumas contas não existem para as microentidades (ex.: 37 Ativos biológicos) e a Portaria assinala-o no Quadro Síntese.

### Classe 1: Meios Financeiros Líquidos

**Classe 1: Meios Financeiros Líquidos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 11 | Caixa | Caixa (numerário) |
| 12 | Depósitos à ordem | Contas bancárias à ordem |
| 13 | Outros depósitos bancários | Outros depósitos bancários (a prazo) |
| 14 | Outros instrumentos financeiros | Derivados, instrumentos detidos para negociação e outros ativos e passivos financeiros ("Outros" para as microentidades) |

### Classe 2: Contas a Receber e a Pagar

**Classe 2: Contas a Receber e a Pagar**

| Código | Conta | Descrição |
| --- | --- | --- |
| 21 | Clientes | Clientes (contas a receber comerciais) |
| 211 | Clientes c/c | Clientes, conta corrente |
| 2111 | Clientes gerais | Clientes gerais |
| 212 | Clientes, títulos a receber | Letras a receber |
| 218 | Adiantamentos de clientes | Adiantamentos de clientes |
| 219 | Perdas por imparidade acumuladas | Perdas por imparidade acumuladas |
| 22 | Fornecedores | Fornecedores (contas a pagar comerciais) |
| 221 | Fornecedores c/c | Fornecedores, conta corrente |
| 222 | Fornecedores, títulos a pagar | Letras a pagar |
| 225 | Faturas em receção e conferência | Faturas em receção e conferência |
| 228 | Adiantamentos a fornecedores | Adiantamentos a fornecedores |
| 23 | Pessoal | Contas do pessoal |
| 231 | Remunerações a pagar | Remunerações a pagar |
| 232 | Adiantamentos | Adiantamentos ao pessoal |
| 24 | Estado e outros entes públicos | Estado e outros entes públicos |
| 241 | Imposto sobre o rendimento | Debitada pelos pagamentos e retenções sofridas; creditada no fim do período pelo imposto estimado. A Portaria não fixa subcontas; a entidade pode subdividir |
| 242 | Retenção de impostos sobre rendimentos | Imposto retido na fonte a terceiros (IRS/IRC), subdivisível pela natureza dos rendimentos |
| 243 | Imposto sobre o valor acrescentado (IVA) | IVA |
| 2431 | IVA: Suportado | IVA suportado |
| 2432 | IVA: Dedutível | IVA dedutível |
| 2433 | IVA: Liquidado | IVA liquidado |
| 2434 | IVA: Regularizações | IVA, regularizações |
| 2435 | IVA: Apuramento | IVA, apuramento |
| 2436 | IVA: A pagar | IVA a pagar |
| 2437 | IVA: A recuperar | IVA a recuperar |
| 2438 | IVA: Reembolsos pedidos | IVA, reembolsos pedidos |
| 2439 | IVA: Liquidações oficiosas | IVA, liquidações oficiosas |
| 244 | Outros impostos | Outros impostos |
| 245 | Contribuições para a Segurança Social | Contribuições para a Segurança Social |
| 246 | Tributos das autarquias locais | Tributos das autarquias locais |
| 25 | Financiamentos obtidos | Financiamentos obtidos (empréstimos) |
| 251 | Instituições de crédito e sociedades financeiras | Empréstimos bancários |
| 26 | Acionistas/sócios | Acionistas/sócios |
| 27 | Outras contas a receber e a pagar | Outras contas a receber e a pagar |
| 271 | Fornecedores de investimentos | Fornecedores de investimentos (credores de capex) |
| 272 | Devedores e credores por acréscimos (periodização económica) | Acréscimos de rendimentos e de gastos |
| 274 | Impostos diferidos | Impostos diferidos |
| 278 | Outros devedores e credores | Outros devedores e credores |
| 28 | Diferimentos | Gastos a reconhecer e rendimentos a reconhecer |
| 29 | Provisões | Provisões |

### Classe 3: Inventários e Ativos Biológicos

**Classe 3: Inventários e Ativos Biológicos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 31 | Compras | Compras |
| 311 | Mercadorias | Compras de mercadorias para revenda |
| 312 | Matérias-primas, subsidiárias e de consumo | Compras de matérias |
| 317 | Devoluções de compras | Devoluções de compras |
| 318 | Descontos e abatimentos em compras | Descontos e abatimentos em compras |
| 32 | Mercadorias | Mercadorias (existências) |
| 33 | Matérias-primas, subsidiárias e de consumo | Matérias (existências) |
| 34 | Produtos acabados e intermédios | Produtos acabados e intermédios |
| 35 | Subprodutos, desperdícios, resíduos e refugos | Subprodutos e desperdícios |
| 36 | Produtos e trabalhos em curso | Produção em curso |
| 37 | Ativos biológicos | Ativos biológicos (conta inexistente para as microentidades) |
| 38 | Reclassificação e regularização de inventários | Reclassificação e regularização |
| 39 | Adiantamentos por conta de compras | Adiantamentos por conta de compras |

### Classe 4: Investimentos (Ativos Fixos)

**Classe 4: Investimentos (Ativos Fixos)**

| Código | Conta | Descrição |
| --- | --- | --- |
| 41 | Investimentos financeiros | Investimentos financeiros |
| 42 | Propriedades de investimento | Propriedades de investimento |
| 43 | Ativos fixos tangíveis | Ativos fixos tangíveis |
| 431 | Terrenos e recursos naturais | Terrenos e recursos naturais |
| 432 | Edifícios e outras construções | Edifícios e outras construções |
| 433 | Equipamento básico | Equipamento básico (maquinaria) |
| 434 | Equipamento de transporte | Equipamento de transporte (viaturas) |
| 435 | Equipamento administrativo | Equipamento administrativo (escritório/informática) |
| 436 | Equipamentos biológicos | Equipamentos biológicos |
| 437 | Outros ativos fixos tangíveis | Outros ativos fixos tangíveis |
| 438 | Depreciações acumuladas | Depreciações acumuladas |
| 439 | Perdas por imparidade acumuladas | Perdas por imparidade acumuladas |
| 44 | Ativos intangíveis | Ativos intangíveis |
| 441 | Goodwill | Goodwill |
| 442 | Projetos de desenvolvimento | Projetos de desenvolvimento |
| 443 | Programas de computador | Programas de computador |
| 444 | Propriedade industrial | Propriedade industrial (patentes, marcas) |
| 446 | Outros ativos intangíveis | Outros ativos intangíveis |
| 448 | Amortizações acumuladas | Amortizações acumuladas |
| 449 | Perdas por imparidade acumuladas | Perdas por imparidade acumuladas |
| 45 | Investimentos em curso | Investimentos em curso |
| 46 | Ativos não correntes detidos para venda | Ativos não correntes detidos para venda |

### Classe 5: Capital, Reservas e Resultados Transitados

**Classe 5: Capital, Reservas e Resultados Transitados**

| Código | Conta | Descrição |
| --- | --- | --- |
| 51 | Capital subscrito | Capital social |
| 52 | Ações (quotas) próprias | Ações (quotas) próprias |
| 53 | Outros instrumentos de capital próprio | Outros instrumentos de capital próprio (ex.: prestações suplementares) |
| 54 | Prémios de emissão | Prémios de emissão |
| 55 | Reservas | Reservas |
| 551 | Reservas legais | Reservas legais |
| 552 | Outras reservas | Outras reservas |
| 56 | Resultados transitados | Resultados transitados |
| 57 | Ajustamentos em ativos financeiros | Ajustamentos em ativos financeiros |
| 58 | Excedentes de revalorização de ativos fixos tangíveis e intangíveis | Excedentes de revalorização |
| 59 | Outras variações no capital próprio | Outras variações no capital próprio |

### Classe 6: Gastos

**Classe 6: Gastos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 61 | Custo das mercadorias vendidas e das matérias consumidas (CMVMC) | Custo dos inventários vendidos e consumidos |
| 62 | Fornecimentos e serviços externos (FSE) | Fornecimentos e serviços externos |
| 621 | Subcontratos | Subcontratos |
| 622 | Serviços especializados | Serviços especializados |
| 6221 | Trabalhos especializados | Trabalhos especializados (contabilidade, jurídicos, informáticos, etc.) |
| 6222 | Publicidade e propaganda | Publicidade e propaganda |
| 6223 | Vigilância e segurança | Vigilância e segurança |
| 6224 | Honorários | Honorários |
| 6225 | Comissões | Comissões |
| 6226 | Conservação e reparação | Manutenção e reparação |
| 6228 | Outros | Outros serviços especializados |
| 623 | Materiais | Materiais |
| 6231 | Ferramentas e utensílios de desgaste rápido | Ferramentas de desgaste rápido |
| 6232 | Livros e documentação técnica | Livros e documentação técnica |
| 6233 | Material de escritório | Material de escritório |
| 6234 | Artigos para oferta | Artigos para oferta |
| 624 | Energia e fluidos | Energia e fluidos |
| 6241 | Eletricidade | Eletricidade |
| 6242 | Combustíveis | Combustíveis |
| 6243 | Água | Água |
| 625 | Deslocações, estadas e transportes | Deslocações, estadas e transportes |
| 6251 | Deslocações e estadas | Deslocações e estadas |
| 6252 | Transportes de pessoal | Transportes de pessoal |
| 6253 | Transportes de mercadorias | Transportes de mercadorias |
| 626 | Serviços diversos | Serviços diversos |
| 6261 | Rendas e alugueres | Rendas e alugueres |
| 6262 | Comunicação | Comunicações (telecomunicações) |
| 6263 | Seguros | Seguros |
| 6264 | Royalties | Royalties |
| 6265 | Contencioso e notariado | Contencioso e notariado |
| 6266 | Despesas de representação | Despesas de representação |
| 6267 | Limpeza, higiene e conforto | Limpeza, higiene e conforto |
| 6268 | Outros serviços | Outros serviços |
| 63 | Gastos com o pessoal | Gastos com o pessoal |
| 631 | Remunerações dos órgãos sociais | Remunerações dos órgãos sociais |
| 632 | Remunerações do pessoal | Remunerações do pessoal |
| 633 | Benefícios pós-emprego | Benefícios pós-emprego |
| 634 | Indemnizações | Indemnizações |
| 635 | Encargos sobre remunerações | Encargos sobre remunerações (Segurança Social a cargo da entidade empregadora) |
| 636 | Seguros de acidentes no trabalho e doenças profissionais | Seguros de acidentes de trabalho |
| 637 | Gastos de ação social | Gastos de ação social |
| 638 | Outros gastos com o pessoal | Outros gastos com o pessoal |
| 64 | Gastos de depreciação e de amortização | Gastos de depreciação e amortização |
| 641 | Propriedades de investimento | Depreciação, propriedades de investimento |
| 642 | Ativos fixos tangíveis | Depreciação, ativos fixos tangíveis |
| 643 | Ativos intangíveis | Amortização, ativos intangíveis |
| 65 | Perdas por imparidade | Perdas por imparidade |
| 66 | Perdas por reduções de justo valor | Perdas por reduções de justo valor |
| 67 | Provisões do período | Provisões do período |
| 68 | Outros gastos | Outros gastos |
| 681 | Impostos | Impostos (ex.: IMI, imposto do selo) |
| 6812 | Impostos indiretos | Impostos indiretos |
| 6813 | Taxas | Taxas |
| 682 | Descontos de pronto pagamento concedidos | Descontos de pronto pagamento concedidos |
| 683 | Dívidas incobráveis | Dívidas incobráveis |
| 684 | Perdas em inventários | Perdas em inventários (sinistros, quebras) |
| 686 | Gastos nos restantes investimentos financeiros | Gastos nos restantes investimentos financeiros |
| 687 | Gastos em investimentos não financeiros | Gastos em investimentos não financeiros |
| 688 | Outros | Outros gastos diversos (ex.: multas, donativos) |
| 69 | Gastos de financiamento | Gastos de financiamento |
| 691 | Juros suportados | Juros suportados |
| 692 | Diferenças de câmbio desfavoráveis | Diferenças de câmbio desfavoráveis |
| 698 | Outros gastos de financiamento | Outros gastos de financiamento (ex.: comissões de financiamento) |

### Classe 7: Rendimentos

**Classe 7: Rendimentos**

| Código | Conta | Descrição |
| --- | --- | --- |
| 71 | Vendas | Vendas de mercadorias e produtos |
| 72 | Prestações de serviços | Prestações de serviços |
| 73 | Variações nos inventários da produção | Variações nos inventários da produção |
| 74 | Trabalhos para a própria entidade | Trabalhos para a própria entidade (capitalizados) |
| 75 | Subsídios à exploração | Subsídios à exploração |
| 76 | Reversões | Reversões de imparidades e provisões |
| 77 | Ganhos por aumentos de justo valor | Ganhos por aumentos de justo valor |
| 78 | Outros rendimentos | Outros rendimentos |
| 781 | Rendimentos suplementares | Rendimentos suplementares |
| 782 | Descontos de pronto pagamento obtidos | Descontos de pronto pagamento obtidos |
| 783 | Recuperação de dívidas a receber | Recuperação de dívidas a receber |
| 784 | Ganhos em inventários | Ganhos em inventários |
| 786 | Rendimentos nos restantes ativos financeiros | Rendimentos nos restantes ativos financeiros |
| 787 | Rendimentos em investimentos não financeiros | Rendimentos em investimentos não financeiros (ex.: mais-valias de ativos fixos) |
| 788 | Outros | Outros rendimentos |
| 79 | Juros, dividendos e outros rendimentos similares | Juros obtidos, dividendos e rendimentos similares |

### Classe 8: Resultados

**Classe 8: Resultados**

| Código | Conta | Descrição |
| --- | --- | --- |
| 81 | Resultado líquido do período | Resultado líquido do período |
| 811 | Resultado antes de impostos | Resultado antes de impostos |
| 812 | Imposto sobre o rendimento do período | Imposto sobre o rendimento do período |
| 8121 | Imposto estimado para o período | Imposto corrente estimado |
| 8122 | Imposto diferido | Imposto diferido |
| 818 | Resultado líquido | Resultado líquido |
| 89 | Dividendos antecipados | Dividendos antecipados |

## Secção 3: Reconhecimento do Rédito

### Base de Caixa vs Base de Acréscimo

**Base de Caixa vs Base de Acréscimo**

| Tipo de entidade | Base | Notas |
| --- | --- | --- |
| Entidades sujeitas ao SNC | Acréscimo (obrigatória) | Para efeitos fiscais, os rendimentos e gastos são imputáveis ao período em que são obtidos ou suportados, independentemente do recebimento ou pagamento (CIRC art. 18.º, n.º 1) |
| Microentidades (NC-ME) | Acréscimo | A NC-ME simplifica a mensuração, mas mantém o acréscimo (gastos reconhecidos quando surge a diminuição de benefícios, NC-ME 3.6) |
| Pessoas singulares com atividade comercial, industrial ou agrícola e volume de negócios médio dos últimos 3 anos até 200.000 EUR | Fora do SNC | Dispensadas do SNC (DL 158/2009, art. 10.º, n.º 1). Deixam de estar dispensadas no período seguinte àquele em que o limite é ultrapassado (art. 10.º, n.º 5) |
| Trabalhadores independentes (Categoria B do IRS) | Regime simplificado ou contabilidade organizada | O regime simplificado aplica coeficientes aos rendimentos; a contabilidade organizada segue o acréscimo |

### Regras-Chave

- **Rédito da venda de bens**: Reconhecido quando, entre outras condições, a entidade transferiu para o comprador os riscos e vantagens significativos da propriedade dos bens (NCRF 20, § 14; NC-ME 12.4). Para efeitos fiscais, considera-se em geral realizado na data da entrega ou expedição ou, se anterior, na da transferência de propriedade (CIRC art. 18.º, n.º 3, al. a)).
- **Rédito de prestação de serviços**: Pela fase de acabamento quando o desfecho pode ser estimado com fiabilidade; caso contrário, só até ao limite dos gastos recuperáveis (NC-ME 12.6). Fiscalmente, na data de conclusão do serviço, exceto serviços continuados ou com mais de um ato, que são imputados proporcionalmente à execução (CIRC art. 18.º, n.º 3, al. b)).
- **NC-ME (microentidades)**: Aplica as mesmas condições de reconhecimento: bens quando os riscos e vantagens passam ao comprador; serviços pela fase de acabamento (NC-ME 12.4 a 12.6).
- **IVA e prazo da fatura**: O imposto torna-se exigível nos termos do art. 7.º do CIVA. A fatura deve ser emitida o mais tardar no 5.º dia útil seguinte ao momento em que o imposto é devido (CIVA art. 36.º, n.º 1, al. a)), ou na data do recebimento, em caso de pagamento antecipado (al. c)).

### Regime Simplificado para Trabalhadores Independentes (Categoria B do IRS)

- **Limite do regime simplificado**: 200.000 EUR de rendimentos da categoria B no período de tributação anterior  _(artigo 28.º, n.º 2, do CIRS)_
- **Coeficiente 0,75**: Rendimentos das atividades profissionais da tabela do artigo 151.º do CIRS  _(artigo 31.º, n.º 1, al. b), do CIRS)_
- **Coeficiente 0,15**: Vendas de mercadorias e produtos, operações com criptoativos (exceto mineração), e serviços de restauração, bebidas e hotelaria (com exceções para o alojamento local)  _(artigo 31.º, n.º 1, al. a), do CIRS)_
- **Coeficiente 0,35**: Prestações de serviços não previstas nas alíneas anteriores  _(artigo 31.º, n.º 1, al. c), do CIRS)_
- **Coeficiente 0,10**: Subsídios destinados à exploração e restantes rendimentos da categoria B não previstos nas outras alíneas (não se aplica às prestações de serviços)  _(artigo 31.º, n.º 1, al. f), do CIRS)_
- **Outros coeficientes**: 0,95 (mineração de criptoativos, propriedade intelectual, rendimentos de capitais e prediais imputáveis), 0,30 (subsídios não destinados à exploração), 0,50 (alojamento local em moradia ou apartamento em área de contenção)  _(artigo 31.º, n.º 1, als. d), e) e h), do CIRS)_
- **Registos no regime simplificado**: Sem contabilidade organizada. O titular regista as faturas emitidas e recebidas (registos do art. 50.º, n.º 1, als. a) a c), do CIVA) e, em separado, os reembolsos de despesas feitas por conta do cliente; os lançamentos são feitos no prazo máximo de 60 dias  _(artigo 116.º, n.os 1 e 4, do CIRS)_. Ficam dispensados os titulares isentos ao abrigo do art. 53.º do CIVA que emitam faturas só pelas aplicações da AT (art. 116.º, n.º 5, al. b))
- **Saída do regime simplificado**: Só cessa quando o limite de 200.000 EUR é ultrapassado em dois períodos consecutivos, ou num só período em mais de 25 %; nesse caso, a contabilidade organizada aplica-se a partir do período seguinte  _(artigo 28.º, n.º 6, do CIRS)_
- **Opção pela contabilidade organizada**: Na declaração de início de atividade ou até ao fim de março do ano em que se pretende mudar; a opção mantém-se até nova declaração de alterações (já não existe o prazo mínimo de 3 anos)  _(artigo 28.º, n.os 3 a 5, do CIRS)_
- **Contabilidade organizada**: Quem não está no regime simplificado tem de dispor de contabilidade organizada, aplicando-se o art. 123.º do CIRC  _(artigo 117.º do CIRS)_

Para titulares do regime de Residente Não Habitual (RNH) ou do Incentivo Fiscal à Investigação Científica e Inovação (IFICI), consulte a skill pt-nhr-ifici para o tratamento específico desses regimes. Para o cálculo do IRS da categoria B, consulte a skill pt-income-tax.

## Secção 4: Classificação de Gastos

### Gastos Dedutíveis (IRC)

Um gasto é dedutível quando é suportado para obter ou garantir os rendimentos sujeitos a IRC e está documentado; as exceções estão no art. 23.º-A do CIRC.

**Gastos Dedutíveis (IRC)**

| Categoria | Código SNC | Dedutibilidade |
| --- | --- | --- |
| Renda (instalações da empresa) | 6261 | Dedutível |
| Eletricidade, combustíveis e água | 6241 / 6242 / 6243 | Dedutível (combustíveis só na parte provada como relativa a bens do ativo ou locados e dentro de consumos normais, art. 23.º-A, n.º 1, al. j)) |
| Honorários e trabalhos especializados (contabilista, advogado) | 6224 / 6221 | Dedutível |
| Seguros (de empresa) | 6263 | Dedutível |
| Publicidade | 6222 | Dedutível |
| Material de escritório | 6233 | Dedutível |
| Telecomunicações | 6262 | Dedutível na parte empresarial |
| Despesas e comissões bancárias | 6268 / 698 | Dedutível |
| Gastos com o pessoal | 63x | Dedutível (participação nos lucros só se paga até ao fim do período seguinte, art. 23.º-A, n.º 1, al. n)) |
| Deslocações e estadas (empresariais) | 6251 | Dedutível mediante documentação |
| Subscrições de software | 6221 | Dedutível |
| Conservação e reparação | 6226 | Dedutível |

### Gastos Parcial ou Totalmente Não Dedutíveis

**Gastos Parcial ou Totalmente Não Dedutíveis** (CIRC art. 23.º-A, n.º 1)

| Categoria | Limitação |
| --- | --- |
| IRC, incluindo as tributações autónomas | Não dedutível (al. a)) |
| Despesas não documentadas | Não dedutíveis (al. b)) + tributação autónoma de 50 % (art. 88.º, n.º 1) |
| Multas, coimas e juros compensatórios e moratórios por infrações não contratuais | Não dedutíveis (al. e)) |
| Ajudas de custo e km em viatura própria não faturados a clientes, sem mapa de controlo por pagamento | Não dedutíveis (al. h)) |
| Depreciações e rendas de viaturas ligeiras de passageiros acima do limite da Portaria 467/2010 | Não dedutíveis na parte excedente (art. 34.º, n.º 1, al. e); art. 23.º-A, n.º 1, al. i)) |
| Pagamentos a entidades em regime fiscal claramente mais favorável | Não dedutíveis, salvo prova de que as operações foram efetivamente realizadas e não têm caráter anormal nem montante exagerado (al. r)) |
| Despesas de representação e encargos com viaturas | Dedutíveis, mas sujeitos a tributação autónoma (art. 88.º) |

### Tributação Autónoma

Tributação adicional incidente sobre determinados gastos, devida ainda que a empresa não tenha lucro tributável (CIRC art. 88.º). Taxas de 2026, alinhadas com a skill pt-corporate-tax:

**Tributação Autónoma**

| Gasto | Taxa |
| --- | --- |
| Despesas de representação (art. 88.º, n.º 7) | 10 % |
| Encargos com viaturas ligeiras de passageiros, custo de aquisição inferior a 37.500 EUR (art. 88.º, n.º 3, al. a)) | 8 % |
| Encargos com viaturas, custo de 37.500 EUR a menos de 45.000 EUR (al. b)) | 25 % |
| Encargos com viaturas, custo igual ou superior a 45.000 EUR (al. c)) | 32 % |
| Híbridos plug-in elegíveis e viaturas a GNV, mesmos escalões (art. 88.º, n.º 18) | 2,5 % / 7,5 % / 15 % |
| Viaturas exclusivamente elétricas (art. 88.º, n.º 20) | 0 % até ao custo fixado na Portaria 467/2010 (62.500 EUR); 10 % se o custo de aquisição exceder esse valor |
| Despesas não documentadas (art. 88.º, n.os 1 e 2) | 50 % (70 % se a entidade for isenta ou não exercer a título principal atividade comercial, industrial ou agrícola) |
| Ajudas de custo e km em viatura própria não faturados a clientes (art. 88.º, n.º 9) | 5 % |
| Pagamentos a entidades em regime fiscal claramente mais favorável (art. 88.º, n.º 8) | 35 % (55 % para as entidades do n.º 2) |
| Agravamento em período com prejuízo fiscal (art. 88.º, n.º 14) | +10 pontos percentuais, exceto no período de início de atividade e no seguinte e, em 2026, nas situações do art. 95.º, n.º 5, da Lei 73-A/2025 (ver pt-corporate-tax) |

Os encargos com viaturas incluem depreciações, rendas ou alugueres, seguros, manutenção e conservação, combustíveis e impostos sobre a posse ou utilização (art. 88.º, n.º 5). As taxas dos n.os 7, 9, 11 e 13 e o agravamento não se aplicam a sujeitos passivos no regime simplificado do IRC (art. 88.º, n.º 16).

## Secção 5: Limiares Ativo vs Gasto

### Regras de Capitalização

**Regras de Capitalização**

| Regra | Detalhe |
| --- | --- |
| Capitalização | Um ativo fixo tangível é reconhecido quando é detido para uso na produção, fornecimento, arrendamento ou fins administrativos e se espera que seja usado durante mais de um período (NC-ME 7.1) |
| Elementos de reduzido valor | Ativos com custo unitário até 1.000 EUR podem ser totalmente depreciados num só período de tributação, salvo se fizerem parte de um conjunto que deva ser depreciado como um todo; constam do mapa de depreciações numa linha própria (DR 25/2009, art. 19.º) |
| Dispêndio subsequente | Componentes, grandes reparações e beneficiações reconhecidos como ativo são depreciáveis (CIRC art. 29.º, n.º 5); a sua taxa calcula-se pela vida útil esperada (art. 31.º, n.º 6) |

### Taxas de Depreciação (Decreto Regulamentar n.º 25/2009: Tabela II, taxas genéricas)

**Taxas de Depreciação (Decreto Regulamentar n.º 25/2009: Tabela II)**  _(DR 25/2009, Tabela II, texto original no Diário da República; única alteração às tabelas: código 2250, Lei 82-D/2014)_

As taxas da Tabela I (por setor de atividade) prevalecem para o equipamento específico do setor; a Tabela II aplica-se aos bens comuns. A vida útil máxima resulta da quota mínima (metade da taxa).

| Tipo de ativo (código Tabela II) | Método | Taxa máxima anual | Vida útil mínima / máxima |
| --- | --- | --- | --- |
| Edifícios industriais (2020) | Linha reta | 5 % | 20 / 40 anos |
| Edifícios comerciais e administrativos (2015) | Linha reta | 2 % | 50 / 100 anos |
| Edifícios habitacionais (2010) | Linha reta | 2 % | 50 / 100 anos |
| Edificações ligeiras (fibrocimento, madeira, zinco) (2005) | Linha reta | 10 % | 10 / 20 anos |
| Máquinas não especificadas (2295) | Linha reta | 12,5 % | 8 / 16 anos |
| Viaturas pesadas e reboques de mercadorias (2385) | Linha reta | 20 % | 5 / 10 anos |
| Viaturas pesadas de passageiros (2380) | Linha reta | 14,28 % | 7 / 14 anos |
| Viaturas ligeiras e mistas (2375) | Linha reta | 25 % | 4 / 8 anos |
| Computadores (2240) | Linha reta | 33,33 % | 3 / 6 anos |
| Programas de computadores (2440) | Linha reta | 33,33 % | 3 / 6 anos |
| Mobiliário (2430) | Linha reta | 12,5 % | 8 / 16 anos |
| Máquinas de escrever, de calcular, de contabilidade e de fotocopiar (2275) | Linha reta | 20 % | 5 / 10 anos |
| Ferramentas e utensílios (2265) | Linha reta | 25 % | 4 / 8 anos |
| Goodwill adquirido numa concentração de atividades empresariais | Partes iguais | 1/15 por período (gasto fiscal nos primeiros 15 períodos, para goodwill reconhecido em períodos iniciados em ou após 1 de janeiro de 2024) | 15 anos |

Limites ao custo de viaturas ligeiras de passageiros para efeitos de depreciação (Portaria 467/2010, art. 1.º, n.º 4): 62.500 EUR (elétricas), 50.000 EUR (híbridas plug-in), 37.500 EUR (GPL ou GNV), 25.000 EUR (restantes). A parte do custo acima do limite não é depreciável fiscalmente (CIRC art. 34.º, n.º 1, al. e)).

### Regras-Chave

- **Método regra**: Linha reta (CIRC art. 30.º, n.º 1). As quotas decrescentes podem ser usadas em ativos fixos tangíveis não adquiridos em estado de uso e que não sejam edifícios, viaturas ligeiras de passageiros ou mistas (salvo serviço público de transportes ou aluguer), mobiliário e equipamentos sociais (art. 30.º, n.º 2). Na NC-ME o método contabilístico é sempre a linha reta (NC-ME 7.14)
- **Coeficientes das quotas decrescentes**: 1,5 (vida útil inferior a 5 anos), 2 (5 ou 6 anos), 2,5 (mais de 6 anos) (CIRC art. 31.º, n.º 4)
- **Quota mínima**: Metade da taxa da linha reta; as quotas mínimas não deduzidas não podem ser recuperadas noutros períodos (CIRC art. 31.º-A, n.os 3 e 4)
- **Quota abaixo da mínima**: Exige comunicação à AT até ao fim do período de tributação, com as quotas e as razões (CIRC art. 31.º-A, n.º 5)
- **Início da depreciação**: Só depois de o ativo entrar em funcionamento ou utilização (CIRC art. 29.º, n.º 4). No primeiro ano o sujeito passivo pode optar por uma taxa proporcional ao número de meses desde o mês de entrada em funcionamento (art. 31.º, n.º 7)
- **Terrenos não depreciáveis**: Não é aceite a depreciação de imóveis na parte do valor do terreno (CIRC art. 34.º, n.º 1, al. b))
- **Vida útil máxima**: Não se aceitam depreciações para além do período máximo de vida útil, que resulta das quotas mínimas (CIRC art. 34.º, n.º 1, al. d), e n.º 2)

## Secção 6: Modelo da Demonstração de Resultados (por Naturezas)

As entidades sujeitas ao SNC apresentam a demonstração dos resultados por naturezas; a demonstração por funções é facultativa (DL 158/2009, art. 11.º, n.os 1 e 2). Linhas do modelo reduzido da Portaria 220/2015 (as subtotais "EBITDA" e "EBIT" correspondem às linhas oficiais indicadas):

### Por Naturezas (modelo padrão para todas as entidades sujeitas ao SNC)

**Modelo Demonstração de Resultados por Naturezas**

```
Vendas e serviços prestados                                      xxx
Subsídios à exploração                                           xxx
Variação nos inventários da produção                           +/-xxx
Trabalhos para a própria entidade                                xxx
Custo das mercadorias vendidas e das matérias consumidas        (xxx)
Fornecimentos e serviços externos                               (xxx)
Gastos com o pessoal                                            (xxx)
Ajustamentos de inventários (perdas/reversões)                 -/+xxx
Imparidade de dívidas a receber (perdas/reversões)             -/+xxx
Provisões (aumentos/reduções)                                  -/+xxx
Outras imparidades (perdas/reversões)                          -/+xxx
Aumentos/reduções de justo valor                               +/-xxx
Outros rendimentos                                               xxx
Outros gastos                                                   (xxx)
                                                              -------
Resultado antes de depreciações, gastos de financiamento
e impostos (EBITDA)                                              xxx

Gastos/reversões de depreciação e de amortização               -/+xxx
                                                              -------
Resultado operacional (antes de gastos de financiamento
e impostos) (EBIT)                                               xxx

Juros e rendimentos similares obtidos                            xxx
Juros e gastos similares suportados                             (xxx)
                                                              -------
Resultado antes de impostos                                      xxx

Imposto sobre o rendimento do período                          -/+xxx
                                                              -------
Resultado líquido do período                                     xxx
```

## Secção 7: Modelo do Balanço

Portugal utiliza o formato vertical com classificação corrente/não corrente (Portaria 220/2015). Linhas principais do modelo:

### Modelo

**Modelo do Balanço**

```
ATIVO

Ativo não corrente
  Ativos fixos tangíveis                                      xxx
  Propriedades de investimento                                xxx
  Goodwill                                                    xxx
  Ativos intangíveis                                          xxx
  Ativos biológicos                                           xxx
  Participações financeiras - método da equivalência patrimonial xxx
  Outros investimentos financeiros                            xxx
  Créditos a receber                                          xxx
  Ativos por impostos diferidos                               xxx
                                                           -------
  Total do ativo não corrente                                 xxx

Ativo corrente
  Inventários                                                 xxx
  Ativos biológicos                                           xxx
  Clientes                                                    xxx
  Estado e outros entes públicos                              xxx
  Capital subscrito e não realizado                           xxx
  Outros créditos a receber                                   xxx
  Diferimentos                                                xxx
  Ativos financeiros detidos para negociação                  xxx
  Outros ativos financeiros                                   xxx
  Ativos não correntes detidos para venda                     xxx
  Caixa e depósitos bancários                                 xxx
                                                           -------
  Total do ativo corrente                                     xxx

TOTAL DO ATIVO                                                xxx
                                                           =======

CAPITAL PRÓPRIO E PASSIVO

Capital próprio
  Capital subscrito                                           xxx
  Ações (quotas) próprias                                    (xxx)
  Outros instrumentos de capital próprio                      xxx
  Prémios de emissão                                          xxx
  Reservas legais                                             xxx
  Outras reservas                                             xxx
  Resultados transitados                                      xxx
  Excedentes de revalorização                                 xxx
  Ajustamentos/outras variações no capital próprio            xxx
  Resultado líquido do período                                xxx
                                                           -------
  Total do capital próprio                                    xxx

Passivo não corrente
  Provisões                                                   xxx
  Financiamentos obtidos                                      xxx
  Responsabilidades por benefícios pós-emprego                xxx
  Passivos por impostos diferidos                             xxx
  Outras dívidas a pagar                                      xxx
                                                           -------
  Total do passivo não corrente                               xxx

Passivo corrente
  Fornecedores                                                xxx
  Adiantamentos de clientes                                   xxx
  Estado e outros entes públicos                              xxx
  Financiamentos obtidos                                      xxx
  Outras dívidas a pagar                                      xxx
  Diferimentos                                                xxx
  Passivos financeiros detidos para negociação                xxx
  Outros passivos financeiros                                 xxx
                                                           -------
  Total do passivo corrente                                   xxx

TOTAL DO CAPITAL PRÓPRIO E PASSIVO                            xxx
                                                           =======
```

## Secção 8: Padrões de Reconciliação Bancária

### Extratos bancários

Os bancos portugueses (Millennium BCP, Caixa Geral de Depósitos, Novo Banco, Santander, BPI, ActivoBank e outros) disponibilizam extratos exportáveis. O formato e os campos variam por banco e por canal: confirme com o cliente o ficheiro que o seu banco entrega (CSV, OFX ou PDF) antes de importar.

### Descrições Habituais de Movimentos

**Descrições Habituais de Movimentos** (padrões práticos, não normas)

| Padrão | Classificação |
| --- | --- |
| TRF, TRANSFERENCIA | Transferência (verificar sentido) |
| DD, DEBITO DIRETO | Débito direto (gasto recorrente) |
| MB, MULTIBANCO | Pagamento ATM/cartão |
| PAGAMENTO DE SERVICOS | Pagamento de serviços (utilidades, Estado, etc.) |
| AT-AUTORIDADE TRIBUTARIA | Pagamento de imposto à AT (conta 24x) |
| SEGURANCA SOCIAL, SS | Pagamento à Segurança Social (conta 245) |
| COMPRA/VENDA MB WAY | Pagamento móvel |
| JUROS | Juros (691 se suportados; 79 se obtidos) |
| COMISSAO, DESPESA | Despesas bancárias |
| IMPOSTO SELO | Imposto do selo (sobre operações bancárias, conta 681) |

## Secção 9: Simplificações para Microentidades e Pequenos Negócios

### Categorias de Dimensão (períodos iniciados em ou após 1 de janeiro de 2026)

O DL 126-B/2025 alterou o art. 9.º do DL 158/2009 e aplica-se às demonstrações financeiras dos exercícios iniciados em ou após 1 de janeiro de 2026. Os limites de número de empregados não mudaram.

**Categorias de Dimensão (2026)**

| Categoria | Total do balanço | Volume de negócios líquido | Número médio de empregados |
| --- | --- | --- | --- |
| Microentidade | ≤ 450.000 EUR (antes: 350.000 EUR) | ≤ 900.000 EUR (antes: 700.000 EUR) | ≤ 10 |
| Pequena entidade | ≤ 5.000.000 EUR (antes: 4.000.000 EUR) | ≤ 10.000.000 EUR (antes: 8.000.000 EUR) | ≤ 50 |
| Média entidade | ≤ 25.000.000 EUR (antes: 20.000.000 EUR) | ≤ 50.000.000 EUR (antes: 40.000.000 EUR) | ≤ 250 |
| Grande entidade | Ultrapassa dois dos três limites da média entidade; as entidades de interesse público são sempre grandes | | |

- **Regra dos 2 de 3 critérios**: Cada categoria abrange as entidades que, à data do balanço, não ultrapassem dois dos três limites (DL 158/2009, art. 9.º). Os limites reportam-se ao período imediatamente anterior; a entidade só sai da categoria quando ultrapassa dois dos três limites em dois períodos consecutivos, a partir do terceiro período, e regressa quando deixa de os ultrapassar em dois períodos consecutivos (art. 9.º-A).
- **Grupos**: Pequenos grupos: balanço 7.500.000 EUR, volume de negócios 15.000.000 EUR, 50 empregados; grupos médios: 25.000.000 EUR, 50.000.000 EUR, 250 empregados (art. 9.º-B, na redação do DL 126-B/2025).

### Normas Aplicáveis

**Normas Aplicáveis**

| Categoria | Norma | Principais simplificações |
| --- | --- | --- |
| Microentidade | NC-ME (obrigatória, salvo opção por NCRF ou NCRF-PE declarada na Modelo 22; DL 158/2009, art. 9.º-D) | Sem impostos diferidos (método do imposto a pagar); ativos ao custo; sem demonstração dos fluxos de caixa nem das alterações no capital próprio; anexo dispensável se as divulgações do art. 11.º, n.º 4, constarem no fim do balanço |
| Pequena entidade | NCRF-PE (por opção, em alternativa às NCRF; art. 9.º-C) | Dispensa da demonstração dos fluxos de caixa e da demonstração das alterações no capital próprio; modelos reduzidos (art. 11.º, n.º 3) |
| Média/Grande | NCRF completas (NCRF 1 a 28) | Balanço, demonstração dos resultados por naturezas, demonstração das alterações no capital próprio, demonstração dos fluxos de caixa e anexo (art. 11.º, n.º 1) |

### Simplificações NC-ME (Microentidades)

- **Demonstrações financeiras**: Balanço e demonstração dos resultados (modelos reduzidos); sem demonstração dos fluxos de caixa nem das alterações no capital próprio (DL 158/2009, art. 11.º, n.º 3)
- **Anexo**: A microentidade fica dispensada do anexo se divulgar, no fim do balanço, os compromissos e garantias fora do balanço, os adiantamentos e créditos a membros dos órgãos sociais e as demais informações do art. 11.º, n.º 4
- **Mensuração de ativos**: Ativos fixos tangíveis ao custo, deduzido da depreciação acumulada (NC-ME 7.6); sem revalorizações; depreciação sempre em linha reta (NC-ME 7.14)
- **Impostos sobre o rendimento**: Método do imposto a pagar, sem impostos diferidos; inclui as tributações autónomas (NC-ME 16.1 e 16.2)
- **Locações**: A NC-ME distingue locações financeiras e operacionais. O locatário reconhece a locação financeira como ativo e passivo (NC-ME 9.5); as rendas de locações operacionais são gasto em linha reta durante o prazo (NC-ME 9.8)

### Empresário em Nome Individual (Trabalhador Independente)

- **Dispensa do SNC**: Pessoas singulares com atividade comercial, industrial ou agrícola cujo volume de negócios médio dos últimos três anos não exceda 200.000 EUR (DL 158/2009, art. 10.º, n.º 1)
- **Regime simplificado**: Até 200.000 EUR de rendimentos da categoria B no ano anterior (CIRS art. 28.º, n.º 2); tributação pela aplicação dos coeficientes do art. 31.º; sem contabilidade organizada, apenas os registos do art. 116.º do CIRS
- **Contabilidade organizada facultativa/obrigatória**: Por opção (art. 28.º, n.º 3) ou quando o regime simplificado cessa (art. 28.º, n.º 6)
- **Contabilista certificado**: Obrigatório quando há contabilidade organizada, porque só ele pode assumir a regularidade técnica e assinar as declarações fiscais baseadas na contabilidade (Estatuto da OCC, art. 10.º, n.º 1, al. b))

Para o tratamento do regime de Residente Não Habitual (RNH) e do Incentivo Fiscal à Investigação Científica e Inovação (IFICI), consulte a skill pt-nhr-ifici.

## Secção 10: Articulação com Skills Fiscais

### Imposto sobre o Rendimento das Pessoas Coletivas (IRC)

- **IES integra dados contabilísticos e fiscais**: A IES cumpre num só envio a declaração anual de informação contabilística e fiscal, o registo da prestação de contas, a informação estatística ao INE, ao Banco de Portugal e à DGAE e a confirmação do beneficiário efetivo (Portaria 191/2025/1, preâmbulo; DL 8/2007, art. 2.º). Entrega até 15 de julho (CIRC art. 121.º, n.º 2); se o período não for o ano civil, até ao dia 15 do 7.º mês após o fim do período (n.º 3)
- **Modelo 22**: Até ao último dia de maio (CIRC art. 120.º, n.º 1); período diferente do ano civil: até ao último dia do 5.º mês após o fim do período (n.º 2)
- **Resultado fiscal e Quadro 07**: O resultado fiscal parte do resultado contabilístico (conta 811/818) com as correções fiscais no Quadro 07 da Modelo 22
- **Principais correções fiscais**: Tributação autónoma, gastos não dedutíveis do art. 23.º-A, depreciações acima das quotas máximas, benefícios fiscais (SIFIDE II, RFAI, DLRR). Ver pt-corporate-tax
- **Taxa de IRC geral**: 19 % nos períodos de tributação iniciados em 2026 (18 % em 2027, 17 % a partir de 2028)  _(artigo 87.º, n.º 1, do CIRC; artigo 3.º da Lei n.º 64/2025; ver a skill pt-corporate-tax)_
- **Taxa reduzida PME primeiros 50.000 EUR**: 15 % em 2026 sobre os primeiros 50.000 EUR de matéria coletável de PME e Small Mid Cap; o excedente paga a taxa geral; derrama estadual sobre a parte do lucro tributável acima de 1.500.000 EUR (art. 87.º-A, n.º 1)  _(artigos 87.º, n.º 2, e 87.º-A do CIRC; ver a skill pt-corporate-tax)_

Utilize a skill pt-corporate-tax para o apuramento do IRC e a skill pt-income-tax para o IRS da categoria B.

### IVA

- **Contas do IVA**: Conta 243 do Código de Contas, subcontas 2431 a 2439
- **Periodicidade mensal vs trimestral**: Declaração mensal se o volume de negócios do ano civil anterior for igual ou superior a 650.000 EUR; trimestral se inferior; entrega até ao dia 20 do 2.º mês seguinte ao período (CIVA art. 41.º, n.º 1)
- **Taxas no continente**: 6 % (Lista I), 13 % (Lista II), 23 % (restantes) (CIVA art. 18.º, n.º 1)
- **Taxas nos Açores**: 4 % / 9 % / 16 %, fixadas pela Região ao abrigo do CIVA art. 18.º, n.º 3 (AT, Ofício Circulado 25045/2024; ver portugal-vat-return)
- **Taxas na Madeira**: 4 % / 12 % / 22 % (AT, Ofício Circulado 25045/2024; ver portugal-vat-return)
- **Conservação dos registos de IVA**: 10 anos civis subsequentes (CIVA art. 52.º, n.º 1)

Utilize a skill portugal-vat-return para detalhes da submissão.

### Faturação, comunicação de faturas e SAF-T (PT)

- **Programa de faturação certificado**: Obrigatório, em exclusivo, para quem tenha tido no ano civil anterior volume de negócios superior a 50.000 EUR, quem utilize programas informáticos de faturação, ou quem tenha ou opte por contabilidade organizada (DL 28/2019, art. 4.º, n.º 1). Abaixo destes casos podem usar-se as aplicações de faturação da AT ou documentos pré-impressos em tipografia autorizada (art. 3.º)
- **Comunicação dos elementos das faturas (e-fatura)**: Até ao dia 5 do mês seguinte ao da emissão, em tempo real, por ficheiro SAF-T (PT) ou por inserção no Portal das Finanças (DL 198/2012, art. 3.º, n.os 1 e 2). Quem está obrigado a produzir o SAF-T (PT) usa o envio em tempo real ou o ficheiro (art. 3.º, n.º 3)
- **Comunicação de inventários**: Entidades com contabilidade organizada obrigadas a inventário comunicam o inventário até 31 de janeiro (DL 198/2012, art. 3.º-A, n.º 1); dispensadas as que estão no regime simplificado (n.º 3). Para os períodos iniciados em ou após 1 de janeiro de 2026, quem não está obrigado a inventário permanente fica dispensado de valorizar o inventário nessa comunicação (Lei 73-A/2025, art. 95.º, n.º 1, al. b))
- **SAF-T (PT) da contabilidade**: Só se aplica aos períodos de 2027 e seguintes, a entregar em 2028 (Lei 73-A/2025, art. 95.º, n.º 2). A IES de 2026 não depende do ficheiro (Portaria 191/2025/1, art. 3.º, n.º 2)
- **Faturas em PDF**: Até 31 de dezembro de 2026 as faturas em PDF são aceites como faturas eletrónicas para todos os efeitos fiscais (Lei 73-A/2025, art. 95.º, n.º 3). Ver portugal-einvoice
- **Capacidade de exportação**: As entidades com contabilidade organizada devem conseguir exportar ficheiros no formato definido por portaria (CIRC art. 123.º, n.º 8)

### Segurança Social

- **Contribuição da entidade empregadora**: 23,75 % da remuneração ilíquida, no regime geral (Código Contributivo, art. 53.º; ISS, Guia Prático de Inscrição, Vinculação e Cessação de Atividade de Trabalhador por Conta de Outrem; ver pt-social-contributions)
- **Contribuição do trabalhador**: 11 % da remuneração ilíquida (idem)
- **Trabalhador independente**: 21,4 % do rendimento relevante; 25,2 % para empresários em nome individual e titulares de EIRL e respetivos cônjuges. O rendimento relevante é 70 % do valor das prestações de serviços e 20 % dos rendimentos da venda de bens e dos serviços de hotelaria, restauração e bebidas (Segurança Social, Guia Prático do Trabalhador Independente, 2026)
- **Registo contabilístico**: Registado na conta 245 até ao pagamento; o encargo da entidade empregadora vai a 635

Utilize a skill pt-social-contributions para detalhes.

### Conservação de Documentos

- **Período de conservação obrigatório**: 10 anos para todos os livros, registos e documentos de suporte, salvo prazo especial; se o sujeito passivo exercer um direito com prazo mais longo, conserva até ao fim do prazo de caducidade da liquidação respetiva  _(DL 28/2019, art. 19.º, n.os 1 e 2; CIVA art. 52.º, n.º 1)_. O antigo n.º 4 do art. 123.º do CIRC foi revogado pelo DL 28/2019
- **Âmbito de aplicação**: Livros, registos, faturas e documentos de suporte, incluindo a documentação da análise, programação e execução dos tratamentos informáticos e as cópias de segurança dos programas de faturação e contabilidade (DL 28/2019, art. 19.º, n.º 4)
- **Conservação eletrónica**: Admitida, com armazenamento seguro, controlos de integridade e acesso e legibilidade pela AT (DL 28/2019, art. 19.º, n.º 3)
- **Local do arquivo**: Em papel: em estabelecimento em Portugal; em suporte eletrónico: em qualquer Estado-membro da UE; fora da UE só com autorização prévia da AT (DL 28/2019, art. 20.º, n.os 1 e 2). O local do arquivo indica-se na declaração de início de atividade (art. 20.º, n.º 5)

## Sources

| Source | URL | Read on |
|---|---|---|
| DL 158/2009 (SNC), republicado pelo DL 98/2015: arts. 9.º a 11.º (categorias, NC-ME, NCRF-PE, dispensa, demonstrações financeiras) | https://www.cnc.min-financas.pt/pdf/SNC/2016/DL_98_2015_2_jun.pdf | 2026-10-30 |
| DL 126-B/2025: novos limites de dimensão a partir de 2026 (arts. 9.º e 9.º-B do DL 158/2009) | https://www.cnc.min-financas.pt/pdf/SNC/DL126_B_2025_05Dez.pdf | 2026-10-30 |
| Portaria 218/2015, Código de Contas SNC | https://www.cnc.min-financas.pt/pdf/SNC/2016/Portaria_218_2015_23Jul_CContas.pdf | 2026-10-30 |
| Portaria 220/2015, modelos de demonstrações financeiras | https://www.cnc.min-financas.pt/pdf/SNC/2016/Portaria_220_2015_24Jul_DF.pdf | 2026-10-30 |
| Aviso 8255/2015, NC-ME | https://www.cnc.min-financas.pt/pdf/SNC/2016/Aviso_8255_2015_29Jul_NC_ME.pdf | 2026-10-30 |
| Aviso 8256/2015, NCRF (NCRF 20 Rédito) | https://www.cnc.min-financas.pt/pdf/SNC/2016/Aviso_8256_2015_29Jul_NCRF_RG.pdf | 2026-10-30 |
| CIRC art. 8.º, período de tributação | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc8.aspx | 2026-10-30 |
| CIRC art. 18.º, periodização | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc18.aspx | 2026-10-30 |
| CIRC art. 23.º-A, encargos não dedutíveis | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc23a.aspx | 2026-10-30 |
| CIRC arts. 29.º, 30.º, 31.º, 31.º-A, depreciações | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc31a.aspx | 2026-10-30 |
| CIRC art. 34.º, depreciações não dedutíveis | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc34.aspx | 2026-10-30 |
| CIRC art. 45.º-A, goodwill em 15 períodos (Lei 82/2023) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc45a.aspx | 2026-10-30 |
| CIRC art. 87.º, taxas de IRC 2026 (Lei 64/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-30 |
| CIRC art. 87.º-A, derrama estadual acima de 1.500.000 EUR | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx | 2026-10-30 |
| CIRC art. 88.º, tributação autónoma | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx | 2026-10-30 |
| CIRC arts. 120.º e 121.º, Modelo 22 e IES | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121.aspx | 2026-10-30 |
| CIRC art. 123.º, obrigações contabilísticas | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc123.aspx | 2026-10-30 |
| CIRS art. 28.º, regime simplificado e opção | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx | 2026-10-30 |
| CIRS art. 31.º, coeficientes | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-10-30 |
| CIRS arts. 116.º e 117.º, registos da categoria B | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs116.aspx | 2026-10-30 |
| CIVA art. 18.º, taxas | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx | 2026-10-30 |
| CIVA art. 36.º, prazo de emissão das faturas | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva36.aspx | 2026-10-30 |
| CIVA art. 41.º, periodicidade (650.000 EUR) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva41.aspx | 2026-10-30 |
| CIVA art. 52.º, conservação por 10 anos (DL 49/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva52.aspx | 2026-10-30 |
| DL 28/2019 (versão consolidada AT): arts. 3.º, 4.º, 19.º e 20.º | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Decreto_Lei_28_2019.pdf | 2026-10-30 |
| DL 198/2012 (versão consolidada AT): arts. 3.º e 3.º-A | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Decreto-Lei%20n%20_198_2012_24_08.pdf | 2026-10-30 |
| Lei 73-A/2025 (OE 2026), art. 95.º (SAF-T contabilidade, inventários, faturas PDF) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei-73-A-2025.pdf | 2026-10-30 |
| Portaria 191/2025/1, IES/DA | https://files.diariodarepublica.pt/1s/2025/04/07500/0005800061.pdf | 2026-10-30 |
| Decreto Regulamentar 25/2009, texto original (Tabela II) | https://files.diariodarepublica.pt/1s/2009/09/17800/0627006285.pdf | 2026-10-30 |
| Decreto Regulamentar 25/2009, versão AT (art. 19.º, elementos de reduzido valor) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/outros_diplomas/Documents/Dec_Regulamentar25_2009.pdf | 2026-10-30 |
| Portaria 467/2010, limites de custo das viaturas | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_467-2010.pdf | 2026-10-30 |
| Estatuto da Ordem dos Contabilistas Certificados (texto da OCC, 2024), art. 10.º | https://www.occ.pt/sites/default/files/public/2024-09/Estatuto_2024.pdf | 2026-10-30 |
| Segurança Social, Guia Prático, Trabalhadores Independentes (21,4 %, 25,2 %, 70 %/20 %) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-30 |
| Segurança Social, Guia Prático, Inscrição, Vinculação e Cessação de Atividade de Trabalhador por Conta de Outrem (19 May 2026: 23,75 % / 11 %) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xlxpq00d9kl2y0p3inyft | 2026-10-30 |
| AT, Ofício Circulado 25045/2024 (taxas do IVA nos Açores e na Madeira) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_25045_2024.pdf | 2026-10-30 |

Not yet confirmed: whether the Azores 2026 regional budget changed the Azores VAT rates (the AT circular is dated 6 December 2024; the Azores budget was not read); the CAE revision now in force (the old version said Rev. 3; DL 28/2019 still cites Rev. 3); the old "anexo NC-ME com máximo de 15 rubricas" claim (no such limit found in the NC-ME or DL 158/2009, art. 11.º); account 6811 label (blank in the Portaria text extracted); the tax treatment of goodwill recognised before 2024 (the old version said 20 years / 5%; the earlier wording of CIRC art. 45.º-A was not read); the bank-by-bank statement export formats (CSV/OFX per bank) from the old version, which have no official source.

## Aviso Legal

Esta skill e os respectivos resultados são disponibilizados apenas para fins informativos e de apoio ao cálculo e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus colaboradores não aceitam qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado (Contabilista Certificado membro da OCC) antes da submissão ou de qualquer actuação com base nos mesmos.

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
