import sqlite3
import pandas as pd


def load_data():
    conn = sqlite3.connect("database/jobs.db")

    jobs_df = pd.read_csv(
        "data/processed/jobs_clean.csv"
    )

    skills_df = pd.read_csv(
        "data/processed/skills_analysis.csv"
    )

    jobs_df.to_sql(
        "jobs",
        conn,
        if_exists="replace",
        index=False
    )

    skills_df.to_sql(
        "skills_analysis",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Données chargées dans database/jobs.db")


if __name__ == "__main__":
    load_data()