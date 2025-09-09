from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from urllib.parse import quote

def generate_readme(dados: dict, template_path: str, output_path: str, pdf_folder: str):
    template_file = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(template_file.parent),
        autoescape=False
    )
    template = env.get_template(template_file.name)

    # Pega todos os PDFs gerados
    pdfs = sorted(Path(pdf_folder).glob("*.pdf"))
    files_list = "\n".join([f"- [{pdf.name}](https://github.com/ellizeurs/Curriculo/blob/main/PDFs/{quote(pdf.name)})" for pdf in pdfs])

    # Renderiza o template
    content = template.render(FILES=files_list, LINKEDIN=dados["personalInformation"].get("linkedin", ""), LATTES=dados["personalInformation"].get("lattes", ""))

    # Salva o README.md
    Path(output_path).write_text(content, encoding="utf-8")
    print(f"README gerado: {output_path}")