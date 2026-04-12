---
name: mx-income-tax
description: >
  Use this skill whenever asked about Mexican individual income tax (ISR) for self-employed individuals (personas físicas con actividades empresariales y profesionales). Trigger on phrases like "how much tax do I pay in Mexico", "ISR", "Declaración Anual", "pagos provisionales", "actividades profesionales", "honorarios", "RESICO", "deducciones personales", "deducciones autorizadas", "RFC", "income tax return Mexico", "SAT", "CFDI", or any question about filing or computing income tax for a self-employed or freelance client in Mexico. Covers Declaración Anual PF, pagos provisionales (monthly), progressive ISR brackets (1.92%–35%), deducciones autorizadas and personales, CFDI invoice requirements, retenciones, RESICO simplificado regime comparison, and IMSS contributions for independientes.
version: 2.0
---

# Mexico Income Tax — Self-Employed / Persona Física (ISR)

## Section 1 — Quick Reference

### ISR Brackets (2025 — Declaración Anual, personas físicas)
| Límite inferior (MXN) | Límite superior (MXN) | Cuota fija | Tasa sobre excedente |
|---|---|---|---|
| $0.01 | $8,952.49 | $0.00 | 1.92% |
| $8,952.50 | $75,984.55 | $171.88 | 6.40% |
| $75,984.56 | $133,536.07 | $4,461.94 | 10.88% |
| $133,536.08 | $155,229.80 | $10,723.55 | 16.00% |
| $155,229.81 | $185,852.57 | $14,194.54 | 17.92% |
| $185,852.58 | $374,837.88 | $19,682.13 | 21.36% |
| $374,837.89 | $590,795.99 | $60,049.40 | 23.52% |
| $590,796.00 | $1,127,926.84 | $110,842.74 | 30.00% |
| $1,127,926.85 | $1,503,902.46 | $271,981.99 | 32.00% |
| $1,503,902.47 | $4,511,707.37 | $392,294.17 | 34.00% |
| $4,511,707.38 | En adelante | $1,414,947.85 | 35.00% |

**Formula:** ISR = cuota fija + (base gravable − límite inferior) × tasa sobre excedente

**Monthly brackets (pagos provisionales):** Same structure but divided by 12 (tabla mensual). Applied to monthly net income.

### RESICO — Régimen Simplificado de Confianza (Alternative)
| Feature | RESICO | Régimen General |
|---|---|---|
| Revenue threshold (2025) | ≤ $3,500,000 MXN/year | Any revenue |
| ISR rate | Flat: 1%–2.5% on gross monthly income (no deductions) | Progressive 1.92%–35% on net income |
| Monthly payment | On gross income × flat rate | On net (revenue − deductions) × progressive rate |
| Deducciones | No deductions allowed | Full deductions autorizadas |
| CFDI requirements | Must issue CFDIs | Must issue CFDIs |
| IVA | Must pay IVA separately | Must pay IVA separately |
| Best for | Low-expense businesses / those who can't document expenses | High-expense businesses / professionals with significant costs |

**RESICO flat ISR rates by income band (monthly gross):**
| Ingresos mensuales (MXN) | Tasa ISR RESICO |
|---|---|
| 0 – $25,000 | 1.00% |
| $25,001 – $50,000 | 1.10% |
| $50,001 – $83,333 | 1.50% |
| $83,334 – $208,333 | 2.00% |
| $208,334 – $291,667 | 2.50% |

### Key Deducciones Autorizadas (Régimen General — Actividades Empresariales/Profesionales)
| Deducción | Condición |
|---|---|
| Gastos de operación (renta oficina, servicios, materiales) | CFDI requerido; estrictamente indispensable |
| Sueldos y salarios de empleados | CFDI de nómina + inscripción IMSS |
| Depreciación de activos fijos | Tasas SAT (computadoras: 30%/año; mobiliario: 10%/año) |
| ISR de trabajadores (enterado al SAT) | Impuesto enterado — no propio |
| Cuotas IMSS (parte patronal si tiene empleados) | Solo si hay empleados |
| Intereses de créditos de negocio | Acreditados y pagados |
| Pérdidas por cuentas incobrables | Documentadas |
| IVA pagado a proveedores (acreditable) | Separado — IVA acreditable |

### Key Deducciones Personales (Declaración Anual — personal, not business)
| Deducción | Límite |
|---|---|
| Honorarios médicos, dentales, hospitalarios | Sin límite, con CFDI |
| Primas de seguro de gastos médicos | Sin límite, con CFDI |
| Intereses de crédito hipotecario (vivienda) | Máximo 1.5 UMA anual (~$52,798 MXN 2025) |
| Donativos (donatarias autorizadas) | 7% del ingreso acumulable anterior |
| Aportaciones voluntarias AFORE | 10% del ingreso acumulable |
| Colegiaturas (educación básica-bachillerato) | $14,200–$24,500 MXN según nivel |
| Gastos funerarios | 1 UMA anual (~$35,199 MXN) |
| Transporte escolar (obligatorio en municipio) | Sin límite, con CFDI |

**Límite global deducciones personales:** 15% del ingreso total ó 5 UMAs anuales (~$175,993 MXN), lo que resulte menor.

### Conservative Defaults
| Item | Default |
|---|---|
| Régimen | RESICO si ingresos ≤ $3.5M y gastos no bien documentados |
| Home office % | No asumir — preguntar % área |
| Vehicle % | No asumir — solicitar km logbook |
| Teléfono/internet | 50% si uso mixto |
| CFDI compliance | Verificar si todos los ingresos tienen CFDI emitidos |

### Red Flag Thresholds
| Situación | Flag |
|---|---|
| Ingresos > $3,500,000 MXN | RESICO no aplica |
| Gastos sin CFDI | No deducibles — riesgo de rechazo SAT |
| Ingresos sin CFDI emitido | Incumplimiento fiscal — obligatorio emitir CFDI |
| Retenciones de ISR no acreditadas | Verificar comprobantes de retención |
| Sin pago de IVA | Si presta servicios, IVA 16% aplica (salvo exentos) |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross income (ingresos brutos) for the year — all CFDIs issued
2. Régimen elegido: RESICO or Régimen General
3. If Régimen General: itemised deducciones autorizadas with CFDIs
4. ISR retenciones already withheld by clients (2/3/10% depending on activity)
5. Pagos provisionales made monthly during the year
6. Personal deducciones (medical, mortgage interest, etc.) for Declaración Anual
7. IVA position (separate — but flag if not filed)

### Refusal Catalogue
**R-MX-1 — No CFDI for expenses**
Refuse expenses without CFDI. State: "Without a valid CFDI (Comprobante Fiscal Digital por Internet), expenses cannot be deducted. The SAT requires CFDI for all deducciones autorizadas."

**R-MX-2 — RESICO threshold exceeded**
If annual income > $3,500,000 MXN: cannot use RESICO. State: "Your income exceeds the $3,500,000 MXN RESICO threshold. You must use the Régimen General de Personas Físicas con Actividades Empresariales y Profesionales."

**R-MX-3 — No CFDI issued for income**
If client did not issue CFDIs for services rendered: flag compliance issue. State: "All income must be supported by a CFDI issued by you to your clients. Failure to issue CFDIs is a tax violation subject to penalties."

**R-MX-4 — Personal expenses as business deductions**
Refuse personal costs as deducciones autorizadas. State: "These are personal expenses. Only expenses strictly indispensable for generating your business income qualify as deducciones autorizadas."

**R-MX-5 — Foreign income without pesos conversion**
Foreign income must be converted to MXN. State: "Income in USD or other currencies must be converted to Mexican pesos using the SAT exchange rate (tipo de cambio publicado por el SAT / Banco de México) on the date of receipt."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| Transferencia de cliente (empresa) | Honorarios / actividades profesionales | Incluir bruto (cliente puede retener ISR) | CFDI emitido obligatorio |
| SPEI de persona moral | Honorarios | Retención ISR posible 10% | Verificar si retuvieron |
| SPEI de persona física | Honorarios | Sin retención ISR usualmente | Incluir bruto |
| Transferencia internacional / SWIFT | Ingresos del exterior | Incluir — convertir a MXN al tipo SAT | Carnê-Leão equivalent: pagos provisionales |
| Stripe depósito | Plataforma digital | Incluir + comisión Stripe como gasto | |
| PayPal transferencia | Plataforma | MXN equivalente | |
| Plataformas digitales (MercadoLibre, Rappi, etc.) | Ingresos plataformas | Plataforma puede retener ISR 35% | Verificar con extrato de plataforma |
| Intereses bancarios | Intereses | ISR retenido por banco — acreditar | Accesorio — no actividad profesional |
| Arrendamiento recibido | Arrendamiento | Régimen separado de arrendamiento | No en este régimen |
| Depósito propio | — | EXCLUIR | |

### 3.2 Expense Patterns (Deducciones Autorizadas — Régimen General)
| Bank Description Pattern | Categoría | ¿Deducible? | Observación |
|---|---|---|---|
| Telcel / AT&T México / Movistar | Teléfono | Parcial — % profesional | T2; CFDI requerido |
| Telmex / Totalplay / Izzi | Internet | % profesional | T2; CFDI requerido |
| CFE (luz) | Electricidad | % oficina en casa | T2 |
| CAPUFE / GAS natural / agua | Servicios | % oficina | T2 |
| Renta oficina (persona moral) | Renta local | 100% — CFDI | Profesional exclusivo |
| Amazon.com.mx / Liverpool office | Material de oficina | 100% — uso profesional, CFDI | |
| Adobe / Slack / Notion / Zoom | Software / SaaS | 100% | CFDI o comprobante |
| Aeromexico / Volaris / Viva Aerobus | Viajes profesionales | 100% — propósito profesional | CFDI boleto |
| Hotel (viaje profesional) | Hospedaje | 100% — propósito profesional | CFDI |
| Restaurante (reunión con cliente) | Alimentos y reuniones | 12.5% del total (límite LISR art. 28) | Con CFDI; no siempre deducible al 100% |
| Cursos / capacitación profesional | Formación | 100% — relacionado a actividad | CFDI |
| Contador / despacho fiscal | Honorarios contables | 100% | CFDI |
| Seguro de responsabilidad civil | Seguros | 100% | CFDI |
| IMSS cuotas (patronales) | Seguridad social | Solo si tiene empleados | CFDI o comprobante IMSS |
| ISR pago provisional (DIOT) | Impuesto | EXCLUIR — no deducible | |
| IVA pagado | IVA | EXCLUIR de ISR — acredita en IVA | |
| Pago tarjeta crédito | — | EXCLUIR — gastos individuales ya capturados | |

### 3.3 Retenciones de ISR (Créditos)
| Situación | Tasa de retención | Tratamiento |
|---|---|---|
| Servicios profesionales a persona moral | 10% del honorario | Crédito en Declaración Anual / pagos provisionales |
| Plataformas tecnológicas | 35% (personas físicas con menores ingresos) o 1%–2.1% | Crédito — verificar con extracto plataforma |
| Sin retención (persona física cliente) | 0% | No hay crédito; pagos provisionales propios obligatorios |
| Exterior (wire, Stripe, PayPal) | 0% retenido en México | Pagos provisionales propios obligatorios |

**Gross up:** Si se recibió neto (retenido 10%): bruto = neto ÷ 0.90. Declarar bruto; crédito = diferencia.

### 3.4 Divisas y Plataformas Internacionales
| Fuente | Moneda | Tratamiento |
|---|---|---|
| USD de clientes EUA | USD | Convertir a MXN usando tipo de cambio SAT en fecha de cobro |
| EUR de clientes europeos | EUR | Convertir con tipo SAT |
| Stripe USD | USD | Usar equivalente MXN del extracto Stripe o tipo SAT |
| PayPal USD | USD | Usar MXN del extracto PayPal |
| Upwork / Fiverr | USD | Gross USD; convertir a MXN; comisión = gasto |
| Google AdSense | USD | Mensual; convertir a MXN |

### 3.5 Transferencias Internas
| Patrón | Tratamiento |
|---|---|
| SPEI a cuenta de ahorro propia | EXCLUIR |
| Retiro personal (honorarios propios sin CFDI) | EXCLUIR — no es gasto |
| Pago tarjeta (AMEX, Banamex, BBVA) | EXCLUIR — gastos individuales capturados |
| Préstamo personal recibido | EXCLUIR — no es ingreso |
| Depósito de capital propio | EXCLUIR |

---

## Section 4 — Worked Examples

### Example 1 — BBVA México: Consultor IT, Régimen General
**Scenario:** IT consultant, $1,200,000 MXN ingresos anuales, $300,000 gastos deducibles (con CFDI), retención ISR $120,000 (10% sobre honorarios), pagos provisionales $80,000

**Bank statement extract (BBVA Empresas):**
```
Fecha         | Descripción                                | Cargo (MXN)    | Abono (MXN)    | Saldo (MXN)
15/04/2025    | SPEI RECIBIDO DE TECHCORP SA DE CV        |                | 180,000.00     | 1,450,000.00
20/04/2025    | SPEI RECIBIDO STARTUP MEXICO              |                |  90,000.00     | 1,540,000.00
25/04/2025    | PAGO ISR PROV PROVISIONAL SAT             | 18,000.00      |                | 1,522,000.00
28/04/2025    | ADOBE SYSTEMS DOMICILIACIÓN               | 1,450.00       |                | 1,520,550.00
30/04/2025    | COMISIÓN MENSUAL BBVA EMPRESAS            | 350.00         |                | 1,520,200.00
```

**Note:** SPEI de $180,000 = honorario bruto $200,000 − 10% retención $20,000.

**Cálculo ISR:**
| Concepto | Monto |
|---|---|
| Ingresos brutos | $1,200,000 |
| Deducciones autorizadas | ($300,000) |
| **Base gravable** | **$900,000** |
| ISR (bracket: $590,796–$1,127,926; cuota $110,842.74 + 30% excedente) | $110,843 + 30%×($900,000−$590,796) = $110,843 + $92,762 = **$203,605** |
| Retenciones ISR | ($120,000) |
| Pagos provisionales | ($80,000) |
| **ISR a pagar** | **$3,605** |

### Example 2 — Citibanamex: Diseñadora, RESICO
**Scenario:** Graphic designer, $480,000 MXN ingresos anuales (promedio $40,000/mes), RESICO, few documented expenses

**Bank statement extract (Citibanamex):**
```
Fecha         | Descripción                                | Cargos (MXN)   | Abonos (MXN)   | Saldo (MXN)
10/03/2025    | SPEI RECIB AGENCIA CREATIVA SA DE CV      |                | 35,000.00      | 285,000.00
15/03/2025    | SPEI RECIB ESTUDIO DIGITAL MX             |                | 18,000.00      | 303,000.00
20/03/2025    | DOMICILIACIÓN FIGMA INC                   | 450.00         |                | 302,550.00
22/03/2025    | SPEI ENVIADO ISR RESICO SAT               | 440.00         |                | 302,110.00
28/03/2025    | COMISIÓN MANTENIMIENTO CTA                | 200.00         |                | 301,910.00
```

**RESICO cálculo mensual (40,000 MXN ingreso promedio):**
- Banda: $25,001–$50,000 → tasa 1.10%
- ISR mensual: $40,000 × 1.10% = **$440 MXN/mes**
- ISR anual RESICO: $440 × 12 = **$5,280 MXN**

**Comparación con Régimen General:**
- Régimen General (sin deducciones): base $480,000 → ISR ~$113,000
- Con deducciones reales hipotéticas $100,000: base $380,000 → ISR ~$75,000
- **RESICO: $5,280 — ahorro masivo para esta situación**

### Example 3 — Santander México: Abogado, Régimen General con Home Office
**Scenario:** Lawyer (abogado), $2,000,000 MXN ingresos, $450,000 gastos, home office (departamento 120m², despacho 25m²)

**Bank statement extract (Santander México):**
```
Fecha         | Descripción                                | Cargo (MXN)    | Abono (MXN)    | Saldo (MXN)
08/05/2025    | SPEI EMPRESA CONSTRUCTORA SA              |                | 250,000.00     | 2,150,000.00
12/05/2025    | SPEI DESPACHO JURIDICO BC                 |                | 120,000.00     | 2,270,000.00
15/05/2025    | RENTA DESPACHO COMPARTIDO                 | 12,000.00      |                | 2,258,000.00
20/05/2025    | SUSCRIPCIÓN WESTLAW MEXICO                | 3,500.00       |                | 2,254,500.00
25/05/2025    | ISR PAGO PROVISIONAL MENSUAL              | 35,000.00      |                | 2,219,500.00
```

**Home office cálculo:**
- % profesional: 25/120 = 20.8%
- Renta mensual $18,000 × 12 = $216,000 × 20.8% = $44,928 deducible/año
- Luz $24,000 × 20.8% = $4,992
- Internet $8,400 × 20.8% = $1,747
- Total home office: $51,667

**Cálculo ISR:**
| Concepto | Monto |
|---|---|
| Ingresos brutos | $2,000,000 |
| Gastos directos | ($398,333) |
| Home office | ($51,667) |
| **Base gravable** | **$1,550,000** |
| ISR: cuota $392,294.17 + 34% × ($1,550,000−$1,503,902.47) | $392,294 + 34%×$46,097 = $392,294 + $15,673 = **$407,967** |
| Retenciones + provisionales | ($350,000) |
| **ISR a pagar** | **$57,967** |

### Example 4 — HSBC México: Desarrollador con Ingresos del Exterior
**Scenario:** Developer, $600,000 MXN domestic + USD $25,000 (≈$450,000 MXN) from US clients, pagos provisionales $120,000

**Bank statement extract (HSBC México):**
```
Fecha         | Descripción                                | Cargo (MXN)    | Abono (MXN)    | Saldo (MXN)
10/06/2025    | SPEI RECIB EMPRESA TECH MX SA             |                | 90,000.00      | 820,000.00
15/06/2025    | TRANSFERENCIA EXTERIOR USD 5,000          |                | 91,500.00      | 911,500.00
20/06/2025    | ISR PROVISIONAL MENSUAL SAT               | 22,000.00      |                | 889,500.00
25/06/2025    | CARGO AWS AMAZON                          | 3,200.00       |                | 886,300.00
30/06/2025    | COMISIÓN HSBC EMPRESAS                    | 450.00         |                | 885,850.00
```

**Tipo de cambio SAT:** USD $25,000 × $18.00 (tipo de cambio hipotético en fecha de cobro) = $450,000 MXN

**Cálculo ISR:**
| Concepto | Monto |
|---|---|
| Ingresos México | $600,000 |
| Ingresos exterior (convertidos) | $450,000 |
| Total ingresos | $1,050,000 |
| Deducciones autorizadas | ($200,000) |
| **Base gravable** | **$850,000** |
| ISR (bracket $590,796–$1,127,926): $110,843 + 30%×($850,000−$590,796) | $110,843 + $77,761 = **$188,604** |
| Pagos provisionales | ($120,000) |
| Retenciones ISR | ($30,000) |
| **ISR a pagar** | **$38,604** |

### Example 5 — Banorte: Arquitecta, Deducciones Personales
**Scenario:** Architect, $800,000 MXN ingresos, $180,000 gastos negocio, deducciones personales: médicos $45,000, hipoteca intereses $52,000, seguro médico $28,000

**Bank statement extract (Banorte Pyme):**
```
Fecha         | Referencia                                 | Cargo (MXN)    | Abono (MXN)    | Saldo (MXN)
12/07/2025    | SPEI CONSTRUCTORA NORTE SA                |                | 150,000.00     | 1,250,000.00
18/07/2025    | SPEI PROYECTO RESIDENCIAL SA              |                |  80,000.00     | 1,330,000.00
22/07/2025    | AUTODESK SUBSCRIPTION                    | 4,200.00       |                | 1,325,800.00
26/07/2025    | PAGO INTERESES HIPOTECA BANORTE           | 12,000.00      |                | 1,313,800.00
30/07/2025    | COMISIÓN MENSUAL BANORTE                  | 300.00         |                | 1,313,500.00
```

**Cálculo ISR:**
| Concepto | Monto |
|---|---|
| Ingresos brutos | $800,000 |
| Deducciones autorizadas (negocio) | ($180,000) |
| Base previa | $620,000 |
| Deducciones personales (médicos + intereses hipoteca capped + seguro médico) | ($125,000) |
| **Base gravable** | **$495,000** |
| ISR (bracket $374,838–$590,796): $60,049 + 23.52%×($495,000−$374,838) | $60,049 + $28,260 = **$88,309** |
| Retenciones + provisionales | ($85,000) |
| **ISR a pagar** | **$3,309** |

### Example 6 — Scotiabank México: Consultor, Pagos Provisionales Mensual
**Scenario:** Management consultant, $150,000 MXN promedio mensual, calculating monthly pago provisional

**Bank statement extract (Scotiabank México):**
```
Fecha         | Descripción                                | Cargo (MXN)    | Abono (MXN)    | Saldo (MXN)
03/08/2025    | SPEI CORPORATIVO GR SA DE CV              |                | 200,000.00     | 1,850,000.00
10/08/2025    | SPEI HOLDING EMPRESARIAL MX               |                | 130,000.00     | 1,980,000.00
15/08/2025    | ISR PROVISIONAL AGOSTO                    | 22,500.00      |                | 1,957,500.00
20/08/2025    | DOMICILIACIÓN SALESFORCE MX               | 8,500.00       |                | 1,949,000.00
25/08/2025    | CARGO SCOTIABANK MENSUALIDAD              | 420.00         |                | 1,948,580.00
```

**Cálculo pago provisional mensual (método simplificado):**
1. Ingresos mes agosto: $330,000
2. Menos: deducciones del mes estimadas: ($60,000)
3. Base gravable mes: $270,000
4. ISR tabla mensual (banda $49,233–$93,382 ≈ $374,838÷12 = $31,237–$590,796÷12 = $49,233): usar tabla mensual
5. ISR mensual ≈ $22,500 (aproximado — usar la tabla mensual exacta del SAT)
6. Menos: retenciones ISR del mes: ($18,000)
7. **Pago provisional: $4,500**

**Nota:** Los pagos provisionales se determinan aplicando la tabla mensual oficial del SAT. El cálculo acumula ingresos del año.

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Residencia Fiscal en México
- **Residente:** Establecimiento permanente en México OR casa habitación en México (cuando también tiene casa en el extranjero: aplicar prueba de centro de intereses vitales) → ingresos mundiales gravados
- **No residente:** Solo ingresos de fuente mexicana; ISR retención en fuente

### CFDI — Comprobante Fiscal Digital
- Obligatorio emitir CFDI por cada ingreso cobrado
- Sistema: portal del SAT (facturación en línea) o PAC (Proveedor Autorizado de Certificación)
- Sin CFDI: ingreso no deducible para el cliente y posible infracción para el emisor
- CFDI de gastos: obligatorio para que las deducciones autorizadas sean válidas

### Tipos de Régimen para PF Actividad Empresarial
| Régimen | Límite | Características |
|---|---|---|
| RESICO PF | ≤ $3.5M MXN | ISR simple 1%–2.5% sobre ingresos brutos |
| Régimen General PF | Sin límite | ISR progresivo sobre utilidad neta |
| RIF (Régimen de Incorporación) | Terminado 2022 | Migrar a RESICO |
| Régimen de Arrendamiento | Solo rentas | Específico para arrendadores |

### IVA — Interacción
- Servicios profesionales: IVA 16% adicional al honorario
- IVA cobrado al cliente: no es ingreso ISR — entregar al SAT
- IVA pagado a proveedores: acreditable contra IVA cobrado
- **Error común:** Incluir IVA cobrado como ingreso gravable para ISR — incorrecto

### IMSS — Persona Física
- Autónomo sin empleados: **no obligado** a IMSS (puede afiliarse voluntariamente)
- Si tiene empleados: sí paga cuotas patronales IMSS — deducibles como gasto de nómina
- Sin IMSS propio: considera afiliación voluntaria o seguro privado (deducible personal si tiene CFDI)

### Pagos Provisionales
- **Frecuencia:** Mensual, a más tardar el día 17 del mes siguiente
- **Método:** Ingresos acumulados enero–mes − deducciones acumuladas × tasa ISR − pagos anteriores − retenciones
- **DARF equivalente México:** Línea de captura en portal SAT / pago bancario
- Incumplimiento: recargos + actualización automática

### Declaración Anual
| Tipo | Plazo |
|---|---|
| Personas físicas (todos los regímenes) | Abril 30 del año siguiente |
| Personas morales | Marzo 31 del año siguiente |
| Declaración complementaria | Dentro del ejercicio en caso de corrección |

### Multas y Recargos
| Situación | Sanción |
|---|---|
| No presentar Declaración Anual | $1,400–$17,370 MXN |
| No presentar pagos provisionales | $1,400–$17,370 MXN por omisión |
| Omisión de ingresos | 55%–75% del ISR omitido |
| No expedir CFDI | $17,020–$97,330 MXN por cada CFDI |
| Recargos | 1.47% mensual sobre el crédito fiscal (2025) |

---

## Section 6 — Tier 2 Catalogue

### T2-MX-1: Oficina en Casa (Home Office)
**Por qué T2:** La proporción profesional/habitacional es un dato que solo el cliente conoce.

**Método:** m² oficina ÷ m² total × renta/luz/internet
**Exige del cliente:** Superficie total del inmueble, superficie exclusiva del despacho, confirmación de uso exclusivamente profesional, CFDI de renta (si aplica).
**Nota SAT:** Para deducir gastos del hogar como oficina, el espacio debe ser de uso exclusivo profesional y el contrato de renta debe estar a nombre de quien deduce (o RFC del negocio).

### T2-MX-2: Automóvil (Uso Profesional)
**Por qué T2:** La proporción km profesional/personal es un dato que solo el cliente tiene.

**Reglas LISR art. 36:**
- Automóviles deducibles hasta $175,000 MXN (valor de adquisición; solo aplica deducción hasta ese monto)
- Combustible, mantenimiento, seguro: deducibles en % profesional
- **Requiere:** km logbook, CFDI de gasolina (tarjeta o factura), CFDI seguro

### T2-MX-3: Teléfono e Internet
**Por qué T2:** División personal/profesional es subjetiva.

**Orientación:** Línea exclusivamente profesional: 100% deducible con CFDI. Uso mixto: % estimado (default 50%–70%). CFDI obligatorio del proveedor para deducción.

### T2-MX-4: Alimentos y Representación
**Por qué T2:** La deducibilidad depende del contexto de la reunión — solo el cliente sabe quién asistió.

**Regla LISR art. 28 fracción XX:** Alimentos y gastos de representación: deducibles hasta el 8.5% de la utilidad fiscal del ejercicio ó 12.5% de los ingresos del ejercicio (lo que resulte menor). Requieren CFDI.

### T2-MX-5: RESICO vs Régimen General — Punto de Equilibrio
**Por qué T2:** La decisión depende de los gastos reales del cliente — que solo él conoce.

**Punto de equilibrio:** Si las deducciones autorizadas son tan altas que en Régimen General el ISR resulta menor que en RESICO, conviene Régimen General.

**Cálculo orientativo:** RESICO: ingresos × tasa RESICO. Régimen General: (ingresos − deducciones) × tasa progresiva. Comparar.

---

## Section 7 — Excel Working Paper

### Hoja 1: Ingresos
| Columna | Contenido |
|---|---|
| A | Fecha |
| B | Cliente |
| C | RFC cliente |
| D | N.° CFDI |
| E | Subtotal (MXN) |
| F | IVA 16% |
| G | Total CFDI |
| H | Retención ISR (si aplica) |
| I | Neto cobrado |
| J | Categoría (Honorarios / Exterior / Excluir) |

**Total ingresos acumulables:** `=SUMIF(J:J,"Honorarios",E:E)+SUMIF(J:J,"Exterior",E:E)`

### Hoja 2: Deducciones Autorizadas
| Columna | Contenido |
|---|---|
| A | Fecha |
| B | Proveedor |
| C | RFC proveedor |
| D | N.° CFDI |
| E | Subtotal HT (MXN) |
| F | Categoría |
| G | % profesional |
| H | Deducible (=E×G) |

### Hoja 3: Cálculo ISR
| Concepto | Monto |
|---|---|
| Ingresos acumulables | |
| Deducciones autorizadas | |
| Utilidad fiscal | |
| Deducciones personales (Declaración Anual) | |
| Base gravable | |
| ISR (tabla anual) | |
| Retenciones ISR acreditables | |
| Pagos provisionales | |
| **ISR a pagar / saldo a favor** | |

### Hoja 4: Pagos Provisionales (Acumulado)
| Mes | Ingresos acum. | Deducc. acum. | Base acum. | ISR acum. | Prev. pagados | A pagar |
|---|---|---|---|---|---|---|
| Enero | | | | | | |
| Febrero | | | | | | |
| ... | | | | | | |

---

## Section 8 — Bank Statement Reading Guide

### BBVA México (Empresas)
- Format: `Fecha | Descripción | Cargo (MXN) | Abono (MXN) | Saldo (MXN)`
- Date: DD/MM/YYYY
- Income = Abono column
- "SPEI RECIBIDO" = incoming wire; "DOMICILIACIÓN" = auto-debit

### Citibanamex
- Format: `Fecha | Descripción | Cargos (MXN) | Abonos (MXN) | Saldo (MXN)`
- Date: DD/MM/YYYY
- Income = Abonos; "SPEI RECIB" = incoming SPEI

### Santander México
- Format: `Fecha | Descripción | Cargo (MXN) | Abono (MXN) | Saldo (MXN)`
- Date: DD/MM/YYYY
- "SPEI EMPRESA" = incoming corporate transfer

### HSBC México
- Format: `Fecha | Descripción | Cargo (MXN) | Abono (MXN) | Saldo (MXN)`
- Date: DD/MM/YYYY
- "TRANSFERENCIA EXTERIOR" = international wire received (note: convert at SAT rate)

### Banorte
- Format: `Fecha | Referencia | Cargo (MXN) | Abono (MXN) | Saldo (MXN)`
- Date: DD/MM/YYYY
- "SPEI" in description = SPEI transfer

### Scotiabank México
- Format: `Fecha | Descripción | Cargo (MXN) | Abono (MXN) | Saldo (MXN)`
- Date: DD/MM/YYYY

### Exclusion Patterns (all Mexican banks)
| Patrón | Acción |
|---|---|
| SPEI enviado cuenta propia | EXCLUIR — transferencia interna |
| Pago tarjeta crédito / AMEX | EXCLUIR — gastos individuales ya capturados |
| ISR pago provisional SAT | EXCLUIR de gastos — crédito en declaración anual |
| IVA pago SAT | EXCLUIR — obligación IVA separada |
| Depósito préstamo / crédito | EXCLUIR — no es ingreso |
| Retiro cajero propio | EXCLUIR |

---

## Section 9 — Onboarding Fallback

**Prioridad 1 (bloqueante):**
1. "¿Cuál fue el total de tus ingresos (suma de todos los CFDIs emitidos) en el año fiscal?"
2. "¿Estás en RESICO o Régimen General de Personas Físicas?"
3. "¿Tienes CFDIs de todos tus gastos de negocio para soportar las deducciones?"

**Prioridad 2 (para cálculo exacto):**
4. "¿Tus clientes te retuvieron ISR (10%)? ¿Tienes los comprobantes de retención?"
5. "¿Realizaste pagos provisionales mensuales de ISR al SAT? Fechas y montos."
6. "¿Cobras IVA a tus clientes? ¿Presentas declaraciones mensuales de IVA?"
7. "¿Tienes ingresos en dólares u otras divisas? De ser así, ¿convertiste al tipo de cambio SAT?"

**Prioridad 3 (deducciones personales):**
8. "¿Tienes gastos médicos u hospitalarios del año (con CFDI y RFC del médico)?"
9. "¿Pagaste intereses de crédito hipotecario por casa habitación?"
10. "¿Tienes seguro de gastos médicos mayores? ¿Con CFDI de la aseguradora?"

**Enfoque conservador:**
- RESICO si ingresos ≤ $3.5M y gastos no bien documentados
- No incluir deducciones sin CFDI válido
- Verificar que todos los ingresos tienen CFDI emitido

---

## Section 10 — Reference Material

### Formularios y Declaraciones Principales
| Formulario | Finalidad |
|---|---|
| Declaración Anual PF | Declaración anual ISR persona física |
| Pagos Provisionales mensuales | ISR mensual acumulado |
| DIOT | Declaración Informativa de Operaciones con Terceros (IVA) |
| CFDI de ingresos | Factura electrónica por cada cobro |
| CFDI de egresos (nota de crédito) | Para corregir CFDIs emitidos |

### Portal del SAT
- **Portal SAT:** sat.gob.mx
- **Mi Cuenta SAT:** Declaraciones y pagos online
- **Facturación CFDI:** sat.gob.mx/factura
- **Tipo de cambio:** sat.gob.mx/tipo_cambio

### Referencias Legales
- LISR (Ley del Impuesto sobre la Renta): Art. 25, 28, 90–93 para PF actividades empresariales
- LIVA (Ley del IVA): Art. 1–9 para servicios
- CFF (Código Fiscal de la Federación): Sanciones y procedimientos

---

## Prohibitions
- No asesorar sobre IVA (Impuesto al Valor Agregado) — requiere skill separada de IVA México
- No asesorar sobre ISR de personas morales (empresas) — esta skill cubre personas físicas únicamente
- No asesorar sobre IMSS patronal en detalle — requiere análisis de nómina separado
- No asesorar sobre regímenes especiales como FIBRAS, SOFOMES u otros regímenes financieros
- No garantizar que el SAT acepte deducciones específicas — cada situación puede ser auditada

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. Mexican tax law is administered by the Servicio de Administración Tributaria (SAT). Clients should consult a Contador Público Certificado (CPC) registered with the IMCP (Instituto Mexicano de Contadores Públicos) for advice specific to their circumstances. Tax brackets, rates, UMA values, and deduction limits change annually — verify current rules at sat.gob.mx.
