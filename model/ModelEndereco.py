from dataclasses import dataclass
class Endereco:
    def __init__(self, cep: str, logradouro: str, complemento: str, unidade: str,
                 bairro: str, localidade: str, uf: str, ibge: str, gia: str,
                 ddd: str, siafi: str):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.unidade = unidade
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi