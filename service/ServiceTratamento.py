import datetime
import re
import math
from datetime import datetime
from typing import Tuple, Optional

class ServiceTratamento:
    @staticmethod
    def capitalize_name(name:str) -> str:

        words_to_keep_lowercase = {"de", "da"}
        words = name.split()

        capitalized_words = [
            word.capitalize() if word.lower() not in words_to_keep_lowercase else word.lower()
            for word in words
        ]

        # Trata a primeira palavra para sempre estar com a inicial maiúscula
        capitalized_words[0] = capitalized_words[0].capitalize()

        return ' '.join(capitalized_words)
    

    @staticmethod
    def gmail_verify(gmail: str) -> str:
        # Verifica se o valor é NaN, None ou um número inválido
        if gmail is None or gmail == 0 or (isinstance(gmail, float) and math.isnan(gmail)):
            gmail = f"padrao{datetime.now().strftime('%Y%m%d%H%M%S')}@ibpv.com"
        else:
            gmail = gmail.strip()
        return gmail
    
    @staticmethod
    def cpf_verify(cpf:str) -> str:
        if cpf is None or cpf == 0 or (isinstance(cpf, float) and math.isnan(cpf)):
            return None
        
        # Remove pontos e traços
        cpf = cpf.replace('.', '').replace('-', '').strip()
        cpf = cpf.strip()
        return cpf
    
    @staticmethod
    def rg_verify(rg:str) -> str:
        if rg is None or rg == 0 or (isinstance(rg, float) and math.isnan(rg)):
            return None
        
        # Remove pontos e traços
        rg = rg.replace('.', '').replace('-', '').strip()
        
        return rg

    @staticmethod
    def tel_verify(tel:str) -> str:
        tel = tel.replace('(','')
        tel = tel.replace(')','')
        tel = tel.replace('-','')
        tel = tel.replace(' ','')
        tel.strip
        return tel 
    
    @staticmethod
    def cep_verify(cep_endereco:str) -> str:
        cep_sem_hifen = cep_endereco.replace('-', '')
        cep_sem_hifen = cep_sem_hifen.replace('.', '')
        cep_sem_hifen = cep_sem_hifen.strip()
        return cep_sem_hifen 
    
    @staticmethod
    def endereco_verify(row:str):
        endereco = row.split("Nº")
        
        endrecosplit = endereco[1]
        enderecoNC = endrecosplit.split("-");

        enderecoNumero = enderecoNC[0].strip()

        if len(enderecoNC) > 1:
            enderecoComplemento = enderecoNC[1].strip()
        else:
         enderecoComplemento = None
        return enderecoNumero, enderecoComplemento
    
    def pastor_batismo_verify(pastor_batismo: str):
        if pastor_batismo is None or (isinstance(pastor_batismo, float) and math.isnan(pastor_batismo)) or pastor_batismo == 0:
            return None
        else:
            return pastor_batismo.capitalize() 
   
    def filho_verify(inputfilho:str):
        filho = False
        if(inputfilho.lower() == "sim"):
            filho = True
        
        return filho


    # Função para converter a data de "dd/mm/yyyy" para um objeto datetime
    def converte_data(data_str):
        try:
            # Tenta converter a string para um objeto datetime
            data = datetime.strptime(data_str, "%d/%m/%Y")
            # Se a conversão for bem-sucedida, formata a data no formato desejado
            return data.strftime("%Y-%m-%d")
        except ValueError:
            # Se ocorrer uma exceção ValueError, retorna None ou uma mensagem de erro
            return None


    def extrair_informacoesBatismo(entry: str) -> Tuple[Optional[str], Optional[str]]:

        if entry is None or entry == 0 or (isinstance(entry, float) and math.isnan(entry)):
            return None, None
        # Expressão regular para detectar datas no formato dd/mm/yyyy
        date_pattern = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
        
        # Verificar se a entrada está no formato "data - igreja"
        if ' - ' in entry:
            partes = entry.split(' - ')
            if len(partes) == 2:
                data_str, igreja = partes
                data_str = data_str.strip()
                igreja = igreja.strip()
                
                try:
                    data = datetime.strptime(data_str, "%d/%m/%Y")
                    data_formatada = data.strftime("%m/%d/%Y")
                    return data_formatada, igreja if igreja else None
                except ValueError:
                    return None, entry.strip()
        else:
            # Tentar encontrar a data na entrada
            date_match = date_pattern.search(entry)
            
            if date_match:
                data_str = date_match.group(0)
                try:
                    data = datetime.strptime(data_str, "%d/%m/%Y")
                    data_formatada = data.strftime("%m/%d/%Y")
                    igreja = entry[date_match.end():].strip(" -")
                    return data_formatada, igreja if igreja else None
                except ValueError:
                    return None, entry.strip()
            else:
                # Se não encontrar uma data, retornar a entrada como nome da igreja
                return None, entry.strip()
        
        return None, None


    def status_verify(status:str) -> int:
        if status.lower() == "ativo":
            return 1
        if status.lower() == "desligado":
            return 0
            
        if status.lower() == "ausente":
            return 3

        if status.lower() == "pre-cad":
            return 2
        
    def dizimo_verify(cod:str):

        if cod == '0':
            return None
        
        if cod == None:
            return None
        
        if cod == 0:
            return None
        
        if isinstance(cod, str) and (not cod or cod.strip() == ''):
            return None
        
        if isinstance(cod, float):
            return None
        
        return cod
    

    def profi_verify(profi:str) -> int:
        if profi == '0':
            return None
        
        if profi == None:
            return None
        
        if profi == 0:
            return None
        
        if isinstance(profi, str) and (not profi or profi.strip() == ''):
            return None
        
        if isinstance(profi, float):
            return None
        
        return profi.lower()
    