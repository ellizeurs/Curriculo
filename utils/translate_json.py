import re
from googletrans import Translator

async def translate_json(data, src="pt", dest="en"):
    translator = Translator()
    pattern = re.compile(r'(\{\{.*?\}\}|\\\{.*?\\\})')  # preserva {{...}} e \{...\}

    async def translate_value(value, key=None):
        if key in ["icon","linkedin", "github"]:
            return value

        if isinstance(value, str) and value.strip():
            # encontra todas as partes a preservar
            matches = pattern.findall(value)
            placeholders = {}
            temp_text = value

            for i, match in enumerate(matches):
                ph = f"_{i}_"
                placeholders[ph] = match
                temp_text = temp_text.replace(match, ph)

            # traduz o texto
            result = await translator.translate(temp_text, src=src, dest=dest)
            translated = result.text

            # restaura exatamente os placeholders originais
            for ph, original in placeholders.items():
                translated = translated.replace(ph, original)

            return translated

        elif isinstance(value, dict):
            return {k: await translate_value(v, k) for k, v in value.items()}
        elif isinstance(value, list):
            return [await translate_value(v) for v in value]
        else:
            return value

    return await translate_value(data)
