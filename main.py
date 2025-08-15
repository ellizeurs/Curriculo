import subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import json

def generate_jinja_pdf(template_path: str, variables: dict, output_name: str = "output"):
    template_file = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(template_file.parent),
        autoescape=False,
        block_start_string="{%",
        block_end_string="%}",
        variable_start_string="{{",
        variable_end_string="}}"
)

    template = env.get_template(template_file.name)

    # Renderiza o conteúdo do LaTeX com as variáveis
    conteudo_renderizado = template.render(variables)

    # Salva o arquivo gerado
    tex_final = template_file.parent.parent / "PDFs" / f"{output_name}.tex"
    tex_final.write_text(conteudo_renderizado, encoding="utf-8")

    # Compila para PDF
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_final.name], cwd=template_file.parent, check=True)

    # Remove arquivos auxiliares
    for ext in [".aux", ".log", ".out"]:
        arq = template_file.parent / f"{output_name}{ext}"
        if arq.exists():
            arq.unlink()

    print(f"PDF gerado: {output_name}.pdf")

if __name__ == "__main__":
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    name = dados["personalInformation"]["name"]
    first_name = name.split()[0]
    sur_name = name.split()[1:]
    dados["firstName"] = first_name
    dados["surName"] = " ".join(sur_name)

    generate_jinja_pdf(
        "templates/ATSFriendly/ATSFriendly.tex.template",
        dados,
        output_name="lista_produtos"
    )
