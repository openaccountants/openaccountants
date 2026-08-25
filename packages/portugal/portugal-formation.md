---
name: portugal-formation
description: "Utilize esta skill sempre que lhe perguntarem sobre constituição, incorporação ou registo de uma empresa em Portugal. Acione perante expressões como \"constituir empresa em Portugal\", \"constituição de Lda\", \"sociedade por quotas\", \"Empresa na Hora\", \"constituição de empresa portuguesa\", \"registar negócio em Portugal\", \"sociedade unipessoal\", \"NIF Portugal\", \"Registo Comercial\", ou qualquer questão sobre o início de uma entidade empresarial em Portugal. Abrange tipos de entidade (Lda, SA, ENI), processo de registo, requisitos de capital, custos, cumprimento pós-constituição e abertura de conta bancária. LEIA SEMPRE esta skill antes de aconselhar sobre a constituição de empresas em Portugal. Trigger also on: \"set up a company in Portugal\", \"Lda formation\", \"sociedade por quotas\", \"Empresa na Hora\", \"Portuguese company formation\", \"register a business Portugal\", \"sociedade unipessoal\", \"NIF Portugal\", \"Registo Comercial\"."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mário Jorge da costa Vale
review_status: current
depends_on:
  - company-formation-workflow-base
category: formation
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Formation

## Portugal — Constituição de Empresa e Selecção de Entidade — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mário Jorge da costa Vale** on 2026-06-04.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Constituição de Empresa

- **Lda — capital mínimo** — €1 por quota (mín. €2 total)  _(CSC)_
- **Unipessoal Lda — capital** — €1  _(CSC)_
- **SA — capital mínimo** — €50.000 (30% à constituição)  _(CSC)_
- **ENI** — Sem personalidade jurídica, responsabilidade ilimitada
- **Empresa na Hora (padrão)** — €360  _(DL 111/2005)_
- **Empresa Online (pacto pré-aprovado)** — €220  _(gov.pt)_
- **Empresa Online (pacto customizado)** — €360  _(gov.pt)_
- **Certificado de admissibilidade** — €75 (online) / €150 (urgente)  _(RNPC)_
- **IES** — Até 15 julho do ano seguinte  _(AT)_
- **IRC (Modelo 22)** — Até 31 maio do ano seguinte  _(AT)_
- **RCBE (beneficiário efetivo)** — Na constituição + confirmação anual  _(IRN)_
- **Declaração início atividade** — 15 dias  _(AT)_
- **Contabilista Certificado** — Obrigatório (responsabilidade legal)  _(DL 158/2009)_
- **Taxa normal** — 2025: 21% ; 2026: 19%  _(Código IRC)_
- **PME — primeiros €50.000** — 2025: 16% ; 2026: 15%  _(Código IRC)_

## Secção 1 -- Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Registo comercial | Instituto dos Registos e do Notariado (IRN) / Conservatória do Registo Comercial |
| Legislação principal | Código das Sociedades Comerciais (CSC); DL 111/2005 (Empresa na Hora) |
| Tempo típico de constituição | 1 hora (Empresa na Hora) até 2 semanas (tradicional/online) |
| Taxa de IRC | 21% (taxa geral); 17% sobre os primeiros €50.000 para PME em regiões do interior |
| Versão da skill | 1.1 |

## Secção 2 -- Comparação de Tipos de Entidade

**Comparação de Tipos de Entidade**

| Característica | Empresário em Nome Individual (ENI) | Sociedade por Quotas (Lda) | Sociedade Unipessoal por Quotas (Unipessoal Lda) | Sociedade Anónima (SA) |
| --- | --- | --- | --- | --- |
| Personalidade jurídica | Não | Sim | Sim | Sim |
| Responsabilidade | Ilimitada | Limitada à entrada de capital | Limitada | Limitada |
| Sócios mínimos | 1 | 2 | 1 | 5 (ou 1 se detida por outra sociedade) |
| Capital social mínimo | N/A | €1 (mínimo €1 por quota) | €1 | €50.000 |
| Tratamento fiscal | IRS (pessoal) | IRC (societário) | IRC (societário) | IRC (societário) |
| Carga administrativa | Baixa | Média | Média | Elevada |
| Auditoria obrigatória | Não | Apenas se ultrapassados os limites | Apenas se ultrapassados os limites | Sim (ROC obrigatório acima dos limites) |

**Predefinição recomendada:** Sociedade por Quotas (Lda) ou Sociedade Unipessoal por Quotas para a maioria dos fins comerciais.

## Secção 3 -- Processo de Registo

### Opção A: Empresa na Hora (Constituição no Próprio Dia)

A "Empresa na Hora" portuguesa é um dos processos de constituição mais rápidos da Europa.

1. **Comparecer num balcão Empresa na Hora** (instalações do IRN, Lojas do Cidadão)
2. **Escolher uma firma pré-aprovada** da Bolsa de Firmas, ou apresentar um certificado de admissibilidade aprovado
3. **Seleccionar um pacto social pré-aprovado** (estatutos-tipo) ou apresentar um próprio
4. **Apresentar identificação** (Cartão de Cidadão ou passaporte + NIF) de todos os sócios fundadores
5. **Nomear um Contabilista Certificado** ou seleccionar um no balcão
6. **Pagar €360** (valor normal) ou €220 (com estatutos pré-aprovados online)
7. **Receber de imediato**: pacto social, código de acesso à certidão permanente, Cartão da Empresa, NIF da empresa, NISS (número de Segurança Social)
8. **Depositar o capital** no prazo de 5 dias úteis numa conta bancária da empresa (ou entregar em caixa social até ao final do primeiro exercício)

### Opção B: Empresa Online 2.0

1. Aceder a gov.pt ou à plataforma Empresa Online
2. Preencher o formulário digital com os dados da empresa
3. Carregar documentos (identificação, estatutos, etc.)
4. Pagar €220 (estatutos pré-aprovados) ou €360 (estatutos personalizados)
5. O IRN processa em 5--10 dias úteis
6. Registo da empresa e NIF emitidos electronicamente

### Opção C: Constituição Tradicional (Conservatória)

1. Obter certificado de admissibilidade (aprovação da firma) junto do RNPC
2. Elaborar o pacto social (estatutos)
3. Outorgar escritura pública perante notário
4. Registar na Conservatória do Registo Comercial
5. Inscrever junto das Finanças e da Segurança Social
6. Demora 1--3 semanas; mais dispendioso devido aos emolumentos notariais

### Passos Pós-Registo (Todas as Opções)

- Inscrição em IRC junto da Autoridade Tributária e Aduaneira
- Inscrição em IVA se aplicável
- Inscrição na Segurança Social como entidade empregadora (em caso de contratação)
- Apresentar a Declaração de Início de Atividade no prazo de 15 dias

## Secção 4 -- Requisitos de Capital

**Requisitos de Capital**

| Tipo de Entidade | Capital Social Mín. | Realização Mín. | Prazo de Realização | Entradas em Espécie |
| --- | --- | --- | --- | --- |
| Lda (vários sócios) | €2 (mín. €1 por quota) | Sem mínimo na constituição | Depósito em 5 dias úteis ou entrega em caixa até ao fim do 1.º exercício | Permitidas (avaliação por ROC obrigatória acima de €5.000) |
| Unipessoal Lda | €1 | Igual à Lda | Igual à Lda | Permitidas |
| SA | €50.000 | 30% na constituição | Restante conforme estatutos | Permitidas (relatório de ROC obrigatório) |

## Secção 5 -- Repartição de Custos

**Repartição de Custos**

| Componente de Custo | Valor (EUR) | Notas |
| --- | --- | --- |
| Empresa na Hora (normal) | €360 | Tudo incluído: registo, NIF, NISS |
| Empresa na Hora (com marca, 1 classe) | €360 + €200 | Inclui registo de marca |
| Empresa Online (estatutos pré-aprovados) | €220 | Processo digital |
| Empresa Online (estatutos personalizados) | €360 | Processo digital |
| Certificado de admissibilidade (se necessário) | €75 (online) / €150 (urgente) | Aprovação de firma fora da Bolsa de Firmas |
| Notário tradicional + registo | €500--€1.500 | Escritura pública + Conservatória |
| Depósito de capital social | €1 (mínimo) | Na prática, recomenda-se €1.000+ |
| **Total (Empresa na Hora)** | **€360** | Opção mais barata e rápida |

### Manutenção Anual

**Manutenção Anual**

| Item | Custo (EUR) |
| --- | --- |
| Contabilista Certificado | €1.200--€3.600/ano |
| Entrega de IES/IRC | Incluído nos honorários do contabilista |
| Certidão permanente (acesso ao registo online) | €25/ano |
| Publicações obrigatórias | Incluído na entrega da IES |

## Secção 6 -- Cumprimento Pós-Constituição

**Cumprimento Pós-Constituição**

| Obrigação | Prazo | Autoridade |
| --- | --- | --- |
| IES (Informação Empresarial Simplificada) | Até 15 de Julho do ano seguinte | Autoridade Tributária |
| Declaração de IRC (Modelo 22) | Até 31 de Maio do ano seguinte | Autoridade Tributária |
| Declarações de IVA | Mensal ou trimestral | Autoridade Tributária |
| Relatório de gestão e contas anuais | Aprovados nos 3 meses seguintes ao fim do exercício | Interno (assembleia geral) |
| Registo Central do Beneficiário Efetivo (RCBE) | Na constituição + confirmação anual | IRN |
| Contribuições para a Segurança Social | Mensal | Instituto da Segurança Social |

## Secção 7 -- Abertura de Conta Bancária

### Documentos Habitualmente Exigidos

- Certidão permanente (certidão online da empresa)
- Pacto social
- NIF da empresa e de todos os gerentes/sócios
- Identificação (Cartão de Cidadão ou passaporte) dos gerentes e sócios
- Comprovativo de morada
- Declaração de início de atividade

### Prazos Típicos

- 1--5 dias (os bancos portugueses são relativamente rápidos para residentes)
- 1--3 semanas para sócios fundadores não residentes

### Bancos Comuns

- Caixa Geral de Depósitos, Millennium BCP, Novo Banco, BPI (tradicionais)
- Revolut Business, Wise Business (digitais)

## Secção 8 -- Considerações para Sócios Fundadores Estrangeiros

**Considerações para Sócios Fundadores Estrangeiros**

| Questão | Resposta |
| --- | --- |
| Gerentes não residentes permitidos? | Sim -- NIF obrigatório (obtido através de representante fiscal) |
| Representante fiscal exigido? | Sim, para residentes fora da UE/EEE (representante nomeado em Portugal para efeitos fiscais) |
| Presença física exigida? | Sim para a Empresa na Hora; aceite procuração para a via tradicional/online |
| Requisitos de apostilha | Documentos estrangeiros exigem apostilha + tradução certificada para português |
| NIF para estrangeiros | Obtido num serviço de Finanças ou via serviços online com representante fiscal |
| Restrições à propriedade estrangeira | Nenhumas para a Lda comum; sectores regulados podem exigir autorizações específicas |
| Golden Visa | Autorização de residência por investimento (€500.000+ em investimento em fundos, conforme reforma de 2023) |

## Secção 9 -- Erros Comuns e Recusas

- **R-PT-F1** — Dispensar o Contabilista Certificado. "Toda a empresa portuguesa tem de ter um Contabilista Certificado (CC) nomeado. Trata-se de uma exigência legal, não opcional. O CC é pessoalmente responsável pela exactidão das declarações fiscais."
- **R-PT-F2** — Não depositar o capital a tempo. "O capital tem de ser depositado no prazo de 5 dias úteis após a constituição via Empresa na Hora, ou entregue em caixa social até ao final do primeiro exercício. O incumprimento pode gerar responsabilidade pessoal dos gerentes."
- **R-PT-F3** — Não residente sem representante fiscal. "Os residentes fora da UE/EEE têm de nomear um representante fiscal em Portugal antes de obter um NIF. Sem NIF não é possível constituir a sociedade."
- **R-PT-F4** — Sociedade veículo para Golden Visa. "A mera constituição da empresa não confere direito ao Golden Visa. O investimento tem de cumprir critérios específicos (investimento em fundos, criação de postos de trabalho, etc.), nos termos da reforma de 2023. Não aconselhe a constituição como via para obtenção de visto sem aconselhamento especializado em imigração."
- **R-PT-F5** — Incumprimento do RCBE. "A falta de entrega e confirmação anual do Registo Central do Beneficiário Efetivo (RCBE) impede a sociedade de celebrar contratos, receber fundos ou distribuir lucros."

## Secção 10 -- Cronograma

**Cronograma**

| Etapa | Duração | Acumulado |
| --- | --- | --- |
| Obter NIF (se sócio estrangeiro) | 1--10 dias | Dia 1--10 |
| Marcação Empresa na Hora | 1 dia (no próprio dia) | Dia 2--11 |
| Empresa legalmente constituída | Imediato | Dia 2--11 |
| Depósito de capital no banco | 1--5 dias | Dia 3--16 |
| Declaração de início de atividade | No prazo de 15 dias | Dia 3--26 |
| Conta bancária totalmente operacional | 1--5 dias | Dia 4--21 |
| Entrega do RCBE | No prazo de 30 dias | Dia 4--41 |
| **Pronta para operar** |  | **Em apenas 1--2 dias (residentes via Empresa na Hora)** |

A Empresa na Hora é um dos processos de constituição de empresas mais rápidos do mundo.

## Aviso Legal

Esta skill e os seus resultados são fornecidos apenas para fins informativos e de cálculo e não constituem aconselhamento jurídico, fiscal ou financeiro. A Open Accountants e os seus contribuidores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado antes de qualquer actuação.

A versão mais actualizada e verificada desta skill encontra-se em [openaccountants.com](https://openaccountants.com).

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
