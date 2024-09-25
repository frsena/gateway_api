from pydantic import BaseModel
from typing import List, Optional


class PesquisaRemedioId(BaseModel):
    """ Fazer a busca pelo o campo da chave
    """
    id: int

class PesquisaRemedio(BaseModel):
    """ Define os campos de pesquisa
    """
    id: Optional[int] = None
    nome: Optional[str] = None

class RemedioSchema(BaseModel):
    """ Define como o remedio deve ser representado
    """
    id: int = 1
    nome: str = "Nesoldina"


class RemedioIncluirSchema(BaseModel):
    """ Define o modelo do objeto remedio para representar na tela de incluir
    """
    nome: str = ""

class ListagemRemedioSchema(BaseModel):
    """ Define como uma listagem de medicamento será retornada.
    """
    remedios:List[RemedioSchema]   

def remedio_incluir_view(remedio):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return RemedioSchema (
        nome = remedio.nome).model_dump()


def remedio_view(remedio):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return RemedioSchema (
        id = remedio.id,
        nome = remedio.nome).model_dump()


def remedios_view(remedios):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    resultado = []
    for remedio in remedios:
        resultado.append({
            "id": remedio.id,
            "nome": remedio.nome
        })
        #resultado.append(RemedioSchema (
        #            id = remedio.id,
        #            nome = remedio.nome).model_dump())
    return resultado


