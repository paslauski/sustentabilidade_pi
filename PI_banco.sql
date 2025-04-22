create database PI;
use PI;
show tables;

create table sustentabilidade(
ID int auto_increment primary key,
DATA_ date unique not null,
CA_GASTO decimal (5,2) not null,
NR_QUANTIDADE int not null,
NR_PORCENTAGEM int not null,
CE_GASTO decimal (3,1) not null,
UT_CARRO boolean not null,
UT_CARONA_COMPARTILHADA boolean not null,
UT_BICICLETA boolean not null,
UT_TRANSPORTE_PUBLICO boolean not null,
UT_CARRO_ELETRICO boolean not null,
UT_CAMINHADA boolean not null 
);

create table resultados(
ID int,
DATA_ date,
CA_RESULTADO varchar(50),
NR_RESULTADO varchar(50),
CE_RESULTADO varchar(50),
UT_RESULTADO varchar(50)
);

alter table resultados
add constraint fk_id_resultado
foreign key (ID) references sustentabilidade(ID);

alter table resultados
add constraint fk_data_resultado
foreign key (DATA_) references sustentabilidade(DATA_);




select * from sustentabilidade;