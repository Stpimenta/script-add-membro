import pandas as pd
from repository.RepositoryPostMembro import post_usuario
from model.ModelMembro import membro
from datetime import datetime
from service.ServiceTratamento import ServiceTratamento

caminho_arquivo = './Pasta1.xlsxa'

# Lê o arquivo Excel para um DataFrame do pandas sem cabeçalho
df = pd.read_excel(caminho_arquivo, header=None, engine='openpyxl')

# Remove todas as linhas onde todos os valores são NaN
df.dropna(how='all', inplace=True)

# Ajusta as opções para exibir todas as colunas e todas as linhas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Escolha dos índices das linhas para processar
inicio = 44 - 1  
fim = 51

# Inicializa vetores para armazenar nomes de usuários com sucesso e sem sucesso
sucesso = []
falha = []

# Lista para armazenar usuários que devem ser tentados novamente
tentar_novamente = []

# Itera sobre as linhas selecionadas do DataFrame
for index in range(inicio, fim):
    row = df.iloc[index]  # Seleciona a linha específica do DataFrame

    enderecoNC, enderecoComplemento = ServiceTratamento.endereco_verify(row[11])
    if enderecoComplemento is not None:
        enderecoComplemento = enderecoComplemento.lower()

    batismoData, batismoIgreja = ServiceTratamento.extrair_informacoesBatismo(row[16])

    if batismoIgreja is not None:
        batismoIgreja = batismoIgreja.lower()

    usuario = membro(
        nome=ServiceTratamento.capitalize_name(row[3]),
        email=ServiceTratamento.gmail_verify(row[15]),
        senha=f'{ServiceTratamento.cpf_verify(row[10])}@',
        data_nascimento=ServiceTratamento.converte_data(row[5]),
        cpf=ServiceTratamento.cpf_verify(row[10]),
        rg_numero=ServiceTratamento.rg_verify(row[9]),
        rua_endereco="",
        uf_endereco="",
        bairro_endereco="",
        cep_endereco=ServiceTratamento.cep_verify(row[12]),
        cidade_endereco="",
        numero_endereco=enderecoNC,
        complemento_endereco=enderecoComplemento,
        filhos=ServiceTratamento.filho_verify(row[18]),
        rule=4,
        token_contribuicao=ServiceTratamento.dizimo_verify(row[2]),
        telefone_pais="+55",
        telefone_numero=ServiceTratamento.tel_verify(row[14]),
        data_batismo=None,
        pastor_batismo=ServiceTratamento.pastor_batismo_verify(row[17]),
        igreja_batismo=batismoIgreja,
        profissao=ServiceTratamento.profi_verify(row[8]),
        estado_civil=row[6].lower(),
        status=ServiceTratamento.status_verify(row[1]),
        genero=int(row[0]),
        url_image=""
    )

    # Faz a requisição
    status_code, response_json = post_usuario(usuario)

    # Trata a resposta
    if status_code == 200:
        sucesso.append(usuario.Nome)  # Adiciona o nome do usuário ao vetor de sucesso
        print(f'Request for {usuario.Nome} succeeded with status code {status_code}')
    else:
        tentar_novamente.append(usuario)  # Adiciona o usuário à lista de tentativa novamente

# Tenta cadastrar os usuários que falharam novamente
for usuario in tentar_novamente:
    status_code, response_json = post_usuario(usuario)

    if status_code == 200:
        sucesso.append(usuario.Nome)  # Adiciona o nome do usuário ao vetor de sucesso
        print(f'Retry request for {usuario.Nome} succeeded with status code {status_code}')
    else:
        falha.append(usuario.Nome)  # Adiciona o nome do usuário ao vetor de falha
        print(f'Retry request for {usuario.Nome} failed with status code {status_code}')

# Após o loop, imprime os vetores de sucesso e falha
print(f'Usuários que deram certo: {sucesso}')
print(f'Usuários que não deram certo: {falha}')


# usuario = membro(
#     nome="Sergio",
#     email="sergio@example.com",
#     senha="SenhaForte123!",
#     data_nascimento="2000-01-01",
#     cpf="12345678900",
#     cep_endereco="06853100",
#     numero_endereco="123",
#     complemento_endereco="casa",
#     bairro_endereco="",
#     cidade_endereco="",
#     rua_endereco="",
#     uf_endereco="",
#     filhos=True,
#     rule=1,
#     token_contribuicao="",
#     rg_numero="1234567",
#     telefone_pais="+55",
#     telefone_numero="999999999",
#     data_batismo="2010-05-10",
#     pastor_batismo="Pastor João",
#     igreja_batismo="Igreja Central",
#     profissao="Desenvolvedor",
#     estado_civil="Solteiro",
#     active=True,
#     genero=1,
#     url_image=""
# )

# status_code, response_json = post_usuario(usuario)

# if response_json is not None:
#     print(f'Status Code: {status_code}')
#     print(f'Response JSON: {response_json}')
# else:
#     print(f'Request failed with status code: {status_code}')



# Usuários que não deram certo: ['Regina Celano Oias', 'Jose Delfino da Silva', 'Neuza Pereira da Silva', 'Alexandre Gomes', 'Marta Pereira Dos Santos Gomes', 'Larissa Gabriela Pimenta Rodrigues', 'Ivo de Lima Alves', '
#                                Murilo Marques S. Guimarães Gonçalves', 'Elivelton de Oliveira Lopes', 'Fernando Assunção de Souza']