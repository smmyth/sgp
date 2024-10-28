from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sistema_gerenciamento.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Troque para um segredo mais seguro em produção
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
