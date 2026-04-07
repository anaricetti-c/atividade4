import pdfplumber as pb
import re

i = 0
cpf = []
with pb.open("licitacao.pdf") as pdf:
    for pagina in pdf.pages:
        pagina_limpa = pagina.extract_text().replace("76.105.543/0001-35","")
        if re.search(r"\d{3}\.\d{3}\.\d{3}-\d{2}",pagina_limpa)!=None:
            cpf = cpf + re.findall(r"\d{3}\.\d{3}\.\d{3}-\d{2}",pagina_limpa)
        i+=1

print (cpf)
