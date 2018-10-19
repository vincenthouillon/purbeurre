CREATE DATABASE purbeurre CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'pbadmin'@'localhost' IDENTIFIED BY 'pbadmin';
USE purbeurre;
GRANT ALL ON purbeurre.* TO 'pbadmin'@'localhost';

-- Create table
CREATE TABLE IF NOT EXISTS Categorie("""
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(140) NOT NULL,
	PRIMARY KEY(id))
	ENGINE=InnoDB
	DEFAULT CHARSET = utf8 COLLATE utf8_unicode_ci;
	""")

