# _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado

with open("emd.csv", "r") as file:
    linhas = file.readlines()
    
data = [linha.strip().split(',') for linha in linhas[1:]]

# 2.1. Lista ordenada alfabeticamente pelas modalidades
modalidades = sorted(set(dado[8] for dado in data)) # dado[8] é a modalidade
with open("resultados.txt", "a") as output_file:
    output_file.write("Lista ordenada alfabeticamente das modalidades desportivas:\n")
    for modalidade in modalidades:
        output_file.write(modalidade + "\n")
    output_file.write("\n___________________________________\n")

# 2.2. Percentagens de atletas aptos e inaptos para a prática desportiva
total_atletas = len(data)
aptos = sum(dado[12] == 'true' for dado in data)
inaptos = total_atletas - aptos
perc_aptos = (aptos/total_atletas) * 100
perc_inaptos = (inaptos/total_atletas) * 100
with open("resultados.txt", "a") as output_file:
    output_file.write("Percentagens de atletas aptos e não aptos para a prática desportiva:\n")
    output_file.write(f"Percentagens de atletas aptos: {perc_aptos}%\n")
    output_file.write(f"Percentagem de atletas inaptos: {perc_inaptos}%\n")
    output_file.write("\n___________________________________\n")

# 2.3. Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35,39], ...
distribuicao_idades = {}
for dado in data:
    idade = int(dado[5])
    intervalo = f"[{idade // 5 * 5}-{idade // 5 * 5 + 4}]"
    distribuicao_idades[intervalo] = distribuicao_idades.get(intervalo, 0) + 1

with open("resultados.txt", "a") as output_file:
    output_file.write("Distribuição de atletas por escalão etário:\n")
    for interval, quantity in sorted(distribuicao_idades.items()):
        output_file.write(f"{interval}: {quantity}\n")
    output_file.write("\n___________________________________\n")