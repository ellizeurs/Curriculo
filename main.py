from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import json
from utils.clean_output_directory import clean_output_directory
from utils.generate_pdfs_for_translation import generate_pdfs_for_translation
from utils.generate_readme import generate_readme


if __name__ == "__main__":
    templates_path = Path("./templates")
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    clean_output_directory(Path("./PDFs"))

    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(generate_pdfs_for_translation, dados, translation, templates_path)
            for translation in dados.get("translations", {})
        ]

        for f in futures:
            f.result()


    # Gera o README.md
    generate_readme(
        template_path="templates/README.md.template",
        output_path="README.md",
        pdf_folder="PDFs"
    )