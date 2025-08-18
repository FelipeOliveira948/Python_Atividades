import requests

def buscar_pais(nome_pais):
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()[0]
        nome_oficial = dados['name']['official']
        linguas = ", ".join(dados['languages'].values()) if 'languages' in dados else "Não disponível"
        regiao = dados.get('region', 'Não disponível')
        subregiao = dados.get('subregion', 'Não disponível')
        capital = ", ".join(dados.get('capital', ['Não disponível']))
        moedas = dados.get('currencies', {})
        if moedas:
            for sigla, info in moedas.items():
                nome_moeda = info.get('name', 'Não disponível')
                simbolo = info.get('symbol', 'Não disponível')
                break 
        else:
            sigla, nome_moeda, simbolo = 'N/A', 'N/A', 'N/A'
        fronteiras = ", ".join(dados.get('borders', ['Nenhuma']))

        print("\n===== INFORMAÇÕES DO PAÍS =====")
        print(f"Nome: {nome_oficial}")
        print(f"Linguagens: {linguas}")
        print(f"Região: {regiao}")
        print(f"Sub-região: {subregiao}")
        print(f"Capital: {capital}")
        print("\n===== MOEDA =====")
        print(f"Sigla: {sigla}")
        print(f"Nome: {nome_moeda}")
        print(f"Símbolo: {simbolo}")
        print("\n===== FRONTEIRAS =====")
        print(f"Países que fazem fronteira: {fronteiras}")

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except (KeyError, IndexError):
        print("Erro ao processar os dados do país. Verifique o nome informado.")

if __name__ == "__main__":
    pais = input("Digite o nome de um país (em inglês, ex: brazil, germany, canada): ").strip().lower()
    buscar_pais(pais)