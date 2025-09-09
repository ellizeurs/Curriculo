from pathlib import Path
import json
from utils.clean_output_directory import clean_output_directory
from utils.generate_all_pdfs import generate_all_pdfs
from utils.generate_readme import generate_readme



if __name__ == "__main__":
    templates_path = Path("./templates")
    output_path = Path("./PDFs")
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    print("Iniciando geração de PDFs...")

    if output_path.exists() and not output_path.is_dir():
        raise NotADirectoryError(f"O caminho {output_path} existe e não é um diretório.")
    elif not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)

    # Limpa o diretório de saída
    clean_output_directory(output_path)

    # Gera os PDFs
    generate_all_pdfs(dados, templates_path)

    # Gera o README.md
    generate_readme(
        template_path="templates/README.md.template",
        output_path="README.md",
        pdf_folder=output_path
    )

    print("Arquivos gerados com sucesso.")