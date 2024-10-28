Sistema de Gerenciamento de Pedidos

Este é um sistema de gerenciamento de pedidos para uma loja online, desenvolvido em Python usando o framework Flask e SQLite como banco de dados. O sistema oferece funcionalidades para cadastro e autenticação de usuários, além do gerenciamento de clientes, produtos, pedidos e detalhes de pedidos.

Funcionalidades

Cadastro e autenticação de usuários (administradores da loja)
Cadastro de clientes com informações básicas
Gerenciamento de produtos com categorias associadas
Processamento de pedidos, incluindo data de compra e cliente associado
Detalhamento de pedidos com informações de valor e desconto de cada produto

Estrutura do Projeto

app.py: Configura o Flask e o banco de dados, além de iniciar a aplicação.
models.py: Define os modelos (tabelas) para Usuário, Cliente, Categoria, Produto, Pedido, e Detalhe do Pedido.
routes.py: Define as rotas para as operações CRUD de cada entidade.

Tecnologias

Python 3
Flask: Framework web para criação de API REST.
Flask_SQLAlchemy: ORM para gerenciamento de banco de dados.
Flask_Bcrypt: Para criptografar senhas de usuários.
Flask_JWT_Extended: Para autenticação e autorização via tokens JWT.
SQLite: Banco de dados relacional usado para simplificação.

Pré-requisitos

Python 3.x
Gerenciador de pacotes pip

Instalação e Configuração

Clone o repositório:
git clone https://github.com/seu-usuario/sistema-gerenciamento-pedidos.git
cd sistema-gerenciamento-pedidos

Instale as dependências:
pip install -r requirements.txt

Configure o banco de dados:

Abra o terminal e execute o seguinte comando no diretório do projeto para criar as tabelas no banco de dados:
from app import db
db.create_all()

Inicie o servidor:
python app.py
Acesse a API no endereço http://127.0.0.1:5000/.

Uso

Endpoints Principais
/register [POST]: Cria um novo usuário administrador. Envie login e senha no corpo da requisição.
/login [POST]: Autentica o usuário. Envie login e senha. Retorna um token JWT para autorização.
/clientes [POST]: Cria um novo cliente. Envie nome e email.
/produtos [POST]: Adiciona um produto ao catálogo. Envie nome e categoria_id.
/pedidos [POST]: Cria um pedido para um cliente. Envie cliente_id.
/detalhes_pedido [POST]: Adiciona detalhes a um pedido, incluindo produto_id, valor e desconto.
Exemplo de Requisição
Use ferramentas como Postman ou curl para testar as requisições.

Exemplo de criação de um cliente:

curl -X POST http://127.0.0.1:5000/clientes -H "Authorization: Bearer <token>" -d '{"nome": "Cliente Teste", "email": "teste@exemplo.com"}'

Observações
O sistema foi desenvolvido com foco na simplicidade e pode ser estendido para uso em produção com configurações adicionais, como um banco de dados mais robusto (ex.: PostgreSQL) e um ambiente de implantação seguro.
Para gerar um token JWT, use o endpoint /login com o login e senha de um usuário criado previamente.

Contribuição

Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/MinhaFeature).
Commit suas mudanças (git commit -am 'Adiciona nova feature').
Push para a branch (git push origin feature/MinhaFeature).
Crie um novo Pull Request.

Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.