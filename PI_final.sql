create database PI;
use PI;
-- drop database PI;
show tables;
-- select * from sustentabilidade;
-- select * from resultados;
-- drop tables sustentabilidade, resultados;
-- drop table resultados;
create table sustentabilidade(
ID int auto_increment primary key,
DATA_ date not null,
CA_GASTO decimal (5,3) not null,
NR_QUANTIDADE int not null,
NR_PORCENTAGEM int not null,
CE_GASTO decimal (5,3) not null,
UT_CARRO enum('S', 'N') not null,
UT_CARONA_COMPARTILHADA enum('S', 'N') not null,
UT_BICICLETA enum('S', 'N') not null,
UT_TRANSPORTE_PUBLICO enum('S', 'N') not null,
UT_CARRO_ELETRICO enum('S', 'N') not null,
UT_CAMINHADA enum('S', 'N') not null
);

create table resultados(
DATA_ date,
CA_RESULTADO varchar(50),
NR_RESULTADO varchar(50),
CE_RESULTADO varchar(50),
UT_RESULTADO varchar(50)
);

ALTER TABLE resultados
ADD COLUMN ID INT PRIMARY KEY AUTO_INCREMENT FIRST;

ALTER TABLE resultados
ADD CONSTRAINT fk_id_sustentabilidade
FOREIGN KEY (ID) REFERENCES sustentabilidade(ID);

