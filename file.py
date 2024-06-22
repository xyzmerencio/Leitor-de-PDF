import pdfplumber
from gtts import gTTS
import os

def extrair_texto_pdf(caminho_pdf):
    texto_completo = ""

    if not texto_completo:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_completo += texto

    return texto_completo

def contar_caracteres(texto):
    return len(texto)

def ler_texto(texto, lingua='pt'):
    tts = gTTS(text=texto, lang=lingua)
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")


# Alterar de acordo com o PDF desejado
caminho_pdf = 'imperialismo_pagao.pdf'

texto_pdf = extrair_texto_pdf(caminho_pdf)
numero_de_caracteres = contar_caracteres(texto_pdf)

print(f'Total de caracteres: {numero_de_caracteres}')

ler_texto(texto_pdf)
