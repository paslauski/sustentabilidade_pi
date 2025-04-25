Show databases;
CREATE DATABASE PI;
USE PI;

CREATE TABLE sustentabilidade(
  ID INT AUTO_INCREMENT PRIMARY KEY,
  DATA_ DATE NOT NULL,
  CA_GASTO DECIMAL(5,2) NOT NULL,
  NR_QUANTIDADE INT NOT NULL,
  NR_PORCENTAGEM INT NOT NULL,
  CE_GASTO DECIMAL(3,1) NOT NULL,
  UT_CARRO ENUM('S', 'N') NOT NULL,
  UT_CARONA_COMPARTILHADA ENUM('S', 'N') NOT NULL,
  UT_BICICLETA ENUM('S', 'N') NOT NULL,
  UT_TRANSPORTE_PUBLICO ENUM('S', 'N') NOT NULL,
  UT_CARRO_ELETRICO ENUM('S', 'N') NOT NULL,
  UT_CAMINHADA ENUM('S', 'N') NOT NULL
);

CREATE TABLE resultados(
  ID INT,
  DATA_ DATE,
  CA_RESULTADO VARCHAR(50),
  NR_RESULTADO VARCHAR(50),
  CE_RESULTADO VARCHAR(50),
  UT_RESULTADO VARCHAR(50),
  MS_RESULTADO VARCHAR(50),
  CONSTRAINT fk_id_resultado FOREIGN KEY (ID) REFERENCES sustentabilidade(ID)
);
INSERT INTO sustentabilidade 
VALUES (1, '2025-12-02', 50, 5, 5, 5, 'S', 'N', 'N', 'N', 'N', 'N');

INSERT INTO resultados (ID, DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO)
VALUES (1,'2025-12-02','Alta Sustentabilidade','Baixa Sustentabilidade','Moderada Sustentabilidade',
'Baixa Sustentabilidade');

INSERT INTO sustentabilidade 
VALUES (2, '2025-12-03', 160, 5, 5, 5, 'S', 'N', 'N', 'N', 'N', 'N');


INSERT INTO resultados (ID, DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO)
VALUES (2,'2025-12-03','Moderada Sustentabilidade','Baixa Sustentabilidade',
'Moderada Sustentabilidade','Baixa Sustentabilidade');

INSERT INTO sustentabilidade 
VALUES (3, '2025-12-03', 160, 5, 5, 5, 'S', 'N', 'N', 'N', 'N', 'N');

INSERT INTO resultados (ID, DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO)
VALUES (3,'2025-12-03','Moderada Sustentabilidade','Baixa Sustentabilidade',
'Moderada Sustentabilidade','Baixa Sustentabilidade');

UPDATE sustentabilidade
SET CE_GASTO = 8
WHERE ID = 1;

UPDATE resultados
SET UT_RESULTADO = "Baixa Sustentabilidade"
WHERE ID = 2;

SELECT * FROM sustentabilidade;
SELECT * FROM resultados;

TRUNCATE TABLE resultados;

ALTER TABLE resultados
DROP FOREIGN KEY fk_id_resultado;

TRUNCATE TABLE sustentabilidade;

DROP TABLE resultados;

DROP TABLE sustentabilidade;
