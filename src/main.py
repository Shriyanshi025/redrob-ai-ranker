from src.config.constants import DATA_DIR
from src.core.job_analyzer import JobAnalyzer
from src.core.job_loader import load_job_description
from src.config.constants import JOB_DESCRIPTION_PATH


def main():

    job_text = load_job_description(JOB_DESCRIPTION_PATH)

    analyzer = JobAnalyzer()

    requirements = analyzer.parse(job_text)

    print(requirements)


if __name__ == "__main__":
    main()