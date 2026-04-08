import pdfplumber as pb
import re

i = 0
nomes_encontrados = []

# EXPLICAÇÃO DA REGEX:
# (?<=Nome:\s) -> Lookbehind: garante que o texto comece após "Nome: " (e um espaço)
# [A-ZÀ-Ÿ]      -> Primeira letra maiúscula
# [a-zà-ÿ]+     -> Resto da primeira palavra minúscula
# (?:\s(?:da|de|do|dos|e)?\s?[A-ZÀ-Ÿ][a-zà-ÿ]+)* -> Outras palavras com iniciais maiúsculas e conectores
regex_nome_exato = r"(?<=Nome:\s)[A-ZÀ-Ÿ][a-zà-ÿ]+(?:\s(?:da|de|do|dos|e)?\s?[A-ZÀ-Ÿ][a-zà-ÿ]+)*"

# Caso os nomes estejam TODOS EM MAIÚSCULAS após o "Nome: ", use esta:
# regex_nome_exato = r"(?<=Nome:\s)[A-ZÀ-Ÿ\s]+"

with pb.open("licitacao.pdf") as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            # Mantemos a limpeza padrão
            pagina_limpa = texto.replace("76.105.543/0001-35", "")
            
            # re.IGNORECASE pode ser usado se "Nome:" variar para "nome:"
            achados = re.findall(regex_nome_exato, pagina_limpa)
            
            for nome in achados:
                nome_limpo = nome.strip() # Remove espaços extras no fim
                if nome_limpo and nome_limpo not in nomes_encontrados:
                    nomes_encontrados.append(nome_limpo)
            
        i += 1

print("Nomes extraídos com sucesso:")
print(nomes_encontrados)
