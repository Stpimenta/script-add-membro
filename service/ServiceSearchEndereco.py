import requests

def viacep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção se houver erro HTTP

        if response.status_code == 200:
            data = response.json()
            endereco = {
                'cep': data.get('cep', ''),
                'logradouro': data.get('logradouro', ''),
                'complemento': data.get('complemento', ''),
                'unidade': data.get('unidade', ''),
                'bairro': data.get('bairro', ''),
                'localidade': data.get('localidade', ''),
                'uf': data.get('uf', ''),
                'ibge': data.get('ibge', ''),
                'gia': data.get('gia', ''),
                'ddd': data.get('ddd', ''),
                'siafi': data.get('siafi', '')
            }
            return endereco
          
        else:
            return response.status_code, None
    
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return 500, None  # Retornar um status de erro

    except Exception as err:
        print(f'Other error occurred: {err}')
        return 500, None  # Retornar um status de erro
    


#     # Exemplo de uso
# cep_digitado = "06853-100"
# endereco = viacep(cep_digitado)

# if endereco:
#     print("Consulta de CEP bem sucedida!")
#     print(f"Dados do CEP {cep_digitado}:")
#     print(f"CEP: {endereco['cep']}")
#     print(f"Logradouro: {endereco['logradouro']}")
#     print(f"Bairro: {endereco['bairro']}")
#     print(f"Cidade: {endereco['localidade']}")
#     print(f"UF: {endereco['uf']}")
#     # E assim por diante para os demais atributos
# else:
#     print(f"Falha ao consultar o CEP {cep_digitado}.")