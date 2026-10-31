---
name: pt-return-assembly-filing
description: "Skill filha de pt-return-assembly para o pacote fiscal anual português do período de tributação de 2026 (entrega em 2027). Contém o mapa de inputs upstream por anexo do Modelo 3 do IRS e do Modelo 22 do IRC, os anexos em vigor, os campos do Quadro 10 do Modelo 22, os identificadores do intake e as instruções de submissão no Portal das Finanças e na Segurança Social Direta (Modelo 3, Modelo 22, IES, IVA, SAF-T), com o resumo de prazos de 2027, as coimas do RGIT e a substituição de declarações. Acionar com: anexos do Modelo 3, anexos do Modelo 22, Quadro 10, submeter Modelo 22, entregar IES, prazos 2027 Portugal, Portugal return annexes, Portugal filing steps. Carregar sempre junto com pt-return-assembly (reconciliações, working paper, pagamento, calendário). Fora do âmbito: o cálculo do imposto (pt-income-tax, pt-corporate-tax, portugal-vat-return, pt-social-contributions), não-residentes (pt-cross-border), preços de transferência (pt-transfer-pricing)."
version: 1.0
jurisdiction: PT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - pt-return-assembly
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PT Return Assembly: Formulários, Anexos e Submissão

## Portugal: Formulários, Anexos e Submissão (filha de pt-return-assembly), Skill v1.0 (período de tributação 2026)

## O que este ficheiro é

Esta é a skill filha de `pt-return-assembly`, a capstone que monta o pacote fiscal anual português do período de tributação de 2026 (declarações entregues em 2027). Carregar primeiro `pt-return-assembly` e depois esta.

A capstone foi dividida em duas a 31 de outubro de 2026 para caber no limite de tamanho da plataforma. Esta skill guarda, sem alterações, as duas secções mais longas da capstone, com a mesma numeração para que as remissões continuem a funcionar:

- **Secção 2**: o que cada skill upstream entrega e onde aparece no Modelo 3 (por anexo) e no Modelo 22 (por anexo e campo do Quadro 10), os anexos em vigor, os identificadores exigidos pelo intake e a coordenação entre AT, Segurança Social e e-fatura.
- **Secção 7**: instruções de submissão do Modelo 3, do Modelo 22, da IES, da declaração periódica de IVA, da comunicação de faturas e SAF-T e da Segurança Social Direta, o resumo de prazos do período 2026, as coimas por atraso e a substituição de declarações.

As reconciliações cross-skill (Secção 3), o working paper para o Contabilista Certificado (Secção 4), o bloco headline (Secção 5), o pagamento (Secção 6), o calendário de ações (Secção 8), as notas para 2027 (Secção 9), o bloco de atestação (Secção 10) e as regras de execução estão em `pt-return-assembly`.

## Secção 2: Entradas Obrigatórias dos Skills Upstream

A skill de montagem **não recalcula nada**. Espera outputs estruturados das skills upstream abaixo. Se uma skill upstream não tiver corrido, a montagem sinaliza a lacuna e continua com os dados disponíveis.

### 2.1 Declaração singular (Modelo 3): inputs

**Inputs Modelo 3**

| Skill upstream | Output consumido | Onde aparece no Modelo 3 |
| --- | --- | --- |
| `pt-income-tax` | Rendimentos da Categoria B (trabalho independente): regime simplificado vs contabilidade organizada, coeficientes do art. 31.º, retenções na fonte, pagamentos por conta, IRS Jovem, taxas progressivas de 2026 e adicional de solidariedade | Anexo B (regime simplificado ou atos isolados), Anexo C (contabilidade organizada) |
| `pt-irs-employees-investment` | Trabalho dependente e pensões (Categoria A e H), rendimentos de capitais (E), prediais (F), mais-valias (G), deduções à coleta | Anexo A, Anexo E, Anexo F, Anexo G, Anexo G1, Anexo H |
| `pt-nhr-ifici` | Regime de Residente Não Habitual (regime transitório) ou IFICI (EBF art. 58.º-A); rendimentos de fonte estrangeira com tratamento próprio | Anexo L |
| `pt-foreign-source-treaties` | Rendimentos de fonte estrangeira, crédito de imposto por dupla tributação internacional (CIRS art. 81.º), aplicação de Convenções para Evitar a Dupla Tributação (CDT) | Anexo J (rendimentos obtidos no estrangeiro) |
| `pt-corporate-tax` | (Apenas se o sujeito passivo for sócio de uma sociedade em transparência fiscal, CIRC art. 6.º) Lucro tributável imputado ao sócio | Anexo D (imputação de rendimentos) |
| `portugal-vat-return` | Para trabalhadores independentes Categoria B com IVA: posição anual de IVA; reconciliação de volume de negócios apenas | Verificação cruzada; não aparece diretamente no Modelo 3 |
| `pt-social-contributions` | Contribuições para a Segurança Social pagas como trabalhador independente; declarações trimestrais | Anexo B / C (contribuições); Anexo SS ao Modelo 3 |
| `portugal-bookkeeping` | Para contabilidade organizada: demonstração de resultados, conciliação fiscal-contabilística | Anexo C (campos de apuramento) |
| `portugal-crypto-tax` | Ganhos com criptoativos (CIRS art. 10.º, n.º 1, al. k)); detenção inferior a 365 dias (tributada) ou igual ou superior a 365 dias (excluída, art. 10.º, n.º 22); mineração e outras operações da Categoria B | Anexo G / Anexo G1 ou Anexo B / C consoante natureza |
| `portugal-payroll` | Trabalhador independente que também recebe rendimentos de trabalho dependente: salários, retenções de IRS, contribuições para a Segurança Social, quotizações sindicais | Anexo A |

**Anexos do Modelo 3 em vigor** (Portaria n.º 104/2026/1, art. 1.º, produz efeitos a 1 de janeiro de 2026): aprovados de novo os anexos A (trabalho dependente e pensões), B (rendimentos empresariais e profissionais, regime simplificado ou atos isolados), C (contabilidade organizada), D (imputação de rendimentos), H (benefícios fiscais e deduções) e J (rendimentos obtidos no estrangeiro); mantidos com novas instruções os anexos E (rendimentos de capitais) e G (mais-valias e outros incrementos patrimoniais); mantidos o rosto e os anexos F (rendimentos prediais), G1 (mais-valias não tributadas) e L (residente não habitual / incentivo fiscal à investigação científica e inovação), aprovados pela Portaria n.º 72-B/2025/1, e o Anexo I (rendimentos de herança indivisa), aprovado pela Portaria n.º 39-B/2024. Os modelos "destinam-se a declarar os rendimentos dos anos de 2015 e seguintes" (art. 1.º, n.º 4), pelo que servem para os rendimentos de 2026 até serem substituídos. As instruções do Anexo H foram depois alteradas pela Portaria n.º 136-C/2026/1.

### 2.2 Declaração de sociedades (Modelo 22): inputs

**Inputs Modelo 22**

| Skill upstream | Output consumido | Onde aparece no Modelo 22 |
| --- | --- | --- |
| `pt-corporate-tax` | Lucro tributável, taxa de IRC (19% para períodos iniciados em 2026; 15% sobre os primeiros €50.000 para PME e Small Mid Cap; 12,5% startups), derrama estadual (CIRC art. 87.º-A), derrama municipal, tributações autónomas (CIRC art. 88.º), prejuízos fiscais (CIRC art. 52.º), benefícios fiscais ao investimento (RFAI, SIFIDE II) | Modelo 22 (apuramento do lucro tributável, matéria coletável e cálculo do imposto); Anexos A, C, D, E |
| `portugal-bookkeeping` | Balancete final pós-encerramento, demonstração de resultados, balanço, mapas de depreciações e amortizações (Modelo 32) | Suporta Modelo 22 + IES |
| `portugal-financial-statements` | Demonstrações financeiras (SNC, NCM ou NCM-ME): Balanço, Demonstração de Resultados por Naturezas, Demonstração das Alterações no Capital Próprio, Demonstração dos Fluxos de Caixa, Anexo | Submetidas via IES; suportam Modelo 22 |
| `portugal-vat-return` | Posição anual de IVA da sociedade; declarações periódicas; pro-rata se aplicável; regularizações | Verificação cruzada; reflete-se na IES |
| `portugal-payroll` | Custos com pessoal, retenções na fonte de IRS dos colaboradores (Categoria A), contribuições para a Segurança Social | Modelo 22 (gastos com pessoal); cruzamento com DMR |
| `pt-social-contributions` | Contribuições da entidade empregadora e dos trabalhadores; membros de órgãos estatutários (MOE); entidades contratantes | DMR + Modelo 22 verificação cruzada |
| `pt-foreign-source-treaties` | Rendimentos de fonte estrangeira da sociedade; crédito por dupla tributação internacional (CIRC art. 91.º); participation exemption (CIRC art. 51.º) | Modelo 22, deduções à coleta e correções ao resultado |
| `pt-transfer-pricing` | Operações com entidades relacionadas (CIRC art. 63.º; Portaria n.º 268/2021) | Correções no Modelo 22; informação na IES |
| `portugal-crypto-tax` | Ganhos e perdas em criptoativos detidos pela sociedade, tratados consoante natureza contabilística | Modelo 22 (correções fiscais ao resultado contabilístico) |

**Impresso a usar para o período de 2026.** O Modelo 22 e os anexos são aprovados por despacho (CIRC art. 117.º, n.º 2). O impresso em vigor a 30 de outubro de 2026 é o do Despacho n.º 320/2026, feito para as alterações legislativas de 2025: o seu campo 347-B ainda multiplica por 20% e o 347-A por 16% (PME) ou 12,5% (startups), as taxas dos períodos de 2025. A declaração do período de 2026 (enviada até 31 de maio de 2027) usa o impresso que estiver aprovado para essa campanha; confirmar o novo despacho antes de preencher.

**Anexos do Modelo 22 em vigor em 2026** (Despacho n.º 320/2026, de 9 de janeiro): aprovados de novo a declaração Modelo 22 e os anexos C, D e F; mantidos os anexos A (períodos de 2015 e seguintes), B (apenas períodos anteriores a 2011), E, G e AIMI, aprovados pelo Despacho n.º 422/2025. Títulos dos formulários da AT: A "Derrama municipal", C "Regiões Autónomas", D "Benefícios fiscais", E "Regime simplificado", F "Organismos de investimento coletivo", G "Regime especial de determinação da matéria coletável" (atividades de transporte marítimo).

**Quadro 10 (Cálculo do imposto) do impresso do Despacho n.º 320/2026.** Campos usados nas reconciliações desta skill; confirmar no impresso aprovado para a campanha de 2027:

| Campo | Conteúdo (fórmula impressa no quadro) |
| --- | --- |
| 347-A / 347-B | Imposto à taxa reduzida (primeiros €50.000) / à taxa normal |
| 351 | Coleta (347-A + 347-B + 349 + 350 + 370): IRC apenas, sem derramas nem tributações autónomas |
| 373 | Derrama estadual (art. 87.º-A) |
| 378 | Coleta total (351 + 373) |
| 353 | Dupla tributação jurídica internacional (art. 91.º) |
| 355 | Benefícios fiscais |
| 356 | Pagamento especial por conta (art. 93.º) |
| 357 / 358 | Total das deduções / total do IRC liquidado (378 - 357) |
| 359 | Retenções na fonte |
| 360 | Pagamentos por conta (art. 105.º) |
| 374 | Pagamentos adicionais por conta (art. 105.º-A) |
| 361 / 362 | IRC a pagar / IRC a recuperar (358 + 371 - 359 - 360 - 374) |
| 364 | Derrama municipal (o Anexo A transporta para este campo) |
| 365 | Tributações autónomas |
| 366 / 369 | Juros compensatórios / juros de mora |
| 367 / 368 | Total a pagar / total a recuperar |

### 2.3 Identificadores exigidos pelo intake

**Identificadores**

| Identificador | Obrigatório para |
| --- | --- |
| **NIF** (Número de Identificação Fiscal), atribuído pela AT a pessoas singulares e coletivas | Todas as declarações |
| **NISS** (Número de Identificação de Segurança Social) | Declarações Segurança Social, DMR, declaração trimestral |
| **NIPC** (Número de Identificação de Pessoa Coletiva), coincide com o NIF da sociedade | Modelo 22, IES |
| **CAE** (Classificação das Atividades Económicas), código principal e códigos secundários | Modelo 22, IES, Anexo B do Modelo 3 (art. 151.º do CIRS e coeficientes) |
| **Senha de acesso ao Portal das Finanças** | Submissão pelo próprio |
| **Senha do Contabilista Certificado** | Nos casos em que a declaração deva por este ser assinada, o CC é identificado por senha atribuída pela AT (Portaria n.º 104/2026/1, art. 2.º, n.º 2) |
| **Regime de IVA**: normal mensal, normal trimestral, isenção do art. 53.º (volume de negócios até €15.000), outros regimes especiais | Declaração periódica de IVA |
| **Domicílio fiscal e estabelecimentos**: concelho (define derrama municipal e o Anexo A) | Modelo 22, Anexo A |
| **Período de tributação** (sociedades com período não coincidente com ano civil) | Modelo 22, IES |
| **Estado civil + dependentes + agregado familiar**; opção por tributação conjunta | Modelo 3, rosto |
| **Residência fiscal** (residente, não residente, RNH, IFICI, Madeira/Açores) | Modelo 3 |
| **IBAN** + comprovativo de titularidade | Reembolsos e pagamentos |

- **Identificador em falta**: se qualquer identificador estiver em falta, a skill de montagem sinaliza-o como "Necessita Input" e produz o working paper com placeholders em vez de parar. Regra interna de trabalho desta skill, não uma regra legal.

### 2.4 Coordenação AT + Segurança Social + e-fatura

Portugal tem obrigações declarativas em portais distintos:

- **AT (Portal das Finanças):** Modelo 3, Modelo 22, IES, declarações periódicas de IVA, comunicação de faturas, DMR, declarações de retenções (Modelo 10, Modelo 39, Modelo 30), IMI, IMT, IUC.
- **Segurança Social (Segurança Social Direta):** contribuições de trabalhadores por conta de outrem e da entidade empregadora, declaração trimestral e contribuições dos trabalhadores independentes, entidades contratantes. A declaração anual dos independentes em contabilidade organizada faz-se através do Anexo SS ao Modelo 3, "enviada aos serviços da Segurança Social pela entidade tributária competente" (ISS, Guia Prático).
- **e-fatura (faturas.portaldasfinancas.gov.pt):** comunicação das faturas emitidas, em tempo real, por ficheiro SAF-T (PT) ou por inserção direta no Portal, até ao dia 5 do mês seguinte (DL 198/2012, art. 3.º, n.os 1 e 2).

A capstone produz **um pacote único integrado** com as três vertentes reconciliadas. Um sócio-gerente de uma sociedade unipessoal por quotas, por exemplo, terá obrigações como contribuinte singular (Modelo 3), como sociedade (Modelo 22 e IES), e perante a Segurança Social (como membro de órgão estatutário). A montagem cruza as três.

## Secção 7: Instruções de Submissão

### 7.1 Submissões no Portal das Finanças

**Canais de submissão**

| Canal | Descrição | Adequado para |
| --- | --- | --- |
| **Portal das Finanças: preenchimento direto** | Formulário online no Portal | Contribuintes singulares; PME simples |
| **Portal das Finanças: envio de ficheiro** | Upload de ficheiros gerados por software de contabilidade | CC profissionais; sociedades com volume |
| **Software certificado de faturação / contabilidade** | Comunicação de faturas em tempo real ou por ficheiro SAF-T (PT) (DL 198/2012, art. 3.º, n.º 1) | Sociedades com ERP; grandes contribuintes |

### 7.2 Submissão do Modelo 3 (IRS)

1. Aceder ao Portal das Finanças com NIF + senha (ou Chave Móvel Digital / Cartão de Cidadão)
2. Menu de IRS: "Entregar Declaração" (Modelo 3)
3. Selecionar ano dos rendimentos 2026
4. Se disponível, o sistema apresenta uma declaração pré-preenchida com dados já comunicados à AT (rendimentos do trabalho, retenções, despesas dedutíveis com base nas faturas comunicadas até ao final de fevereiro de 2027, CIRS art. 78.º-B, n.º 5)
5. Validar e corrigir os anexos pré-preenchidos; acrescentar os anexos aplicáveis (Portaria n.º 104/2026/1):
   - Anexo A (rendimentos do trabalho dependente e pensões)
   - Anexo B (rendimentos empresariais e profissionais: regime simplificado ou atos isolados)
   - Anexo C (rendimentos empresariais e profissionais: contabilidade organizada)
   - Anexo D (imputação de rendimentos)
   - Anexo E (rendimentos de capitais)
   - Anexo F (rendimentos prediais)
   - Anexo G (mais-valias e outros incrementos patrimoniais)
   - Anexo G1 (mais-valias não tributadas)
   - Anexo H (benefícios fiscais e deduções)
   - Anexo I (rendimentos de herança indivisa)
   - Anexo J (rendimentos obtidos no estrangeiro)
   - Anexo L (residentes não habituais / IFICI)
   - Anexo SS (Segurança Social, trabalhadores independentes)
6. Validar: o Portal executa verificações lógicas e aritméticas; resolver erros e analisar avisos
7. Submeter: o sistema emite comprovativo de entrega. A declaração considera-se apresentada na data da submissão, sob condição de correção de erros em 30 dias (Portaria n.º 104/2026/1, art. 3.º, n.º 2)
8. Aguardar nota de liquidação

**Rendimentos de fonte estrangeira com crédito de imposto ainda não determinado no Estado da fonte:** o prazo do n.º 1 é prorrogado até 31 de dezembro desse ano, desde que o contribuinte comunique à AT, dentro do prazo normal, que cumpre as condições (CIRS art. 60.º, n.os 3 e 4).

**Contabilista Certificado:** quando a Categoria B é tributada com base em contabilidade organizada (Anexo C), a declaração é assinada pelo CC, identificado por senha atribuída pela AT (Portaria n.º 104/2026/1, art. 2.º, n.º 2; Estatuto da OCC, art. 10.º, n.º 1, al. b)).

**Atenção:** declarar o IBAN de que o contribuinte é titular no Portal das Finanças, para o reembolso ser pago por transferência.

### 7.3 Submissão do Modelo 22 (IRC)

As sociedades comerciais e as demais entidades do CIRC art. 123.º, n.º 1, são obrigadas a dispor de contabilidade organizada. As declarações fiscais que assentam nessa contabilidade são assinadas pelo Contabilista Certificado (Estatuto da OCC, art. 10.º, n.º 1, al. b)), que submete com a sua senha.

1. CC acede ao Portal das Finanças com as suas credenciais
2. Menu de IRC: "Entregar Declaração" (Modelo 22), no impresso aprovado para a campanha de 2027 (ver Secção 2.2: o impresso do Despacho n.º 320/2026 ainda traz as taxas dos períodos de 2025)
3. Selecionar período de tributação 2026
4. Preencher os quadros do rosto do Modelo 22: identificação do sujeito passivo e do CC, tipo de declaração, período de tributação, regime de tributação, apuramento do lucro tributável (correções ao resultado contabilístico), apuramento da matéria coletável, cálculo do imposto, tributações autónomas, retenções e pagamentos por conta, outras informações
5. Juntar os anexos aplicáveis (Despacho n.º 320/2026):
   - Anexo A (derrama municipal): quando a sociedade tem estabelecimentos em mais de um município e matéria coletável superior a €50.000 (repartição pela massa salarial; ver pt-corporate-tax)
   - Anexo C (Regiões Autónomas)
   - Anexo D (benefícios fiscais: RFAI, SIFIDE II e outros)
   - Anexo E (regime simplificado de IRC)
   - Anexo F (organismos de investimento coletivo)
   - Anexo G (regime especial do transporte marítimo)
   - Anexo AIMI (prédios afetos a uso pessoal dos sócios e gerentes, para efeitos do adicional ao IMI)
6. Validar e submeter: o Portal emite comprovativo
7. Pagar o imposto autoliquidado até 31 maio 2027 (CIRC art. 104.º, n.º 1, al. b)); o reembolso, quando a declaração é enviada no prazo e sem erros, é feito até ao fim do 3.º mês seguinte ao envio (art. 104.º, n.º 3)

**Grupos (RETGS):** a sociedade dominante envia a declaração do grupo e cada sociedade do grupo envia a sua (CIRC art. 120.º, n.º 6).

**Cessação de atividade:** a declaração do período da cessação é enviada até ao último dia do 3.º mês seguinte (CIRC art. 120.º, n.º 3).

### 7.4 Submissão da IES (Informação Empresarial Simplificada)

A IES é a declaração anual de informação contabilística e fiscal do CIRC art. 117.º, n.º 1, al. c), "enviada nos termos e com os anexos que para o efeito sejam mencionados no respectivo modelo" (art. 121.º, n.º 1). Submetida pelo CC.

1. CC acede ao Portal das Finanças
2. Menu: "IES / Declaração Anual"
3. Preencher o rosto e os anexos aplicáveis do modelo da IES em vigor (informação contabilística SNC, NCM ou NCM-ME; informação de IVA; operações com entidades relacionadas, CIRC art. 63.º; outros consoante a atividade)
4. Validar e submeter até **15 julho 2027** (CIRC art. 121.º, n.º 2): o Portal emite comprovativo
5. O dossier de preços de transferência, quando exigido, é constituído até ao mesmo prazo (ver `pt-transfer-pricing`; isenção para rendimentos totais inferiores a €10.000.000, Portaria n.º 268/2021)

### 7.5 Submissão da Declaração Periódica de IVA

1. CC ou sujeito passivo acede ao Portal das Finanças
2. Menu de IVA: "Declaração Periódica"
3. Selecionar período (mês ou trimestre)
4. Preencher os quadros da declaração e, se houver regularizações, os anexos dos campos 40 e 41; no Quadro 06 apura-se o imposto a entregar ao Estado (campo 93) ou o crédito a recuperar (campos 94, 95 e 96) (AT, Ofício-Circulado n.º 25119/2026). Os restantes números de campo estão em `portugal-vat-return`. A Portaria n.º 298/2026/1 aprovou um novo modelo que só se aplica às declarações de períodos iniciados a partir de 1 de julho de 2027; desde 1 de julho de 2026 já vale a quadrícula «Regime Grupos IVA» no Quadro 01 para as entidades de um grupo de IVA (Lei n.º 62/2025), cujo apuramento global é feito na declaração do grupo (mesmo ofício-circulado)
5. Submeter até dia 20 do 2.º mês seguinte (CIVA art. 41.º, n.º 1) e pagar até dia 25 do 2.º mês seguinte (CIVA art. 27.º, n.º 1). A declaração de junho e do 2.º trimestre segue o calendário especial descrito em `portugal-vat-return`
6. A declaração é devida mesmo em período sem operações tributáveis (ver `portugal-vat-return`)

### 7.6 Comunicação de faturas e SAF-T (PT)

**Comunicação de faturas e SAF-T**

| Obrigação | Como | Prazo |
| --- | --- | --- |
| **Comunicação de faturas à AT** | Em tempo real, por ficheiro SAF-T (PT), ou por inserção direta no Portal das Finanças (DL 198/2012, art. 3.º, n.º 1) | Até **dia 5** do mês seguinte ao da emissão (art. 3.º, n.º 2) |
| **Comunicação do inventário** (entidades com contabilidade organizada obrigadas a inventário) | Ficheiro por transmissão eletrónica | Até **31 de janeiro**, inventário a 31 de dezembro do ano anterior (DL 198/2012, art. 3.º-A, n.º 1) |
| **SAF-T (PT) da contabilidade** | Capacidade de exportação obrigatória (CIRC art. 123.º, n.º 8) | A pedido da AT, nomeadamente em inspeção |
| **SAF-T Auditoria fiscal** | Sob solicitação da AT em inspeções | Prazo fixado na notificação |

### 7.7 Submissões na Segurança Social Direta

**Submissões Segurança Social Direta**

| Declaração | Prazo |
| --- | --- |
| **Declaração de remunerações** (entidade empregadora) | Confirmação ou correção dos valores apurados pelo sistema até ao dia 20 do mês seguinte; o silêncio vale como aceitação (Código Contributivo art. 40.º, n.º 8) |
| **Declaração trimestral** dos trabalhadores independentes | Até ao **último dia de janeiro, abril, julho e outubro**, relativa aos três meses anteriores (ISS, Guia Prático) |
| **Anexo SS ao Modelo 3** (independentes em contabilidade organizada e declaração anual) | Com o Modelo 3, enviado à Segurança Social pela AT (ISS, Guia Prático) |
| **Início / fim de atividade** de empresários em nome individual e titulares de EIRL só com atividade industrial ou comercial | Online, "no mês em que a alteração acontecer" (ISS, Guia Prático) |

### 7.8 Resumo de prazos (período 2026)

**Resumo de prazos**

| Tipo de declarante | Declaração | Autoridade | Prazo |
| --- | --- | --- | --- |
| Singular (residente) | Modelo 3 IRS + Anexos | AT | **1 abril a 30 junho 2027** (CIRS art. 60.º, n.º 1) |
| Sociedade (período = ano civil) | Modelo 22 IRC + Anexos, e pagamento | AT | **31 maio 2027** (CIRC art. 120.º, n.º 1; art. 104.º, n.º 1, al. b)) |
| Sociedade | IES | AT | **15 julho 2027** (CIRC art. 121.º, n.º 2) |
| Sujeito passivo IVA mensal | Declaração periódica de dezembro 2026 | AT | **22 fevereiro 2027** (20 fevereiro é sábado; regra em `portugal-vat-return`); pagamento até **25 fevereiro 2027** |
| Sujeito passivo IVA trimestral | Declaração periódica do 4.º trimestre 2026 | AT | **22 fevereiro 2027** (20 fevereiro é sábado); pagamento até **25 fevereiro 2027** |
| Empregador | DMR de dezembro 2026 | AT | **10 janeiro 2027** (CIRS art. 119.º, n.º 1, al. c), i)) |
| Entidade devedora de rendimentos | Documento comprovativo dos rendimentos e retenções de 2026 ao titular | Contribuinte | **20 janeiro 2027** (CIRS art. 119.º, n.º 1, al. b)) |
| Substituto tributário | Modelo 10 (restantes rendimentos de 2026) | AT | **Final de fevereiro 2027** (CIRS art. 119.º, n.º 1, al. c), ii)) |
| Entidade que paga rendimentos sujeitos a retenção liberatória | Modelo 39 (rendimentos de 2026) | AT | **Final de fevereiro 2027** (CIRS art. 119.º, n.º 12, al. b)) |
| Entidade que paga rendimentos com isenção, dispensa ou redução de taxa (art. 71.º) | Declaração própria | AT | **Final de julho 2027** (CIRS art. 119.º, n.º 2, al. a)) |
| Entidade que paga rendimentos a não residentes | Modelo 30 | AT | **Até ao fim do 2.º mês seguinte** ao pagamento (CIRS art. 119.º, n.º 7, al. a)) |
| Trabalhador independente | Declaração trimestral SS (outubro a dezembro 2026) | SS | **31 janeiro 2027** |
| Todos os emitentes de faturas | Comunicação das faturas de dezembro 2026 | AT (e-fatura) | **5 janeiro 2027** |
| Entidades com inventário | Comunicação do inventário a 31 dezembro 2026 | AT | **31 janeiro 2027** |
| Grupos multinacionais com rendimentos consolidados de €750.000.000 ou mais no período anterior | Declaração financeira e fiscal por país (CIRC art. 117.º, n.º 1, al. d), e art. 121.º-A, n.º 1) | AT | **12 meses** após o fim do período de relato (art. 121.º-A, n.º 3); cada entidade do grupo comunica quem declara até ao prazo do Modelo 22 (art. 121.º-A, n.º 4) |

### 7.9 Coimas por atraso

**Coimas por atraso**

| Infração | Coima | Base legal |
| --- | --- | --- |
| Falta ou atraso na entrega de declaração que permita à AT determinar a matéria coletável (Modelo 3, Modelo 22, IVA, IES) | €150 a €3.750 | RGIT art. 116.º, n.º 1 |
| Falta ou atraso na apresentação de declarações, documentos, comunicações (DMR, Modelo 10, comunicação de faturas, SAF-T) | €150 a €3.750 | RGIT art. 117.º, n.º 1 |
| Falta ou atraso nas declarações de início, alteração ou cessação de atividade | €300 a €7.500 | RGIT art. 117.º, n.º 2 |
| Pessoas coletivas | Limites mínimo e máximo elevados para o dobro; máximo de €165.000 em caso de dolo | RGIT art. 26.º, n.os 1 e 4 |
| Falta de entrega da prestação tributária (imposto, retenções, pagamentos por conta): negligência | 15% a metade do imposto em falta | RGIT art. 114.º, n.º 2 |
| Falta de entrega da prestação tributária: dolo, sem crime | Valor da prestação em falta até ao dobro | RGIT art. 114.º, n.º 1 |
| Juros compensatórios: liquidação retardada por facto do sujeito passivo, declaração fora de prazo | Contam-se dia a dia | LGT art. 35.º, n.os 1, 3 e 6 |
| Juros de mora: imposto não pago no prazo legal | 7,221% ao ano desde 1 de janeiro de 2026, a taxa das dívidas ao Estado | LGT art. 44.º, n.º 3; Aviso n.º 18/2026/2 (IGCP) |

- **Dispensa de coima**: não é aplicada coima quando, nos cinco anos anteriores, o agente não foi condenado nem beneficiou de dispensa ou redução, a infração não causou prejuízo efetivo à receita e a falta está regularizada; a falta de entrega de imposto conta sempre como prejuízo (RGIT art. 29.º, n.os 1 a 3).

### 7.10 Substituição de declaração

- **IRC**: quando tenha sido liquidado imposto inferior ao devido ou declarado prejuízo superior ao efetivo, a declaração de substituição pode ser apresentada "ainda que fora do prazo", pagando o imposto em falta (CIRC art. 122.º, n.º 1). Quando a autoliquidação resultou em imposto superior ao devido, a substituição faz-se no prazo de um ano a contar do termo do prazo legal (art. 122.º, n.º 2). O pagamento da diferença é feito até ao dia do envio da declaração de substituição (art. 104.º, n.º 1, al. c)).
- **IRS**: a declaração é ainda apresentada nos 30 dias imediatos a qualquer facto que altere os rendimentos já declarados (CIRS art. 60.º, n.º 2). Uma declaração submetida com erros pode ser corrigida no prazo de 30 dias (Portaria n.º 104/2026/1, art. 3.º, n.º 2).
- **Coimas**: regularização espontânea pode beneficiar da dispensa do RGIT art. 29.º, se reunidos os requisitos; em consequência de inspeção não há essa atenuação, e pode haver crime fiscal se houver ocultação.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| CIRS art. 60 (Modelo 3, 1 April to 30 June; foreign tax credit extension) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-30 |
| CIRS art. 57 (return and annexes; two residence statuses) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs57.aspx | 2026-10-30 |
| Portaria n.º 104/2026/1 (Modelo 3 annexes, electronic filing, CC password, 30-day correction) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/portaria-104-2026-1.pdf | 2026-10-30 |
| Portaria n.º 136-C/2026/1 (Anexo H instructions) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/portaria-136-c-2026-1.pdf | 2026-10-30 |
| Despacho n.º 320/2026 (Modelo 22 and annexes in force in 2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-320-2026.pdf | 2026-10-30 |
| AT, Modelo 22 annex forms A, C, D, E, F, G (form titles) | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF (and M22ANC, M22AND, M22ANE, M22ANF, M22ANG) | 2026-10-30 |
| CIRC art. 87 and Lei 64/2025 art. 3 (19% 2026, 18% 2027, 17%, 15% SME, 12.5% startups) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-30 |
| CIRC art. 87-A (derrama estadual) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx | 2026-10-30 |
| CIRC art. 88 (autonomous taxation) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx | 2026-10-30 |
| CIRC art. 52 (losses 65%, no time limit, change of ownership) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx | 2026-10-30 |
| CIRC arts. 104, 105, 106, 107 (payment rules, payments on account, PEC repealed, limits) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx (and irc105, irc106, irc107) | 2026-10-30 |
| CIRC arts. 117, 120, 121, 122, 123 (returns, Modelo 22 and IES deadlines, substitution, organised accounts, SAF-T export) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc120.aspx (and irc117, irc121, irc122, irc123) | 2026-10-30 |
| CIRS arts. 28 and 31 (EUR 200,000 limit; coefficients; invoices by end February) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx (and irs28) | 2026-10-30 |
| CIRS arts. 71, 72, 10 (28% and 35% final withholding; 28% special rate; crypto 365 days) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx (and irs72, irs10) | 2026-10-30 |
| CIRS art. 78-B (invoices by end February, 15 March, 31 March) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78b.aspx | 2026-10-30 |
| CIRS art. 119 (20 January statement, DMR by the 10th, Modelo 10 and Modelo 39 by end February, Modelo 30, end of July return) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx | 2026-10-30 |
| CIVA arts. 41, 27, 52 (return by the 20th, payment by the 25th, 10-year retention) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva41.aspx (and iva27, iva52) | 2026-10-30 |
| CIVA art. 53 (EUR 15,000 exemption) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx | 2026-10-30 |
| Decreto-Lei n.º 198/2012, arts. 3 and 3-A (invoice reporting by the 5th; inventory by 31 January) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Decreto-Lei%20n%20_198_2012_24_08.pdf | 2026-10-30 |
| RGIT arts. 26, 29, 114, 116, 117 (fines) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx (and rgit26, rgit29, rgit114, rgit117) | 2026-10-30 |
| LGT arts. 35, 44, 45 (compensatory interest, late interest, 4-year limitation) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt45.aspx (and lgt35, lgt44) | 2026-10-30 |
| ISS, Guia Prático, Trabalhadores Independentes (21.4%, 25.2%, 70% / 20%, EUR 20, IAS 2026 EUR 537.13, quarterly declaration, payment 10th to 20th, Anexo SS) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-30 |
| Portaria n.º 268/2021 (transfer pricing file: EUR 10,000,000, EUR 100,000 / EUR 500,000) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_268_2021.pdf | 2026-10-30 |
| Estatuto da Ordem dos Contabilistas Certificados (2024 edition), art. 10 | https://www.occ.pt/sites/default/files/public/2024-09/Estatuto_2024.pdf | 2026-10-30 |
| Portaria n.º 72-B/2025/1 (Modelo 3 annexes F, G1, L and their titles) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_72_B_2025_1.pdf | 2026-10-30 |
| Portaria n.º 39-B/2024 (Modelo 3 Anexo I, rendimentos de herança indivisa) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_39_B_2024.pdf | 2026-10-30 |
| Despacho n.º 320/2026, Modelo 22 form, Quadro 10 (field numbers; field 347 still at 20% / 16%) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-320-2026.pdf | 2026-10-30 |
| Código dos Regimes Contributivos (Lei 110/2009), arts. 40(8), 43, 53, 69(2), 155(2), 168 (34.75% = 23.75% + 11%; declaration by the 20th; employer payment 1st to 25th from 1 January 2026, DL 127/2025) | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 | 2026-10-30 |
| IGCP, Aviso n.º 18/2026/2 (late-payment interest 7.221% from 1 January 2026) | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-30 |
| AT, Ofício-Circulado n.º 25119/2026 (VAT return: fields 40, 41, 93 to 96; Portaria 298/2026/1 new model for periods from 1 July 2027; VAT groups box from 1 July 2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio-Circulado-25119-2026.pdf | 2026-10-30 |
| CIRC art. 121-A (country-by-country report: EUR 750,000,000, 12 months, notification by the Modelo 22 deadline) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121a.aspx | 2026-10-30 |

Not yet confirmed: the act approving Anexo SS to the Modelo 3 (the ISS guide describes it, the approving act was not read); the Modelo 22 form and Quadro 10 field numbers for the 2027 campaign (the 2026 period), because that form is not yet approved: the field map in Section 2.2 is from the Despacho 320/2026 form; the other Modelo 22 quadros and the periodic VAT return field numbers other than 40, 41 and 93 to 96; the Modelo 22 annex subjects of B (pre-2011 only) beyond what the AT form titles show; the IES annex letters and contents; the 15-day Social Security deadline for start, cessation or suspension of activity; the AT IBAN and the digit counts of NIF, NISS and Multibanco references. The full list for the package is in pt-return-assembly.

## Disclaimer final

OpenAccountants: skills de contabilidade open-source para IA.
Isto não constitui aconselhamento fiscal. Todos os outputs devem ser revistos e, quando a declaração assenta em contabilidade organizada, assinados por um Contabilista Certificado inscrito na OCC (Ordem dos Contabilistas Certificados), antes de submissão no Portal das Finanças, na Segurança Social Direta, ou em qualquer outra plataforma oficial.
