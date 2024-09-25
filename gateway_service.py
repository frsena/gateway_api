
from flask_openapi3 import Tag
from flask import request
import requests


from app import app
from schemas import *

url_remedio = "http://remedioapi:5000"
url_medicacao = "http://medicamentoapi:5001"
#url_medicacao = "http://localhost:5001"
#url_remedio = "http://localhost:5000"


Remedio_tag = Tag(name="Remedio", description="Cadastrar Remedios")
Medicacao_tag = Tag(name="Crontrole de Medicamento", description="Cadastrar medicação")
Localizador_tag = Tag(name="Localizar farmacia", description="Localizar famarcia mais perto atravez do cep")


# Chamar a api cadastro de Remedio



def busca_remedio_id(id):
    """ Busca o medicamento pelo codigo
    """
    try:
        query = {'id':id}
        response = requests.get(f"{url_remedio}/remedio",params=query)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()

    return data



@app.get('/remedios', tags=[Remedio_tag],
         responses={"200": ListagemRemedioSchema, "404": ErrorSchema})
def busca_remedios():
    """ Retorna todos os remedios cadastrados
    """
    try:
        response = requests.get(f"{url_remedio}/remedios")
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()
   
    return data


@app.get('/pesquisarRemedios', tags=[Remedio_tag],
         responses={"200": ListagemRemedioSchema, "404": ErrorSchema})
def pesquisar_remedios(query: PesquisaRemedio):
    """ 
        pesquisa o medicamento pelo codigo e pela descrição, caso não passe nenhum parametro retorna a lista toda
    """
    try:
  
        response = requests.get(f"{url_remedio}/pesquisa",params=query)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()

    return data

@app.post('/incluirRemedio', tags=[Remedio_tag],
         responses={"200": RemedioSchema, "400": ErrorSchema})
def incluir_remedios(form: RemedioIncluirSchema):
    """ 
        pesquisa o medicamento pelo codigo e pela descrição, caso não passe nenhum parametro retorna a lista toda
    """
    try:

        rem = remedio_incluir_view(form)

        response = requests.post(f"{url_remedio}/remedio",data=rem)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()

    if(response.status_code == 200):
        return data, 200
    else:
        return data, 400


@app.put('/atualizarRemedio', tags=[Remedio_tag],
         responses={"200": ListagemRemedioSchema, "404": ErrorSchema})
def atualizar_remedios(form: RemedioSchema):
    """ 
        atualizar um remedio
    """
    try:
        rem = remedio_view(form)
        response = requests.put(f"{url_remedio}/atualizar",rem)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()
    if(response.status_code == 200):
        return data, 200
    else:
        return data, 400


@app.delete('/deletarRemedio', tags=[Remedio_tag],
         responses={"200": ListagemRemedioSchema, "404": ErrorSchema})
def deletar_remedios(query: PesquisaRemedioId):
    """ 
        pesquisa o medicamento pelo codigo e pela descrição, caso não passe nenhum parametro retorna a lista toda
    """
    try:

        response = requests.delete(f"{url_remedio}/deletar",params=query)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()

    return data



# Chamar a api cadastro de controle da medicacao

@app.get('/medicamento', tags=[Medicacao_tag],
         responses={"200": MedicamentoSchema, "404": ErrorSchema})
def busca_medicamento_id(query: PesquisaMedicamentoId):
    """ Busca o medicamento pelo codigo
    """
    try:
        response = requests.get(f"{url_medicacao}/medicamento",params=query)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()
    return medicamento_view(data)


@app.get('/medicamentos', tags=[Medicacao_tag],
         responses={"200": ListagemMedicamentoSchema, "404": ErrorSchema})
def busca_medicamentos():
    """ Retorna todos as medicações cadastradas
    """
    try:
        response = requests.get(f"{url_medicacao}/medicamentos")
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()

    return data


@app.get('/pesquisarMedicamentos', tags=[Medicacao_tag],
         responses={"200": ListagemMedicamentoSchema, "404": ErrorSchema})
def pesquisar_medicamentos(query: PesquisaMedicamento):
    """ 
        pesquisa o medicamento pelo codigo e pela descrição, caso não passe nenhum parametro retorna a lista toda
    """
    try:
       
        response = requests.get(f"{url_medicacao}/pesquisa",params=query)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    dados = response.json()

    
    if(response.status_code == 400):
       return dados, 400
    
    """ 
        Buscar a descrciao do remedio na api de remedio
    """
    medicamentos = []

    for item in dados:

        #medicamento_view(medicamento)
        remedio = busca_remedio_id(item['remedio_id'])

        medicacao = medicamento_completo_view(item,remedio)
        medicamentos.append(medicacao)
       # medicamento.remedio = remedio


    return medicamentos

@app.post('/incluirMedicamento', tags=[Medicacao_tag],
         responses={"200": MedicamentoSchema, "400": ErrorSchema})
def incluir_medicamento(form: MedicamentoIncluirSchema):
    """ 
        incluir o medicamento
    """
    try:
  
        rem = medicamento_incluir_view(form)
        response = requests.post(f"{url_medicacao}/medicamento",data=rem)

    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    dados = response.json()

    if(response.status_code == 200):
        remedio = busca_remedio_id(dados['remedio_id'])
        medicamento = medicamento_completo_view(dados,remedio)

        return medicamento, 200
    else:
        return medicamento, 400


@app.put('/atualizarMedicamento', tags=[Medicacao_tag],
         responses={"200": ListagemMedicamentoSchema, "404": ErrorSchema})
def atualizar_medicamento(form: MedicamentoSchema):
    """ 
        atualizar um medicamento cadastrado
    """
    try:
        rem = medicamento_atualizar_view(form)
        response = requests.put(f"{url_medicacao}/atualizar",rem)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()
    if(response.status_code == 200):
        return data, 200
    else:
        return data, 400


@app.delete('/deletarMedicamento', tags=[Medicacao_tag],
         responses={"200": ListagemMedicamentoSchema, "404": ErrorSchema})
def deletar_medicamento(query: PesquisaMedicamentoId):
    """ 
        Excluir um medicamento cadastrado
    """
    try:
        response = requests.delete(f"{url_medicacao}/delete",params=query)
    except requests.exceptions.ConnectionError:
        return "Service unavailable", 404
    data = response.json()
    return data
    


# Chamar a api do google para encontrar farmacia perto


def obter_geometria(cep):
    """ 
        obter a latitude e longitude passando o cep no api do google
    """

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': cep,
        'key': 'AIzaSyBdIqsb8oOfxtOqdmNAi-P_cJ7ZWhiqVLw'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        geocode_result = response.json()

    if not geocode_result['results']:
        raise ValueError("Cep não encontrou nenhuma farmacia")
         

    location = geocode_result['results'][0]['geometry']['location']
    return location['lat'], location['lng']


def obter_todos_ids_locais(lat, lng):
    """ 
        obter as identificações dos locais encontrado em um raio de 2000 metros atraves da latitude e longitude no api do google
    """
    urlFind = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    paramsFind = {       
        'location': f'{lat},{lng}',
        'fields': 'place_id',
        'radius':'2000',
        'type':'pharmacy',
        'key': 'AIzaSyBdIqsb8oOfxtOqdmNAi-P_cJ7ZWhiqVLw'
    }
    local_response = requests.get(urlFind, params=paramsFind)

    if local_response.status_code == 200:
        local_resultado = local_response.json()

    if not local_resultado['results']:
        raise ValueError("Cep não encontrou nenhuma farmacia")
    
    return local_resultado['results']

def obter_dados_local(local_resultado):
    """ 
        obter os dados atraves do id do local no api do google
    """
    resultado = []
    for local in local_resultado:
        local_id =local['place_id']
        urlDetais = 'https://maps.googleapis.com/maps/api/place/details/json'
        params = {
            'place_id': local_id,
            'fields': 'name,formatted_address,formatted_phone_number',
            'key': 'AIzaSyBdIqsb8oOfxtOqdmNAi-P_cJ7ZWhiqVLw'
        }
        detalhe_response = requests.get(urlDetais, params=params)
        if detalhe_response.status_code == 200:
            detalhe_resultado = detalhe_response.json()
        if not detalhe_resultado['result']:
            raise ValueError("Cep não encontrou nenhuma farmacia")
                        
        resultado.append({
            'nome' : detalhe_resultado['result']['name'],
            'endereco' : detalhe_resultado['result']['formatted_address'],
            'telefone' :detalhe_resultado['result'].get('formatted_phone_number', 'Telefone não disponível')
        })
    return resultado


@app.get('/localizacao', tags=[Localizador_tag],
         responses={"200": ListagemLocalizacaoSchema, "404": ErrorSchema})
def busca_localizacao(query: LocalizarCepSchema):
    """ Retorna todos os remedios cadastrados
    """
    try:
        if not query.cep:
            error_msg = "CEP não pode esta vazio."
            return {"mesage": error_msg}, 404   

        lat, lng = obter_geometria(query.cep)


        local_resultado = obter_todos_ids_locais(lat, lng)
       
        resultado = obter_dados_local(local_resultado)
        
    except requests.exceptions.ConnectionError :
         return  {"mesage": 'Serviço esta com problema tente mais tarde'}, 404  
    except ValueError:
        return  {"mesage": 'Cep não encontrou nenhuma farmacia'}, 404 

    return resultado
    
