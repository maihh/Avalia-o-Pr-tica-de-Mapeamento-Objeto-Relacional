create database loja_forward;

use loja_forward;

create table loja(
	cnpj_loja integer primary key,
	nome_loja varchar(200) not null,
	endereço_loja varchar(200) not null,
	telefone_loja integer(10) not null,
	email_loja varchar(200) not null
	);

insert into loja values
	(77777777000161, 'Forward', 'Rua Ator Paulo Gustavo', 1139727777, 'lojaforward@gmail.com');

create table funcionarios(
	id_funcionario integer primary key,
	nome_funcionario varchar(200) not null,
	cpf_funcionario integer(11) not null,
	endereco_funcionario varchar(200) not null,
	nascimento_funcionario date not null
	);

insert into funcionarios values
	(130613, 'Im Nayeon', 81729872801, 'Rua Gangdonggu, Bairro Twice, numero 21', 19952209),
	(130614, 'Yoo Kyungwan', 81789172801, 'Rua Suwon Gyeonggido, Bairro Twice, numero 1', 19960111),
	(130615, 'Hirai Momo', 64589172801, 'Rua Kyotanabe, Bairro Quioto, numero 9', 19960911),
	(130616, 'Minatozaki Sana', 18297392801, 'Rua Osake, Bairro Osaka, numero 29', 19962912);

create table telefone_funcionario(
	id_telefone_funcionario integer primary key,
	numero_telefone varchar(16) not null,
	id_funcionario integer not null,
	constraint fk_id_funcionario_telefone
	foreign key (id_funcionario)
	references funcionarios(id_funcionario)
	);

create table clientes(
	id_cliente integer primary key,
    nome_cliente varchar(200) not null,
    cpf_cliente integer not null
    );

insert into clientes values
	(820391, 'Jeon JungKook', 83949371801),
    (820392, 'Kim TaeHyung', 27896524801),
    (820393, 'Park Jimin', 25236857801);
	
create table produtos(
    id_produto integer primary key,
    nome_produto varchar(200) not null,
    quantidade_produto varchar(200) not null,
    descricao_produto varchar(200) not null,
    preco_unidade_produto varchar(200) not null
    );

insert into produtos values
    (839109,'Converse All Star Cano Alto - Preto - 37', 52, 'O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.', 240),
    (839110,'Converse All Star Cano Alto - Amarelo - 38', 40, 'O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.', 240),
    (839111,'Converse All Star Cano Alto - Vermelho - 37', 62, 'O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.', 220),
	(839112,'Converse All Star Cano Alto - Branco - 36', 70, 'O ALL STAR é um produto de tecido e sola de borracha plataforma, versátil e clássico.', 250);

create table pedidos(
    id_pedido integer primary key,
    instante_pedido datetime not null
    );