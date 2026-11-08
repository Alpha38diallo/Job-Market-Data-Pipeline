import pandas as pd
from pathlib import Path


def transform_jobs():
    input_file = "data/raw/jobs_raw.csv"
    output_file = "data/processed/jobs_clean.csv"

    df = pd.read_csv(input_file)

    # Suppression des doublons
    df = df.drop_duplicates()

    # Gestion des valeurs manquantes
    df = df.fillna("Unknown")

    # Standardisation des colonnes
    df.columns = [col.lower().strip() for col in df.columns]

    # Uniformisation des textes
    text_columns = ["title", "company", "location", "description"]

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    df.to_csv(output_file, index=False)

    print(f"{len(df)} offres nettoyées sauvegardées dans {output_file}")


if __name__ == "__main__":
    transform_jobs()