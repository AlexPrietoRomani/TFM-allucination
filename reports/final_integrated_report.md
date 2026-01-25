# Reporte Final Integrado: Chatbot Arándanos (V0 vs V1)

**Fecha Ejecución**: 2026-01-24T18:44:30.831036
**Modelo Evaluado**: gpt-oss:20b
**Total Preguntas Evaluadas**: 2

## 1. Resumen de Desempeño

| Métrica | V0 (Baseline) | V1 (RAG) | Delta/Score |
|---|---|---|---|
| **Latencia** | 130.71s | 42.23s | -88.48s |
| **Tasa de Citación** | N/A | 0.0% | - |
| **Fidelidad (Faithfulness)** | - | 1.00 | 0.0 - 1.0 |
| **Relevancia Contextual** | - | 1.00 | 0.0 - 1.0 |
| **FactScore (Hechos)** | - | 1.00 | 0.0 - 1.0 |


## 2. Detalle de Respuestas y Evaluación

### Q1: Según los Lineamientos MIP de SENASA, ¿qué debe especificarse obligatoriamente en el “Plan de Manejo Fitosanitario para el control de plagas” (Anexo 1.2) y qué instrucción operativa indica el documento sobre cómo usar ese mismo formato durante la campaña y para auditorías?

**📚 V1 (RAG) Generado** ⚠️
> **Información obligatoria que debe aparecer en el “Plan de Manejo Fitosanitario para el control de plagas” (Anexo 1.2)**  
> - Nombre del ingrediente activo utilizado.  
> - Fecha de aplicación.  
> - Dosis (cantidad) del agroquímico aplicado durante el período de crecimiento.  
> 
> (Conforme a lo exigido en el registro de control de plagas que debe contener “nombre de ingrediente activo, fecha de aplicación y dosis del agroquímico” – *Lineamientos para Exportación de Arándanos a China* ID lineamientos‑sag‑china‑2015).
> 
> ---
> 
> **Instrucción operativa sobre el uso de ese mismo formato durante la campaña y para auditorías**  
> - El plan debe ser llenado y validado con el nombre y la firma de un profesional o técnico con conocimientos fitosanitarios.  
> - Se debe mantener como registro durante toda la campaña (desde la floración hasta la cosecha) y entregarlo a AQSIQ cuando sea solicitado, para auditoría de la autoridad de control fitosanitario (AQSIQ).  
> - Además, el plan sirve para el monitoreo continuo de plagas y enfermedades de preocupación, asegurando que todas las actividades de control se documenten y estén disponibles para revisión.  
> 
> (Indicaciones contenidas en el mismo *Lineamientos para Exportación de Arándanos a China* ID lineamientos‑sag‑china‑2015).

**Evaluación de Calidad:**

---

### Q2: En los Lineamientos MIP de SENASA (Control cultural/mecánico), ¿cada cuántos días como mínimo debe realizarse el recojo de frutos caídos y a qué profundidad (cm) deben enterrarse, específicamente para cultivos hospedantes de moscas de la fruta?

**📚 V1 (RAG) Generado** ⚠️
> I don't have enough information in my documents to answer this.

**Evaluación de Calidad:**
- **Fidelidad**: 1.00 _(La respuesta afirma que en cultivos hospedantes de moscas de la fruta el recojo y entierro de frutos caídos debe realizarse al menos cada 7 días y enterrarse por debajo de 20 cm, exactamente lo que indica el apartado de "Control cultural/mecánico" en el contexto. No se incluye ninguna afirmación no respaldada por el material proporcionado.)_
- **Relevancia**: 1.00 _(El contexto recuperado incluye exactamente la información solicitada: se indica que en cultivos hospedantes de moscas de la fruta el recojo de frutos caídos debe hacerse al menos cada 7 días y que los frutos deben enterrarse a una profundidad de 20 cm.)_
- **FactScore**: 1.00 (4.0/4.0 claims)
  - *Desglose de Hechos:*
    - `[{'claim': 'El control cultural/mecánico es una práctica establecida en los Lineamientos del Manejo Integrado de Plagas (MIP) de SENASA.', 'label': 'Soportado', 'reason': 'El contexto describe explícitamente un apartado llamado "Control cultural/mecánico" dentro de los Lineamientos del Manejo Integrado de Plagas (MIP) de SENASA, indicando que es una práctica establecida.'}, {'claim': 'El control cultural/mecánico del MIP se aplica en cultivos hospedantes de moscas de la fruta.', 'label': 'Soportado', 'reason': 'El contexto indica explícitamente que el control cultural/mecánico se debe aplicar en los cultivos hospedantes de moscas de la fruta, describiendo acciones como el recojo y entierro de frutos caídos.'}, {'claim': 'La recolección de frutos caídos debe realizarse al menos cada 7 días.', 'label': 'Soportado', 'reason': 'El contexto indica que el recojo y entierro de frutos caídos debe realizarse al menos cada 7 días.'}, {'claim': 'Los frutos caídos deben enterrarse a una profundidad de por debajo de 20\u202fcm de la superficie del suelo.', 'label': 'Soportado', 'reason': 'El contexto indica que los frutos caídos deben enterrarse por debajo de 20\u202fcm de la superficie del suelo, coincidiendo con la afirmación.'}]`

---

