# Leitura de PDF em Áudio

Este projeto contém um script em Python que extrai o texto de um arquivo PDF, conta o número de caracteres no texto e lê o texto em áudio usando a biblioteca Google Text-to-Speech (gTTS).

**Adendo:** Este projeto foi desenvolvido em Windows, portanto as instruções são específicas para este sistema operacional.

## Requisitos

- Python 3.6 ou superior
- As seguintes bibliotecas Python:
  - pdfplumber
  - gTTS

## Instalação

1. Clone este repositório ou baixe o arquivo ZIP e extraia-o para o seu diretório preferido.

2. Instale as bibliotecas necessárias usando `pip`:

    ```
    pip install pdfplumber gtts
    ```

3. Você pode precisar instalar um player de MP3 como `mpg321` para reproduzir o arquivo de áudio gerado. Para instalar o `mpg321`, faça o download e a instalação apropriados para o seu sistema Windows.

## Uso

1. Coloque o arquivo PDF que você deseja processar no mesmo diretório do script.

2. Edite o script e substitua o nome do PDF do projeto pelo nome do seu arquivo PDF.

3. Execute o script usando Python:

    ```
    python file.py
    ```

4. O script vai:
    - Extrair o texto do PDF.
    - Contar o número de caracteres no texto extraído.
    - Converter o texto em um arquivo de áudio MP3 chamado `audio.mp3`.
    - Reproduzir o arquivo de áudio gerado.