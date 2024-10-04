#repositoryMembro
import json
import requests
from model.ModelMembro import membro
from service.ServiceSearchEndereco import viacep

url = "http://192.168.1.199:5287/api/Usuario"
jwt_token = "eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIwIiwiZXhwIjoxNzIxMTMwMDM5fQ.beuk5QmwWsQ-MxhUmJbXHS17sYVrYyj31KbfA35WXoo"

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
    
     
    