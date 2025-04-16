# 📊 Scorecard Interactivo en Python con Dash

Este repositorio contiene una **aplicación web interactiva** desarrollada en Python utilizando el framework 🐍 [Dash](https://dash.plotly.com/), que simula un **scorecard** con tendencias, coberturas y comparaciones auditadas de datos para diferentes clientes ficticios.

---

## ✅ ¿Qué es un Scorecard?

Un **Scorecard** es una herramienta de visualización y evaluación que resume métricas clave de desempeño (KPIs) para tomar decisiones estratégicas. Se utiliza ampliamente en:

- 📈 **Business Intelligence (BI)** para monitorear metas, indicadores y resultados por áreas o segmentos.
- 🤖 **Data Science** para modelar tendencias, evaluar calidad de datos, detectar anomalías o analizar comportamiento de usuarios.
- 🧑‍💼 **Áreas Comerciales y de Finanzas** para ver resultados en el tiempo, evaluar cobertura y tomar decisiones ágiles.

---

## 🚀 ¿Qué hace este Scorecard?

Esta aplicación permite:

- 🔍 **Seleccionar un cliente** y visualizar:
  - Su **score individual** mes a mes.
  - Una **tendencia auditada** global del mercado o segmento.
  - Un **indicador de cobertura (%)**, donde:
    - < 100% → **Bajocobertura** (faltan datos o calidad deficiente).
    - 100% → **Cobertura ideal**.
    - > 100% → **Sobrecobertura** (datos duplicados, erróneos o excesivos).

- 📊 **Visualización dual**:
  - Líneas de score y tendencia.
  - Barras con eje secundario para la cobertura.

- 🌐 Estilo limpio, minimalista, colores suaves y diseño responsivo.

---

## ⚙️ ¿Cómo usar este proyecto?

### 1. Clona el repositorio:

```bash
git clone https://github.com/AlbertoMadinRivera/Scorecard-interactivo.git
cd Scorecard-interactivo
