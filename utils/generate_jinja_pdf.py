import subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def generate_jinja_pdf(template_path: str, variables: dict, output_name: str):
    template_file = Path(template_path)

    # Pasta de saída sempre ./PDFs relativa ao script
    output_dir = (Path(__file__).parent / "../PDFs").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(template_file.parent),
        autoescape=False,
        block_start_string="{%",
        block_end_string="%}",
        variable_start_string="{{",
        variable_end_string="}}",
    )

    template = env.get_template(template_file.name)

    # Renderiza o conteúdo do LaTeX com as variáveis
    conteudo_renderizado = template.render(variables)

    # Salva o arquivo gerado na pasta PDFs
    tex_final = output_dir / f"{output_name}.tex"
    tex_final.write_text(conteudo_renderizado, encoding="utf-8")

    # Compila para PDF dentro da pasta PDFs
    try:
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_final.name],
            cwd=output_dir,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Erro na compilação do PDF: {e}")

    # Remove arquivos auxiliares
    for ext in [".aux", ".log", ".out", ".tex"]:
        arq = output_dir / f"{output_name}{ext}"
        if arq.exists():
            arq.unlink()

    print(f"PDF gerado: {output_dir / f'{output_name}.pdf'}")
