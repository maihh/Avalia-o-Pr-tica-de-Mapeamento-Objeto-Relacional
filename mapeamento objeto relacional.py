Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id_funcionario = Column(Integer, primary_key=True)
    nome_funcionário = Column(String(200), nullable=False)
    cpf_funcionario = Column(Integer(11), nullable=False)
    endereco_funcionario = Column(String(200), nullable=False)
    
class Cliente(Base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True)
    nome_cliente = Column(String(200), nullable=False)
    cpf_cliente = Column(Integer(11), nullable=False)
    
class Produtos(Base):
    __tablename__ = "produtos"
    id_produto = Column(Integer, primary_key=True)
    nome_produto = Column(String(200), nullable=False)
    quantidade_produto = Column(String(200), nullable=False)
    descricao_produto = Column(String(200), nullable=False)
    preco_unidade_produto = Column(String(100), nullable=False)
   
Base.metadata.drop.all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
funcionarios = [funcionario(
    id_funcionario="130613",
    nome_funcionario="Im Nayeon",
    cpf_funcionario="81729872801",
    endereco_funcionario="Rua Gangdonggu, Bairro Twice, numero 21"),
    funcionario(
    id_funcionario="130614",
    nome_funcionario="Yoo Kyungwan",
    cpf_funcionario="81789172801",
    endereco_funcionario="Rua Suwon Gyeonggido, Bairro Twice, numero 1"),
    funcionario(
    id_funcionario="130615",
    nome_funcionario="Hirai Momo",
    cpf_funcionario="64589172801",
    endereco_funcionario="Rua Kyotanabe, Bairro Quioto, numero 9"),
    funcionario(
    id_funcionario="130616",
    nome_funcionario="Minatozaki Sana",
    cpf_funcionario="18297392801",
    endereco_funcionario="Rua Osake, Bairro Osaka, numero 29")]
    
clientes = [cliente(
    id_cliente="820391",
    nome_cliente="Jeon JungKook",
    cpf_cliente="83949371801"),
    cliente(
    id_cliente="820392",
    nome_cliente="Kim TaeHyung",
    cpf_cliente="27896524801"),
    cliente(
    id_cliente="820393",
    nome_cliente="Park Jimin",
    cpf_cliente="25236857801")]
    
produtos = [produto{
    id_produto="839109",
    nome_produto="Converse All Star Cano Alto - Preto - 37",
    quantidade_produto="52",
    descricao_produto="O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.",
    preco_unidade_produto="240"),
    produto{
    id_produto="839110",
    nome_produto="Converse All Star Cano Alto - Amarelo - 38",
    quantidade_produto="Converse All Star Cano Alto - Amarelo - 38",
    descricao_produto="O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.",
    preco_unidade_produto="240"),
    produto{
    id_produto="839111",
    nome_produto="Converse All Star Cano Alto - Vermelho - 37",
    quantidade_produto="70",
    descricao_produto="O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.",
    preco_unidade_produto="220"),
    produto{
    id_produto="839112",
    nome_produto="Converse All Star Cano Alto - Branco - 36",
    quantidade_produto="70",
    descricao_produto="O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.",
    preco_unidade_produto="250")]

with Session.begin() as session:
    for funcionario in funcionarios:
        session.add(funcionario)
        
with Session.begin as session:
    for cliente in clientes:
        session.add(cliente)
    
with Session.begin() as session
    for produto in produtos:
        session.add(produto)