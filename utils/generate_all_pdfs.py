from concurrent.futures import ProcessPoolExecutor
from utils.generate_pdfs_for_translation import generate_pdfs_for_translation

def generate_all_pdfs(dados, templates_path):
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(generate_pdfs_for_translation, dados, translation, templates_path)
            for translation in dados.get("translations", {})
        ]

        for f in futures:
            f.result()