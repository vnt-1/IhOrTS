CREATE DATABASE plantas_db;
use plantas_db;

CREATE TABLE plantas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome_popular VARCHAR(255) NOT NULL,
    nome_cientifico VARCHAR(255) NOT NULL,
    imagem_path TEXT
);

CREATE TABLE dados(
	id_dados INT AUTO_INCREMENT PRIMARY KEY,
    temperatura DECIMAL NOT NULL,
    luminosidade INT NOT NULL,
    umidade DECIMAL NOT NULL
);

ALTER TABLE plantas ADD COLUMN estatus CHAR(1) DEFAULT 'A';
ALTER TABLE dados ADD COLUMN estatus CHAR(1) DEFAULT 'A';

SELECT * FROM plantas;
SELECT * FROM dados;