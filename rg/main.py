import pdfplumber as pb
import re

i = 0
rg = []
with pb.open("licitacao.pdf") as pdf:
    for pagina in pdf.pages:
        pagina_limpa = pagina.extract_text().replace("76.105.543/0001-35","")
        if re.search(r"\d{2}\.\d{3}\.\d{3}-\d{2}",pagina_limpa)!=None:
            rg = rg + re.findall(r"\d{2}\.\d{3}\.\d{3}-\d{2}",pagina_limpa)
        i+=1

print (rg)
