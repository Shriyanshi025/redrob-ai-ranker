from pathlib import Path
from docx import Document


def load_job_description(path: Path) -> str:
    document = Document(path)

    return "\n".join(
        paragraph.text.strip()
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    )
