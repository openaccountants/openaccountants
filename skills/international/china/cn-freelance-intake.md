---
name: cn-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help with Chinese tax compliance AND mentions freelancing, self-employment, software developer, contractor, individual industrial commercial household (个体工商户), limited liability company (有限公司), or WFOE in China. Trigger phrases (mixed Chinese + English) "中国个税年度汇算", "中国 SME 税务", "上海公司报税", "深圳 freelancer 税务", "WFOE 报税", "金税四期 合规", "个体工商户经营所得", "China tax filing", "China freelance tax", "China comprehensive income annual reconciliation", "WFOE annual return". REQUIRED entry point — downstream cn-iit, cn-corporate-tax, cn-vat, cn-fapiao-einvoice, cn-social-insurance, cn-withholding, cn-stamp-tax, cn-formation, cn-return-assembly. ALWAYS-read closer in Chinese 在开始任何中国税务工作流前必须先阅读本技能.
jurisdiction: CN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CN Freelance Intake

## 中国 — 自由职业者与中小企业税务承接 — 技能 v1.0

## 本文件用途

中国境内自由职业者、个体工商户、个人独资企业、有限责任公司（一般纳税人 / 小规模纳税人）及外商投资企业（WFOE）创始人的税务承接编排器。所有中国下游内容技能均依赖本技能先行产出结构化承接包。

工作职责：(1) 确认纳税人是否在范围内；(2) 判定税务居民身份（年度内累计 183 天或在中国境内有住所）；(3) 主体规模与税务身份分类（个体工商户 / 个独 / 有限公司一般纳税人 / 小规模纳税人 / WFOE）；(4) 识别需调用的下游技能；(5) 交付 `cn-return-assembly` 进行最终装配。最终成果面向具备资质的中国税务师（CTA）或注册会计师（CPA）复核签字 — 本技能不是最终申报责任人。

## 一、决策树速查

```
中国税务居民？（年度内累计 183 天 或 有住所） -> 否 = 拒绝
       |
主体类型？
       |
       +-- 个体工商户 / 个人独资
       |     -> cn-iit（经营所得 5 级累进 5%-35%）
       |     -> cn-vat（一般为小规模纳税人 1%/3%）
       |     -> cn-social-insurance
       |
       +-- 有限公司 — 小规模纳税人（年销售额 ≤ 500 万元）
       |     -> cn-corporate-tax（25% / 小型微利 5% / 高新技术 15%）
       |     -> cn-vat（1% 征收率）
       |     -> cn-fapiao-einvoice（数电发票）
       |     -> cn-social-insurance
       |
       +-- 有限公司 — 一般纳税人（年销售额 > 500 万元 或主动登记）
       |     -> cn-corporate-tax（25% / 5% / 15%）
       |     -> cn-vat（13% / 9% / 6% 进销项抵扣）
       |     -> cn-fapiao-einvoice（数电发票）
       |     -> cn-social-insurance
       |     -> cn-withholding（如有跨境付款）
       |
       +-- 外商投资企业（WFOE）
             -> cn-corporate-tax
             -> cn-vat
             -> cn-fapiao-einvoice
             -> cn-withholding（跨境付款代扣代缴 10%）
             -> cn-social-insurance
             -> cn-formation（设立 / 外汇登记）
```

平行路由（与主体类型无关）：

- 雇佣员工 → 调用 `cn-iit`（工资薪金代扣代缴）+ `cn-social-insurance`（五险一金）。
- 开具发票 → 调用 `cn-fapiao-einvoice`（数电发票全面铺开）。
- 跨境付款（特许权使用费 / 服务费 / 股息） → 调用 `cn-withholding`。
- 签订合同 / 设立账簿 → 调用 `cn-stamp-tax`（印花税）。
- 主体不清或拟新设 → 调用 `cn-formation`。
- 始终最后 → `cn-return-assembly`。

## 二、必备输入与拒绝清单

### 2.1 必备输入

可从文件推断或在缺口阶段补问，承接前必须全部齐备：

- **身份与登记**：法定名称（营业执照 / 身份证）、统一社会信用代码（18 位）、纳税人识别号、主管税务机关（省 / 市 / 区税务局）、行业代码（GB/T 4754-2017）、注册地、经营地。
- **主体类型**：自然人 / 个体工商户 / 个人独资企业 / 合伙企业 / 有限责任公司（小规模 / 一般纳税人）/ 股份有限公司 / WFOE / 中外合资 / 分公司。
- **税务身份**：增值税纳税人资格（小规模 / 一般纳税人）、是否高新技术企业、是否小型微利企业、是否享受研发加计扣除、是否上市。
- **2025 年度收入**：营业收入（增值税口径不含税）、按月销售额明细、境内外收入区分、关联交易金额。
- **历史记录**：上一年度企业所得税申报表（A 类 / B 类）、个人所得税综合所得汇算清缴记录、是否有税务行政处罚、是否欠税。
- **运营情况**：员工人数、社保 / 公积金缴费基数、数电发票开具情况、外汇登记（如有跨境）。
- **专项附加扣除（自然人 / 个体工商户主）**：子女教育、继续教育、大病医疗、住房贷款利息、住房租金、赡养老人、3 岁以下婴幼儿照护。
- **文件资料**：银行流水 2025、销项发票 / 进项发票、银行回单、上一年度申报表、工资表、社保缴费凭证、外汇收支凭证（如有）。

### 2.2 拒绝清单（超出本技能范围）

- 部分年度居民 / 非税务居民个人 → 拒绝；建议聘请国际税务师。
- 上市公司、新三板挂牌公司、Pre-IPO 重组 → 拒绝。
- 集团并表、跨境重组、特殊性税务处理（财税[2009]59 号、国税[2009]698 号） → 拒绝。
- 转让定价同期资料、国别报告（BEPS Action 13） → 拒绝。
- 海关 / 进出口退税复杂筹划 → 拒绝。
- 已被税务机关稽查或立案 → 拒绝。
- 外籍个人享受"六年豁免"（财政部 税务总局公告 2019 年第 34 号）需个案分析 → 标记复核，原则上保守按全球所得纳税处理（以最新公告为准）。
- 年营业收入 > 5 亿元 / 员工 > 200 人 → 拒绝（已超出 SME 范畴）。

## 三、税务居民判定

依据《中华人民共和国个人所得税法》（2018 修订）第一条、《中华人民共和国企业所得税法》第二条及《财政部 税务总局关于在中国境内无住所的个人居住时间判定标准的公告》（2019 年第 34 号）。

### 3.1 自然人 / 个体工商户主

- **居民个人构成条件** — 在中国境内有住所（因户籍、家庭、经济利益关系而在中国境内习惯性居住）；或 在中国境内无住所但一个纳税年度内（公历 1 月 1 日至 12 月 31 日）累计居住满 183 天。居民个人就全球所得纳税。外籍居民个人可适用"六年豁免"规则（连续不满六年且单次离境超 30 天可重新起算），暂适用至 2025 年底（以最新公告为准 — 复核确认）。非居民个人：未在境内有住所且一个纳税年度内累计居住不满 183 天 → **拒绝**（本技能仅覆盖居民个人）。  _(《中华人民共和国个人所得税法》（2018 修订）第一条；《财政部 税务总局关于在中国境内无住所的个人居住时间判定标准的公告》（2019 年第 34 号）)_

### 3.2 企业

- **居民企业构成条件** — 依法在中国境内成立的企业（包括有限公司、个人独资企业以企业为主体登记部分、合伙企业按规定、WFOE 等）；或 依照外国（地区）法律成立但实际管理机构在中国境内的企业。居民企业就全球所得纳税。非居民企业：在中国境内未设立机构、场所，或虽设立但所得与该机构、场所无实际联系 → 适用源泉扣缴 10%（或税收协定优惠税率）→ 路由 `cn-withholding`。  _(《中华人民共和国企业所得税法》第二条)_

### 3.3 双重居民身份的协调

存在协定居民身份冲突时，依《OECD 范本》及具体协定第 4 条加比规则（永久性住所 → 重要利益中心 → 习惯性居所 → 国籍 → 协商）。复核师确认；本技能不作终局判定。

## 四、主体规模与税务身份

### 4.1 个体工商户 / 个人独资企业

- **税务规则** — 不缴企业所得税，生产经营所得适用 5 级超额累进 5%-35%（个人所得税法附件二）。增值税：原则上小规模纳税人，征收率 1%（2027 年底前减按 1%，财政部 税务总局公告 2023 年第 19 号 → 复核 2025 年延续公告）。月销售额 ≤ 10 万元（季度 ≤ 30 万元） → 增值税免税（财政部 税务总局公告 2023 年第 19 号）。印花税：合同金额按比例。路由：`cn-iit` + `cn-vat` + `cn-fapiao-einvoice` + `cn-social-insurance` + `cn-stamp-tax`。  _(个人所得税法附件二；财政部 税务总局公告 2023 年第 19 号)_

### 4.2 有限责任公司 — 小规模纳税人

- **税务规则** — 年应税销售额 ≤ 500 万元（财税[2018]33 号）。增值税征收率 3%（减按 1% 至 2027 年底）。企业所得税 25%；小型微利企业（应纳税所得额 ≤ 300 万元、从业人数 ≤ 300、资产总额 ≤ 5000 万元）减按 5% 实际税率（财政部 税务总局公告 2023 年第 12 号、2024 年第 23 号 → 复核 2025 延续）。路由：`cn-corporate-tax` + `cn-vat` + `cn-fapiao-einvoice` + `cn-social-insurance` + `cn-stamp-tax`。  _(财税[2018]33 号；财政部 税务总局公告 2023 年第 12 号、2024 年第 23 号)_

### 4.3 有限责任公司 — 一般纳税人

- **税务规则** — 年应税销售额 > 500 万元，或主动申请。增值税：货物销售 13%、不动产 / 建筑 / 交通 / 邮政 9%、服务 / 无形资产 6%；进项税额可抵扣。出口退税：免、抵、退；适用增值税出口退税率表。企业所得税 25%；高新技术企业 15%（科技部 财政部 税务总局国科发火[2016]32 号、国税函[2009]203 号）。路由：`cn-corporate-tax` + `cn-vat` + `cn-fapiao-einvoice` + `cn-social-insurance` + `cn-stamp-tax`（+ `cn-withholding` 如有跨境）。  _(国科发火[2016]32 号；国税函[2009]203 号)_

### 4.4 外商投资企业（WFOE）

- **税务规则** — 自 2020 年 1 月 1 日《外商投资法》施行起，WFOE / 中外合资统一适用《公司法》。税务身份与境内有限公司一致（小规模 / 一般纳税人）。跨境付款：股息预提 10%（协定可降至 5%）、特许权使用费 10%（协定降至 6%-10%）、利息 10%。外汇登记：每笔超过等值 5 万美元跨境付款需办理税务备案表（《服务贸易等项目对外支付税务备案表》）。路由：`cn-corporate-tax` + `cn-vat` + `cn-fapiao-einvoice` + `cn-withholding` + `cn-social-insurance` + `cn-formation` + `cn-stamp-tax`。  _(《外商投资法》（自 2020 年 1 月 1 日起施行）)_

## 五、问题清单（按 ask_user_input_v0 风格批量收集）

### 5.1 第一批 — 居民身份与主体性质（单次 `ask_user_input_v0` 调用，5 题）

- **Q1 税务居民身份 2025：** 居民个人（中国公民 / 有住所） | 居民个人（无住所但累计 ≥ 183 天） | 部分年度居民 / 非居民 | 不确定。
- **Q2 主体类型：** 自然人（无登记） | 个体工商户 | 个人独资企业 | 合伙企业 | 有限责任公司 | 股份有限公司 | WFOE / 外资 | 分公司 | 不确定。
- **Q3 注册地（省 / 市）：** 自由文本（影响地方附加税及优惠政策）。
- **Q4 增值税纳税人身份：** 小规模纳税人 | 一般纳税人 | 未登记（自然人） | 不确定。
- **Q5 是否享受以下优惠：** 高新技术企业（15%） | 小型微利企业（5%） | 研发费用加计扣除 | 软件企业"两免三减半" | 西部大开发 15% | 海南自贸港 15% | 无 | 不确定。

**路由表 5.1**

| 回答 | 行动 |
| --- | --- |
| Q1 居民个人 | 继续 |
| Q1 部分年度 / 非居民 | **拒绝** — 本技能仅覆盖居民个人；建议聘请国际税务师 |
| Q1 不确定 | 进入"3.1 居民身份测算"询问境内居住天数 |
| Q2 自然人 / 个体 / 个独 | 路由 `cn-iit`（经营所得） |
| Q2 有限公司 / 股份 / WFOE | 路由 `cn-corporate-tax` |
| Q2 不确定 | 先路由 `cn-formation` |
| Q4 小规模 | 路由 `cn-vat`（1%/3% 减按 1%） |
| Q4 一般纳税人 | 路由 `cn-vat`（13/9/6 进销项） |
| Q5 高新 / 小微 / 研发加计 | 在 `cn-corporate-tax` 中应用对应税率与扣除 |

### 5.2 第二批 — 营业规模与运营（单次调用，5 题）

- **Q6 2025 年度营业收入（不含税）：** ≤ 10 万元 / 月 | 10 万 - 500 万元 | 500 万 - 5000 万元 | 5000 万 - 5 亿元 | > 5 亿元 | 不确定（由文件推断）。
- **Q7 员工人数：** 无 | 1-5 人 | 6-20 人 | 21-100 人 | > 100 人。
- **Q8 是否有跨境业务：** 无 | 出口商品 | 出口服务（适用零税率 / 免税） | 跨境付款（特许权 / 服务费 / 股息） | 多种。
- **Q9 研发活动：** 无 | 有但未申请加计扣除 | 已申请加计扣除（100% 制造业 / 100% 科技型中小企业 / 75% 其他） | 不确定。
- **Q10 是否上市 / Pre-IPO：** 否 | 新三板挂牌 | A 股上市 | 港股 / 美股上市 | Pre-IPO 重组中。

**路由表 5.2**

| 回答 | 行动 |
| --- | --- |
| Q6 ≤ 10 万 / 月 | 增值税免税；仍需 `cn-vat` 申报 0 |
| Q6 10 万 - 500 万 | 小规模纳税人；`cn-vat` 1% |
| Q6 500 万 - 5000 万 | 一般纳税人或临近门槛；标记复核 |
| Q6 > 5 亿元 | **拒绝** — 超 SME 范围 |
| Q7 ≥ 1 人 | 路由 `cn-iit`（工资薪金代扣代缴）+ `cn-social-insurance` |
| Q7 > 200 人 | **拒绝** — 超 SME 范围 |
| Q8 出口 / 跨境付款 | 路由 `cn-vat`（出口退税）+ `cn-withholding`（跨境预提） |
| Q9 加计扣除 | 在 `cn-corporate-tax` 中应用 R&D 加计 |
| Q10 上市 / Pre-IPO | **拒绝** |

### 5.3 第三批 — 发票与合规（单次调用，4 题）

- **Q11 发票开具：** 数电发票（全电）| 增值税专用发票（纸质 / 电子） | 增值税普通发票 | 不开具 | 不确定。
- **Q12 进项发票管理：** 全部认证抵扣 | 部分认证（有滞留） | 未开始管理 | 不适用（小规模）。
- **Q13 是否曾收到异常凭证 / 失控发票：** 否 | 是（已处理） | 是（未处理） | 不确定。
- **Q14 银行流水与申报收入差异：** 一致 | 流水大于申报（差 < 10%） | 流水大于申报（差 ≥ 10%） | 不确定。

**路由表 5.3**

| 回答 | 行动 |
| --- | --- |
| Q11 任意开票 | 路由 `cn-fapiao-einvoice`（数电发票为强制方向） |
| Q12 部分认证 / 未管理 | 标记复核；可能错失抵扣或形成滞留 |
| Q13 异常凭证未处理 | **金税四期高风险** — 标记复核；不可忽略 |
| Q14 差 ≥ 10% | **金税四期预警风险** — 标记复核；按银行流水保守估算 |

### 5.4 第四批 — 专项附加扣除（仅自然人 / 个体业主，单次调用，1 题）

- **Q15 2025 适用的专项附加扣除（多选）：** 子女教育（每孩 2000 元 / 月） | 婴幼儿照护（每孩 2000 元 / 月） | 继续教育（400 元 / 月 或 3600 元 / 年） | 大病医疗（自付 ≥ 1.5 万元，限 8 万元） | 住房贷款利息（1000 元 / 月） | 住房租金（800/1100/1500 元 / 月） | 赡养老人（独生 3000 元 / 月 / 非独分摊） | 无。

路由：传 `cn-iit` 用于综合所得汇算或个体经营所得扣除。

## 六、下游技能路由逻辑

```
cn-freelance-intake（本技能）
   │
   ├── 主体性质判定
   │     ├── 自然人 / 个体 / 个独 → cn-iit
   │     └── 有限公司 / 股份 / WFOE → cn-corporate-tax
   │
   ├── 增值税
   │     ├── 小规模纳税人 → cn-vat（1%/3% 减按 1%）
   │     └── 一般纳税人 → cn-vat（13/9/6 进销项）
   │
   ├── 发票 → cn-fapiao-einvoice（数电发票）
   ├── 员工 → cn-iit（工资薪金）+ cn-social-insurance
   ├── 跨境付款 → cn-withholding
   ├── 合同 / 账簿 → cn-stamp-tax
   ├── 新设主体 / 重组 → cn-formation
   │
   └── 最后装配 → cn-return-assembly
```

**触发条件对照表**

| 触发条件 | 必调用 | 可选 |
| --- | --- | --- |
| 个体工商户 / 个独 | cn-iit, cn-vat, cn-social-insurance, cn-stamp-tax | cn-fapiao-einvoice（如开票） |
| 有限公司（小规模） | cn-corporate-tax, cn-vat, cn-fapiao-einvoice, cn-social-insurance, cn-stamp-tax | cn-withholding |
| 有限公司（一般纳税人） | cn-corporate-tax, cn-vat, cn-fapiao-einvoice, cn-social-insurance, cn-stamp-tax | cn-withholding |
| WFOE | 全部 | — |

## 七、金税四期合规清单

金税四期（"金税工程"第四期）自 2021 年试点、2024-2025 全面铺开，核心是"以数治税"：通过共享平台贯通税务、银行、社保、海关、市场监管、外汇等数据，形成全方位画像。下列点均为高风险预警触发点：

1. **发票流向异常** — 上下游异常名单、走逃户、虚开嫌疑、左手倒右手。
2. **银行流水与申报收入不匹配** — 个人卡收公款、对私转账高频高额、私户对公私混用。
3. **个税申报与社保基数不一致** — 工资薪金申报数远低于社保基数；劳务报酬异常拆分。
4. **增值税与企业所得税收入不匹配** — 主营业务收入差异超 10% 预警。
5. **进销项严重不匹配** — 长期高税负或零税负、留抵异常累积、税负率显著偏离行业均值。
6. **跨境付款无完税证明** — 服务贸易等项目对外支付未办理税务备案表；预提所得税未代扣代缴。
7. **股东借款超 1 年未还** — 视同股息（财税[2003]158 号），按 20% 补缴个税。
8. **私车公用 / 私房公用未规范** — 无租赁合同、无发票。
9. **关联交易定价偏离** — 关联方利息超出 2:1 债资比、关联购销价格不公允。
10. **隐瞒境外所得 / 境外资产** — CRS 信息交换、外籍居民个人全球纳税。

对每项触发点，本技能在承接包 `compliance_risk_flags` 字段中记录，由 `cn-return-assembly` 在最终复核简报中呈现。

## 八、外籍创始人特殊处理（WFOE / 个人税务）

### 8.1 外籍居民个人

- **规则** — 一个纳税年度内在中国境内累计居住 ≥ 183 天 → 居民个人。连续不满六年（每次离境超 30 天可重新起算）享受"六年豁免"，境外所得且境外支付部分可豁免（财政部 税务总局公告 2019 年第 35 号；本规则原文适用至 2025 年底 — **标注"以最新公告为准"**）。居民个人就境内所得 + 已超六年的境外所得纳税；非居民期仅就境内所得纳税。综合所得（工资薪金、劳务报酬、稿酬、特许权使用费）适用 3%-45% 七级超额累进；年终汇算清缴期 3 月 1 日至 6 月 30 日。八项免税津贴（住房、子女教育、语言培训、搬迁、出差、探亲、洗衣、餐补）原优惠至 2023 年底 → 现已延续至 2027 年底（财政部 税务总局公告 2023 年第 29 号 → 复核 2025 适用）；外籍居民个人可在专项附加扣除与免税津贴间二选一。  _(财政部 税务总局公告 2019 年第 35 号；财政部 税务总局公告 2023 年第 29 号)_

### 8.2 WFOE 架构推荐

- **规则** — 优先 WFOE + 香港或 BVI 控股 + 境外母公司（必要时叠加 VIE 协议控制）。香港控股利益：股息预提税降至 5%（中港税收安排第 10 条）、特许权使用费降至 7%；BVI 无协定但提供资产隔离。跨境付款合规：每笔 ≥ 等值 5 万美元服务贸易付款须办理税务备案；预提所得税在合同义务发生时代扣代缴。外汇管理：FDI 资本金登记（37 号文）、ODI 备案、外债登记；服务贸易付汇凭税务备案表。转让定价：关联方借款债资比 2:1（金融企业 5:1）；关联交易超 4000 万元 / 关联融资超 1 亿元需准备同期资料（本地文档） — 涉及即标记复核。  _(中港税收安排第 10 条；37 号文)_

### 8.3 个人所得税申报口径

- **规则** — 外籍高管 / 创始人在 WFOE 取得董事费 / 工资 → 按工资薪金代扣代缴；境外支付部分仍需自行申报。股权激励（限制性股票 / 期权 / 股票增值权）→ 按"工资薪金"分摊计税；境内外工作天数比例划分（国税发[1994]148 号、财税[2018]164 号）。取得境外股息红利 → 综合所得汇算清缴中按 20% 单独计税（境外已纳税额可抵免）。  _(国税发[1994]148 号；财税[2018]164 号)_

## 九、保守默认值

遇歧义优先采用更保守（更高税负 / 更严合规）结论，并在 `conservative_defaults_applied` 字段记录。

**保守默认值表**

| 不确定情形 | 保守默认 |
| --- | --- |
| 主体性质不清 | 按 **有限公司 + 一般纳税人** 处理（更高合规要求） |
| 居民身份临界（≈ 180 天） | 按 **居民个人** 全球纳税 |
| 年汇算清缴 | **全部综合所得一并申报**（工资薪金 + 劳务 + 稿酬 + 特许权） |
| 跨境付款是否享受税收协定 | 自行判定不享受 → **按 10% 法定税率扣缴**；标记复核协定备案 |
| 社保 / 公积金缴费基数 | 按 **实际工资基数**（避免低报触发金税四期预警） |
| 增值税纳税人身份临界（年销售额 ≈ 500 万元） | 按 **一般纳税人** 处理 |
| 小型微利企业判定临界 | 假设 **不享受** 5% 优惠；标记复核 |
| 高新技术企业资格期满 | 按 **25% 法定税率** 计算；标记复核续期 |
| 关联交易定价 | 按 **独立交易原则** 估算公允价格；标记同期资料义务 |
| 数电发票适用 | 假设 **数电发票全面铺开** → 路由 `cn-fapiao-einvoice` |
| 印花税适用 | 假设 **适用** → 路由 `cn-stamp-tax` |
| 异常凭证 / 失控发票存在 | 按 **进项转出** 处理；标记复核 |
| 股东借款超 1 年 | 按 **视同股息** 20% 个税；标记复核 |
| 研发加计扣除资料完整性 | 假设 **资料不完整** → 不应用加计；标记复核归集 |

## 十、参考资料

主要法律法规与规范性文件（2025 年度有效，复核师应核对 2025 年度修订及最新公告）：

- **《中华人民共和国个人所得税法》**（2018 修订，自 2019 年 1 月 1 日起施行）及实施条例。
- **《中华人民共和国企业所得税法》**（2007 颁布，2017、2018 修订）及实施条例。
- **《中华人民共和国增值税暂行条例》**（2017 修订）及实施细则；增值税改革配套财税文件（财税[2016]36 号"营改增"试点全面推开等）。
- **《中华人民共和国税收征收管理法》**（2015 修订）。
- **《中华人民共和国印花税法》**（自 2022 年 7 月 1 日起施行）。
- **《中华人民共和国发票管理办法》**（2023 修订）。
- **《中华人民共和国外商投资法》**（自 2020 年 1 月 1 日起施行）及实施条例。
- **《中华人民共和国公司法》**（2023 修订，自 2024 年 7 月 1 日起施行）。
- **财政部 税务总局公告 2023 年第 12 号 / 2024 年第 23 号** — 小型微利企业减按 5% 优惠延续。
- **财政部 税务总局公告 2023 年第 19 号** — 小规模纳税人增值税减按 1% 优惠（至 2027 年底）。
- **财政部 税务总局公告 2023 年第 29 号** — 外籍个人八项免税津贴延续至 2027 年底。
- **财政部 税务总局公告 2019 年第 34 号** — 无住所个人居住时间判定。
- **财政部 税务总局公告 2019 年第 35 号** — 无住所个人所得税政策（六年豁免）。
- **财税[2018]164 号** — 个人所得税法修改后优惠政策衔接（年终奖、股权激励、外籍津贴）。
- **财税[2009]59 号** — 企业重组所得税处理（特殊性税务处理）。
- **国家税务总局公告 2014 年第 67 号** — 股权转让所得个人所得税管理办法。
- **国科发火[2016]32 号** — 高新技术企业认定管理办法。
- **国家税务总局公告 2022 年第 13 号、2024 年第 30 号** — 数电发票（全电发票）推行。
- **《国家税务总局关于深化"放管服"改革更大力度推进优化税务执法方式的意见》**（金税四期总体方案）。

## 十一、与 cn-return-assembly 的衔接

完成缺口填补与自检后，输出简短交接信息：(a) 纳税人 + 主体类型 + 行业代码 + 纳税人识别号 + 注册地；(b) 选定的税务身份与适用税率（含引用条文）；(c) 下游技能运行顺序；(d) 明确不运行的技能与原因；(e) 复核提醒（税务师 CTA / 注册会计师 CPA 在电子税务局申报前签字）。然后调用 `cn-return-assembly` 并传递结构化承接包。

### 11.1 结构化承接包（内部 JSON，传 cn-return-assembly）

```json
{
  "jurisdiction": "CN",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "uscc": "",
    "tax_id": "",
    "tax_authority": "",
    "industry_code": "",
    "registered_location_province": "",
    "registered_location_city": "",
    "entity_type": "natural_person|getihu|geren_duzi|partnership|llc_small|llc_general|joint_stock|wfoe|jv|branch",
    "residency_status": "resident_individual|resident_enterprise|non_resident",
    "is_foreign_founder": false
  },
  "tax_status": {
    "vat_taxpayer_type": "small_scale|general|exempt|none",
    "hnte_qualified": false,
    "small_micro_qualified": false,
    "rd_super_deduction_applied": false,
    "software_enterprise_holiday": false,
    "regional_preference": ""
  },
  "revenue": {
    "annual_revenue_cny": 0,
    "monthly_breakdown_available": false,
    "domestic_share_pct": 0,
    "export_share_pct": 0,
    "related_party_share_pct": 0
  },
  "operations": {
    "employee_count": 0,
    "has_cross_border_payments": false,
    "has_cross_border_receipts": false,
    "rd_activity": "none|partial|full",
    "listed_status": "private|nq|a_share|hk_us|pre_ipo"
  },
  "compliance_risk_flags": {
    "fapiao_anomaly": false,
    "bank_revenue_gap_over_10pct": false,
    "iit_socsec_mismatch": false,
    "vat_cit_revenue_mismatch": false,
    "input_output_imbalance": false,
    "cross_border_no_filing": false,
    "shareholder_loan_over_1y": false,
    "private_use_corporate_assets": false,
    "related_party_pricing_concern": false,
    "undisclosed_offshore_income": false
  },
  "foreign_founder": {
    "applicable": false,
    "days_in_china_2025": 0,
    "six_year_rule_applies": false,
    "holding_structure": "direct|hk|bvi|cayman|other",
    "transfer_pricing_doc_required": false
  },
  "iit_special_deductions": {
    "child_education": false,
    "infant_care": false,
    "continuing_education": false,
    "serious_illness": false,
    "mortgage_interest": false,
    "rent": false,
    "elderly_support": false
  },
  "documents_received": [],
  "downstream_skills_to_load": [],
  "open_flags": [],
  "refusals_triggered": [],
  "conservative_defaults_applied": []
}
```

### 11.2 交接示例（个体工商户，深圳，年营业额 80 万元，无员工）

> 承接完成。张明，个体工商户，统一社会信用代码 91440300MA5xxxxxxx，深圳市福田区税务局主管，行业代码 6210（软件开发），纳税人识别号同 USCC。2025 年营业收入 80 万元，居民个人，无员工。增值税：小规模纳税人，征收率 1%（财政部 税务总局公告 2023 年第 19 号），月销售额超 10 万元免税门槛 → 按 1% 申报；个人所得税：经营所得 5 级累进 5%-35%，应纳税所得额 = 收入 - 成本 - 费用 - 损失（含 6 万元投资者本人减除费用 + 专项附加扣除）；专项附加扣除：子女教育 + 赡养老人（独生）共 5000 元 / 月。运行：cn-iit, cn-vat, cn-fapiao-einvoice（数电发票）, cn-social-insurance, cn-stamp-tax, cn-return-assembly。不运行：cn-corporate-tax（非企业主体）、cn-withholding（无跨境）、cn-formation（已设立）。需税务师（CTA）在电子税务局申报前签字。开始装配。

### 11.3 自检清单（承接前 14 项必过）

1. 使用 `ask_user_input_v0` 而非散文式提问完成 5.1 居民身份与主体批次。
2. 居民身份判定明确（居民个人 / 居民企业 / 非居民 + 拒绝）。
3. 主体类型已设定。
4. 增值税纳税人身份已设定（小规模 / 一般 / 免税 / 无）。
5. 2025 年营业收入档位已记录（CNY）。
6. 适用税率与优惠政策已附引用（公告号 / 法条号）。
7. 跨境业务标记已设定，触发 `cn-withholding` 路由。
8. 员工人数已设定，> 0 触发 `cn-social-insurance` + 工资薪金 IIT。
9. 数电发票路由 `cn-fapiao-einvoice` 已确认（除完全不开票自然人外均路由）。
10. 印花税路由 `cn-stamp-tax` 已确认（除完全无合同账簿外均路由）。
11. 金税四期风险点逐项检查并记录（11 项 `compliance_risk_flags`）。
12. 外籍创始人字段（如适用）已捕获，标记复核同期资料 / 协定备案义务。
13. 所有保守默认值已记录引用。
14. 开场陈述与交接信息中均包含复核提醒（CTA / CPA）。

## 免责声明

本技能及其输出仅供信息和计算用途，不构成税务、法律或财务建议。OpenAccountants 及其贡献者对因使用本技能产生的任何错误、遗漏或后果不承担责任。所有输出在向中国税务机关（电子税务局）申报或据以行动之前，必须由具备资质的中国税务师（CTA）或注册会计师（CPA）复核签字。

最新经验证版本维护于 [openaccountants.com](https://openaccountants.com)。

---

*OpenAccountants — 面向 AI 的开源会计技能*
*本输出在申报或据以行动之前必须经具备资质的专业人士复核。*
*最新已验证技能：openaccountants.com | 错误反馈：github.com/openaccountants/openaccountants*

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
