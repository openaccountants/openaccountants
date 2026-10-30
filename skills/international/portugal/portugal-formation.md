---
name: portugal-formation
description: "Utilize esta skill sempre que lhe perguntarem sobre constituição, incorporação ou registo de uma empresa em Portugal em 2026. Acione perante expressões como \"constituir empresa em Portugal\", \"constituição de Lda\", \"sociedade por quotas\", \"Empresa na Hora\", \"Empresa Online\", \"constituição de empresa portuguesa\", \"registar negócio em Portugal\", \"sociedade unipessoal\", \"NIF Portugal\", \"Registo Comercial\", \"beneficiário efetivo\", \"RCBE\", ou qualquer questão sobre o início de uma entidade empresarial em Portugal. Abrange tipos de entidade (Lda, Unipessoal Lda, SA, ENI), Código das Sociedades Comerciais (capital, entradas, reserva legal, revisor oficial de contas), emolumentos do IRN para 2026 (Empresa na Hora, Empresa Online, certificado de admissibilidade, certidão permanente), RCBE, inscrição fiscal, obrigações pós-constituição e abertura de conta bancária. Fora do âmbito, ver: pt-corporate-tax (cálculo do IRC), portugal-vat-return (IVA), pt-social-contributions (Segurança Social), portugal-bookkeeping (contabilidade e SNC), pt-cross-border (não residentes). LEIA SEMPRE esta skill antes de aconselhar sobre a constituição de empresas em Portugal. Trigger also on: \"set up a company in Portugal\", \"Lda formation\", \"sociedade por quotas\", \"Empresa na Hora\", \"Portuguese company formation\", \"register a business Portugal\", \"sociedade unipessoal\", \"NIF Portugal\", \"Registo Comercial\", \"beneficial owner register Portugal\"."
version: 1.2
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Formation

## Portugal: Constituição de Empresa e Seleção de Entidade, Skill v1.2 (2026)

> Source-cited draft: not reviewed by an accountant.

Esta skill cobre a escolha da forma jurídica e a constituição de uma sociedade comercial em Portugal em 2026. Os números de imposto vêm das skills de domínio do mesmo pacote, que mandam quando os números divergem:

- `pt-corporate-tax`: taxas de IRC, derramas, Modelo 22 e IES.
- `portugal-vat-return`: registo e periodicidade do IVA.
- `pt-social-contributions`: contribuições de trabalhadores e membros de órgãos estatutários (gerentes).
- `portugal-bookkeeping`: contabilidade organizada, SNC e SAF-T.
- `pt-cross-border`: não residentes e estabelecimento estável.

## Rates and thresholds

### Constituição de Empresa

- **Lda: capital**: livremente fixado; cada quota tem no mínimo €1, com pelo menos 2 sócios (logo, €2 no mínimo)  _(CSC art. 7.º, n.º 2, art. 201.º e art. 219.º, n.º 3)_
- **Unipessoal Lda: capital**: quota única de no mínimo €1  _(CSC art. 219.º, n.º 3, e art. 270.º-A; justica.gov.pt, Capital social)_
- **SA: capital mínimo**: €50.000; pode ser diferida a realização de até 70% das entradas em dinheiro (ou seja, pelo menos 30% realizado)  _(CSC art. 276.º, n.º 5, e art. 277.º, n.º 2)_
- **SA: valor nominal mínimo da ação**: 1 cêntimo  _(CSC art. 276.º, n.º 3)_
- **ENI**: sem personalidade jurídica, responsabilidade ilimitada; tributado em IRS (ver `pt-income-tax`)
- **Empresa na Hora (pedido normal)**: €360  _(RERN art. 27.º, n.º 3.1; IRN, Criar Empresa na Hora)_
- **Empresa na Hora com marca (uma classe)**: €200 segundo a tabela do IRN; €44 por cada classe adicional  _(IRN, Criar Empresa na Hora)_
- **Empresa Online (pacto pré-aprovado)**: €220 normal / €440 urgente  _(RERN art. 27.º, n.º 3.6; IRN, Criar Empresa Online)_
- **Empresa Online (pacto elaborado pelos sócios)**: €360 normal / €720 urgente  _(RERN art. 27.º, n.º 3.7; IRN, Criar Empresa Online)_
- **Registo de constituição pela via tradicional**: €360  _(RERN art. 22.º, n.º 2.1)_
- **Certificado de admissibilidade**: €75; a urgência acresce o valor do emolumento do ato (€75), total €150; validade 3 meses  _(RERN art. 23.º, n.º 2.1 e 2.2; gov.pt)_
- **Certidão permanente (assinatura)**: €25 por 1 ano; €40 por 2; €60 por 3; €70 por 4 anos  _(RERN art. 22.º, n.º 13.4)_
- **Depósito do capital (Lda, Unipessoal)**: 5 dias úteis, ou declaração de entrega nos cofres da sociedade até ao fim do primeiro exercício económico  _(CSC art. 202.º, n.º 4; IRN, Capital social)_
- **RCBE (beneficiário efetivo)**: declaração inicial em 30 dias após o registo; atualização em 30 dias após cada alteração; confirmação anual até 31 de dezembro  _(RJRCBE arts. 12.º, 14.º e 15.º)_
- **Inscrição em IRC**: sociedade sujeita a registo comercial: 15 dias a partir da apresentação a registo na Conservatória; entidade não sujeita a registo comercial: 90 dias a partir da inscrição no RNPC. Quando a declaração de início de atividade do IVA deva ser entregue dentro desse prazo, vale como declaração de inscrição  _(CIRC art. 118.º, n.os 1 e 2)_
- **Declaração de início de atividade (IVA)**: antes de iniciar a atividade  _(CIVA art. 31.º, n.º 1)_
- **IES**: até 15 de julho do ano seguinte  _(CIRC art. 121.º, n.º 2)_
- **IRC (Modelo 22)**: até ao último dia de maio do ano seguinte  _(CIRC art. 120.º, n.º 1)_
- **Contabilidade organizada**: obrigatória para sociedades comerciais; atrasos de execução até 90 dias no máximo  _(CIRC art. 123.º, n.os 1 e 3)_
- **Taxa normal de IRC**: 19% nos períodos iniciados em 2026  _([CIRC art. 87.º](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx); ver `pt-corporate-tax`)_
- **PME: primeiros €50.000 de matéria coletável**: 15% em 2026  _(CIRC art. 87.º, n.º 2; Lei 64/2025 art. 3.º; ver `pt-corporate-tax`)_

## Secção 1: Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Registo comercial | Instituto dos Registos e do Notariado (IRN): Conservatória do Registo Comercial e Registo Nacional de Pessoas Coletivas (RNPC) |
| Legislação principal | Código das Sociedades Comerciais (CSC); DL 111/2005 (Empresa na Hora); DL 125/2006 (Empresa Online); Regulamento Emolumentar dos Registos e Notariado (RERN, DL 322-A/2001); Lei 89/2017 (RCBE) |
| Tempo de constituição | Empresa na Hora: todo o processo "num único balcão, num único momento" (IRN). Empresa Online: o IRN não publica um prazo; analisa o pedido depois do pagamento |
| Custo de constituição (2026) | €360 Empresa na Hora; €220 ou €360 Empresa Online (RERN art. 27.º) |
| Taxa de IRC | 19% (taxa geral, períodos iniciados em 2026); 15% sobre os primeiros €50.000 de matéria coletável para PME e Small Mid Cap (ver `pt-corporate-tax`) |
| Versão da skill | 1.2 |

## Secção 2: Comparação de Tipos de Entidade

**Comparação de Tipos de Entidade**

| Característica | Empresário em Nome Individual (ENI) | Sociedade por Quotas (Lda) | Sociedade Unipessoal por Quotas (Unipessoal Lda) | Sociedade Anónima (SA) |
| --- | --- | --- | --- | --- |
| Personalidade jurídica | Não | Sim | Sim | Sim |
| Responsabilidade | Ilimitada | Limitada à entrada de capital | Limitada | Limitada |
| Sócios mínimos | 1 | 2 (CSC art. 7.º, n.º 2) | 1, pessoa singular ou coletiva (art. 270.º-A) | 5 (art. 273.º); 1 se for outra sociedade a única acionista (art. 488.º) |
| Capital social mínimo | N/A | €2 (mínimo €1 por quota, art. 219.º, n.º 3) | €1 | €50.000 (art. 276.º, n.º 5) |
| Tratamento fiscal | IRS (pessoal) | IRC (societário) | IRC (societário) | IRC (societário) |
| Carga administrativa | Baixa | Média | Média | Elevada |
| Revisor oficial de contas (ROC) | Não | Só se, sem conselho fiscal, ultrapassar 2 de 3 limites em 2 anos seguidos: balanço €1.500.000, vendas €3.000.000, 50 trabalhadores (art. 262.º, n.º 2) | Igual à Lda | Sempre: fiscal único ROC, ou conselho fiscal com ROC, ou ROC separado (arts. 413.º e 414.º) |
| Reserva legal | N/A | 5% do lucro até 20% do capital, nunca inferior a €2.500 (arts. 218.º e 295.º) | Igual à Lda | 5% do lucro até 20% do capital (art. 295.º, n.º 1) |

**Predefinição recomendada:** Sociedade por Quotas (Lda) ou Sociedade Unipessoal por Quotas para a maioria dos fins comerciais.

**Limite à unipessoal (CSC art. 270.º-C).** Uma pessoa singular só pode ser sócia de uma única sociedade unipessoal por quotas, e uma sociedade por quotas não pode ter como sócio único uma sociedade unipessoal por quotas. Em caso de violação, qualquer interessado pode pedir a dissolução por via administrativa. Pergunte sempre se o cliente já detém outra unipessoal.

## Secção 3: Processo de Registo

### Opção A: Empresa na Hora (Constituição no Próprio Dia)

O IRN faz a constituição "num único balcão, num único momento". Permite criar sociedade unipessoal por quotas, sociedade por quotas e sociedade anónima (não sociedades anónimas europeias).

1. **Comparecer num balcão Empresa na Hora**, em qualquer balcão, seja qual for a sede. É necessária a presença de todos os sócios.
2. **Escolher a firma**: da Bolsa de Firmas e Denominações (lista pré-aprovada) ou apresentar um certificado de admissibilidade já aprovado pelo RNPC.
3. **Escolher um pacto social pré-aprovado** (modelo).
4. **Apresentar identificação**: Cartão de Cidadão, Bilhete de Identidade, passaporte ou autorização de residência, e o NIF de cada sócio pessoa singular. Sócios pessoas coletivas apresentam o cartão de pessoa coletiva, a ata que dá poderes aos representantes, os documentos destes e o pacto atualizado.
5. **Indicar o Contabilista Certificado (CC)**: escolher um da Bolsa de CCs no balcão, ou entregar a declaração de início de atividade num serviço de Finanças até 15 dias depois da criação da empresa.
6. **Pagar €360** (pedido normal). Com marca associada, ver a Secção 5.
7. **Receber no fim**: pacto social, código de acesso à certidão permanente, código de acesso ao Cartão da Empresa e número de Segurança Social da empresa. Com o registo definitivo, os atributos de gerente ou administrador no SCAP são dados sem custos.
8. **Depositar o capital** em 5 dias úteis na conta da sociedade, salvo se já depositado no ato ou se os sócios declararem a entrega nos cofres da sociedade até ao fim do primeiro exercício económico.
9. **Declarar o beneficiário efetivo** (RCBE) no prazo de 30 dias.

### Opção B: Empresa Online (serviço Empresa 2.0)

1. Aceder ao serviço Empresa 2.0 com Cartão de Cidadão, Chave Móvel Digital, certificado digital de profissional jurídico ou autenticação europeia (eIDAS). Um cidadão estrangeiro pode usar a Chave Móvel Digital associada ao passaporte ou eIDAS.
2. Preencher o formulário: tipo de sociedade, sócios e gerentes ou administradores, CAE e objeto, capital, sede, firma e beneficiário efetivo. Documentos em língua estrangeira levam tradução.
3. Pagar (MB Way, Multibanco ou cartão de crédito) em 48 horas a contar da submissão: €220 com pacto pré-aprovado, €360 com pacto elaborado pelos sócios; o pedido urgente custa o dobro (€440 ou €720).
4. Todos os sócios assinam digitalmente o pacto e a aceitação do cargo.
5. O IRN analisa o pedido. Havendo inconformidades, há 5 dias seguidos para corrigir, com custo adicional de €30; sem correção, o registo pode ficar provisório ou ser recusado.
6. Se aprovado, recebe por e-mail os códigos do cartão da empresa e da certidão permanente, o pacto e o número de Segurança Social.

**Não é possível a Empresa Online** se um sócio for menor de 18 anos, se algum sócio não tiver NIF português, se a sociedade resultar de fusão ou cisão, se um sócio for sociedade estrangeira sem NIPC português, ou se o capital for realizado em espécie. Na Empresa Online a entrada de capital só pode ser feita em dinheiro.

### Opção C: Constituição Tradicional (Conservatória)

1. Obter certificado de admissibilidade da firma junto do RNPC (€75; válido 3 meses).
2. Elaborar o pacto social (estatutos).
3. Reduzir o contrato a escrito com as assinaturas reconhecidas presencialmente; só é exigida forma mais solene (por exemplo, escritura) quando os bens com que os sócios entram o exijam (CSC art. 7.º, n.º 1).
4. Registar a constituição na Conservatória do Registo Comercial (€360, RERN art. 22.º, n.º 2.1). O emolumento é único e inclui a inscrição no ficheiro central de pessoas coletivas e a publicação obrigatória (art. 22.º, n.º 1).
5. Inscrever a sociedade nas Finanças (CIRC art. 118.º) e na Segurança Social.
6. É a via para entradas em espécie complexas e pactos à medida. Os custos de advogado ou notário não têm tabela pública nesta skill.

### Passos Pós-Registo (Todas as Opções)

- Inscrição em IRC: uma sociedade comercial está sujeita a registo comercial, por isso entrega a declaração de inscrição em 15 dias a partir da apresentação a registo na Conservatória (o prazo de 90 dias a partir da inscrição no RNPC é só para entidades não sujeitas a registo comercial). Quando a declaração de início de atividade do IVA deva ser entregue dentro desse prazo, vale como declaração de inscrição (CIRC art. 118.º, n.os 1 e 2).
- Declaração de início de atividade para IVA antes de iniciar a atividade (CIVA art. 31.º, n.º 1). Periodicidade e regras: ver `portugal-vat-return`.
- Caixa postal eletrónica (ou adesão às notificações eletrónicas no Portal das Finanças) comunicada à AT em 30 dias a contar do início de atividade (LGT art. 19.º, n.os 12 e 14).
- Inscrição na Segurança Social como entidade empregadora quando contratar, e contribuições de gerentes remunerados: ver `pt-social-contributions`.
- Declaração do beneficiário efetivo (RCBE) em 30 dias (RJRCBE art. 12.º, n.º 1).

## Secção 4: Requisitos de Capital

**Requisitos de Capital**

| Tipo de Entidade | Capital Social Mín. | Realização Mín. | Prazo de Realização | Entradas em Espécie |
| --- | --- | --- | --- | --- |
| Lda (vários sócios) | €2 (mín. €1 por quota) | O contrato pode diferir as entradas em dinheiro (CSC art. 202.º, n.º 4) | Depósito em 5 dias úteis, ou declaração de entrega nos cofres da sociedade até ao fim do 1.º exercício (art. 202.º, n.º 4); confirmação na primeira assembleia geral anual seguinte (art. 202.º, n.º 6) | Permitidas; relatório de ROC independente obrigatório, sem limite mínimo de valor (art. 28.º, n.º 1). Não na Empresa Online |
| Unipessoal Lda | €1 | Igual à Lda | Igual à Lda | Igual à Lda |
| SA | €50.000 | 30% das entradas em dinheiro (só 70% podem ser diferidos, art. 277.º, n.º 2) | O IRN indica depósito de pelo menos 30% em 5 dias após a disponibilização da certidão permanente; o CSC exige o depósito das entradas realizadas em conta aberta em nome da futura sociedade até à celebração do contrato (art. 277.º, n.º 3) | Permitidas (relatório de ROC, art. 28.º) |

Não são admitidas contribuições de indústria (só trabalho) nas Lda e SA (CSC arts. 202.º, n.º 1, e 277.º, n.º 1). Atividades reguladas por lei especial podem exigir capital mínimo superior (IRN).

**Reserva legal.** Pelo menos 5% do lucro de cada exercício vai para a reserva legal até esta atingir 20% do capital (CSC art. 295.º, n.º 1). Numa Lda a reserva legal nunca é inferior a €2.500 (art. 218.º, n.º 2), mesmo com capital de €1 ou €2. Isto limita a distribuição de lucros nos primeiros anos.

## Secção 5: Repartição de Custos

**Repartição de Custos (emolumentos de 2026)**

| Componente de Custo | Valor (EUR) | Notas |
| --- | --- | --- |
| Empresa na Hora (normal) | €360 | Valor único: inclui a aprovação da firma no balcão, a publicação obrigatória e os atos de registo comercial (RERN art. 27.º, n.os 3.1 e 3.4) |
| Empresa na Hora com marca (uma classe) | €200 na tabela do IRN; +€44 por classe adicional | A página do IRN não diz se os €200 acrescem aos €360; confirme no balcão |
| Empresa na Hora com entradas em espécie | €360 + custo do registo de transmissão de cada bem | Segundo o RERN (IRN) |
| Empresa Online (pacto pré-aprovado) | €220 (urgente €440) | RERN art. 27.º, n.º 3.6 |
| Empresa Online (pacto dos sócios) | €360 (urgente €720) | RERN art. 27.º, n.º 3.7 |
| Correção de inconformidades (online) | €30 | IRN |
| Certificado de admissibilidade | €75; urgente €150 | RERN art. 23.º, n.os 2.1 e 2.2 |
| Registo de constituição (via tradicional) | €360 | RERN art. 22.º, n.º 2.1; mais custos de reconhecimento de assinaturas ou escritura, não tabelados aqui |
| Depósito de capital social | €1 por quota (mínimo legal) | Considere a reserva legal mínima de €2.500 numa Lda |
| **Total mínimo (Empresa Online, pacto pré-aprovado)** | **€220** | Opção mais barata, mas exige NIF português para todos os sócios |
| **Total (Empresa na Hora)** | **€360** | Constituição no próprio dia |

### Manutenção Anual

**Manutenção Anual**

| Item | Custo (EUR) |
| --- | --- |
| Contabilista Certificado | Honorários livres; não há tabela oficial |
| Entrega de IES/IRC | Normalmente incluída nos honorários do contabilista |
| Certidão permanente (assinatura) | €25 por 1 ano; €40 por 2; €60 por 3; €70 por 4 anos (RERN art. 22.º, n.º 13.4) |
| Alterações ao contrato de sociedade | €200; com aumento ou redução de capital €225 (RERN art. 22.º, n.os 2.4 e 2.4.1) |
| Publicações obrigatórias | Incluídas no emolumento do registo (RERN art. 22.º, n.º 1) |

## Secção 6: Cumprimento Pós-Constituição

**Cumprimento Pós-Constituição**

| Obrigação | Prazo | Autoridade |
| --- | --- | --- |
| Declaração de inscrição em IRC | 15 dias a partir da apresentação a registo na Conservatória do Registo Comercial; 90 dias a partir da inscrição no RNPC só para entidades não sujeitas a registo comercial (CIRC art. 118.º, n.º 1) | Autoridade Tributária |
| Declaração de início de atividade (IVA) | Antes de iniciar a atividade (CIVA art. 31.º); na Empresa na Hora sem CC indicado, até 15 dias depois da criação (IRN) | Autoridade Tributária |
| Declaração de alterações | 15 dias se sujeito a IVA, 30 dias nos restantes casos; dispensada para factos sujeitos a registo comercial (CIRC art. 118.º, n.os 5 e 7) | Autoridade Tributária |
| Caixa postal eletrónica | 30 dias a contar do início de atividade (LGT art. 19.º, n.º 12) | Autoridade Tributária |
| Contabilidade organizada | Sem atrasos superiores a 90 dias desde o fim do mês das operações (CIRC art. 123.º, n.º 3) | Autoridade Tributária |
| IES (Informação Empresarial Simplificada) | Até 15 de julho do ano seguinte (CIRC art. 121.º, n.º 2) | Autoridade Tributária |
| Declaração de IRC (Modelo 22) | Até ao último dia de maio do ano seguinte (CIRC art. 120.º, n.º 1) | Autoridade Tributária |
| Declarações de IVA | Mensal se o volume de negócios do ano anterior for de €650.000 ou mais; trimestral abaixo (CIVA art. 41.º; ver `portugal-vat-return`) | Autoridade Tributária |
| Relatório de gestão e contas anuais | Apreciados em 3 meses após o fim do exercício; 5 meses com contas consolidadas ou equivalência patrimonial (CSC art. 65.º, n.º 5) | Interno (assembleia geral) |
| RCBE: declaração inicial | 30 dias após o registo de constituição (RJRCBE art. 12.º, n.º 1) | IRN |
| RCBE: atualização | Até 30 dias após o facto que altera a informação (art. 14.º, n.º 1) | IRN |
| RCBE: confirmação anual | Até 31 de dezembro; pode ser feita com a IES; dispensada se houve atualização no mesmo ano (art. 15.º) | IRN |
| Contribuições para a Segurança Social | Ver `pt-social-contributions` | Instituto da Segurança Social |

Para os períodos de tributação diferentes do ano civil, os prazos do Modelo 22 e da IES contam do fim do período (CIRC arts. 120.º, n.º 2, e 121.º, n.º 3).

## Secção 7: Abertura de Conta Bancária

### Documentos Habitualmente Exigidos

São exigências dos bancos, não da lei societária; confirme com o banco escolhido.

- Certidão permanente (código de acesso)
- Pacto social
- NIF da empresa e de todos os gerentes/sócios
- Identificação (Cartão de Cidadão ou passaporte) dos gerentes e sócios
- Comprovativo de morada
- Declaração de início de atividade
- Declaração do beneficiário efetivo (RCBE)

### Prazos

Os bancos não têm prazo legal. Para não residentes, conte com mais documentação e mais tempo. Lembre-se do prazo de 5 dias úteis para o depósito do capital quando os sócios não optaram pela entrega até ao fim do exercício.

### Bancos Comuns

- Caixa Geral de Depósitos, Millennium BCP, Novo Banco, BPI (tradicionais)
- Revolut Business, Wise Business (digitais; confirme se emitem IBAN português)

## Secção 8: Considerações para Sócios Fundadores Estrangeiros

**Considerações para Sócios Fundadores Estrangeiros**  _(https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt19.aspx)_

| Questão | Resposta |
| --- | --- |
| Gerentes não residentes permitidos? | Sim. Precisam de NIF português |
| Representante fiscal exigido? | Residentes fora do território nacional designam representante com residência em Portugal (LGT art. 19.º, n.º 6). É facultativo para residentes na UE/EEE (n.º 8). Não é obrigatório para quem adira às notificações eletrónicas (morada única digital, regime do Portal das Finanças ou caixa postal eletrónica) (n.º 15) |
| Presença física exigida? | Empresa na Hora: presença de todos os sócios. Empresa Online: sem presença, mas todos os sócios precisam de NIF português e de autenticação e assinatura digital (Chave Móvel Digital associada ao passaporte ou eIDAS para estrangeiros) |
| Sócio sociedade estrangeira | Precisa de NIPC e NIF português, certidão do registo comercial do país da sede, pacto atualizado, ata se aplicável e declaração do beneficiário efetivo (IRN, Empresa Online) |
| Documentos estrangeiros | Documentos em língua estrangeira levam tradução (IRN) |
| NIF para estrangeiros | Obtido num serviço de Finanças ou online, com representante fiscal se residente fora da UE/EEE e sem adesão às notificações eletrónicas |
| Restrições à propriedade estrangeira | Nenhumas para a Lda comum; setores regulados podem exigir autorizações específicas e capital mínimo superior |
| Golden Visa | A autorização de residência para investimento (ARI) tem regras próprias na Lei 23/2007, art. 3.º, alteradas em 2023. Não foram relidas hoje: ver "Not yet confirmed" |

## Secção 9: Erros Comuns e Recusas

- **R-PT-F1**: Dispensar o Contabilista Certificado. "Toda a sociedade comercial tem de ter contabilidade organizada (CIRC art. 123.º, n.º 1), e a constituição pede a indicação de um Contabilista Certificado (IRN). Só um Contabilista Certificado inscrito na Ordem pode assumir a responsabilidade técnica pela contabilidade de uma entidade com contabilidade organizada e assinar as suas demonstrações financeiras e declarações fiscais (Estatuto da OCC, art. 10.º, n.º 1, alínea b)). Não é opcional."
- **R-PT-F2**: Não depositar o capital a tempo. "Na Empresa na Hora e na Empresa Online há 5 dias úteis para depositar o capital, salvo depósito no ato ou declaração de entrega nos cofres da sociedade até ao fim do primeiro exercício. Os sócios declaram a entrega sob sua responsabilidade (CSC art. 202.º, n.os 4 e 6)."
- **R-PT-F3**: Não residente sem representante fiscal. "Os residentes fora da UE/EEE têm de designar um representante fiscal em Portugal, salvo se aderirem às notificações eletrónicas (LGT art. 19.º, n.os 6, 8 e 15). Sem NIF não é possível constituir a sociedade online."  _(https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt19.aspx)_
- **R-PT-F4**: Sociedade veículo para Golden Visa. "A mera constituição da empresa não confere autorização de residência para investimento. Os requisitos estão na Lei 23/2007 e foram alterados em 2023. Não aconselhe a constituição como via para obtenção de visto sem aconselhamento especializado em imigração."
- **R-PT-F5**: Incumprimento do RCBE. "Enquanto a declaração e a confirmação do RCBE não estiverem cumpridas, a sociedade não pode distribuir lucros nem adiantamentos sobre lucros, contratar com o Estado e outras entidades públicas, nem concorrer a concessões de serviços públicos (RJRCBE art. 37.º, n.º 1). A falta de registo atualizado do beneficiário efetivo é contraordenação com coima de €1.000 a €50.000 (Lei 89/2017 art. 6.º, n.º 1)."
- **R-PT-F6**: Segunda unipessoal. "Uma pessoa singular só pode ser sócia de uma sociedade unipessoal por quotas. Uma segunda unipessoal do mesmo sócio pode ser dissolvida por via administrativa a pedido de qualquer interessado (CSC art. 270.º-C)."
- **R-PT-F7**: Entradas em espécie sem ROC. "Qualquer entrada em bens diferentes de dinheiro precisa de relatório de um ROC sem interesses na sociedade, qualquer que seja o valor (CSC art. 28.º, n.º 1). A Empresa Online não aceita entradas em espécie."
- **R-PT-F8**: Distribuir todo o lucro com capital de €1. "Numa Lda, 5% do lucro vai para a reserva legal até 20% do capital e nunca abaixo de €2.500 (CSC arts. 218.º e 295.º). Com capital mínimo, a reserva legal tem de chegar a €2.500 antes de deixar de reter lucros."

## Secção 10: Cronograma

**Cronograma (prazos legais; durações práticas variam)**

| Etapa | Prazo | Fonte |
| --- | --- | --- |
| Obter NIF (se sócio estrangeiro) | Sem prazo legal; antes da constituição | LGT art. 19.º |
| Certificado de admissibilidade (se não usar a Bolsa de Firmas) | Válido 3 meses | gov.pt |
| Empresa na Hora | No próprio dia, num único balcão | IRN |
| Empresa Online | Pagamento em 48 horas; correções em 5 dias seguidos | IRN |
| Depósito de capital no banco | 5 dias úteis (ou até ao fim do 1.º exercício, se declarado) | IRN; CSC art. 202.º |
| Declaração de início de atividade | Antes de iniciar a atividade (IVA); 15 dias após a Empresa na Hora se o CC não foi indicado no balcão | CIVA art. 31.º; IRN |
| Inscrição em IRC | 15 dias a partir da apresentação a registo comercial | CIRC art. 118.º, n.º 1 |
| Caixa postal eletrónica | 30 dias a contar do início de atividade | LGT art. 19.º, n.º 12 |
| Entrega do RCBE | 30 dias após o registo | RJRCBE art. 12.º |
| **Pronta para operar** | Residentes via Empresa na Hora: a sociedade fica constituída no próprio dia | IRN |

## Sources

| Source | URL | Read on |
|---|---|---|
| IRN, Criar Empresa na Hora (fees, documents, 5 working days, 30-day RCBE, 15-day início de atividade) | https://justica.gov.pt/Servicos/Empresa-na-Hora | 2026-10-30 |
| IRN, Criar Empresa Online (Empresa 2.0: fees normal and urgent, EUR 30 correction, exclusions) | https://justica.gov.pt/Servicos/Empresa-Online | 2026-10-30 |
| IRN, Capital social (minimum quota EUR 1, SA EUR 50,000 and 30%, deposit options) | https://justica.gov.pt/Como-criar-uma-empresa-online/Capital-social | 2026-10-30 |
| gov.pt, Pedir o certificado de admissibilidade de firma ou denominação (validity three months) | https://www.gov.pt/servicos/pedir-o-certificado-de-admissibilidade-de-firma-ou-denominacao | 2026-10-30 |
| Código das Sociedades Comerciais, consolidated (arts. 7, 28, 65, 201, 202, 218, 219, 262, 270-A, 270-C, 273, 276, 277, 295, 413, 414, 488) | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/1986-34443975 | 2026-10-30 |
| Regulamento Emolumentar dos Registos e Notariado (DL 322-A/2001), consolidated (arts. 22, 23, 27) | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2001-34475775 | 2026-10-30 |
| Lei 89/2017 and Regime Jurídico do RCBE, consolidated (Lei art. 6; RJRCBE arts. 12, 14, 15, 37) | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2017-108031925 | 2026-10-30 |
| CIRC art. 87, IRC rates 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-30 |
| CIRC art. 118, declaração de inscrição | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc118.aspx | 2026-10-30 |
| CIRC art. 120, Modelo 22 by the last day of May | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc120.aspx | 2026-10-30 |
| CIRC art. 121, IES by 15 July | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121.aspx | 2026-10-30 |
| CIRC art. 123, contabilidade organizada, 90-day limit | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc123.aspx | 2026-10-30 |
| CIVA art. 31, declaração de início de atividade | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva31.aspx | 2026-10-30 |
| CIVA art. 41, monthly or quarterly returns (EUR 650,000) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva41.aspx | 2026-10-30 |
| LGT art. 19, tax representative and electronic mailbox | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt19.aspx | 2026-10-30 |
| Estatuto da Ordem dos Contabilistas Certificados (DL 452/99 as amended, OCC consolidated text in force from 1 March 2024), art. 10(1)(b), acts reserved to Contabilistas Certificados | https://www.occ.pt/sites/default/files/public/2024-09/Estatuto_2024.pdf | 2026-10-30 |

Not yet confirmed: whether the IRN's EUR 200 "pedido com marca associada" at Empresa na Hora is charged on top of the EUR 360 or replaces it (the IRN page lists both without saying; the RERN has no trade-mark fee); whether a power of attorney (procuração) is accepted instead of personal presence at Empresa na Hora, and for the online and traditional routes (the old file said yes for those two); whether foreign documents need an apostille and a certified translation (the IRN pages ask only for a translation); the old claim that a late capital deposit makes the managers personally liable; the Golden Visa (ARI) investment routes and amounts after the 2023 reform (Lei 23/2007 art. 3, not re-read); the old practical estimates, which have no official source: Empresa Online processing in 5 to 10 working days, traditional route in 1 to 3 weeks and EUR 500 to 1,500 for notary and registration, Contabilista Certificado fees of EUR 1,200 to 3,600 a year, "EUR 1,000 or more" of capital in practice, bank account opening in 1 to 5 days (1 to 3 weeks for non-residents), and NIF in 1 to 10 days.

## Aviso Legal

Esta skill e os seus resultados são fornecidos apenas para fins informativos e de cálculo e não constituem aconselhamento jurídico, fiscal ou financeiro. A Open Accountants e os seus contribuidores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado antes de qualquer atuação.

A versão mais atualizada desta skill encontra-se em [openaccountants.com](https://openaccountants.com).

> Contributed by Ryan Duguid.

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
