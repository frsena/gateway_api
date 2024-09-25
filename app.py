from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS


info = Info(title="Controle Requisição de medicação", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)


import documentacao_service 
import gateway_service 

app.run()