import pandas as pd

SKILLS = [
    "python",
    "sql",
    "docker",
    "airflow",
    "spark",
    "kafka",
    "aws",
    "azure",
    "gcp",
    "git",
    "postgresql",
    "snowflake",
    "databricks"
]


def analyze_skills():
    df = pd.read_csv("data/processed/jobs_clean.csv")

    skill_counts = {}

    text_data = (
        df["description"].astype(str)
        + " "
        + df["tags"].astype(str)
    ).str.lower()

    for skill in SKILLS:
        count = text_data.str.contains(skill, na=False).sum()
        skill_counts[skill] = count

    result_df = (
        pd.DataFrame(
            skill_counts.items(),
            columns=["skill", "count"]
        )
        .sort_values("count", ascending=False)
    )

    print("\n=== Top compétences demandées ===\n")
    print(result_df)

    result_df.to_csv(
        "data/processed/skills_analysis.csv",
        index=False
    )


if __name__ == "__main__":
    analyze_skills()