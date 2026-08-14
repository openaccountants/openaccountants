---
name: pt-nhr-ifici
description: "Utilizar este skill sempre que questões envolvam o regime do Residente Não Habitual (RNH) em Portugal ou o seu sucessor, o Incentivo Fiscal à Investigação Científica e Inovação (IFICI). Acionar perante expressões como \"RNH\", \"Residente Não Habitual\", \"IFICI\", \"Incentivo Fiscal à Investigação Científica e Inovação\", \"20% taxa fixa\", \"nómadas digitais Portugal\", \"isenção rendimentos estrangeiros\", \"Modelo 3 anexo L\", \"Atividades de Elevado Valor Acrescentado\", \"AEVA\", \"Portaria 187/2024\", \"EBF artigo 58.º-A\", \"Despacho 230/2019\", \"pensões estrangeiras Portugal\", \"convenções dupla tributação Portugal\". Também acionar em pedidos formulados em inglês: \"Portugal NHR regime\", \"Portugal digital nomad tax\", \"non-habitual resident Portugal\", \"IFICI scheme Portugal\", \"20% flat rate Portugal\", \"foreign income exemption Portugal\", \"Portugal pension tax 10%\", \"Portugal tax residency\", \"NHR replacement Portugal\". Cobre o RNH legado criado pelo DL 249/2009 (fechado a novos pedidos desde 1 jan 2024 pela Lei 82/2023), o IFICI introduzido pela Portaria n.º 187/2024/1 ao abrigo do art.º 58.º-A do EBF, a taxa fixa de 20% sobre rendimentos das categorias A e B em Atividades de Elevado Valor Acrescentado, a matriz de isenção de rendimentos de fonte estrangeira por tipo de rendimento e país, o tratamento das pensões estrangeiras (incluindo a tributação a 10% introduzida pelo OE 2020), mais-valias e dividendos estrangeiros, convenções de dupla tributação aplicáveis (~80 acordos), processo de candidatura no Portal das Finanças até 31 de março do ano seguinte ao da residência, perda de estatuto por interrupção da residência, e preenchimento do Anexo L do Modelo 3. LER SEMPRE este skill antes de tratar fiscalidade RNH/IFICI em Portugal."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - pt-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PT Nhr Ifici

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | República Portuguesa |
| Regime(s) cobertos | RNH (legado, DL 249/2009) e IFICI (sucessor, EBF art.º 58.º-A) |
| Moeda | EUR (Euro) |
| Ano fiscal | Ano civil (1 de janeiro a 31 de dezembro) |
| Legislação RNH | Decreto-Lei n.º 249/2009, de 23 de setembro (criação); CIRS art.º 16.º n.º 8 a 12 |
| Legislação IFICI | Estatuto dos Benefícios Fiscais (EBF), art.º 58.º-A; Portaria n.º 187/2024/1 |
| Lei de encerramento do RNH | Lei n.º 82/2023, de 29 de dezembro (Orçamento do Estado para 2024) |
| Autoridade fiscal | Autoridade Tributária e Aduaneira (AT) |
| Portal | Portal das Finanças (https://www.portaldasfinancas.gov.pt) |
| Prazo de candidatura | Até 31 de março do ano seguinte ao da inscrição como residente fiscal |
| Duração do estatuto | 10 anos consecutivos (não renovável, não recuperável após interrupção) |
| Declaração anual | Modelo 3 do IRS, Anexo L (residentes não habituais) |
| Prazo Modelo 3 | 1 de abril a 30 de junho do ano seguinte (regime geral IRS) |
| Validado por | Pendente — requer validação por Contabilista Certificado (CC) inscrito na OCC ou advogado em Portugal |
| Data de validação | Pendente |
| Versão do skill | 1.0 |

### Quadro comparativo — RNH vs IFICI vs Regime geral IRS

**Quadro comparativo — RNH vs IFICI vs Regime geral IRS**  _(CIRS (todo))_

| Característica | RNH (legado, até 31 dez 2023) | IFICI (a partir de 1 jan 2024) | Regime geral IRS |
| --- | --- | --- | --- |
| Base legal | DL 249/2009; CIRS art.º 16.º n.º 8-12 | EBF art.º 58.º-A; Portaria 187/2024/1 | CIRS (todo) |
| Aberto a novos pedidos? | **Não — fechado desde 1 jan 2024** (Lei 82/2023). Pedidos transitórios admitidos durante 2024 sob condições específicas. | Sim, para pedidos a partir de 1 jan 2024 | Sempre aplicável por defeito |
| Duração | 10 anos | 10 anos | Sem limite |
| Taxa sobre rendimentos das categorias A e B em AEVA exercidas em Portugal | 20% taxa fixa | 20% taxa fixa | Tabela progressiva 13% — 48% (escalões IRS 2025) + sobretaxa de solidariedade 2,5% / 5% |
| Lista de Atividades de Elevado Valor Acrescentado (AEVA) | Despacho n.º 230/2019, de 4 de julho (lista ampla — engenheiros, médicos, gestores, profissionais TIC, etc.) | Portaria n.º 187/2024/1 (lista restrita — investigação científica, ensino superior, indústrias de elevada qualificação) | Não aplicável |
| Isenção de rendimentos de fonte estrangeira (cat. E, F, G, H) | Ampla — isenção se sujeitos a tributação no Estado da fonte ao abrigo de CDT ou Modelo OCDE | Mais restrita — isenção para certos tipos (categoria B AEVA, E, F, G) se sujeitos a tributação no Estado da fonte; pensões e algumas mais-valias **excluídas** | Tributação mundial — englobamento ou taxa especial (28% capital), com crédito por dupla tributação internacional (art.º 81.º CIRS) |
| Pensões estrangeiras (categoria H) | **Isentas até 31 mar 2020**; tributadas a **10% taxa fixa** para pedidos a partir de 1 abr 2020 (alteração do OE 2020) | **Não cobertas** — pensões estrangeiras tributadas pelo regime geral (englobamento progressivo) | Englobamento, tabela progressiva IRS |
| Profissão / atividade requerida | Não obrigatório exercer AEVA (taxa 20% só se aplicava a quem exercesse; isenção de rendimentos estrangeiros independente) | **Obrigatório** — o requerente tem de exercer efetivamente uma atividade qualificada constante da Portaria | Não aplicável |
| Aplicação | Portal das Finanças, até 31 mar do ano N+1 | Portal das Finanças + entidades certificadoras (FCT, AICEP, IAPMEI, ANI, conforme atividade) | Inscrição como residente fiscal apenas |
| Declaração anual | Modelo 3 + Anexo L | Modelo 3 + Anexo L (com indicação do regime IFICI) | Modelo 3, anexos consoante rendimentos |

### Defaults conservadores — instantâneo

**Defaults conservadores — instantâneo**

| Ambiguidade | Default |
| --- | --- |
| RNH ou IFICI aplicável? | Verificar data de inscrição como residente: ≤ 31 dez 2023 (com pedido até 31 mar 2024) → RNH; ≥ 1 jan 2024 → IFICI ou regime geral |
| Atividade qualificada como AEVA — dúvida na classificação CAE / código de profissão | Não aplicar taxa de 20% sem confirmação documental; tributar no regime geral e sinalizar para revisão |
| Pensão estrangeira sob RNH com pedido entre 1 abr 2020 e 31 dez 2023 | Tributar a 10% taxa fixa (não isenta) |
| Pensão estrangeira sob IFICI | Não isenta — englobar no regime geral |
| Isenção de dividendo / juro / royalty estrangeiro sob RNH/IFICI | Verificar CDT aplicável; se a CDT atribui poder de tributação ao Estado da fonte (mesmo que tributação efetiva seja nula), aplicar isenção; sem CDT, verificar Modelo OCDE |
| Estatuto interrompido por perda de residência fiscal | Anos perdidos **não** se recuperam ao reentrar |
| Pedido apresentado após 31 mar do ano N+1 | A AT pode indeferir; o contribuinte pode reclamar mas o default é regime geral |
| Atividade em IFICI sem certificação da entidade competente (FCT/AICEP/IAPMEI/ANI) | Indeferir o benefício de 20%; tributar no regime geral |

## Secção 2 — Entradas Obrigatórias e Catálogo de Recusas

### Entradas obrigatórias

**Mínimo viável** — confirmação de (a) residência fiscal em Portugal no ano em causa (permanência > 183 dias ou centro de interesses vitais nos termos do art.º 16.º n.º 1 do CIRS), (b) inexistência de residência fiscal em Portugal nos 5 anos anteriores (requisito tanto do RNH como do IFICI), (c) data de inscrição como residente fiscal junto da AT, (d) NIF português, (e) morada fiscal portuguesa válida, e (f) inscrição como RNH ou IFICI já efetuada (ou a efetuar) no Portal das Finanças.

**Recomendado** — passaporte / documento de identificação, comprovativo da residência anterior (certificado de residência fiscal do país de saída), contrato de arrendamento ou escritura de aquisição de imóvel em Portugal, contrato de trabalho ou comprovativo da atividade independente, certificado da atividade qualificada (para IFICI: emitido por FCT, AICEP, IAPMEI ou ANI consoante a tipologia), inscrição em ordem profissional quando aplicável (Ordem dos Médicos, Ordem dos Engenheiros, etc.), comprovativos dos rendimentos de fonte estrangeira (declarações fiscais do país da fonte, certificados de retenção, dividendos pagos, pensões), CDT aplicável ao país da fonte, e Modelo 3 do ano anterior (se já residente).

### Catálogo de recusas

- **R-PT-NHR-1** — Pedido de RNH com data de inscrição como residente posterior a 31 dez 2023 (fora das condições transitórias da Lei 82/2023)  _(RNH fechado a novos pedidos pela Lei 82/2023; encaminhar para IFICI ou regime geral)_
- **R-PT-NHR-2** — Contribuinte com residência fiscal em Portugal em qualquer dos 5 anos anteriores  _(Requisito de não-residência prévia falha — nem RNH nem IFICI aplicáveis)_
- **R-PT-NHR-3** — Recuperação do estatuto após interrupção (saída e regresso)  _(RNH/IFICI não permite "recomeço" — anos perdidos não se recuperam)_
- **R-PT-NHR-4** — Atividade qualificada como AEVA sob IFICI sem certificação da entidade competente  _(Sem certificação da FCT/AICEP/IAPMEI/ANI o benefício de 20% é indeferido)_
- **R-PT-NHR-5** — Pedido de RNH apresentado após o prazo legal (31 mar do ano N+1) sem reclamação tempestiva  _(Caducidade do direito ao pedido)_
- **R-PT-NHR-6** — Pensão estrangeira sob RNH com inscrição a partir de 1 abr 2020 a ser tratada como isenta  _(OE 2020 alterou para 10% taxa fixa — não isenta)_
- **R-PT-NHR-7** — Aplicação simultânea de RNH e IFICI  _(Regimes mutuamente exclusivos)_
- **R-PT-NHR-8** — Pedido de classificação como AEVA para atividade não constante das listas oficiais (Despacho 230/2019 ou Portaria 187/2024)  _(Não enquadrável; tributar no regime geral)_
- **R-PT-NHR-9** — Tributação no Estado da fonte invocada para isenção sem documento de suporte (declaração fiscal estrangeira, certificado de retenção)  _(Sem prova, presumir não tributação no estrangeiro e indeferir isenção)_
- **R-PT-NHR-10** — Mais-valias de criptoativos detidos < 365 dias sob RNH/IFICI  _(Regime cripto (Lei 24-D/2022) tributa a 28% — RNH/IFICI não alteram esta regra para detenções curtas)_
- **R-PT-NHR-11** — Contribuinte de nacionalidade portuguesa que regressa a Portugal e pede RNH/IFICI sem cumprir o requisito dos 5 anos  _(Nacionalidade portuguesa não isenta do requisito de não-residência prévia; verificar registo histórico na AT)_
- **R-PT-NHR-12** — Pedido de aplicação retroativa a anos anteriores ao da inscrição como residente  _(Não permitido — o regime aplica-se a partir do ano da inscrição como residente fiscal)_

### Recusas fora de âmbito

Este skill **não cobre**: regime fiscal das stock options para trabalhadores qualificados (CIRS art.º 43.º-C e regimes especiais), regime do Programa Regressar (Lei 71/2018), Golden Visa / Autorização de Residência para Investimento (matéria de imigração, não fiscal), tributação de trusts estrangeiros sob RNH/IFICI (matéria complexa que requer parecer específico), pedidos de informação vinculativa à AT, contencioso fiscal sobre indeferimento de RNH/IFICI, e fiscalidade dos Açores e Madeira (regiões autónomas com taxas próprias — coordenar com skill regional).

## Secção 3 — RNH (Regime Antigo) — Fechado a Novos Pedidos Desde 1 jan 2024

### 3.1 Base legal e história

- **Criação do RNH** — O regime do Residente Não Habitual (RNH) foi criado pelo Decreto-Lei n.º 249/2009, de 23 de setembro, no contexto do Programa de Apoio à Internacionalização da Economia Portuguesa. As regras de fundo foram integradas no Código do IRS (CIRS) nos n.os 8 a 12 do art.º 16.º.  _(Decreto-Lei n.º 249/2009, de 23 de setembro; CIRS art.º 16.º n.º 8-12)_
- **Alteração — Lei 2/2020** — Lei n.º 2/2020, de 31 de março (OE 2020) — introduziu a taxa de 10% sobre pensões estrangeiras (substituindo a isenção total), com efeitos para inscrições a partir de 1 de abril de 2020.  _(Lei n.º 2/2020, de 31 de março)_
- **Alteração — Lei 82/2023** — Lei n.º 82/2023, de 29 de dezembro (OE 2024) — encerrou o regime a novos pedidos com efeitos a 1 de janeiro de 2024, mantendo o regime transitório (art.º 236.º da Lei 82/2023) para quem (i) já fosse residente em 2023 ou (ii) tivesse manifestado intenção de mudança antes de 31 de dezembro de 2023 com documentação comprovativa (contrato de trabalho, contrato de arrendamento, matrícula em estabelecimento de ensino, visto de residência).  _(Lei n.º 82/2023, de 29 de dezembro, art.º 236.º)_

### 3.2 Requisitos de elegibilidade

- **Requisito 1 — Residência fiscal** — Tornar-se residente fiscal em Portugal no ano de inscrição — preencher um dos critérios do art.º 16.º n.º 1 do CIRS: (a) permanência em território português por mais de 183 dias, seguidos ou interpolados, em qualquer período de 12 meses com início ou termo no ano em causa, ou (b) ter em Portugal, num qualquer dia do período mencionado, habitação em condições que façam supor a intenção atual de a manter e ocupar como residência habitual.  _(CIRS art.º 16.º n.º 1)_
- **Requisito 2 — Não residência anterior** — Não ter sido residente fiscal em Portugal nos 5 anos anteriores — verificado por cruzamento com o cadastro histórico da AT.
- **Requisito 3 — Prazo do pedido** — Apresentar o pedido até 31 de março do ano seguinte ao da inscrição como residente — através do Portal das Finanças.

### 3.3 Duração e perda

- **Duração** — Duração: 10 anos consecutivos, contados a partir do ano da inscrição como residente fiscal, não renovável.
- **Perda do estatuto** — Perda do estatuto ocorre se o contribuinte deixar de ser residente fiscal em Portugal em qualquer ano dos 10. Os anos perdidos não se recuperam — se reentrar como residente, retoma apenas o tempo remanescente do período original (caso ainda não tenha decorrido), ou nada (se já decorridos 10 anos desde a inscrição original).

### 3.4 Benefícios fiscais (resumo)

- **Categorias A e B em Portugal em AEVA** — 20% percent (Taxa especial; opção pelo englobamento permitida (art.º 72.º n.º 13), normalmente desvantajosa para rendimentos altos)  _(art.º 72.º n.º 10 do CIRS)_
- **Lista AEVA aplicável ao RNH** — Despacho n.º 230/2019, de 4 de julho (substituiu a Portaria 12/2010), com lista ampla de profissões (~50 códigos), incluindo arquitetos, engenheiros, médicos, dentistas, professores universitários, profissionais de TIC, gestores e administradores, investidores, etc.  _(Despacho n.º 230/2019, de 4 de julho)_
- **Categoria A estrangeiro** — Isentos em Portugal se (i) tributados no Estado da fonte ao abrigo de CDT, ou (ii) na ausência de CDT, tributados no Estado da fonte e não considerados obtidos em Portugal.  _(art.º 81.º n.º 4 do CIRS)_
- **Categoria B estrangeiro em AEVA** — Isentos se sujeitos a tributação no Estado da fonte ao abrigo de CDT ou Modelo OCDE, e desde que não provenientes de territórios de tributação privilegiada (lista da Portaria 150/2004 e alterações).  _(Portaria 150/2004)_
- **Categorias E, F e G estrangeiro** — Isentos se puderem ser tributados no Estado da fonte ao abrigo de CDT, ou na ausência de CDT, ao abrigo do Modelo OCDE, e não provierem de paraíso fiscal.
- **Pensões estrangeiras (categoria H) — inscrição até 31 mar 2020** — Isenção percent (sujeito a verificação dos requisitos de tributação no Estado da fonte ou de não-residência da fonte em Portugal)
- **Pensões estrangeiras (categoria H) — inscrição a partir de 1 abr 2020** — 10% percent (taxa fixa)  _(art.º 72.º n.º 12 do CIRS, redação da Lei 2/2020)_

### 3.5 Regime transitório da Lei 82/2023

- **Critérios do regime transitório** — O art.º 236.º da Lei 82/2023 manteve a possibilidade de pedido de RNH em 2024 para pessoas que, à data de 31 de dezembro de 2023, já cumpriam um dos seguintes critérios (não exaustivo, verificar texto legal): Contrato de trabalho ou contrato de prestação de serviços em vigor com entidade portuguesa, ou contrato em vigor cujas funções se realizem em território nacional; Contrato de arrendamento ou outro contrato relativo ao uso ou posse de imóvel em Portugal; Reserva ou contrato-promessa de aquisição de direito real sobre imóvel em Portugal; Matrícula ou inscrição para dependentes em estabelecimento de ensino domiciliado em território português; Visto de residência ou autorização de residência válidos; Procedimento iniciado até 31 de dezembro de 2023 de concessão de visto ou autorização de residência. Para estes casos, o pedido de RNH podia ser apresentado até 31 de março de 2025 (ano seguinte ao da inscrição como residente, presumindo inscrição em 2024). **TBC — verificar prazos exatos no texto do art.º 236.º conforme alterações posteriores.**  _(art.º 236.º da Lei 82/2023)_

## Secção 4 — IFICI (Incentivo Fiscal à Investigação Científica e Inovação) — Substituto

### 4.1 Base legal

- **Base legal IFICI** — Estatuto dos Benefícios Fiscais (EBF), art.º 58.º-A — aditado pela Lei n.º 82/2023, de 29 de dezembro. Portaria n.º 187/2024/1, de 30 de julho — define a lista de atividades qualificadas, as entidades certificadoras e os procedimentos de candidatura. Em vigor para pedidos de inscrição como residente a partir de 1 de janeiro de 2024.  _(EBF art.º 58.º-A; Portaria n.º 187/2024/1, de 30 de julho)_

### 4.2 Requisitos de elegibilidade

- **Requisitos IFICI** — 1. Tornar-se residente fiscal em Portugal (mesmo critério do art.º 16.º n.º 1 CIRS). 2. Não ter sido residente fiscal em Portugal nos 5 anos anteriores. 3. Exercer efetivamente uma das atividades qualificadas constantes da Portaria n.º 187/2024, mediante certificação por uma das entidades competentes. 4. Não ter beneficiado anteriormente do RNH nem do regime do art.º 12.º-A do CIRS (regime do "ex-residente" — Programa Regressar).  _(CIRS art.º 16.º n.º 1; Portaria n.º 187/2024)_

### 4.3 Atividades qualificadas (Portaria 187/2024)

**Atividades qualificadas (Portaria 187/2024)**  _(Portaria n.º 187/2024)_

| Categoria | Atividade | Entidade certificadora |
| --- | --- | --- |
| 1 | Docência no ensino superior e investigação científica (instituições do SCTN — Sistema Científico e Tecnológico Nacional) | Fundação para a Ciência e a Tecnologia (FCT) |
| 2 | Postos de trabalho e membros de órgãos sociais em entidades certificadas como centros de tecnologia e inovação | Agência Nacional de Inovação (ANI) |
| 3 | Profissões qualificadas e membros de órgãos sociais em entidades beneficiárias do regime fiscal de apoio ao investimento (RFAI) ou consideradas relevantes para a economia nacional | AICEP — Agência para o Investimento e Comércio Externo de Portugal, ou IAPMEI — Agência para a Competitividade e Inovação |
| 4 | Investigação e desenvolvimento de pessoal cujos custos sejam elegíveis para efeitos do SIFIDE (Sistema de Incentivos Fiscais em Investigação e Desenvolvimento Empresarial) | ANI |
| 5 | Postos de trabalho e membros de órgãos sociais em entidades certificadas como startups nos termos da Lei n.º 21/2023, de 25 de maio | Startup Portugal (mediante IAPMEI) |

A lista é claramente mais restrita do que a do Despacho 230/2019 — exclui profissões liberais genéricas (médicos, dentistas em clínica privada, arquitetos a título individual), administradores não vinculados às categorias acima, e gestores de fundos não-elegíveis.

### 4.4 Benefícios fiscais (IFICI)

- **Categorias A e B em Portugal em AEVA** — 20% percent (Taxa especial; opção pelo englobamento permitida (art.º 72.º n.º 13), normalmente desvantajosa para rendimentos altos)  _(art.º 72.º n.º 10 do CIRS)_
- **Rendimentos de fonte estrangeira IFICI** — Categorias A, B (na atividade qualificada), E, F e G: isenção se puderem ser tributados no Estado da fonte ao abrigo de CDT, ou na ausência de CDT, ao abrigo do Modelo OCDE, e não provierem de paraíso fiscal. Pensões estrangeiras (categoria H): NÃO isentas — tributação pelo regime geral (englobamento progressivo). Mais-valias mobiliárias de paraísos fiscais: não cobertas pela isenção.

### 4.5 Duração

- **Duração IFICI** — 10 anos consecutivos, contados a partir do ano da inscrição como residente fiscal. Não renovável; perda por interrupção da residência segue as regras do RNH legado.

### 4.6 Procedimento de candidatura ao IFICI

- **Procedimento de candidatura ao IFICI** — 1. Inscrição como residente fiscal em Portugal no Portal das Finanças (obtenção do NIF + alteração de morada). 2. Obtenção da certificação da atividade qualificada junto da entidade competente (FCT, ANI, AICEP, IAPMEI, ou Startup Portugal). Esta certificação deve ser obtida até 15 de janeiro do ano seguinte ao da inscrição como residente. 3. Submissão do pedido de inscrição como beneficiário do IFICI no Portal das Finanças — até 15 de janeiro do ano seguinte ao da inscrição como residente (prazo da Portaria 187/2024). **TBC — confirmar se o prazo se mantém em 31 de março após alterações regulamentares.** 4. A entidade certificadora comunica a certificação à AT até 15 de fevereiro do ano seguinte. 5. A AT confirma a inscrição e o estatuto produz efeitos no ano da inscrição como residente.  _(Portaria n.º 187/2024)_

## Secção 5 — Taxa Fixa 20% — Atividades de Elevado Valor Acrescentado (AEVA)

### 5.1 Princípio

- **Taxa especial AEVA** — 20% percent (Aplicável a rendimentos das categorias A e B auferidos em Portugal no exercício de uma AEVA, em vez da tabela progressiva de IRS (que para 2025 atinge 48% no escalão mais alto))

### 5.2 Lista AEVA aplicável ao RNH — Despacho n.º 230/2019

**Lista AEVA aplicável ao RNH — Despacho n.º 230/2019**  _(Despacho n.º 230/2019, de 4 de julho)_

| Grupo CPP | Exemplos de profissões |
| --- | --- |
| 112 | Diretores gerais e gestores executivos |
| 12 | Diretores de serviços administrativos e comerciais |
| 13 | Diretores de produção e de serviços especializados |
| 21 | Especialistas em ciências físicas, matemáticas, engenharias e técnicas afins (engenheiros civis, mecânicos, eletrotécnicos, químicos, etc.) |
| 221 | Médicos |
| 2261 | Dentistas e estomatologistas |
| 231 | Professores do ensino universitário |
| 25 | Especialistas em tecnologias da informação e comunicação (programadores, analistas de sistemas, web designers, administradores de bases de dados, etc.) |
| 264 | Autores, jornalistas e linguistas |
| 265 | Artistas criativos e das artes do espetáculo (com restrições) |
| 31 | Técnicos e profissões de nível intermédio das ciências e engenharia |

A lista completa contém ~50 códigos. Profissões fora da lista (assistentes administrativos, vendedores, condutores, etc.) não beneficiam da taxa de 20%.

### 5.3 Lista AEVA aplicável ao IFICI — Portaria n.º 187/2024

- **Exclusões relevantes face ao RNH** — Mais restrita — apenas as 5 categorias listadas na Secção 4.3. Exemplos de exclusões relevantes face ao RNH: Médico em clínica privada por conta própria (sem vínculo a entidade certificada): excluído do IFICI. Dentista em consultório próprio: excluído. Arquiteto a título individual sem vínculo a entidade certificada: excluído. Programador freelancer sem vínculo a startup certificada ou entidade RFAI: excluído do IFICI mas pode ter beneficiado do RNH.  _(Portaria n.º 187/2024)_

### 5.4 Operacionalização

- **Operacionalização** — O contribuinte declara o rendimento no Anexo L do Modelo 3, indicando o código CPP da atividade. A AT cruza com a inscrição do contribuinte como RNH/IFICI e aplica a taxa de 20%. Caso a atividade declarada não conste da lista AEVA aplicável, o rendimento é tributado às taxas progressivas gerais. A taxa de 20% não inclui sobretaxa de solidariedade (art.º 68.º-A CIRS, que se aplica apenas ao englobamento).  _(art.º 68.º-A CIRS)_

### 5.5 Quadro de receção (não recepção — ortografia post-1990)

O termo correto em português europeu é "receção" (não "recepção"), conforme Acordo Ortográfico de 1990. Da mesma forma, "facto" (não "fato"), "atividade" (não "actividade"), "ótimo" (não "óptimo"), "adoção" (não "adopção").

## Secção 6 — Isenção de Rendimentos de Fonte Estrangeira — Matriz por Tipo + País

### 6.1 Princípio geral

- **Princípio geral da isenção** — Tanto o RNH legado como o IFICI atribuem isenção (ou tributação reduzida) a certos rendimentos de fonte estrangeira, desde que estes possam ser tributados no Estado da fonte ao abrigo da Convenção para Evitar a Dupla Tributação (CDT) aplicável, ou na ausência de CDT, ao abrigo do Modelo de Convenção Fiscal da OCDE, e desde que o Estado da fonte não conste da lista de paraísos fiscais (Portaria n.º 150/2004 e alterações). Note-se que o critério é "poder ser tributado" e não "ser efetivamente tributado" — basta que a CDT atribua o poder de tributação ao Estado da fonte (mesmo que a taxa efetiva nesse Estado seja zero por isenção interna). Esta interpretação tem sido confirmada pela jurisprudência arbitral (CAAD) em diversos processos.  _(Portaria n.º 150/2004)_

### 6.2 Matriz por tipo de rendimento — RNH (legado)

**Matriz por tipo de rendimento — RNH (legado)**

| Categoria | Tipo de rendimento | Tratamento sob RNH |
| --- | --- | --- |
| A | Salários estrangeiros | Isentos se tributados no Estado da fonte (CDT) ou se não considerados obtidos em Portugal |
| B | Honorários profissionais estrangeiros em AEVA | Isentos se sujeitos a tributação no Estado da fonte (CDT/OCDE) e não de paraíso fiscal |
| E | Dividendos estrangeiros | Isentos se a CDT atribuir poder de tributação ao Estado da fonte e este não for paraíso fiscal |
| E | Juros estrangeiros | Isentos sob condições análogas aos dividendos |
| E | Royalties estrangeiros | Isentos sob condições análogas |
| F | Rendimentos prediais estrangeiros | Isentos se tributáveis no Estado da fonte (regra geral CDT/OCDE — Estado da localização do imóvel tem poder de tributação) |
| G | Mais-valias mobiliárias estrangeiras | Isentas em geral, **exceto** mais-valias de partes de capital de sociedades em paraíso fiscal e algumas exceções específicas |
| G | Mais-valias imobiliárias estrangeiras | Isentas (regra CDT — Estado da localização tem poder de tributação) |
| H | Pensões estrangeiras (inscrição ≤ 31 mar 2020) | Isentas se tributadas no Estado da fonte ou se não consideradas obtidas em Portugal |
| H | Pensões estrangeiras (inscrição ≥ 1 abr 2020) | **10% taxa fixa** (não isentas) |

### 6.3 Matriz por tipo de rendimento — IFICI

**Matriz por tipo de rendimento — IFICI**

| Categoria | Tipo de rendimento | Tratamento sob IFICI |
| --- | --- | --- |
| A | Salários estrangeiros (na atividade qualificada) | Isentos sob condições análogas ao RNH |
| B | Honorários estrangeiros (na atividade qualificada) | Isentos sob condições análogas |
| E | Dividendos, juros, royalties estrangeiros | Isentos se tributáveis no Estado da fonte (CDT/OCDE) e não de paraíso fiscal |
| F | Rendimentos prediais estrangeiros | Isentos |
| G | Mais-valias mobiliárias estrangeiras | Isentas, com as mesmas exceções do RNH |
| G | Mais-valias imobiliárias estrangeiras | Isentas |
| H | **Pensões estrangeiras** | **NÃO isentas — tributação pelo regime geral (englobamento progressivo IRS)** |

### 6.4 Países críticos — observações sobre CDT

**Países críticos — observações sobre CDT**  _(Portugal tem cerca de 80 CDT em vigor)_

| País | Observação |
| --- | --- |
| Estados Unidos | CDT em vigor (1994). Pensões privadas (401(k), IRA) — tributação partilhada com regra residual; sob RNH legado normalmente isentas (pré 2020) ou tributadas a 10% (pós-abr 2020). Social Security tributada apenas no Estado pagador (EUA) sob a CDT. |
| Reino Unido | CDT em vigor. Pensões privadas (SIPP) abrangidas pelo art.º 17 da CDT. Pós-Brexit a aplicação manteve-se. |
| França | CDT em vigor. **Particularmente sensível** — França criticou publicamente o regime RNH e a CDT teve interpretação restritiva sobre certas pensões públicas. |
| Suécia | **CDT denunciada unilateralmente pela Suécia em junho 2021, com efeitos a partir de 1 de janeiro de 2022.** Sem CDT em vigor desde então, as pensões suecas pagas a residentes em Portugal passaram a ser tributadas integralmente na Suécia e o tratamento de isenção sob RNH ficou comprometido. |
| Finlândia | Tensão semelhante à Sueca; CDT renegociada com protocolo que reduziu o atrativo do RNH para pensionistas finlandeses. |
| Holanda | CDT em vigor. Pensões — regime misto consoante natureza (pública vs privada). |
| Brasil | CDT em vigor. **Atenção à interpretação do art.º 17 (pensões)** — tem suscitado discussão entre AT e Receita Federal do Brasil sobre a tributação de pensões de funcionários públicos. |
| Paraísos fiscais (Portaria 150/2004): Andorra, Bahrein, Belize, Bermudas, Catar, etc. | **Não beneficiam de isenção** sob RNH/IFICI mesmo que existam acordos de troca de informação. |

### 6.5 Categoria H — Pensões estrangeiras (RNH legado): regra dos 10%

- **Regra dos 10% pensões RNH** — A taxa de 10% incide sobre o valor bruto da pensão, sem deduções específicas, sem englobamento, sem aplicação de sobretaxa de solidariedade. Crédito por dupla tributação internacional: o art.º 81.º n.º 5 do CIRS permite a dedução do imposto pago no Estado da fonte, até ao limite do imposto português devido sobre essa pensão (10% do valor bruto). Se o Estado da fonte tributar a pensão acima de 10%, o excesso não é recuperável em Portugal. A regra dos 10% aplica-se durante os 10 anos do estatuto. Após o termo, a pensão é englobada às taxas gerais IRS.  _(art.º 81.º n.º 5 do CIRS)_

## Secção 7 — Tratamento de Pensões Estrangeiras (RNH Legado vs IFICI)

### 7.1 Quadro consolidado

**Quadro consolidado**

| Cenário | Tratamento |
| --- | --- |
| RNH com inscrição como residente até 31 mar 2020 (com pedido até 31 mar 2021) | Isenção (sujeito a requisitos de tributação no Estado da fonte ou de não-obtenção em Portugal) |
| RNH com inscrição como residente a partir de 1 abr 2020 até 31 dez 2023 | **10% taxa fixa** sobre o valor bruto da pensão |
| RNH ao abrigo do regime transitório da Lei 82/2023 (inscrição em 2024) | **10% taxa fixa** (não isenção, regime pós-2020) |
| IFICI (inscrição em 2024 ou posterior) | **Englobamento ao regime geral IRS** — tabela progressiva 13% a 48% + sobretaxa de solidariedade (se aplicável) |
| Regime geral sem RNH/IFICI | Englobamento ao regime geral IRS |

### 7.2 Crédito por dupla tributação internacional

- **Crédito por dupla tributação** — Em todos os cenários, o art.º 81.º do CIRS permite crédito pelo imposto pago no Estado da fonte, limitado ao imposto português efetivamente devido sobre essa pensão. O crédito é declarado no Anexo J do Modelo 3 (rendimentos obtidos no estrangeiro).  _(art.º 81.º do CIRS)_

### 7.3 Pensões públicas vs privadas

- **Pensões públicas vs privadas** — As CDT distinguem entre: Pensões públicas (art.º 19 do Modelo OCDE): pagas pelo Estado ou por subdivisão política a antigos funcionários públicos. Tributação exclusiva no Estado pagador na maioria das CDT — fora do escopo da isenção RNH/IFICI (a CDT atribui poder exclusivo ao Estado da fonte, e Portugal não pode tributar). Pensões privadas (art.º 18 do Modelo OCDE): regra geral, tributação exclusiva no Estado da residência (Portugal). Aqui é que o RNH/IFICI opera — Portugal teria poder de tributar, mas RNH legado isenta ou tributa a 10%. A leitura de cada CDT é determinante. Algumas CDT (ex.: Holanda, art.º 18) permitem ao Estado da fonte tributar pensões privadas acima de certos limites — caso em que o critério "poder ser tributado no Estado da fonte" se verifica e a isenção sob RNH aplica-se.  _(Modelo OCDE art.º 18 e 19)_

## Secção 8 — Mais-Valias e Dividendos Estrangeiros

### 8.1 Mais-valias mobiliárias estrangeiras

- **Mais-valias mobiliárias estrangeiras** — Sob RNH e IFICI: Mais-valias da alienação de ações, obrigações, unidades de participação em fundos, etc., obtidas no estrangeiro são isentas se a CDT permitir a tributação no Estado da fonte, ou (na ausência de CDT) ao abrigo do Modelo OCDE. Atenção: a maioria das CDT segue o Modelo OCDE no art.º 13.º n.º 5, atribuindo tributação exclusiva ao Estado da residência (Portugal). Nestes casos, o critério "poder ser tributado no Estado da fonte" não se verifica e a isenção não se aplica — a mais-valia é tributada em Portugal à taxa de 28%. Exceções: mais-valias de partes de capital de sociedades com ativo essencialmente imobiliário (substantial holding rules) — algumas CDT permitem tributação no Estado da fonte; nesses casos, isenção sob RNH/IFICI aplica-se.  _(art.º 72.º n.º 1 al. c) CIRS; Modelo OCDE art.º 13.º n.º 5)_

### 8.2 Mais-valias imobiliárias estrangeiras

- **Mais-valias imobiliárias estrangeiras** — Sob CDT (art.º 13.º n.º 1 do Modelo OCDE), o Estado da localização do imóvel tem poder de tributação. Portanto, mais-valias imobiliárias estrangeiras são tipicamente isentas sob RNH/IFICI em Portugal (sujeito a documentação da tributação no Estado da fonte).  _(Modelo OCDE art.º 13.º n.º 1)_

### 8.3 Mais-valias de criptoativos

- **Mais-valias de criptoativos** — Lei n.º 24-D/2022 (OE 2023) introduziu o regime fiscal de criptoativos no CIRS. Detenções < 365 dias: tributação a 28% taxa especial (ou englobamento opcional). RNH/IFICI não isentam estas mais-valias de curto prazo. Detenções ≥ 365 dias: isenção (regime geral, não depende de RNH/IFICI). Mais-valias de criptoativos com origem em paraísos fiscais: tributação a 35%.  _(Lei n.º 24-D/2022; art.º 72.º n.º 17 CIRS)_

### 8.4 Dividendos estrangeiros

- **Dividendos estrangeiros** — Sob RNH e IFICI: Isentos se a CDT atribuir poder de tributação ao Estado da fonte. A maioria das CDT segue o Modelo OCDE (art.º 10.º) — tributação partilhada entre Estado da fonte (taxa limitada, tipicamente 15% para dividendos de carteira) e Estado da residência. Como o Estado da fonte tem poder de tributação (mesmo que limitado), o critério da isenção sob RNH/IFICI verifica-se e a isenção aplica-se em Portugal. Sem CDT: aplica-se o Modelo OCDE — mesma análise. Exceção: dividendos de sociedades em paraísos fiscais — não isentos.  _(Modelo OCDE art.º 10.º)_

### 8.5 Juros estrangeiros

- **Juros estrangeiros** — Análise análoga aos dividendos. CDT modelo OCDE (art.º 11.º) prevê tributação partilhada — Estado da fonte com taxa limitada (tipicamente 10%) e Estado da residência. Critério verifica-se e isenção aplica-se sob RNH/IFICI (exceto paraísos fiscais).  _(Modelo OCDE art.º 11.º)_

### 8.6 Royalties estrangeiros

- **Royalties estrangeiros** — CDT modelo OCDE (art.º 12.º) atribui tributação exclusiva ao Estado da residência. Portanto, sob o Modelo, o Estado da fonte não pode tributar — critério da isenção sob RNH/IFICI não se verifica e os royalties são tributados em Portugal. Mas: muitas CDT bilaterais (incluindo a maioria das celebradas por Portugal) desviam-se do Modelo OCDE e permitem tributação partilhada de royalties — caso em que a isenção sob RNH/IFICI aplica-se. Análise CDT por CDT é indispensável.  _(Modelo OCDE art.º 12.º)_

## Secção 9 — Processo de Candidatura à AT (Portal das Finanças)

### 9.1 Pré-requisitos (comum a RNH e IFICI)

- **Pré-requisitos** — 1. NIF português — obtido junto da AT, presencialmente ou via representante fiscal (se ainda não residente). Cidadãos da UE/EEE não necessitam de representante fiscal; cidadãos de países terceiros, sim. 2. Inscrição como residente fiscal em Portugal — alteração de morada fiscal no Portal das Finanças para uma morada portuguesa (própria, arrendada ou cedida). 3. Não residência fiscal em Portugal nos 5 anos anteriores — verificável no cadastro da AT.

### 9.2 Procedimento RNH (apenas para regime transitório Lei 82/2023, encerrado em 2024)

- **Procedimento RNH transitório** — 1. Aceder ao Portal das Finanças (https://www.portaldasfinancas.gov.pt) com NIF + senha (ou Cartão de Cidadão / Chave Móvel Digital). 2. Menu: Cidadãos → Serviços → Outros Serviços → Inscrição Residente Não Habitual. 3. Preencher formulário declarando: (a) data de inscrição como residente, (b) declaração sob compromisso de não ter sido residente nos 5 anos anteriores, (c) atividade exercida e código CPP. 4. Submeter até 31 de março do ano seguinte ao da inscrição como residente. 5. A AT analisa o pedido e emite decisão (deferimento ou indeferimento) — prazo legal de 30 dias, mas frequentemente excedido na prática. 6. Em caso de indeferimento, possibilidade de reclamação graciosa (30 dias) e impugnação judicial / pedido CAAD (90 dias).

### 9.3 Procedimento IFICI

- **Procedimento IFICI** — 1. Inscrição como residente fiscal no Portal das Finanças. 2. Obtenção da certificação da atividade qualificada junto da entidade competente: FCT — investigação científica e docência ensino superior. ANI — centros tecnológicos, SIFIDE, startups (em articulação com IAPMEI). AICEP / IAPMEI — RFAI, atividades relevantes para a economia nacional. Startup Portugal / IAPMEI — startups certificadas Lei 21/2023. A certificação é solicitada à entidade competente com documentação da atividade, contrato de trabalho / contrato de prestação de serviços, CV, etc. Cada entidade tem o seu próprio procedimento e prazos. 3. Submissão do pedido de inscrição como beneficiário IFICI no Portal das Finanças — até 15 de janeiro do ano seguinte ao da inscrição como residente (prazo da Portaria 187/2024). 4. A entidade certificadora comunica diretamente à AT a certificação, até 15 de fevereiro do ano seguinte. 5. A AT confirma a inscrição ou indefere; comunica decisão via Portal das Finanças.  _(Portaria n.º 187/2024)_

### 9.4 Declaração anual — Modelo 3 + Anexo L

**Anexos do Modelo 3**

| Anexo | Conteúdo |
| --- | --- |
| Rosto | Identificação, agregado familiar, opções de tributação |
| A | Rendimentos da categoria A (trabalho dependente) |
| B | Rendimentos da categoria B (trabalho independente) |
| E | Rendimentos da categoria E (capitais) |
| F | Rendimentos da categoria F (prediais) |
| G | Mais-valias |
| H | Benefícios fiscais e deduções à coleta |
| J | Rendimentos obtidos no estrangeiro |
| L | **Residentes não habituais — específico** |
| SS | Anexo da Segurança Social (categoria B) |

Independentemente de estar inscrito como RNH ou IFICI, o contribuinte tem de apresentar a declaração anual de IRS (Modelo 3) entre 1 de abril e 30 de junho do ano seguinte ao do rendimento.

O Anexo L inclui: Indicação do regime aplicável (RNH ou IFICI). Identificação da atividade exercida e código CPP (RNH) ou referência à certificação (IFICI). Rendimentos tributados à taxa fixa de 20%. Rendimentos isentos de fonte estrangeira (cruzamento com Anexo J). Pensões estrangeiras tributadas a 10% (RNH pós-2020). Opção pelo englobamento (se aplicável).

### 9.5 Documentação a manter (arquivo do contribuinte)

- **Documentação e período de conservação** — Comprovativo da inscrição como residente fiscal. Comprovativo da inscrição como RNH/IFICI (extrato do Portal das Finanças). Certificação da atividade (IFICI) — original e cópias. Contratos de trabalho / contratos de prestação de serviços. Declarações fiscais do(s) Estado(s) da fonte para rendimentos estrangeiros. Certificados de retenção na fonte estrangeiros. CDT aplicável (texto consolidado). Modelo 3 e anexos de cada ano. Período de conservação: 4 anos (regra geral RGIT) ou 10 anos para documentos relacionados com investimentos imobiliários e mais-valias diferidas. Recomendação prática: manter por toda a duração do estatuto (10 anos) mais 4 anos adicionais.  _(RGIT)_

## Secção 10 — Exemplos Práticos

### Exemplo 10.1 — Nómada digital americano em Lisboa (IFICI, 2025)

**Perfil**: Jane Smith, 34 anos, programadora full-stack norte-americana, mudou-se para Lisboa em março de 2025 com visto D8 (nómada digital). Trabalha remotamente para uma sociedade de software dos EUA (W-2 employee) e adicionalmente presta serviços de consultoria a uma startup portuguesa certificada nos termos da Lei 21/2023. Sem residência fiscal em Portugal nos 5 anos anteriores.

**Rendimentos 2025**:
- Salário americano (W-2): USD 145.000 (≈ EUR 134.000).
- Honorários de consultoria à startup portuguesa: EUR 36.000.
- Dividendos de carteira de ações americanas (broker EUA): USD 4.200 (≈ EUR 3.900) — retenção na fonte de 30% reduzida a 15% via Form W-8BEN ao abrigo da CDT EUA-Portugal.
- Juros de conta-poupança americana: USD 800 (≈ EUR 740).

**Análise**:
1. **Residência fiscal**: Jane permanece > 183 dias em Portugal em 2025 → residente fiscal em Portugal pelo ano completo (com aplicação do art.º 16.º n.º 2 sobre residência parcial verificar — mas para este exemplo simplifica-se).
2. **Elegibilidade IFICI**: cumpre o requisito de não-residência anterior. A atividade de consultoria à startup certificada qualifica-se na categoria 5 da Portaria 187/2024 (postos de trabalho / membros de órgãos sociais em startups certificadas). Obtém certificação via Startup Portugal/IAPMEI. **Importante**: o salário americano (W-2) não está abrangido pela atividade qualificada IFICI — apenas a consultoria à startup PT.
3. **Tributação dos honorários portugueses (EUR 36.000)** — categoria B, atividade qualificada IFICI: **taxa fixa de 20%** = EUR 7.200.
4. **Tributação do salário americano (EUR 134.000)** — categoria A, rendimento estrangeiro:
   - Sob CDT EUA-Portugal (art.º 15), salários de trabalho dependente exercido fisicamente nos EUA são tributáveis nos EUA. **Mas**: Jane trabalha **a partir de Lisboa** (remotamente) — sob a CDT, o trabalho é considerado exercido em Portugal. Portugal tem poder de tributação. Os EUA tributam pela cidadania (saving clause).
   - Sob IFICI: a isenção de categoria A estrangeira aplica-se apenas se o rendimento for de **atividade qualificada**. O W-2 não está vinculado à atividade qualificada IFICI → **englobado ao regime geral** = ~EUR 47.500 de IRS.
   - Crédito por imposto pago nos EUA: limitado ao IRS proporcional sobre esse rendimento.
   - **Conservador**: tratar como englobado, com crédito CDT até ao limite.
5. **Dividendos americanos (EUR 3.900)** — categoria E. CDT EUA-Portugal (art.º 10) atribui poder partilhado → critério verifica-se → **isenção sob IFICI**. Reporta no Anexo J + Anexo L.
6. **Juros americanos (EUR 740)** — categoria E. Análise análoga → **isenção sob IFICI**.

**Resumo IRS 2025**:
- Categoria B (IFICI 20%): EUR 7.200.
- Categoria A (englobamento geral): ~EUR 47.500 (com crédito CDT).
- Categoria E (isenta IFICI): EUR 0 em Portugal.
- **Total IRS aproximado**: EUR 54.700 (TBC com cálculo exato + sobretaxa solidariedade se aplicável).

**Alertas**: a estrutura é subóptima — Jane beneficiaria mais se renegociasse o salário americano como contrato de prestação de serviços vinculado à startup PT, enquadrando-o na atividade qualificada IFICI a 20%. Encaminhar para parecer fiscal específico.

### Exemplo 10.2 — Pensionista francês no Algarve (RNH regime transitório, inscrição 2024)

**Perfil**: Jean-Pierre Dupont, 67 anos, francês, reformado da segurança social francesa e de fundo de pensão complementar privado. Mudou-se para Albufeira em outubro de 2024 ao abrigo do regime transitório da Lei 82/2023 (tinha contrato-promessa de compra de apartamento assinado em outubro de 2023). Apresentou pedido de RNH em janeiro de 2025.

**Rendimentos 2025**:
- Pensão pública francesa (CNAV — Caisse Nationale d'Assurance Vieillesse): EUR 28.000.
- Pensão privada complementar (AGIRC-ARRCO): EUR 12.000.
- Juros de obrigações francesas: EUR 1.800.

**Análise**:
1. **RNH transitório aplicável**: inscrição como residente em outubro de 2024 → pedido apresentado até 31 mar 2025 → admitido.
2. **Pensão pública francesa (CNAV)**: pensão pública sob art.º 19 da CDT Portugal-França (1971) → tributação **exclusiva** em França. Portugal não pode tributar. **Não entra em IRS português** (declarada no Anexo J apenas para informação).
3. **Pensão privada (AGIRC-ARRCO)**: pensão privada sob art.º 18 da CDT → tributação **partilhada** com regra residual de tributação no Estado da residência. Em Portugal, sob RNH com inscrição pós-2020: **taxa fixa de 10%** = EUR 1.200.
4. **Juros franceses (EUR 1.800)**: categoria E. CDT (art.º 11) — tributação partilhada → critério verifica-se → **isenção sob RNH**.

**Resumo IRS 2025**:
- Pensão pública (não tributada PT): EUR 0.
- Pensão privada (10% RNH): EUR 1.200.
- Juros (isentos RNH): EUR 0.
- **Total IRS**: EUR 1.200 + sobretaxa de solidariedade (não se aplica a taxas especiais).

**Alertas**: confirmar (a) que a CNAV é classificada como pensão pública (alguns elementos da CNAV podem ser híbridos) e (b) o tratamento sob CDT Portugal-França para a AGIRC-ARRCO em sede de retenção francesa. Encaminhar para confirmação CDT.

### Exemplo 10.3 — Investigador IFICI no Porto (2025)

**Perfil**: Dr. Ana Rodríguez Pérez, 41 anos, cidadã espanhola, contratada como investigadora principal num projeto de IA da Universidade do Porto a partir de janeiro de 2025. Veio diretamente de uma universidade nos Países Baixos (Delft) onde residiu de 2020 a 2024. Nunca foi residente fiscal em Portugal.

**Rendimentos 2025**:
- Salário Universidade do Porto (categoria A): EUR 58.000.
- Royalties de patentes registadas em Espanha (categoria B/E híbrida — assumir categoria E): EUR 7.500, retenção na fonte espanhola de 19% (CDT Portugal-Espanha permite tributação partilhada de royalties).
- Dividendos de fundos de investimento holandeses: EUR 2.300.

**Análise**:
1. **Elegibilidade IFICI**: cumpre o requisito de não-residência anterior. A atividade de investigação na Universidade do Porto qualifica-se na **categoria 1 da Portaria 187/2024** (docência no ensino superior e investigação científica). Obtém certificação via FCT.
2. **Salário Universidade do Porto (EUR 58.000)** — categoria A, atividade qualificada IFICI: **taxa fixa de 20%** = EUR 11.600.
3. **Royalties espanholas (EUR 7.500)**: CDT Portugal-Espanha (art.º 12) atribui tributação partilhada (taxa máxima de 5% no Estado da fonte) → critério verifica-se → **isenção sob IFICI** em Portugal. A retenção espanhola de 19% pode estar acima da taxa CDT (5%) — recomendar pedido de reembolso ao Estado espanhol.
4. **Dividendos holandeses (EUR 2.300)**: CDT Portugal-Países Baixos (art.º 10) — tributação partilhada → **isenção sob IFICI**.

**Resumo IRS 2025**:
- Categoria A (IFICI 20%): EUR 11.600.
- Royalties (isentas IFICI): EUR 0 em Portugal.
- Dividendos (isentos IFICI): EUR 0 em Portugal.
- **Total IRS**: EUR 11.600.

Comparação com regime geral: o IRS sobre EUR 58.000 às taxas progressivas 2025 rondaria EUR 17.500 + sobretaxa de solidariedade. **Poupança IFICI ≈ EUR 5.900/ano**, multiplicada por 10 anos = ~EUR 59.000 de poupança ao longo do estatuto (sem considerar os rendimentos estrangeiros).

## Secção 11 — Defaults Conservadores

**Defaults Conservadores**

| Decisão | Default conservador | Justificação |
| --- | --- | --- |
| Classificação da atividade como AEVA (lista RNH) | Não aplicar 20% sem confirmação documental do código CPP e enquadramento na lista do Despacho 230/2019 | Risco de indeferimento da AT com regularização retroativa |
| Classificação da atividade como qualificada IFICI | Exigir certificação **prévia** da entidade competente antes de aplicar 20% | A AT só aceita IFICI mediante certificação formal |
| Pensão estrangeira com inscrição RNH em 2020 — data exata desconhecida (mar ou abr 2020) | Aplicar **10% taxa fixa** (mais conservador para a AT) e reverter para isenção apenas se documentação prove inscrição até 31 mar 2020 | A regra da Lei 2/2020 é clara — data-corte de 1 abr 2020 |
| Isenção de rendimento estrangeiro sem documentação clara da CDT aplicável e do tratamento no Estado da fonte | Não aplicar isenção; tributar em Portugal | Inversão do ónus da prova favorece a AT |
| Royalty estrangeira sob RNH/IFICI | Verificar a CDT específica (não presumir tratamento Modelo OCDE) | A maioria das CDT de Portugal **desvia-se** do Modelo OCDE no art.º 12 |
| Mais-valia estrangeira mobiliária | Default — **tributar a 28% em Portugal** (Modelo OCDE atribui poder exclusivo ao Estado da residência); isenção só se CDT específica atribuir poder de tributação ao Estado da fonte | Maioria dos casos não cumpre o critério de isenção |
| Mais-valia de criptoativos sob RNH/IFICI (detenção < 365 dias) | Tributar a 28% (regime cripto não se sobrepõe ao RNH/IFICI) | Lei 24-D/2022 prevalece sobre RNH/IFICI |
| Contribuinte chega após 31 mar do ano N+1 com pedido de RNH transitório | Indeferir; aconselhar pedido tempestivo em ano fiscal seguinte ou regime geral | Caducidade do direito |
| IFICI — atividade certificada mas com vínculo laboral em entidade não-certificada | Não aplicar IFICI; o vínculo tem de ser com entidade certificada (não basta a atividade ser do tipo qualificado) | Portaria 187/2024 exige certificação da entidade empregadora / contratante |
| Suécia — pensões pós-2022 sob RNH | Tributar a 10% em Portugal (RNH pós-2020) **mais** atender que a denúncia da CDT pode mudar o tratamento. Recomendar parecer específico. | Denúncia da CDT alterou o equilíbrio |
| Sobretaxa de solidariedade IRS sobre rendimentos a 20% IFICI/RNH | Não aplicar — a sobretaxa só incide sobre englobamento | Art.º 68.º-A CIRS limita ao englobamento |
| Cumulação RNH + Programa Regressar | Não permitida — apenas um regime aplicável | Lei 71/2018 estabelece exclusão |

## Secção 12 — Fontes

### Legislação primária

- **Decreto-Lei n.º 249/2009, de 23 de setembro** — criação do regime RNH.
- **Código do IRS (CIRS)**, em particular:
  - Art.º 16.º n.os 8 a 12 — definição de residente não habitual.
  - Art.º 72.º n.os 10, 12 e 13 — taxas especiais RNH (20% e 10%).
  - Art.º 81.º — eliminação da dupla tributação internacional.
- **Estatuto dos Benefícios Fiscais (EBF), art.º 58.º-A** — IFICI, aditado pela Lei n.º 82/2023, de 29 de dezembro.
- **Lei n.º 82/2023, de 29 de dezembro (OE 2024)** — encerramento do RNH e criação do IFICI; regime transitório no art.º 236.º.
- **Lei n.º 2/2020, de 31 de março (OE 2020)** — introdução da taxa de 10% sobre pensões estrangeiras.
- **Lei n.º 24-D/2022, de 30 de dezembro (OE 2023)** — regime fiscal dos criptoativos.

### Legislação complementar (portarias, despachos)

- **Despacho n.º 230/2019, de 4 de julho** — lista de Atividades de Elevado Valor Acrescentado (AEVA) para efeitos do RNH.
- **Portaria n.º 187/2024/1, de 30 de julho** — regulamentação do IFICI: atividades qualificadas, entidades certificadoras, procedimentos.
- **Portaria n.º 12/2010, de 7 de janeiro** — lista AEVA original (revogada pelo Despacho 230/2019).
- **Portaria n.º 150/2004, de 13 de fevereiro** — lista de países, territórios e regiões com regimes de tributação privilegiada (paraísos fiscais), e suas alterações posteriores.

### Convenções de Dupla Tributação relevantes

- CDT Portugal-EUA (Resolução AR 39/95, em vigor desde 1996).
- CDT Portugal-França (Decreto-Lei 105/71, em vigor desde 1972).
- CDT Portugal-Reino Unido (em vigor desde 1969, com Protocolo).
- CDT Portugal-Espanha (Decreto 14/95).
- CDT Portugal-Países Baixos (Decreto 28/2000).
- CDT Portugal-Brasil (Resolução AR 33/2001).
- **CDT Portugal-Suécia** — **denunciada unilateralmente pela Suécia em junho 2021, com efeitos a partir de 1 jan 2022.**

Lista completa das ~80 CDT em vigor: Portal das Finanças → Acordos Internacionais.

### Modelos e instruções

- **Modelo 3 do IRS** e respetivas instruções de preenchimento (atualizadas anualmente pelo Despacho do Diretor-Geral da AT).
- **Anexo L do Modelo 3** — residentes não habituais.
- **Anexo J do Modelo 3** — rendimentos obtidos no estrangeiro.

### Doutrina administrativa

- **Circulares da AT** sobre interpretação do RNH (ver Portal das Finanças → Doutrina Administrativa).
- **Informações vinculativas** emitidas pela Direção de Serviços do IRS sobre casos concretos do RNH e (mais recentemente) IFICI.

### Jurisprudência

- **CAAD — Centro de Arbitragem Administrativa**: vasta jurisprudência arbitral sobre RNH, em particular sobre (i) interpretação do critério "pode ser tributado" no Estado da fonte, (ii) pensões públicas vs privadas, (iii) qualificação como AEVA. Pesquisa em https://caad.org.pt.
- **STA — Supremo Tribunal Administrativo**: acórdãos pontuais sobre indeferimento de RNH e contagem do prazo dos 5 anos.

### Recursos institucionais

- **Autoridade Tributária e Aduaneira (AT)** — Portal das Finanças (https://www.portaldasfinancas.gov.pt).
- **Fundação para a Ciência e a Tecnologia (FCT)** — certificação IFICI categoria 1 (https://www.fct.pt).
- **Agência Nacional de Inovação (ANI)** — certificação IFICI categorias 2 e 4.
- **AICEP — Agência para o Investimento e Comércio Externo de Portugal** — certificação IFICI categoria 3.
- **IAPMEI — Agência para a Competitividade e Inovação** — certificação IFICI categorias 3 e 5.
- **Ordem dos Contabilistas Certificados (OCC)** — boletins técnicos sobre RNH e IFICI.

### Notas de versão e validação

- **Versão**: 1.0
- **Data**: 2025 (ano fiscal de referência: 2025; declarações apresentadas em 2026).
- **Validação pendente**: requer revisão por Contabilista Certificado inscrito na OCC ou advogado fiscalista registado na Ordem dos Advogados, com prática comprovada em fiscalidade internacional e regime RNH/IFICI.
- **TBC (To Be Confirmed)**:
  - Prazo exato de submissão IFICI no Portal das Finanças (15 janeiro vs 31 março) — Portaria 187/2024 indica 15 janeiro mas práticas administrativas têm-se ajustado.
  - Texto final do art.º 236.º da Lei 82/2023 com alterações posteriores em OE 2025 (Lei n.º 45-A/2024).
  - Lista exaustiva de profissões abrangidas pela categoria 3 da Portaria 187/2024 (entidades RFAI / relevantes para a economia).

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
