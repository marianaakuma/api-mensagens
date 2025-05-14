class mensagem(db.Model, UserMixin):
  __tablename__="mensagem"
  id = db.Column(db.Integer, primary_key=True)
  mensagem = db.Column(db.String(100))
  

  def __init__(self,mensagem,):
    self.nome = mensagem
 
  def __repr__(self):
    return "mensagem: {}".format(self.mensagem)