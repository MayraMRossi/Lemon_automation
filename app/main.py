from flask import Flask
from api.email_controller import email_blueprint
from api.intent_controller import intent_blueprint
from api.rag_controller import rag_blueprint

app = Flask(__name__)

app.register_blueprint(email_blueprint, url_prefix="/emails")
app.register_blueprint(intent_blueprint, url_prefix="/intents")
app.register_blueprint(rag_blueprint, url_prefix="/rag")

if __name__ == "__main__":
    run(host="0.0.0.0", port=8080, debug=True)