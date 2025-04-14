use BD170225416;
show tables;
#drop tables Consumo_Agua, Nao_Reciclaveis, Uso_Transporte, Consumo_Energia ;
create table Consumo_Agua
(
CA_ID int auto_increment primary key,
CA_NOME varchar (35) not null,
CA_DATA date,
CA_GASTO decimal (5,2)
);

create table Nao_Reciclaveis
(
NR_ID int auto_increment primary key,
NR_NOME varchar (35) not null,
NR_DATA date,
NR_QUANTIDADE int unsigned,
NR_PORCENTAGEM int unsigned
); 

create table Consumo_Energia
(
CE_ID int auto_increment primary key,
CE_NOME varchar (35) not null,
CE_DATA date,
CE_GASTO decimal (3,1)
); 

create table Uso_Transporte
(
UT_ID int auto_increment primary key,
UT_NOME varchar (35) not null,
UT_DATA date,
UT_MEIO enum ('1','2','3')
); 

insert into Consumo_Agua( CA_NOME,CA_DATA,CA_GASTO)
values ('Roberta','2025-01-01','100');

insert into Nao_Reciclaveis ( NR_NOME,NR_DATA,NR_QUANTIDADE,NR_PORCENTAGEM)
values ('Roberta','2025-01-01','10','40');

insert into Consumo_Energia ( CE_NOME,CE_DATA,CE_GASTO)
values ('Roberta','2025-01-01','4');

insert into Uso_Transporte ( UT_NOME,UT_DATA,UT_MEIO)
values ('Roberta','2025-01-01','1');


select * from Consumo_Energia;


