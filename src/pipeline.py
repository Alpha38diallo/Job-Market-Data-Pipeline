import logging
import logger_config

from extract import extract_jobs
from transform import transform_jobs
from analysis import analyze_skills
from load import load_data

def run_pipeline():
    logging.info("Début du pipeline")

    extract_jobs()
    logging.info("Extraction terminée")

    transform_jobs()
    logging.info("Transformation terminée")

    analyze_skills()
    logging.info("Analyse terminée")

    load_data()
    logging.info("Chargement terminé")

    logging.info("Pipeline terminé avec succès")

    print("Pipeline terminé avec succès.")


if __name__ == "__main__":
    run_pipeline()