#modelMembroPy
from typing import Optional
class membro:
    def __init__(self, nome: str, email: str, senha: str, cpf:str,cep_endereco: str,
                 numero_endereco: str,complemento_endereco: str,data_nascimento: str,
                 filhos: bool,rule: int,
                 token_contribuicao: Optional[str] = None, rg_numero: Optional[str] = None,
                 telefone_pais: Optional[str] = None, telefone_numero: Optional[str] = None,
                 bairro_endereco: Optional[str] = None, cidade_endereco: Optional[str] = None,
                 rua_endereco: Optional[str] = None, 
                 uf_endereco: Optional[str] = None,
                 data_batismo: Optional[str] = None, pastor_batismo: Optional[str] = None,
                 igreja_batismo: Optional[str] = None, 
                 profissao: Optional[str] = None, estado_civil: Optional[str] = None,
                 status: Optional[int] = None, 
                 genero: Optional[int] = None, url_image: Optional[str] = None):
        
        self.Nome = nome
        self.Email = email
        self.Senha = senha
        self.Cpf = cpf
        self.TokenContribuicao = token_contribuicao
        self.RGnumero = rg_numero
        self.Telefone_pais = telefone_pais
        self.TelefoneNumero = telefone_numero
        self.BairroEdereco = bairro_endereco
        self.CidadeEndereco = cidade_endereco
        self.RuaEdereco = rua_endereco
        self.CepEndereco = cep_endereco
        self.NumeroEndereco = numero_endereco
        self.UfEndereco = uf_endereco
        self.ComplementoEndereco = complemento_endereco
        self.Data_nascimento = data_nascimento
        self.dataBatismo = data_batismo
        self.pastorBatismo = pastor_batismo
        self.igrejaBatismo = igreja_batismo
        self.filhos = filhos
        self.profissao = profissao
        self.estadoCivil = estado_civil
        self.status = status
        self.Rule = rule
        self.genero = genero
        self.urlImage = url_image