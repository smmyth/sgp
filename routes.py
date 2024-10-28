from flask import request, jsonify
from app import app, db, bcrypt, jwt
from models import Usuario, Cliente, Pedido, DetalhePedido, Produto, Categoria
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['senha']).decode('utf-8')
    new_user = Usuario(login=data['login'], senha=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Usuario.query.filter_by(login=data['login']).first()
    if user and bcrypt.check_password_hash(user.senha, data['senha']):
        token = create_access_token(identity=user.id)
        return jsonify({'token': token})
    return jsonify({'message': 'Login ou senha incorretos'}), 401

@app.route('/clientes', methods=['POST'])
@jwt_required()
def create_cliente():
    data = request.get_json()
    new_cliente = Cliente(nome=data['nome'], email=data['email'])
    db.session.add(new_cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente criado com sucesso!'})

@app.route('/produtos', methods=['POST'])
@jwt_required()
def create_produto():
    data = request.get_json()
    categoria = Categoria.query.filter_by(id=data['categoria_id']).first()
    if not categoria:
        return jsonify({'message': 'Categoria não encontrada'}), 404
    new_produto = Produto(nome=data['nome'], categoria_id=data['categoria_id'])
    db.session.add(new_produto)
    db.session.commit()
    return jsonify({'message': 'Produto criado com sucesso!'})

@app.route('/pedidos', methods=['POST'])
@jwt_required()
def create_pedido():
    data = request.get_json()
    cliente = Cliente.query.filter_by(id=data['cliente_id']).first()
    if not cliente:
        return jsonify({'message': 'Cliente não encontrado'}), 404
    new_pedido = Pedido(cliente_id=data['cliente_id'])
    db.session.add(new_pedido)
    db.session.commit()
    return jsonify({'message': 'Pedido criado com sucesso!', 'pedido_id': new_pedido.id})

@app.route('/detalhes_pedido', methods=['POST'])
@jwt_required()
def create_detalhe_pedido():
    data = request.get_json()
    pedido = Pedido.query.filter_by(id=data['pedido_id']).first()
    produto = Produto.query.filter_by(id=data['produto_id']).first()
    if not pedido or not produto:
        return jsonify({'message': 'Pedido ou Produto não encontrado'}), 404
    new_detalhe = DetalhePedido(
        pedido_id=data['pedido_id'],
        produto_id=data['produto_id'],
        valor=data['valor'],
        desconto=data.get('desconto', 0)
    )
    db.session.add(new_detalhe)
    db.session.commit()
    return jsonify({'message': 'Detalhe do pedido adicionado com sucesso!'})
