import asyncio
from utils.generate_jinja_pdf import generate_jinja_pdf
from utils.translate_json import translate_json
from concurrent.futures import ProcessPoolExecutor

def generate_pdfs_for_translation(dados, translation, templates_path):
    name = dados["personalInformation"]["name"]
    first_name = name.split()[0]
    sur_name = name.split()[1:]
    dados["firstName"] = first_name
    dados["surName"] = " ".join(sur_name)

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
