import pdfplumber as pb
import re

i = 0
telefone = []
# Regex corrigida: R$, espaço opcional, milhares, ponto opcional, centenas e centavos
# Esta regex pega formatos como R$ 1.234,56 ou R$ 12,00
regex_valor = r"\(\d{2}\)\s?\d{4,5}-\d{4}"

with pb.open("licitacao.pdf") as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            pagina_limpa = texto.replace("76.105.543/0001-35", "")
            
            achados = re.findall(regex_valor, pagina_limpa)
            telefone.extend(achados)
            
        i += 1

print(telefone)
