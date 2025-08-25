import requests
import pandas as pd
from pathlib import Path

# URL del dataset EVOA (Explotación de oro de aluvión por municipio)
BASE_URL = "https://www.datos.gov.co/resource/g48d-yu62.json"

# Carpeta donde guardaremos los CSV/Excel
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def fetch_data(limit=50000) -> pd.DataFrame:
    """
    Extrae datos desde la API de datos.gov.co con paginación
    y devuelve un DataFrame con todas las filas.
    """
    all_data = []
    offset = 0

    while True:
        url = f"{BASE_URL}?$limit={limit}&$offset={offset}"
        resp = requests.get(url)
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        all_data.extend(batch)
        offset += limit

    df = pd.DataFrame(all_data)
    print("Shape final:", df.shape)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpieza y transformación del DataFrame.
    Convierte columnas numéricas y elimina nulos en campos clave.
    """
    numeric_cols = [
        "a_o",
        "hectareas_con_permisos",
        "hectareas_en_transito_a",
        "hectareas_explotacion_ilicita",
        "total_evidencia_explotacion",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Quitar filas sin año, departamento o municipio
    subset_cols = [c for c in ["a_o", "departamento", "municipio"] if c in df.columns]
    if subset_cols:
        df = df.dropna(subset=subset_cols)

    return df


def save_to_csv(df: pd.DataFrame, filename: str = "mineria_ilegal.csv") -> Path:
    """
    Guarda el DataFrame en formato CSV en la carpeta data/.
    """
    path = DATA_DIR / filename
    df.to_csv(path, index=False, encoding="utf-8-sig")
    return path


def top_departamentos_ilicita(df: pd.DataFrame, n: int = 10) -> pd.Series:
    """
    Retorna los top n departamentos por hectáreas de explotación ilícita.
    """
    if (
        "departamento" not in df.columns
        or "hectareas_explotacion_ilicita" not in df.columns
    ):
        print("[WARN] Columnas necesarias no encontradas en el DataFrame")
        return pd.Series()

    return (
        df.groupby("departamento")["hectareas_explotacion_ilicita"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )
