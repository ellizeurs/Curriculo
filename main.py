from pathlib import Path
import json
from utils.clean_output_directory import clean_output_directory
from utils.generate_all_pdfs import generate_all_pdfs
from utils.generate_readme import generate_readme



if __name__ == "__main__":
    templates_path = Path("./templates")
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Limpa o diretório de saída
    clean_output_directory(Path("./PDFs"))

    # Gera os PDFs
    generate_all_pdfs(dados, templates_path)

    # Gera o README.md
    generate_readme(
        template_path="templates/README.md.template",
        output_path="README.md",
        pdf_folder="PDFs"
    )