from pydantic import BaseModel
from typing import List

class LocalizacaoSchema(BaseModel):
    """ Define como o remedio deve ser representado
    """
    nome: str = "Nome da Famacia"
    endereco: str = "Endereco completo"
    telefone: str = "(00)00000000"


class ListagemLocalizacaoSchema(BaseModel):
    """ Define como uma listagem de medicamento será retornada.
    """
    localizacao:List[LocalizacaoSchema] 

class LocalizarCepSchema(BaseModel):
    """ Fazer a busca pelo o campo da chave
    """
    cep: int
