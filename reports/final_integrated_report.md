# Reporte Final Integrado: Chatbot Arándanos (V0 vs V1 vs V2)

**Fecha Ejecución**: 2026-01-24 22:29:13.173870
**Total Preguntas**: 2

## 1. Resumen Comparativo de Desempeño

| Métrica | V0 (Baseline) | V1 (RAG) | V2 (Agente) |
|---|---|---|---|
| **Latencia (s)** | 130.71 | 42.23 | 44.97 |
| **Fidelidad (0-1)** | N/A | 1.00 | 0.93 |
| **FactScore** | N/A | 1.00 | N/A (Internal) |


## 2. Detalle por Pregunta

### Q1: Según los Lineamientos MIP de SENASA, ¿qué debe especificarse obligatoriamente en el “Plan de Manejo Fitosanitario para el control de plagas” (Anexo 1.2) y qué instrucción operativa indica el documento sobre cómo usar ese mismo formato durante la campaña y para auditorías?

**V1 (RAG)** [Fidelidad: nan]
> **Información obligatoria que debe aparecer en el “Plan de Manejo Fitosanitario para el control de plagas” (Anexo 1.2)**  
>- Nombre del ingrediente activo utilizado.  
>- Fecha de aplicación.  
>- Dosis (cantidad) del agroquímico aplicado durante el período de crecimiento.  
>
>(Conforme a lo exigido en el registro de control de plagas que debe contener “nombre de ingrediente activo, fecha de aplicación y dosis del agroquímico” – *Lineamientos para Exportación de Arándanos a China* ID lineamientos‑sag‑china‑2015).
>
>---
>
>**Instrucción operativa sobre el uso de ese mismo formato durante la campaña y para auditorías**  
>- El plan debe ser llenado y validado con el nombre y la firma de un profesional o técnico con conocimientos fitosanitarios.  
>- Se debe mantener como registro durante toda la campaña (desde la floración hasta la cosecha) y entregarlo a AQSIQ cuando sea solicitado, para auditoría de la autoridad de control fitosanitario (AQSIQ).  
>- Además, el plan sirve para el monitoreo continuo de plagas y enfermedades de preocupación, asegurando que todas las actividades de control se documenten y estén disponibles para revisión.  
>
>(Indicaciones contenidas en el mismo *Lineamientos para Exportación de Arándanos a China* ID lineamientos‑sag‑china‑2015).

**V2 (Agente)** [Fidelidad: 0.95 | Retries: 0]
> En los arándanos la larva de **Proeulia spp.** provoca un **daño externo al fruto**, manifestándose como heridas o manchas visibles en la superficie de la baya. Este daño se observa principalmente en la **zona exterior (piel o exocarpio) del arándano**.

---

### Q2: En los Lineamientos MIP de SENASA (Control cultural/mecánico), ¿cada cuántos días como mínimo debe realizarse el recojo de frutos caídos y a qué profundidad (cm) deben enterrarse, específicamente para cultivos hospedantes de moscas de la fruta?

**V1 (RAG)** [Fidelidad: 1.00]
> I don't have enough information in my documents to answer this.

**V2 (Agente)** [Fidelidad: 0.90 | Retries: 0]
> **Cálculo del factor de cobertura (Fc)**  
>
>1. **Paso 1 – Determinar el porcentaje de cobertura (Pc)**  
>   \[
>   Pc=\frac{X}{Eh}
>   \]
>   donde  
>   * **X** = área sombreada (o ancho de follaje) en metros.  
>   * **Eh** = espaciamiento entre hileras en metros.  
>
>2. **Paso 2 – Convertir Pc a Fc**  
>   \[
>   Fc = 0.92 \times Pc + 0.187
>   \]
>   Esta ecuación es la que se utiliza en el Manual de Arándano y se deriva de un promedio de varias formas de estimación de la cobertura del follaje.
>
>---
>
>### Coeficientes de cultivo (Kc) recomendados (zona central de Chile)
>
>| Rango de meses | Kc |
>|----------------|----|
>| **Junio – Agosto** | **0.7** (se aplica también a junio, pues la tabla no ofrece un valor distinto) |
>| **Septiembre** | **0.7** |
>| **Octubre – Noviembre** | **0.8** (Octubre) y **0.9** (Noviembre) |
>| **Diciembre – Febrero** | **1.0** (para los tres meses) |
>
>> *Fuente*: Cuadro 5.1 del Manual de Arándano – Coeficientes de cultivo de arándano para la zona central de Chile.
>
>---
>
>#### Resumen rápido
>
>- **Fc** se obtiene con `Fc = 0.92 × (X/Eh) + 0.187`.
>- Los **Kc** recomendados según el mes son:
>  * 0.7 (Jun‑Ago y Sept).
>  * 0.8 (Oct) / 0.9 (Nov).
>  * 1.0 (Dic‑Feb).
>
>Con estos valores, la ecuación de evapotranspiración del cultivo `ETc = ET0 × Kc × Fc` puede aplicarse de forma precisa a las plantaciones de arándanos en la zona central de Chile.

---

