import pdfplumber as pb
import re

i = 0
cnpjs = []
with pb.open("licitacao.pdf") as pdf:
    for pagina in pdf.pages:
        pagina_limpa = pagina.extract_text().replace("76.105.543/0001-35","")
        if re.search(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}",pagina_limpa)!=None:
            cnpjs = cnpjs + re.findall(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}",pagina_limpa)
        print(i)
        i+=1

print(cnpjs)
