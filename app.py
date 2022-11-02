from flask import Flask
from flask_smorest import Api
from endpoints.endpoints import root as rep
from endpoints.endpoints import user as uep
from endpoints.endpoints import card as cep
from endpoints.endpoints import deck as dep
from endpoints.endpoints import rules as ruep
from endpoints.endpoints import game as gep


app = Flask(__name__, template_folder='./templates')


app.config["SECRET_KEY"]= 'Trali-la-la-la-la-gramofon-gra.'
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Lifegame"
app.config["API_VERSION"] = "v0.1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(rep)
api.register_blueprint(uep)
api.register_blueprint(cep)
api.register_blueprint(dep)
api.register_blueprint(ruep)
api.register_blueprint(gep)
