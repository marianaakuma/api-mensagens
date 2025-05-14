from flask import Flask, jsonify, request
from models.mensagem import mensagem 
from utils import db,lm


app.config[' jsonify__DATABASE_URI'] = 'jsonify:///app.db'

db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)


@app.route('/mensagens', methods=['POST'])
def criar_mensagem():
    global proximo_id
    dados = request.get_json()
    nova_mensagem = {"id": proximo_id, "conteudo": dados['conteudo']}
    mensagens.append(nova_mensagem)
    proximo_id += 1
    return jsonify(nova_mensagem), 201

# Listar todas
@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(mensagens)

# Obter por ID
@app.route('/mensagens/<int:id>', methods=['GET'])
def obter_mensagem(id):
    for m in mensagens:
        if m['id'] == id:
            return jsonify(m)
    return jsonify({"erro": "Mensagem não encontrada"}), 404

# Atualizar por ID
@app.route('/mensagens/<int:id>', methods=['PUT'])
def atualizar_mensagem(id):
    dados = request.get_json()
    for m in mensagens:
        if m['id'] == id:
            m['conteudo'] = dados['conteudo']
            return jsonify(m)
    return jsonify({"erro": "Mensagem não encontrada"}), 404

# Deletar por ID
@app.route('/mensagens/<int:id>', methods=['DELETE'])
def deletar_mensagem(id):
    for m in mensagens:
        if m['id'] == id:
            mensagens.remove(m)
            return jsonify({"mensagem": "Mensagem deletada"})
    return jsonify({"erro": "Mensagem não encontrada"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)