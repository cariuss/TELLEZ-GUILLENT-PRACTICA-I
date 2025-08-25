from services import (
    fetch_data,
    clean_data,
    save_to_csv,
    top_departamentos_ilicita,
)

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def run_etl():
    # 1. Extraer
    df_raw = fetch_data()
    print(f"[INFO] Datos brutos: {df_raw.shape}")

    # 2. Limpiar/transformar
    df_clean = clean_data(df_raw)
    print(f"[INFO] Datos limpios: {df_clean.shape}")

    # 3. Guardar
    out_path = save_to_csv(df_clean)
    print(f"[INFO] Datos guardados en: {out_path}")

    # 4. Análisis: Top 10 departamentos
    ranking = top_departamentos_ilicita(df_clean, n=10)
    print("\n[INFO] Top 10 departamentos con más hectáreas ilícitas:\n")
    print(ranking)

    # 5. Visualización
    if not ranking.empty:
        ranking.plot(
            kind="bar",
            figsize=(10, 5),
            title="Top 10 Departamentos - Hectáreas ilícitas",
        )
        plt.ylabel("Hectáreas ilícitas")
        plt.xlabel("Departamento")
        plt.tight_layout()
        plt.savefig("data/top10_ilicita.png")
        print("[INFO] Gráfico guardado en data/top10_ilicita.png")

    # 6. Machine Learning sencillo (regresión lineal)
    features = [
        "hectareas_con_permisos",
        "hectareas_en_transito_a",
        "total_evidencia_explotacion",
    ]
    target = "hectareas_explotacion_ilicita"

    # Filtrar datos para ML
    df_ml = df_clean.dropna(subset=features + [target])
    if df_ml.empty:
        print("[WARN] No hay datos suficientes para entrenar modelo ML")
        return df_clean, ranking, None

    X = df_ml[features]
    y = df_ml[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"[INFO] Modelo entrenado. R² en test = {score:.3f}")

    return df_clean, ranking, model
