import requests
import pandas as pd
from pathlib import Path


URL = "https://www.arbeitnow.com/api/job-board-api"


def extract_jobs():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    jobs = data["data"]

    df = pd.DataFrame(
        [
            {
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "remote": job.get("remote"),
                "job_type": job.get("job_types"),
                "tags": job.get("tags"),
                "description": job.get("description"),
                "created_at": job.get("created_at"),
            }
            for job in jobs
        ]
    )

    Path("data/raw").mkdir(parents=True, exist_ok=True)

    output_file = "data/raw/jobs_raw.csv"
    df.to_csv(output_file, index=False)

    print(f"{len(df)} offres sauvegardées dans {output_file}")


if __name__ == "__main__":
    extract_jobs()