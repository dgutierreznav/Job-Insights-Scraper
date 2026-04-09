import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import re
import time

# --- MODULARIZACIÓN (Funciones independientes) ---

def obtener_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error al acceder a {url}: {e}")
        return None

def limpiar_texto(texto):
    if not texto: return "N/A"
    # Quitamos tabulaciones, saltos de línea y espacios dobles
    limpio = re.sub(r'\s+', ' ', texto).strip()
    return limpio

def extraer_datos_oferta(oferta):
    try:
        tag_titulo = oferta.find('a', class_='text-cyan-700')
        titulo = tag_titulo.text.strip()
        link = tag_titulo['href']
        empresa = oferta.find('a', class_='text-primary').text.strip()
        
        # Limpieza profunda de la info (Ciudad, Fecha, etc.)
        info_sucia = oferta.find('span', class_='text-gray-800').text
        info_limpia = limpiar_texto(info_sucia)
        
        return {
            "puesto": titulo,
            "empresa": empresa,
            "info_completa": info_limpia,
            "enlace": link
        }
    except:
        return None

# --- PAGINACIÓN (Escalabilidad) ---

def ejecutar_pipeline(paginas=3):
    todas_las_ofertas = []
    
    for p in range(1, paginas + 1):
        print(f"Extrayendo página {p}...")
        url = f"https://www.tecnoempleo.com/busqueda-empleo.php?te=data+analyst&pagina={p}"
        soup = obtener_soup(url)
        
        if soup:
            ofertas_html = soup.find_all('div', class_='row fs--15')
            for item in ofertas_html:
                datos = extraer_datos_oferta(item)
                if datos:
                    todas_las_ofertas.append(datos)

        time.sleep(1) 
    
    return pd.DataFrame(todas_las_ofertas)

# --- PERSISTENCIA EN SQL ---

def guardar_en_sql(df):
    conn = sqlite3.connect('data/empleos_tech.db')
    df.to_sql('ofertas', conn, if_exists='replace', index=False)
    conn.close()
    print("¡Datos guardados en la base de datos SQL (empleos_tech.db)!")

# --- MAIN ---

if __name__ == "__main__":
    # Extraer y Modular
    df_empleos = ejecutar_pipeline(paginas=3) 
    
    if not df_empleos.empty:
        # Limpieza extra: Separar ciudad si es posible
        df_empleos['ciudad'] = df_empleos['info_completa'].str.split('(').str[0].str.strip()
        
        # Guardar
        guardar_en_sql(df_empleos)
        df_empleos.to_csv('data/ofertas_tecnoempleo.csv', index=False, encoding='utf-8-sig')
        print(f"Proceso finalizado. {len(df_empleos)} ofertas procesadas.")