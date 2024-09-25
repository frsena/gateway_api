from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from schemas import RemedioSchema,remedio_view

class PesquisaMedicamentoId(BaseModel):
    """ Fazer a busca pelo o campo da chave
    """
    id: int
  

class PesquisaMedicamento(BaseModel):
    """ Define os campos de pesquisa
    """
    id: Optional[int] = None
    descricao: Optional[str] = None


class MedicamentoSchema(BaseModel):
    """ Define o modelo do objeto modelo para representar na tela
    """
    id: int = 1
    descricao: str = "Dores de cabeça."
    quantidade_dia: Optional[int] = 5
    quantidade_vezes_dia: int = 2
    data_inicio_medicacao: str = "0000/00/00 00:00:00"
    observacao: str = "Ingerir após as refeições."
    remedio_id: int = 1  

class MedicamentoIncluirSchema(BaseModel):
    """ Define o modelo do objeto medicamento para representar na tela de incluir
    """
    descricao: str 
    quantidade_vezes_dia: int 
    observacao: str = ""
    quantidade_dia: Optional[int] = None
    data_inicio_medicacao: datetime 
    remedio_id: int 

class MedicamentoAlterarSchema(MedicamentoIncluirSchema):
    """ Define o modelo do objeto medicamento para representar na tela de alteração
    """
    id:int


 

class ListagemMedicamentoSchema(BaseModel):
    """ Define como uma listagem de medicamento será retornada.
    """
    item:List[MedicamentoSchema]


def medicamento_completo_view(medicamento,remedio):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return {
        "id": medicamento['id'],
        "remedio": remedio['nome'],
        "descricao": medicamento['descricao'],
        "quantidade_dia": medicamento['quantidade_dia'],
        "quantidade_vezes_dia": medicamento['quantidade_vezes_dia'],
        "data_inicio_medicacao": datetime.strptime(medicamento['data_inicio_medicacao'], "%Y-%m-%d %H:%M:%S").date().strftime("%Y-%m-%d"),
        "observacao": medicamento['observacao'],
        "remedio_id": remedio['id']
        }


def medicamento_view(medicamento):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return {
        "id": medicamento['id'],
        "descricao": medicamento['descricao'],
        "quantidade_dia": medicamento['quantidade_dia'],
        "quantidade_vezes_dia": medicamento['quantidade_vezes_dia'],
        "data_inicio_medicacao": datetime.strptime(medicamento['data_inicio_medicacao'], "%Y-%m-%d %H:%M:%S").date().strftime("%Y-%m-%d"),
        "observacao": medicamento['observacao'],
        "remedio_id": medicamento['remedio_id']
        }

def medicamento_atualizar_view(medicamento):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return {
        "data_inicio_medicacao": medicamento.data_inicio_medicacao,
        "descricao": medicamento.descricao,
        "id": medicamento.id,
        "quantidade_dia": medicamento.quantidade_dia,
        "quantidade_vezes_dia": medicamento.quantidade_vezes_dia,
        "observacao": medicamento.observacao,
        "remedio_id": medicamento.remedio_id,
        }

def medicamento_incluir_view(medicamento):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return {
        "data_inicio_medicacao": medicamento.data_inicio_medicacao.strftime("%Y-%m-%d %H:%M:%S"),
        "descricao": medicamento.descricao,
        "quantidade_dia": medicamento.quantidade_dia,
        "quantidade_vezes_dia": medicamento.quantidade_vezes_dia,
        "observacao": medicamento.observacao,
        "remedio_id": medicamento.remedio_id,
        }


