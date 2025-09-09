from pathlib import Path
import os

def clean_output_directory(output_dir: Path):
    """
    Remove all files in the output directory except for the PDF files.
    """
    for file in output_dir.iterdir():
        os.remove(file) if file.is_file() else None
    print(f"Limpando diretório de saída: {output_dir}")
