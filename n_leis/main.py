import pdfplumber as pb
import re

i = 0
lista_leis = [] 


regex_padrao = r"[Nn]º?\s*(\d+[\/\-]\d+)"

with pb.open("licitacao.pdf") as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            # Mantém a sua limpeza de CNPJ
            pagina_limpa = texto.replace("76.105.543/0001-35", "")
            
            # O findall agora ignora maiúsculas/minúsculas com re.IGNORECASE
            achados = re.findall(regex_padrao, pagina_limpa, re.IGNORECASE)
            lista_leis.extend(achados)
            
            i += 1

print("Números encontrados:")
print(lista_leis)
