# TPC1: Análise de um Dataset
## 2024-02-12

## Autor:
- A100066
- Ricardo Miguel Queirós de Jesus

## Resumo:

Neste código, um ficheiro csv('emd.cdv') é lido, extraindo para uma lista, as linhas do ficheiro.
Para a lista ordenada alfabeticamente pelas modalidades, é usado simplesmente a função sorted, passando como argumento, um set com as modalidades presentes em cada linha.
Para o o cálculo das percentagens de atletas aptos e inaptos para a prática desportiva, comecei por somar o total de atletas aptos através da coluna 'resultado', e o total de linhas do csv, que me dá o total de atletas presentes no ficheiro. Com estes dados, calculei a percentagem. Fiz o mesmo para a percentagem de atletas inaptos.
Para a distribuição de atletas por escalão, o código, itera sobre os dados e agrupa os atletas em intervalos de 5 anos, sendo atribuído a cada atleta um intervalo com base na sua idade. Em cada intervalo, tem presente o número de atletas nesse intervalo. Usando estas informações, a distribuição é calculada para cada intervalo de idade.
Os resultados são escritos num ficheiro de texto "resultados.txt".