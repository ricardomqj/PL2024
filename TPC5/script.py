import sys
import json
import ply.lex as lex

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'ADICIONAR',
    'SAIR'
)

def t_LISTAR(t):
    r"(LISTAR)"
    return t

def t_MOEDA(t):
    r'MOEDA[ ]+(\s*[1c|2c|5c|10c|20c|50c|1e|2e],?\s)+'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR[ ]A\d+'
    return t

def t_ADICIONAR(t):
    r'ADICIONAR[ ]\w+\d+[ ]?(\d+e\d+c|\d+c|\d+c|\d+e)'
    return t

def t_SAIR(t):
    r'SAIR'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.elexer.skip(1)
    
def vending_machine():
    lexer = lex.lex()
    saldo = 0
    
    for line in sys.stdin:
        lexer.input(line)
        for tok in lexer:
            if(tok.type == "LISTAR"):
                print("cod       |     nome                     |  quantidade   |     preco    ")
                for produto in produtos:
                    print(f"{produto['cod']: <5}     |     {produto['nome']: <20}     |     {produto['quant']: <5}     |     {produto['preco']:<5}    ")
            elif(tok.type == "MOEDA"):
                coins = tok.value.split()[1].split(",")
                for coin in coins:
                    if coin.endswith('e'):
                        saldo += int(coin[:-1]) * 100
                    elif coin.endswith('c'):
                        saldo += int(coin[:-1])
                euros = saldo // 100
                cents = saldo % 100
                print("Saldo = " + f"{euros}e{cents:02d}c")
            elif(tok.type == "SELECIONAR"):
                cod_produto = tok.value.split()[1]
                found = False
                for produto in produtos:
                    if cod_produto == produto['cod']:
                        found = True
                        if produto['quant'] == 0:
                            print("Produto não tem stock!") 
                            break
                        if int(produto['preco']*100) > saldo:
                            print("Saldo insuficiente para satisfazer o seu pedido")
                            euros = saldo // 100
                            cents = saldo % 100
                            preco_produto = int(produto['preco']*100)
                            euros2 = preco_produto // 100
                            cents2 = preco_produto % 100 
                            print(f"Saldo = {euros}e{cents:02d}c; Pedido = {euros2}e{cents2:02d}c")
                            break
                        elif int(produto['preco']*100) <= saldo:
                            print("Pode retirar o produto dispensado " + '" ' + produto['nome'] + ' "')
                            saldo -= int((produto['preco']) * 100)
                            produto['quant']-=1
                            euros = saldo // 100
                            cents = saldo % 100
                            print("Saldo = " + f"{euros}e{cents:02d}c")
                            break
                if found == False:
                    print("Produto não existente em stock!")

            elif(tok.type == "ADICIONAR"):
                name = tok.value.split()[1]
                stock = int(tok.value.split()[2])

                exists = False
                for produto in produtos:
                    if produto['nome'] == name:
                        produto['quant'] += stock
                        exists = True
                        break
                if not exists:
                    id = len(produtos) + 1
                    cod = 'A' + str(id)
                    
                    preco = tok.value.split()[3]
                    
                    euros_str, cents_str = preco.split('e')

                    euros = int(euros_str)
                    cents = int(cents_str[:-1]) 

                    total = euros + cents / 100.0

                    produtos.append({'cod': cod, 'nome': name, 'quant': stock, 'preco': total})
                print(f"Produto {name} adicionado à máquina!")
            
            elif(tok.type == "SAIR"):
                moedas = [2,1,50,20,10,5,2,1]
                quant = [0, 0, 0, 0, 0, 0, 0, 0]
                valores = [200, 100, 50, 20, 10, 5, 2, 1]
                count = 0
                troco = "Troco : "
                
                if saldo == 0:
                    troco += "0c"
                
                while saldo > 0:
                    for i, valor in enumerate(valores):
                        if saldo >= valor:
                            saldo -= valor
                            quant[i] += 1
                            break
                
                while count < len(quant):
                    if count < 2 and quant[count] > 0:
                        troco += f"{moedas[count]}e "
                    elif count >= 2 and quant[count] > 0:
                        troco += f"{moedas[count]}c "
                    count+=1
                print(troco)
                print("Até à próxima!")
                
                jsonData["stock"] = produtos
                with open("vending_stock.json",'w') as arquivo:
                    json.dump(jsonData,arquivo,indent=2)
                    
                sys.exit()
                
if __name__ == "__main__":
    
    file_path = "stock.json"
    
    with open(file_path, 'r') as arquivo:
        jsonData = json.load(arquivo)
        produtos = jsonData["stock"]
        
    vending_machine()