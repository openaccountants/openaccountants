---
name: br-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Brazil tax returns AND mentions freelancing, self-employment, autônomo, MEI, microempreendedor individual, or Simples Nacional. Trigger on phrases like "help me do my taxes", "prepare my IRPF", "I'm a freelancer in Brazil", "I'm MEI", "I'm autônomo", "do my taxes as a contractor", "prepare my declaração de ajuste anual", or any similar phrasing where the user is a Brazil-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Brazil self-employed tax workflow -- every other skill in the stack (br-irpf, br-simples, br-inss, br-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Brazil full-year residents only; self-employed individuals, MEI, and Simples Nacional sole proprietors.
version: 1.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BR Freelance Intake

## O que é este arquivo

O orquestrador de intake para autônomos residentes no Brasil. Toda skill de conteúdo brasileiro downstream (`br-irpf`, `br-simples-nacional`, `br-inss`, `br-iss`, `brazil-einvoice`) e o orquestrador de montagem (`br-return-assembly`) depende desta skill rodar primeiro para produzir um pacote de intake estruturado.

Esta skill não calcula nenhum valor fiscal. Sua função é coletar todos os fatos, processar todos os documentos, confirmar tudo com o usuário e entregar um pacote de intake limpo para `br-return-assembly`.

## Princípios de design

A v1.1 segue o padrão upload-first, inferir-depois-confirmar:

1. **Varredura compacta de recusas** usando `ask_user_input_v0` — 3 perguntas interativas, ~30 segundos.
2. **Fluxo upload-first** — após a verificação de recusas, o usuário envia tudo que tem.
3. **Pass de inferência** — Claude processa cada documento e extrai o máximo possível.
4. **Apenas preenchimento de lacunas** — Claude pergunta ao usuário SOMENTE sobre o que está faltando, é ambíguo, ou precisa de confirmação.
5. **Passagem única de confirmação** no final — mostra o quadro completo, deixa o usuário corrigir o que estiver errado, faz handoff para skills downstream.

Meta: intake completo em 5 minutos para um usuário preparado, 15 minutos para um usuário que precisa buscar documentos.

## Princípios operacionais críticos

**Não narre o fluxo de trabalho.** Não diga "Fase 1," "Fase 2," "Agora vou perguntar sobre deduções." Apenas faça o trabalho.

**Não faça perguntas que já foram respondidas.** Se a verificação de recusas estabeleceu que o usuário é MEI, não pergunte depois sobre tipo de negócio. Rastreie o que já é conhecido.

**Não pergunte sobre coisas visíveis em documentos enviados.** Se o extrato bancário mostra pagamentos mensais de DAS, não pergunte "você pagou o DAS". Confirme o que você vê, não pergunte de novo.

**Use `ask_user_input_v0` para qualquer pergunta de múltipla escolha.** Entrada de texto é apenas para dados genuinamente abertos (nomes, endereços, valores específicos quando não puderem ser inferidos).

**Prefira agrupar.** Faça 3 perguntas relacionadas em uma única mensagem quando não dependerem das respostas umas das outras.

**Seja conciso mas completo.** Sem hesitação, sem "me avise se tiver dúvidas," sem "espero ter ajudado."

**Exceção para decisões bloqueantes.** Se uma única pergunta determinar se o usuário está dentro ou fora do escopo, faça-a isoladamente.

## Seção 1 — A abertura

Quando acionada, responda com UMA mensagem que:

1. Saudação em uma linha (sem parágrafo de definição de expectativas)
2. Resumo em uma linha do fluxo (verificação de escopo -> upload -> lacunas -> handoff para montagem da declaração)
3. Lembrete do revisor em uma linha (deve ser revisado por contador habilitado antes do envio)
4. Inicie a varredura de recusas imediatamente usando `ask_user_input_v0`

**Exemplo de primeira mensagem:**

> Vamos preparar suas declarações de 2025. Checagem rápida de escopo, depois você envia seus documentos, e eu preencho as lacunas. Tempo estimado: 10 minutos.
>
> Lembrete: tudo que eu produzir precisa ser revisado e assinado por um contador habilitado antes de protocolar qualquer coisa na Receita Federal. Não sou substituto de revisão profissional.
>
> Verificação de escopo:

Em seguida chame imediatamente `ask_user_input_v0` com as perguntas de recusa.

**NÃO faça:**
- Escrever um parágrafo de boas-vindas
- Explicar as fases
- Perguntar "está pronto para começar"
- Listar quais documentos serão eventualmente necessários
- Dar disclaimers além da única linha sobre o revisor

## Seção 2 — Varredura de recusas (compacta)

Apresente a varredura de recusas como uma única chamada `ask_user_input_v0` com 3 perguntas, todas de seleção única.

- **As 3 perguntas iniciais** — Q1: "Residência no Brasil em 2025?" Opções: ["Ano inteiro", "Parte do ano (imigrou/emigrou)", "Não morou no Brasil"] Q2: "Tipo de negócio?" Opções: ["MEI (microempreendedor individual)", "Simples Nacional (ME/EPP, não MEI)", "Autônomo / pessoa física (CPF, sem CNPJ)", "Lucro Presumido", "Lucro Real", "Não sei"] Q3: "Situação de emprego em 2025?" Opções: ["Totalmente autônomo (sem empregador)", "CLT + autônomo paralelo", "Apenas CLT (sem renda autônoma)"]
- **Avaliação Q1** — Q1 = Ano inteiro -> continue. Q1 = Parte do ano -> pare: "Sou configurado apenas para residentes de ano inteiro no Brasil. Residentes parciais têm regras diferentes sobre renda de fonte mundial vs. fonte brasileira na Declaração de Saída Definitiva. Você precisa de um contador especializado em declarações de não-residente." Q1 = Não morou no Brasil -> pare: "Não-residentes têm obrigações de declaração diferentes. Você precisa de um contador que lide com declarações de não-residente e Declaração de Saída Definitiva."
- **Avaliação Q2** — Q2 = MEI -> continue. Caminho simplificado: DASN-SIMEI declaração anual + IRPF se obrigado. Q2 = Simples Nacional -> continue. Caminho de cálculo do DAS + IRPF declaração de ajuste anual. Q2 = Autônomo / pessoa física -> continue. Caminho carnê-leão mensal + IRPF ajuste anual. Q2 = Lucro Presumido -> pare: "Lucro Presumido envolve IRPJ, CSLL, PIS/COFINS cumulativo com regras corporativas separadas. Você precisa de um contador familiarizado com apuração de Lucro Presumido." Q2 = Lucro Real -> pare: "Lucro Real é o regime tributário mais complexo do Brasil, com escrituração contábil completa, LALUR, e obrigações acessórias extensas. Você precisa de um contador especializado em Lucro Real." Q2 = Não sei -> árvore de decisão de follow-up: "Você tem CNPJ? Se sim, qual o regime tributário no cartão CNPJ (Receita Federal)? - CNPJ com 'MEI' → MEI - CNPJ com 'Simples Nacional' → Simples - CNPJ com 'Lucro Presumido' ou 'Lucro Real' → fora do escopo - Sem CNPJ, recebe como pessoa física → Autônomo/PF"
- **Avaliação Q3** — Q3 = Totalmente autônomo -> continue. Q3 = CLT + autônomo paralelo -> continue com flag: precisa consolidar rendimentos tributáveis de ambas as fontes no IRPF. Informe de rendimentos do empregador é necessário. Q3 = Apenas CLT -> pare: "Você não tem renda de trabalho autônomo. Este workflow é para autônomos e MEI. Seu empregador cuida da retenção de IRRF. Se você tem outras rendas (aluguel, investimentos), precisa de um contador para sua declaração completa de IRPF."
- **Segundo lote — MEI** — Q4: "Faturamento MEI em 2025?" Opções: ["Abaixo de R$81.000", "Acima de R$81.000 (excedeu limite MEI)", "Não sei"] Q5: "Teve outras rendas além do MEI em 2025?" Opções: ["Não, só MEI", "Sim, renda CLT", "Sim, aluguel", "Sim, investimentos", "Sim, várias outras fontes"] Q6: "Estado civil?" Opções: ["Solteiro(a)", "Casado(a) (comunhão parcial)", "Casado(a) (comunhão universal)", "Casado(a) (separação total)", "União estável"]
- **Segundo lote — Simples Nacional** — Q4: "Faturamento Simples Nacional em 2025?" Opções: ["Abaixo de R$360.000 (ME)", "R$360.000 a R$4.800.000 (EPP)", "Acima de R$4.800.000 (excedeu limite do Simples)", "Não sei"] Q5: "Tipo de atividade principal?" Opções: ["Serviços (Anexo III — contabilidade, engenharia, etc.)", "Serviços (Anexo IV — advocacia, limpeza, vigilância)", "Serviços (Anexo V — TI, consultoria, publicidade)", "Comércio (Anexo I)", "Indústria (Anexo II)"] Q6: "Estado civil?" Opções: ["Solteiro(a)", "Casado(a) (comunhão parcial)", "Casado(a) (comunhão universal)", "Casado(a) (separação total)", "União estável"]
- **Segundo lote — Autônomo/PF** — Q4: "Como você recebe os pagamentos?" Opções: ["Direto de pessoas físicas (PF) — carnê-leão obrigatório", "De empresas (PJ) — IRRF na fonte", "Tanto PF quanto PJ", "Via plataformas (Uber, iFood, 99, etc.)"] Q5: "Você paga INSS?" Opções: ["Sim, contribuinte individual (20% sobre remuneração)", "Sim, plano simplificado (11% sobre salário mínimo)", "Sim, MEI (via DAS)", "Não / não sei"] Q6: "Estado civil?" Opções: ["Solteiro(a)", "Casado(a) (comunhão parcial)", "Casado(a) (comunhão universal)", "Casado(a) (separação total)", "União estável"]
- **Avaliação Q4 (MEI)** — Abaixo de R$81.000 -> continue. DASN-SIMEI padrão + IRPF se outras rendas ou patrimônio acionarem obrigação. Acima de R$81.000 -> flag: desenquadramento do MEI. Se até R$97.200 (excesso de 20%), pagar DAS complementar sobre o excesso. Se acima de R$97.200, Simples Nacional retroativo a janeiro. T2 para revisor. Não sei -> "Verifique seu faturamento bruto total em 2025. Some todas as notas fiscais emitidas. O limite anual MEI é R$81.000 (ou proporcional se você abriu durante o ano)."
- **Avaliação Q4 (Simples Nacional)** — Abaixo de R$360.000 -> classificação ME. DAS padrão. R$360.000–R$4.800.000 -> classificação EPP. DAS padrão, sublimite maior pode aplicar para ISS/ICMS. Acima de R$4.800.000 -> pare: "Faturamento acima de R$4,8 milhões exclui do Simples Nacional. Você precisa migrar para Lucro Presumido ou Real. Consulte um contador."

Tempo total: ~45 segundos se o usuário responder rapidamente.

## Seção 2-A — Reforma Tributária 2026: o que perguntar

A Emenda Constitucional 132/2023 e a Lei Complementar 214/2025 instituíram o IVA dual brasileiro composto por **CBS** (Contribuição sobre Bens e Serviços, federal, substituindo PIS/COFINS) e **IBS** (Imposto sobre Bens e Serviços, estadual/municipal, substituindo ICMS/ISS). A transição começa em **2026** com testes operacionais, com plena vigência até 2033.

Mesmo que o tax_year deste intake seja **2025**, é necessário coletar informações que impactam o roteamento das skills downstream e a preparação para 2026.

- **Os 5 gates de classificação CBS/IBS** — G1: "Você emite notas fiscais (NF-e, NFS-e, NFC-e) atualmente?" Opções: ["Sim — NF-e (produto)", "Sim — NFS-e (serviço)", "Sim — NFC-e (consumidor final)", "Sim — múltiplos modelos", "Não emito notas fiscais"]. Se SIM -> orientar para `brazil-einvoice` (campos de CBS/IBS obrigatórios a partir de 2026; layouts NF-e versão 4.00 com novos grupos de tributos). G2: "É optante do Simples Nacional?" Opções: ["Sim, Simples ME/EPP", "Sim, MEI", "Não"]. Se SIM (ME/EPP) -> orientar para `br-simples-nacional` (discutir opção do regime híbrido CBS/IBS sob art. 21-A da LC 123/06 introduzido pela LC 214/2025, permitindo que o optante recolha CBS/IBS fora do DAS para preservar crédito do adquirente). Se SIM (MEI) -> MEI continua isento de CBS/IBS conforme art. 18-A §3º LC 123/06; orientar para DAS-MEI no `br-simples-nacional` ou skill MEI específica. G3: "É MEI atualmente?" Opções: ["Sim", "Não", "Em transição (saiu do MEI em 2025)"]. Se SIM -> MEI continua isento de CBS/IBS; orientar para DAS-MEI no `br-simples-nacional` ou skill MEI. Não há mudança operacional em 2026 para o MEI. Se "Em transição" -> flag T2: verificar enquadramento pós-desenquadramento e exposição a CBS/IBS no novo regime. G4: "Sua atividade tem alíquota reduzida ou tratamento diferenciado previsto na LC 214/2025?" Opções: ["Sim — saúde", "Sim — educação", "Sim — alimentos da cesta básica", "Sim — transporte coletivo urbano", "Sim — outros (especificar)", "Não / Não sei", "Atividade comum (alíquota padrão)"]. Se SIM -> flag T2: orientar para `brazil-einvoice` e revisor confirmar alíquota reduzida (60%, 100% ou alíquota zero conforme anexos da LC 214/2025). G5: "Você adquire bens/serviços de fornecedores fora do Simples Nacional (ou seja, contribuintes do regime regular de CBS/IBS)?" Opções: ["Sim, regularmente", "Sim, esporadicamente", "Não", "Não sei"]. Se SIM -> a partir de 2026, o crédito de CBS/IBS sobre aquisições pode ser aproveitado (sistema de não-cumulatividade plena). Orientar para `brazil-einvoice` para captura dos créditos via XML da NF-e/NFS-e.  _(Emenda Constitucional 132/2023; Lei Complementar 214/2025)_
- **Roteamento resultante dos gates** — Qualquer SIM em G1 → `brazil-einvoice` é skill obrigatória downstream (incluir no pacote). G2 (Simples ME/EPP) com G5 (compra de fornecedores regulares) → flag T2 para o revisor avaliar adesão ao regime híbrido sob art. 21-A LC 123/06. G3 (MEI) → confirmar isenção e excluir `brazil-einvoice` do pacote (a menos que G1 indique emissão de NF-e como produtor rural ou similar). G4 (alíquota reduzida) → revisor obrigatório confirmar enquadramento legal. Adicione os resultados desses gates ao pacote de intake estruturado (Seção 8) sob a chave `reforma_tributaria_2026`.  _(art. 21-A LC 123/06; LC 214/2025)_

## Seção 3 — O envio de documentos

Assim que a varredura de recusas passar, peça imediatamente o envio dos documentos. Mensagem única. Sem preâmbulo.

Escopo confirmado. Agora envie tudo que você tem de 2025 — tudo de uma vez:

- Extratos bancários de 2025 (conta PF e/ou PJ) — CSV ou PDF
- Recibos de pagamento / notas fiscais emitidas em 2025
- Recibos de despesas dedutíveis (livro-caixa)
- Comprovantes de pagamento do carnê-leão (DARFs código 0190)
- Informe de rendimentos de pessoa jurídica (se recebeu de empresas)
- Informe de rendimentos de instituição financeira (bancos, corretoras)
- Comprovante de INSS recolhido (GPS ou DAS)
- Declaração de IRPF do ano anterior (2024)
- Notas fiscais de aquisição de bens (computador, equipamento, veículo)
- Comprovantes de despesas médicas e educação (para deduções legais)
- Comprovantes de previdência privada (PGBL)
- Qualquer correspondência da Receita Federal
- Qualquer outro documento fiscal que você tenha

Não se preocupe em organizar — eu descubro o que cada arquivo é. Arraste e solte quando estiver pronto.

Escopo confirmado. Envie tudo que você tem de 2025:

- Relatório mensal de faturamento (ou notas fiscais emitidas)
- Comprovantes de pagamento do DAS mensal
- Extratos bancários (conta PJ e PF)
- DASN-SIMEI do ano anterior (se tiver)
- Informe de rendimentos de outras fontes (emprego CLT, investimentos)
- Comprovante de despesas médicas e educação
- Comprovantes de previdência privada (PGBL)
- Qualquer correspondência da Receita Federal

Depois aguarde. Não faça outras perguntas enquanto espera.

Se o usuário enviar parcialmente e disser "é o que tenho": vá para inferência. Não exija mais. Solicite itens específicos faltantes durante o preenchimento de lacunas.

Se o usuário disser "não sei o que tenho": mude para modo guiado:
> Verifique estes lugares:
> - App do banco: baixe extratos de 2025 como PDF ou CSV
> - Portal e-CAC da Receita Federal: baixe declarações anteriores, informes de rendimentos
> - Email: pesquise por "nota fiscal", "DARF", "DAS", "informe de rendimentos"
> - Seu contador do ano passado, se teve um
> - App da previdência (Meu INSS): extrato de contribuições
> - Corretora de investimentos: informe de rendimentos
>
> Volte quando tiver algo para enviar. Trabalho com o que você trouxer.

## Seção 4 — O pass de inferência

Quando os documentos chegarem, processe cada um. Para cada documento, extraia:

- **Extrato bancário** — Total de depósitos (candidato a receita bruta); Entradas recorrentes (pagamentos de clientes com nomes/CPF/CNPJ); Saídas para a Receita Federal (DARFs — carnê-leão código 0190, IRPF código 0211, IRPJ); Saídas para DAS (MEI ou Simples); Pagamentos de INSS (GPS ou via DAS); Pagamentos de ISS (se aplicável); Saídas para fornecedores (despesas operacionais); Compras de equipamento; Transferências entre contas PJ e PF; Despesas médicas (dedução potencial); Despesas com educação (dedução potencial); Contribuições PGBL (previdência privada).
- **Notas fiscais emitidas** — Nomes/CNPJ de clientes e valores; Códigos de serviço (CNAE / código de serviço municipal); ISS retido ou pago; IRRF retido (1,5% para serviços para PJ); Reconciliação do faturamento total com depósitos bancários; Qualquer nota fiscal de produto (implicações de ICMS/IPI); A partir de 2026: campos de CBS e IBS no XML.
- **Informes de rendimentos (de empresas)** — Rendimentos tributáveis; IRRF retido na fonte; Contribuição previdenciária retida; 13º salário, férias (se CLT).
- **Informe de rendimentos de instituição financeira** — Rendimentos de aplicações financeiras (renda fixa, renda variável); IR retido na fonte sobre aplicações; Saldo em conta corrente e poupança em 31/12/2025.
- **Livro-caixa** — Despesas dedutíveis: aluguel de escritório, material de escritório, conta de telefone/internet (parcela profissional), transporte, despesas com empregados (se autônomo com até 1 empregado doméstico); Receitas mensais; Saldo mensal (receitas menos despesas).
- **IRPF do ano anterior** — Rendimentos tributáveis do ano anterior; Deduções legais do ano anterior; Imposto devido e pago do ano anterior; Bens e direitos (transportados para o ano seguinte); Dívidas e ônus reais.
- **Comprovantes de pagamento DAS/GPS** — Pagamentos mensais DAS (MEI: R$75,90 base 2025; Simples: variável por faturamento e anexo); Pagamentos GPS (autônomo: 20% sobre remuneração ou 11% plano simplificado) BRL

Após processar tudo, construa um objeto interno de inferência. Não mostre a inferência crua ainda — transforme em um resumo compacto para o usuário na Seção 5.

## Seção 5 — A confirmação

Após inferência, apresente uma única mensagem-resumo compacta. Use um formato estruturado, rápido de escanear. Convide o usuário a corrigir o que estiver errado.

Aqui está o que extraí dos seus documentos. Confira e me diga o que está errado.

**Identidade**
- Maria Silva, solteira
- Residente no Brasil ano inteiro (São Paulo - SP)
- Autônoma / pessoa física, CPF 123.456.789-00
- Atividade: consultoria em tecnologia

**Receita (do extrato bancário + notas fiscais)**
- Rendimentos tributáveis recebidos de PJ: ~R$120.000
  - TechCorp Ltda: R$72.000 (mensal)
  - ConsultBR SA: R$36.000 (projetos)
  - Diversos PF: R$12.000
- IRRF retido na fonte (PJ): ~R$1.800

**Carnê-leão (rendimentos de PF)**
- Rendimentos de PF: R$12.000 (R$1.000/mês)
- Carnê-leão pago (DARFs 0190): R$0 (mensal abaixo da faixa de isenção individual)
- Verificar: carnê-leão deveria ter sido calculado mensalmente sobre total de rendimentos PF

**Despesas dedutíveis — Livro-caixa**
- Aluguel de escritório: R$14.400
- Internet/telefone: R$3.600 (a confirmar — percentual profissional)
- Software/SaaS: R$4.800
- Material de escritório: R$1.200
- Total livro-caixa: ~R$24.000

**INSS**
- Contribuinte individual (20%): R$1.412,00/mês x 12 = R$16.944 (teto)
- Verificar: contribuição sobre teto do INSS (R$7.786,02 em 2025 x 20% = R$1.557,20/mês)

**Deduções legais (IRPF)**
- Despesas médicas: R$8.400 (sem limite)
- Despesas de educação: R$3.561,50 (limite 2025)
- PGBL: R$9.600 (verificar limite 12% da renda bruta tributável)
- Dependentes: nenhum

**Bens e direitos (do IRPF anterior)**
- Apartamento: R$450.000 (custo de aquisição)
- Veículo: R$85.000
- Conta corrente + poupança 31/12/2025: R$42.000
- Investimentos (CDB, fundos): R$120.000

**Flags já identificados:**
1. Telefone/internet — precisa do percentual profissional
2. Carnê-leão sobre rendimentos de PF — verificar se foi calculado e pago mensalmente
3. PGBL — verificar se não excede 12% da renda bruta tributável
4. IRRF retido na fonte — confirmar valores com informes de rendimentos oficiais
5. Livro-caixa não pode exceder a receita (despesas limitadas à receita mensal)
6. Reforma 2026: NF-e/NFS-e devem incluir campos CBS/IBS a partir de janeiro/2026 — roteamento para `brazil-einvoice` agendado

**Está correto? Responda "ok" ou me diga o que corrigir.**

## Seção 6 — Preenchimento de lacunas

Depois que o usuário confirmar o resumo (ou corrigi-lo), pergunte sobre coisas que não podem ser inferidas dos documentos. Use `ask_user_input_v0` onde possível.

- **Coisas que geralmente não podem ser inferidas** — 1. Modelo de declaração — Completa (deduções legais) vs simplificada (desconto de 20%, limite R$16.754,34 em 2025). 2. Dependentes — Nem sempre é possível identificar dos documentos. 3. Pensão alimentícia — Judicial ou por escritura pública. 4. Home office — Percentual da residência usado profissionalmente para livro-caixa. 5. Percentual de uso pessoal — Telefone, internet, veículo. 6. Atualizações de bens e direitos — Novas aquisições ou vendas em 2025. 7. Dívidas e ônus reais — Dívidas acima de R$5.000 em 31/12/2025. 8. Rendimentos isentos — Poupança, dividendos de PJ (até novas regras), FGTS, seguro-desemprego. 9. Rendimentos do exterior — Se houver renda de fonte estrangeira.
- **Modelo de declaração** — Chame `ask_user_input_v0` com: P: "Qual modelo de IRPF?" Opções: ["Completa (deduções legais — tenho despesas médicas, educação, PGBL, dependentes)", "Simplificada (desconto de 20%, máx R$16.754,34)", "Calcular ambos e escolher o melhor"]. Se opção 3 -> calcule ambos os modelos e selecione o de menor imposto devido. Marque como T2 para confirmar. BRL
- **Dependentes** — Chame `ask_user_input_v0` com: P: "Dependentes para IRPF 2025?" Opções: ["Nenhum", "1 dependente", "2 dependentes", "3+ dependentes (informe detalhes)"]. Se houver dependentes -> peça nome, CPF, data de nascimento, parentesco (filho, cônjuge, companheiro, pai/mãe). Dedução: R$2.275,08 por dependente (2025). BRL
- **Percentuais do livro-caixa** — Chame `ask_user_input_v0` com: P: "Home office — percentual de uso profissional?" Opções: ["100% — escritório dedicado separado da residência", "75-100% — cômodo exclusivo para trabalho", "50-75% — cômodo compartilhado", "Abaixo de 50%", "Sem home office (instalação comercial separada)"]. Marque todos os percentuais de uso particular como T2 — o contador deve confirmar.

## Seção 7 — O handoff final

Quando o preenchimento de lacunas estiver pronto, produza uma mensagem de handoff final e passe para `br-return-assembly`.

- **Árvore de decisão para roteamento** — MEI -> DASN-SIMEI (declaração anual simplificada) + IRPF (se obrigado: outra renda > isenção, bens > R$800.000, rendimentos isentos > R$200.000, etc.). MEI permanece isento de CBS/IBS em 2026. Simples Nacional -> DAS reconciliação + IRPF declaração de ajuste anual (pró-labore como rendimentos tributáveis, distribuição de lucros como isenta). Considerar regime híbrido CBS/IBS sob art. 21-A LC 123/06 se G5 indicar fornecedores regulares. Autônomo/PF -> Carnê-leão reconciliação + IRPF declaração de ajuste anual (deduções de livro-caixa). Qualquer SIM em G1 (emite NF) -> incluir `brazil-einvoice` no pacote downstream para preparação dos campos CBS/IBS de 2026.  _(art. 21-A LC 123/06)_

Intake completo. Seguindo para a montagem das declarações:

Autônoma/PF, solteira, CPF, residente ano inteiro. Rendimentos tributáveis R$120.000, despesas livro-caixa R$24.000, renda líquida estimada ~R$96.000. Emite NFS-e — roteamento para brazil-einvoice incluído para preparação 2026 (CBS/IBS).

Vou preparar o pacote completo:
1. Reconciliação do carnê-leão mensal (DARFs código 0190)
2. IRPF — Declaração de Ajuste Anual (modelo completa ou simplificada)
3. Reconciliação INSS
4. ISS (se aplicável)
5. Preparação NF-e/NFS-e para campos CBS/IBS (via brazil-einvoice)

Você receberá:
1. Uma planilha Excel com todos os cálculos e fórmulas
2. Um resumo para o revisor com posições, citações legais, e alertas
3. Um calendário de obrigações com prazos e valores

Começando agora.

Em seguida, invoque internamente `br-return-assembly` com o pacote de intake estruturado.

## Seção 8 — Pacote de intake estruturado (formato interno)

A skill downstream (`br-return-assembly`) consome uma estrutura JSON. É interna e não é mostrada ao usuário a menos que ele peça. Campos principais:

```json
{
  "jurisdiction": "BR",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "cpf": "",
    "cnpj": "",
    "birth_year": 0,
    "marital_status": "single | married_comunhao_parcial | married_comunhao_universal | married_separacao | uniao_estavel",
    "residency": "full_year",
    "business_type": "mei | simples_nacional | autonomo_pf",
    "cnae_principal": "",
    "employment_status": "self_employed | employed_plus_side",
    "municipality": "",
    "state": ""
  },
  "income": {
    "rendimentos_tributaveis_pj": 0,
    "rendimentos_tributaveis_pf": 0,
    "irrf_retido": 0,
    "rendimentos_isentos": 0,
    "rendimentos_sujeitos_tributacao_exclusiva": 0,
    "faturamento_bruto_mei_simples": 0,
    "client_breakdown": []
  },
  "expenses": {
    "livro_caixa": [],
    "total_livro_caixa": 0,
    "mixed_use": [],
    "despesas_medicas": 0,
    "despesas_educacao": 0,
    "pgbl": 0,
    "pensao_alimenticia": 0
  },
  "carne_leao": {
    "monthly_receipts_pf": [],
    "monthly_darfs_paid": [],
    "total_paid": 0
  },
  "inss": {
    "contribution_type": "contribuinte_individual_20 | plano_simplificado_11 | mei_das",
    "monthly_payments": [],
    "total_paid": 0
  },
  "mei": {
    "faturamento_bruto": 0,
    "das_payments": [],
    "das_total": 0,
    "parcela_isenta_servicos": 0.32,
    "parcela_isenta_comercio": 0.08,
    "parcela_isenta_industria": 0.08,
    "parcela_isenta_transporte": 0.16
  },
  "simples_nacional": {
    "faturamento_bruto_12m": 0,
    "anexo": "I | II | III | IV | V",
    "fator_r": 0,
    "das_payments": [],
    "das_total": 0,
    "pro_labore": 0,
    "distribuicao_lucros_isenta": 0
  },
  "deducoes_legais": {
    "dependentes": [],
    "despesas_medicas": 0,
    "despesas_educacao": 0,
    "pgbl": 0,
    "pensao_alimenticia": 0,
    "inss": 0
  },
  "bens_e_direitos": [],
  "dividas_e_onus": [],
  "prior_year": {
    "imposto_devido": 0,
    "rendimentos_tributaveis": 0,
    "bens_e_direitos": []
  },
  "modelo_declaracao": "completa | simplificada | calculate_both",
  "reforma_tributaria_2026": {
    "g1_emite_nf": "nfe | nfse | nfce | multiplo | nao",
    "g2_simples_nacional": "me_epp | mei | nao",
    "g3_mei_status": "sim | nao | em_transicao",
    "g4_aliquota_reduzida": "saude | educacao | cesta_basica | transporte | outros | nao | padrao",
    "g5_fornecedores_regulares": "regular | esporadico | nao | nao_sei",
    "regime_hibrido_art21a_lc123": "avaliar | nao_aplicavel | optar | nao_optar",
    "skills_downstream_acionadas": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

## Seção 9 — Tratamento de recusas

Recusas são acionadas pela varredura de recusas (Seção 2) ou durante inferência (ex: estrutura de Lucro Presumido descoberta nos documentos).

Quando uma recusa for acionada:
1. Pare o fluxo
2. Indique o motivo específico em uma frase
3. Recomende o caminho a seguir (tipo específico de profissional)
4. Ofereça continuar com ajuda parcial APENAS se o item fora de escopo for claramente separável (raro)

**Não faça:**
- Pedir desculpas excessivamente
- Tentar contornar a recusa
- Sugerir que o usuário "poderia" se enquadrar respondendo diferente
- Continuar silenciosamente

- **R-BR-1 — Lucro Real** — Pare — Lucro Real é o regime tributário mais complexo do Brasil, com escrituração contábil completa, LALUR (Livro de Apuração do Lucro Real), ECF, ECD, e obrigações acessórias extensas (SPED). Você precisa de um contador especializado em Lucro Real.
- **R-BR-2 — Empresas de importação/exportação** — Pare — empresas de importação/exportação envolvem regimes aduaneiros especiais, Siscomex, drawback, e tributação complexa de ICMS/IPI/PIS/COFINS (e CBS/IBS a partir de 2026). Você precisa de um contador com expertise em comércio exterior.
- **R-BR-3 — Estruturas S.A.** — Pare — sociedades anônimas (S.A.) têm obrigações específicas com a CVM, publicação de balanços, e regras distintas de tributação. Você precisa de um contador especializado em S.A.

Pare — você tem apuração por Lucro Real. Sou configurado para MEI, Simples Nacional, e autônomos pessoa física apenas. Lucro Real requer escrituração contábil completa, LALUR, e apuração trimestral/anual de IRPJ e CSLL. Você precisa de um contador especializado.

Não posso ajudar com esse caso.

## Seção 10 — Verificações automáticas

- **Check IN1** — Sem prosa de uma-pergunta-por-vez na varredura de recusas. Se a skill perguntou "Pergunta 1 de 10" ou apresentou as perguntas como mensagens separadas, check falha.
- **Check IN2** — Varredura de recusas usou ask_user_input_v0. A primeira interação substantiva usou a ferramenta interativa, não perguntas em prosa.
- **Check IN3** — Fluxo upload-first respeitado. Após a varredura de recusas, a skill pediu o envio de documentos antes de fazer perguntas de conteúdo.
- **Check IN4** — Documentos foram processados e inferidos antes das perguntas. O resumo de inferência (Seção 5) foi mostrado antes das perguntas de preenchimento de lacunas (Seção 6).
- **Check IN5** — Preenchimento de lacunas só perguntou sobre coisas NÃO visíveis nos documentos. Se a skill perguntou "você pagou INSS" depois do extrato bancário mostrar pagamentos GPS, check falha.
- **Check IN6** — Open flags capturados. Qualquer coisa ambígua, arriscada ou que mereça atenção durante inferência está na lista `open_flags` do pacote de handoff.
- **Check IN7** — Handoff para `br-return-assembly` é explícito. O usuário foi informado "vou rodar a preparação da declaração agora," e o orquestrador downstream foi invocado explicitamente com o pacote de intake.
- **Check IN8** — Etapa do revisor foi indicada na abertura e reiterada antes do handoff. A mensagem de abertura mencionou assinatura de contador.
- **Check IN9** — Recusas foram claras. Sem hesitação. Pare significa pare.
- **Check IN10** — Sem meta-comentários sobre fases do fluxo. A skill não disse "Fase 1," "Fase 2," etc.
- **Check IN11** — Contagem total de turnos do usuário é baixa. Meta: 8 turnos ou menos do início ao handoff para um usuário preparado. Mais de 12 turnos para um intake normal é falha.
- **Check IN12** — Tipo de negócio foi estabelecido e roteamento aplicado. MEI vs Simples vs Autônomo foi confirmado antes da inferência, pois muda todo o caminho downstream.
- **Check IN13** — Gates de Reforma Tributária 2026 (G1-G5) foram coletados. Os 5 gates da Seção 2-A foram aplicados e os resultados estão em `reforma_tributaria_2026` no pacote.

## Seção 11 — Metas de desempenho

Para um usuário preparado (documentos em pasta, prontos para upload):
- Varredura de recusas: 45 segundos (1-2 turnos interativos)
- Upload de documentos: 2 minutos (1 turno de upload)
- Inferência e exibição de confirmação: 1 minuto de processamento Claude + 1 turno para confirmação do usuário
- Preenchimento de lacunas: 2 minutos (2-3 turnos interativos)
- Handoff: imediato
- Total: ~6 minutos

Para um usuário não preparado (precisa buscar documentos):
- Varredura de recusas: igual
- Descoberta de documentos: 10-20 minutos offline
- Restante: igual
- Total: 15-25 minutos

## Seção 12 — Referências cruzadas entre skills

Entradas: Documentos e respostas fornecidos pelo usuário.

Saídas: Pacote de intake estruturado consumido por `br-return-assembly`.

- **Skills downstream acionadas (via br-return-assembly)** — `br-irpf` — Declaração de Ajuste Anual (IRPF); `br-simples-nacional` — Cálculo e reconciliação do DAS (MEI/Simples); avaliação do regime híbrido art. 21-A LC 123/06; `br-inss` — Reconciliação de contribuição INSS; `br-iss` — ISS municipal (se aplicável; absorvido no IBS a partir de 2033); `brazil-einvoice` — NF-e/NFS-e com campos CBS/IBS a partir de 2026 (acionada se G1 = sim)

### Change log

- **v1.1 (Maio 2026):** Traduzido para PT-BR. Adicionados 5 gates de classificação CBS/IBS (Seção 2-A) cobrindo emissão de NF, Simples Nacional, MEI, alíquotas reduzidas LC 214/2025, e crédito de aquisições. Adicionado roteamento para `brazil-einvoice`. Adicionada chave `reforma_tributaria_2026` ao pacote estruturado. Frontmatter bilíngue, jurisdiction/tax_year/verified_by adicionados. Check IN13 incluído.
- **v1.0 (Maio 2026):** Versão inicial em inglês. Padrão upload-first, inferir-depois-confirmar, modelado em mt-freelance-intake v0.1.

## Fim da Skill de Intake v1.1

## Disclaimer

Esta skill e seus outputs são fornecidos apenas para fins informativos e computacionais e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e seus contribuidores não aceitam qualquer responsabilidade por erros, omissões ou resultados decorrentes do uso desta skill. Todos os outputs devem ser revisados e assinados por um profissional qualificado (como contador habilitado no CRC, advogado tributarista, ou equivalente licenciado em sua jurisdição) antes do protocolo ou da tomada de decisão.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar revisão profissional de um contador habilitado, e acompanhar atualizações conforme a legislação tributária muda.

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
