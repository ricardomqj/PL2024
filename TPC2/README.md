# TPC2: Nome do TPC2
## 2024-02-17

## Autor:
- A100066
- Ricardo Miguel Queirós de Jesus

## Resumo:

Neste trabalho, elaborou-se um conversor de MD para HTML, tendo em conta os seguintes elementos:

- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

        In: # Exemplo

        Out: <h1>Exemplo</h1>

- Bold: pedaços de texto entre "**":

        In: Este é um **exemplo** ...

        Out: Este é um <b>exemplo</b> ...

- Itálico: pedaços de texto entre "*":

        In: Este é um *exemplo* ...

        Out: Este é um <i>exemplo</i> ...ss

- Lista numerada:

        In:
        1. Primeiro item
        2. Segundo item
        3. Terceiro item

        Out:
        <ol>
        <li>Primeiro item</li>
        <li>Segundo item</li>
        <li>Terceiro item</li>
        </ol>

- Link: [texto](endereço URL)

        In: Como pode ser consultado em [página da UC](http://www.uc.pt)

        Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

- Imagem: ![texto alternativo](path para a imagem)

        In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...

        Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>