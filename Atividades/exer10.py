import requests

def buscar_cep(cep: str):

    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        
        if response.status_code == 200:
            data = response.json()

            
            if "erro" in data:
                print("CEP não encontrado!")
            else:
                uf = data.get("uf")
                cidade = data.get("localidade")

                print("\n ///// Olá motorista, endereço encontrado: ///// \n")
                print(f"CEP: {data.get('cep')}")
                print(f"Logradouro: {data.get('logradouro')}")
                print(f"Região: {data.get('regiao')}")
                print(f"Bairro: {data.get('bairro')}")
                print(f"Cidade: {data.get('localidade')}")
                print(f"Estado: {data.get('uf')}")

                if uf != "SP":
                    print("\n ///// Aviso: este CEP não é do estado de São Paulo, pertence a outra região. /////")
                else:
                    if cidade == "São Paulo":
                        print("\n ///// Este CEP pertence à capital: São Paulo. /////")
                    else:
                        print("\n ///// Este CEP pertence a uma cidade vizinha dentro do estado de São Paulo. /////")
        else:
            print(f" ///// Erro na requisição / Código: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(" ///// Ocorreu um erro de conexão: ", e)


while True:
    cep_digitado = input("\nDigite o CEP (ou 'sair' para encerrar):")
    
    if cep_digitado.lower() == "sair":
        print("  ///// Encerrando o sistema, até logo!  /////")
        break

    cep_limpo = cep_digitado.replace("-", "").replace(" ", "")

    if not cep_limpo.isdigit() or len(cep_limpo) != 8:
        print(" ///// CEP inválido! Digite exatamente 8 números, ex: 01001000 /////")
        continue
    
    buscar_cep(cep_digitado)