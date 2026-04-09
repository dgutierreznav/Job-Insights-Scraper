# Job-Insights-Scraper

## Descripción
Este proyecto es un **Pipeline de Datos completo (ETL)** diseñado para extraer, procesar y analizar ofertas de empleo para el perfil de **Data Analyst**. El sistema automatiza la recopilación de datos desde portales de empleo (actualmente configurado para Tecnoempleo), limpia la información mediante técnicas de ingeniería de datos y la almacena de forma estructurada para su posterior análisis.

El objetivo principal es identificar qué empresas están contratando más, qué ciudades lideran la demanda y qué modalidades de trabajo (remoto/híbrido) son predominantes en el sector tecnológico.

---

## Características Técnicas
- **Extracción (Scraping):**
      - Uso de `BeautifulSoup` y `Requests` con gestión de cabeceras para una extracción eficiente y ética.
- **Paginación Automática:**
     - Capacidad para escalar el scraping a múltiples páginas de resultados de forma iterativa.
- **Transformación de Datos (Cleaning):**
     - Limpieza de strings, eliminación de ruidos (tabulaciones, saltos de línea) y normalización de nombres mediante **Regex** y **Pandas**.
- **Almacenamiento (SQL):**
     - Implementación de persistencia de datos en una base de datos relacional **SQLite** y exportación paralela a formato **CSV**.
- **Visualización de Datos:**
     - Generación de insights mediante un **Jupyter Notebook** interactivo con gráficas de tendencias.

---

## Stack Tecnológico

- **Lenguaje:** `Python 3.12`
- **Librerías:** `Pandas`, `BeautifulSoup4`, `Requests`, `Matplotlib`, `SQLite3`
- **Entorno:** `VS Code` / `Jupyter Notebooks`

---

## Estructura del Proyecto

```
BUSCADOR_EMPLEO/
├── buscador_tecnoempleo.py
├── data/
│   ├── empleos_tech.db
│   └── ofertas_tecnoempleo.csv
├── notebooks/
│   └── analisis_visual.ipynb
└── requirements.txt
```

---

## Instalación y Uso

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/Job-Insights-Scraper.git](https://github.com/TU_USUARIO/Job-Insights-Scraper.git)

2. Instala las librerías necesarias:
   ```bash
   pip install -r requirements.txt

3. Ejecuta el extractor de datos:
   ```bash
   python src/buscador_tecnoempleo.py

---

## Adaptar este ScrapeR a otros portales de empleo

El código ha sido diseñado de forma modular para facilitar su adaptación a otras webs de empleo (LinkedIn, Indeed, etc.):
  
  **1. Mapeo de Clases**:
      - Identifica el contenedor principal de la oferta y las clases de los elementos (título, empresa, info).
      
  **2. Actualización de Selectores**:
      - Cambia los parámetros en la función `extraer_datos_oferta` (etiquetas `div`, `a`, `span`).
      
  **3. Ajuste de URL**:
      - Modifica la estructura de la URL base y el parámetro de paginación (ej: `&page=` en lugar de `&pagina=`).

---

## Visualizaciones e Insights

A través del análisis realizado en el Notebook, se pueden obtener métricas como:

  **- Top 10 Empresas con más vacantes:** Identificación de los principales empleadores en el sector.
  **- Distribución Geográfica:** Mapa de calor de las ciudades con mayor oferta.
  **- Análisis de Modalidad:** Porcentaje de ofertas 100% remoto vs. modelos híbridos.
