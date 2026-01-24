# Reporte Comparativo V0 (Baseline) vs V1 (RAG)

**Total Preguntas**: 10

## Latencia Promedio
- V0: 3.68s
- V1: 3.68s
- Impacto RAG: +0.00s

## Calidad Heurística
- Tasa de Citación en V1: 30.0%

## Detalle por Pregunta

### Q1: ¿Cuál es el REI para Abamectina en arándanos?

**V0 (Baseline)**
> I don't have enough information in my documents to answer this....

**V1 (RAG)**
> I don't have enough information in my documents to answer this....

*Cita detectada: ❌*
---

### Q2: ¿Qué grupo FRAC tiene el uso de Captan?

**V0 (Baseline)**
> Captan está clasificado en el **grupo FRAC M4 (Ftalimidas)**【Source: 2021 Southeast Regional Blueberry Integrated Management Guide (ID: 2021-southeast-blueberry-guide)】....

**V1 (RAG)**
> Captan está clasificado en el **grupo FRAC M4 (Ftalimidas)**【Source: 2021 Southeast Regional Blueberry Integrated Management Guide (ID: 2021-southeast-blueberry-guide)】....

*Cita detectada: ✅*
---

### Q3: ¿Cuál es el PHI del Espinosad en arándano para exportación a USA?

**V0 (Baseline)**
> I don't have enough information in my documents to answer this....

**V1 (RAG)**
> I don't have enough information in my documents to answer this....

*Cita detectada: ❌*
---

### Q4: ¿Está permitido el uso de Clorpirifos en arándanos orgánicos?

**V0 (Baseline)**
> No tengo suficiente información en mis documentos para responder si el clorpirifos está permitido o no en la producción de arándanos orgánicos....

**V1 (RAG)**
> No tengo suficiente información en mis documentos para responder si el clorpirifos está permitido o no en la producción de arándanos orgánicos....

*Cita detectada: ❌*
---

### Q5: ¿Qué fungicidas se recomiendan para Botrytis en floración?

**V0 (Baseline)**
> Los productos que aparecen como opciones de manejo para el **Botrytis (floración)** son:

| Producto (ingredientes activos) | Código FRAC | Dosis recomendada | Momento de aplicación |
|--------------------------------|-------------|-------------------|-----------------------|
| **Cyprodinil + Fludio...

**V1 (RAG)**
> Los productos que aparecen como opciones de manejo para el **Botrytis (floración)** son:

| Producto (ingredientes activos) | Código FRAC | Dosis recomendada | Momento de aplicación |
|--------------------------------|-------------|-------------------|-----------------------|
| **Cyprodinil + Fludioxonil** (Switch 62.5 WG) | FRAC 9 + 12 | 11 – 14 oz / acre | Primera aplicación al inicio de la floración; aplicaciones subsecuentes cada 7‑10 días durante la floración. No superar 56 oz / acre/año y ...

*Cita detectada: ✅*
---

### Q6: ¿Cuál es el límite máximo de residuos (MRL) de Azoxistrobina en la UE?

**V0 (Baseline)**
> I don't have enough information in my documents to answer this....

**V1 (RAG)**
> I don't have enough information in my documents to answer this....

*Cita detectada: ❌*
---

### Q7: ¿El Fenhexamid tiene efecto curativo o preventivo?

**V0 (Baseline)**
> I don't have enough information in my documents to answer this....

**V1 (RAG)**
> I don't have enough information in my documents to answer this....

*Cita detectada: ❌*
---

### Q8: ¿Cuántas aplicaciones máximas de Switch 62.5 WG se permiten por temporada?

**V0 (Baseline)**
> Se pueden hacer **máximo dos aplicaciones** de Switch 62.5 WG en una temporada, ya que el manual indica que “no se deben hacer más de dos aplicaciones secuenciales antes de usar otro fungicida con un MOA diferente” y limita el uso a 56 oz / acre por año【Source: 2021 Southeast Regional Blueberry Inte...

**V1 (RAG)**
> Se pueden hacer **máximo dos aplicaciones** de Switch 62.5 WG en una temporada, ya que el manual indica que “no se deben hacer más de dos aplicaciones secuenciales antes de usar otro fungicida con un MOA diferente” y limita el uso a 56 oz / acre por año【Source: 2021 Southeast Regional Blueberry Integrated Management Guide】....

*Cita detectada: ❌*
---

### Q9: ¿Es compatible mezclar Fosetil-Al con cobre?

**V0 (Baseline)**
> No. El fosetil‑Al **no debe mezclarse en tanque con cobre**; la guía indica que “no se debe mezclar en tanque con cobre y fertilizantes foliares” porque puede producir daño al follaje o al fruto【Source: 2021 Southeast Regional Blueberry Integrated Management Guide (ID: 2021-southeast-blueberry-guide...

**V1 (RAG)**
> No. El fosetil‑Al **no debe mezclarse en tanque con cobre**; la guía indica que “no se debe mezclar en tanque con cobre y fertilizantes foliares” porque puede producir daño al follaje o al fruto【Source: 2021 Southeast Regional Blueberry Integrated Management Guide (ID: 2021-southeast-blueberry-guide)】....

*Cita detectada: ✅*
---

### Q10: ¿Qué ingrediente activo controla mejor la Drosophila suzukii?

**V0 (Baseline)**
> I don't have enough information in my documents to answer this....

**V1 (RAG)**
> I don't have enough information in my documents to answer this....

*Cita detectada: ❌*
---

