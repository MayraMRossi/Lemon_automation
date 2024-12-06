from flask import Flask
from api.email_controller import email_blueprint
from api.intent_controller import intent_blueprint
from api.rag_controller import rag_blueprint
from api.response_controller import response_blueprint
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(email_blueprint, url_prefix="/emails")
app.register_blueprint(intent_blueprint, url_prefix="/intents")
app.register_blueprint(rag_blueprint, url_prefix="/rag")
app.register_blueprint(response_blueprint, url_prefix="/response")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)