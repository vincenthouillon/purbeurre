CREATE DATABASE purbeurre CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'pbadmin'@'localhost' IDENTIFIED BY 'pbadmin';
USE purbeurre;
GRANT ALL ON purbeurre.* TO 'pbadmin'@'localhost';

USE purbeurre;
DROP TABLE IF EXISTS Records;


-- Create table Records
CREATE TABLE IF NOT EXISTS Records (
	id INT NOT NULL AUTO_INCREMENT,
	code VARCHAR(140) NOT NULL,
	product_name VARCHAR(140) NOT NULL,
	quantity VARCHAR(80),
	brand VARCHAR(140),
	store VARCHAR(140),
	nutriscore VARCHAR(1) NOT NULL,
	url VARCHAR(140) NOT NULL,
	category VARCHAR(140) NOT NULL,
	PRIMARY KEY(id)
	)
	ENGINE=InnoDB DEFAULT CHARSET = utf8 COLLATE utf8_unicode_ci;

-- To avoid duplicate product
CREATE UNIQUE INDEX UK_code ON Records (code);