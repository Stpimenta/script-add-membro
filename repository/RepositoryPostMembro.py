#repositoryMembro
import json
import requests
from model.ModelMembro import membro
from service.ServiceSearchEndereco import viacep

url = ""
jwt_token = ""

def post_usuario(usuario: membro):
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }

    endereco = viacep(usuario.CepEndereco)
    if endereco:
        usuario.BairroEdereco = endereco['bairro']
        usuario.CidadeEndereco = endereco['localidade']
        usuario.RuaEdereco = endereco['logradouro']
        usuario.UfEndereco = endereco['uf']
        print("Consulta de CEP bem sucedida!")

    else:
        print(f"Falha ao consultar o CEP")

    try:
        response = requests.post(url, headers=headers, json=vars(usuario))
        response.raise_for_status()  # Lança exceção se houver erro HTTP
        
        if response.status_code == 200:
            return response.status_code, response.json()
        else:
            return response.status_code, None
    
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return response.status_code, response
    
    except Exception as err:
        print(f'Other error occurred: {err}')
        return 500, None  # Retornar um status de erro
    
     
    