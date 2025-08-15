from concurrent.futures import ProcessPoolExecutor
import asyncio
from pathlib import Path
import json
from utils.clean_output_directory import clean_output_directory
from utils.generate_jinja_pdf import generate_jinja_pdf
from utils.translate_json import translate_json
from utils.generate_readme import generate_readme


if __name__ == "__main__":
    templates_path = Path("./templates")
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    name = dados["personalInformation"]["name"]
    first_name = name.split()[0]
    sur_name = name.split()[1:]
    dados["firstName"] = first_name
    dados["surName"] = " ".join(sur_name)

    translations = dados.get("translations", {})

    clean_output_directory(Path("./PDFs"))

    for translation in translations:
        if translation["value"] == dados.get("language"):
            dados_traduzidos = dados
        else:
            dados_traduzidos = asyncio.run(translate_json(dados, src=dados.get("language"), dest=translation["value"]))
        with ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(
                    generate_jinja_pdf,
                    templates_path / template / f"{template}.tex.template",
                    dados_traduzidos,
                    output_name=f"{first_name} - {template} - {translation['name']}",
                )
                for template in dados["templates"]
            ]

            for f in futures:
                f.result()

    # Gera o README.md
    generate_readme(
        template_path="templates/README.md.template",
        output_path="README.md",
        pdf_folder="PDFs"
    )