#create database PI;
#use PI;
show tables;
#drop tables sustentabilidade, resultados;
create table sustentabilidade(
ID int auto_increment primary key,
DATA_ date not null,
CA_GASTO decimal (5,2) not null,
NR_QUANTIDADE int not null,
NR_PORCENTAGEM int not null,
CE_GASTO decimal (3,1) not null,
UT_CARRO enum('S', 'N') not null,
UT_CARONA_COMPARTILHADA enum('S', 'N') not null,
UT_BICICLETA enum('S', 'N') not null,
UT_TRANSPORTE_PUBLICO enum('S', 'N') not null,
UT_CARRO_ELETRICO enum('S', 'N') not null,
UT_CAMINHADA enum('S', 'N') not null
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
add constraint fk_id_resultados
foreign key (ID) references sustentabilidade(ID);

alter table resultados
add constraint fk_data_resultado
foreign key (DATA_) references sustentabilidade(DATA_);


alter table resultados
add column Id_s int;

alter table resultados
add constraint fk_ID
foreign key (Id_s) references sustentabilidade(ID);



insert into sustentabilidade values(1, '2025-12-02', 50, 5, 5, 5, 'S', 'S', 'S', 'S', 'S', 'S');
alter table resultados
drop foreign key fk_data_resultados;
