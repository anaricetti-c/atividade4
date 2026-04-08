import pdfplumber as pb
import re

i = 0
dinheiro = []
# Regex corrigida: R$, espaço opcional, milhares, ponto opcional, centenas e centavos
# Esta regex pega formatos como R$ 1.234,56 ou R$ 12,00
regex_valor = r"R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}"

with pb.open("licitacao.pdf") as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            pagina_limpa = texto.replace("76.105.543/0001-35", "")
            
            achados = re.findall(regex_valor, pagina_limpa)
            dinheiro.extend(achados)
            
        i += 1

print(dinheiro)
