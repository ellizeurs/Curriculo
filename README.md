# Currículo em LaTeX

Este repositório contém meu currículo desenvolvido em LaTeX, preenchido e traduzido automaticamente com Jinja e Googletrans.

## Como Compilar

Existem duas formas de gerar os PDFs do currículo:

### 1. Localmente (Manual)

1. Certifique-se de ter o LaTeX instalado no seu computador. Recomendamos distribuições como [TeX Live](https://www.tug.org/texlive/) ou [MiKTeX](https://miktex.org/).
2. Navegue até o diretório do repositório.
3. Instale as dependências Python:
   ```bash
   pip install -r requirements.txt
   ````

4. Execute o comando:

   ```bash
   python main.py
   ```
5. Os arquivos PDF serão gerados na pasta `PDFs/`.

### 2. Via GitHub Actions (Automático)

1. Faça um **fork** deste repositório.
2. Edite o arquivo `dados.json` com suas informações pessoais.
3. Ao dar um **push** na sua branch, o workflow será disparado automaticamente.
4. O workflow irá gerar os PDFs atualizados e atualizar o `README.md` com os nomes dos arquivos.
5. Todos os PDFs serão sincronizados na pasta `PDFs/` do seu repositório fork.

## Arquivos gerados

- [Ellizeu - ATSFriendly - English.pdf](https://github.com/ellizeurs/Curriculo/blob/main/PDFs/Ellizeu%20-%20ATSFriendly%20-%20English.pdf)
- [Ellizeu - ATSFriendly - Español.pdf](https://github.com/ellizeurs/Curriculo/blob/main/PDFs/Ellizeu%20-%20ATSFriendly%20-%20Espa%C3%B1ol.pdf)
- [Ellizeu - ATSFriendly - Português.pdf](https://github.com/ellizeurs/Curriculo/blob/main/PDFs/Ellizeu%20-%20ATSFriendly%20-%20Portugu%C3%AAs.pdf)
- [Ellizeu - CleanCV - English.pdf](https://github.com/ellizeurs/Curriculo/blob/main/PDFs/Ellizeu%20-%20CleanCV%20-%20English.pdf)
- [Ellizeu - CleanCV - Español.pdf](https://github.com/ellizeurs/Curriculo/blob/main/PDFs/Ellizeu%20-%20CleanCV%20-%20Espa%C3%B1ol.pdf)
- [Ellizeu - CleanCV - Português.pdf](https://github.com/ellizeurs/Curriculo/blob/main/PDFs/Ellizeu%20-%20CleanCV%20-%20Portugu%C3%AAs.pdf)

## Links Importantes

* [Currículo Lattes](http://lattes.cnpq.br/1344771646421983)
* [Perfil no LinkedIn](https://www.linkedin.com/in/ellizeurs/)