# Minha API em REST

Essa app faz parte de um pequeno projeto para ter um controle das medicações de uma pessoa, composto por um front(app_medicacao_front) e tres apis (remedio_api, medicamento_apio, gateway_api) e um api externo (googleapis)

O objetivo desse api e facilitar a comuncicação da interface com o backend ao inves do front chamar varios api, irá chamar somente esse api.
Esse api depende fortemente dos apis remedio_api e medicamento_api para funcionar, os containers precisam estar na mesma rede e iniciados.
Caso precise rodar o projeto sem o docker é necessario ir no arquivo gateway_service.py e mudar o caminho das apis remedio_api e medicamento_api para localhost
Temos tambem uma chamada para api do goolge para localizar as farmacias mais perto.


As principais tecnologias que serão utilizadas aqui é o:
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)

---
### Instalação


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Executando o servidor


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5002
```


---
### Acesso no browser

Abra o [http://localhost:5002/#/](http://localhost:5002/#/) qno navegador que levará para uma tela que pode fazer alguns testes na api.



---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t gateway_api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:
OBS: 1 - --network estou definindo uma rede comum para todos os containeres para ter comunicação entre eles.
     2 - Caso alterar o nome do container e não definir o network do container o medicamento_api irá funcionar sozinho, mas o sistema como todo não irá funcionar. 

Caso nao tenha criado a rede comum, executar o comando abaixo
```
docker network create mvp3medicamento
```
```
$ docker run -d -p 5002:5002 --name gatewayapi --network mvp3medicamento gateway_api
  
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5002/#/](http://localhost:5002/#/) no navegador que levará para uma tela que pode fazer alguns testes na api.
