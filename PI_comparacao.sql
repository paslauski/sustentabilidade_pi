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
  Id_s INT,
  CONSTRAINT fk_id_resultado FOREIGN KEY (ID) REFERENCES sustentabilidade(ID),
  CONSTRAINT fk_ID FOREIGN KEY (Id_s) REFERENCES sustentabilidade(ID)
);

INSERT INTO sustentabilidade 
VALUES (1, '2025-12-02', 50, 5, 5, 5, 'S', 'S', 'S', 'S', 'S', 'S');

INSERT INTO resultados (ID, DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO, Id_s)
SELECT
  s.ID,
  s.DATA_,

  CASE
    WHEN s.CA_GASTO < 150 THEN 'Alta Sustentabilidade'
    WHEN s.CA_GASTO >= 150 AND s.CA_GASTO <= 200 THEN 'Moderada Sustentabilidade'
    ELSE 'Baixa Sustentabilidade'
  END,

  CASE
    WHEN s.NR_PORCENTAGEM > 50 THEN 'Alta Sustentabilidade'
    WHEN s.NR_PORCENTAGEM >= 20 AND s.NR_PORCENTAGEM <= 50 THEN 'Moderada Sustentabilidade'
    ELSE 'Baixa Sustentabilidade'
  END,

  CASE
    WHEN s.CE_GASTO < 5 THEN 'Alta Sustentabilidade'
    WHEN s.CE_GASTO BETWEEN 5 AND 10 THEN 'Moderada Sustentabilidade'
    ELSE 'Baixa Sustentabilidade'
  END,

  CASE
    WHEN (s.UT_CARRO = 'S' OR s.UT_CARONA_COMPARTILHADA = 'S') AND 
         (s.UT_BICICLETA = 'S' OR s.UT_TRANSPORTE_PUBLICO = 'S' OR s.UT_CARRO_ELETRICO = 'S' OR s.UT_CAMINHADA = 'S')
    THEN 'Moderada Sustentabilidade'

    WHEN s.UT_CARRO = 'S' OR s.UT_CARONA_COMPARTILHADA = 'S'
    THEN 'Baixa Sustentabilidade'

    WHEN s.UT_BICICLETA = 'S' OR s.UT_TRANSPORTE_PUBLICO = 'S' OR s.UT_CARRO_ELETRICO = 'S' OR s.UT_CAMINHADA = 'S'
    THEN 'Alta Sustentabilidade'

    ELSE 'Sem Dados'
  END,

  s.ID

FROM sustentabilidade s;
