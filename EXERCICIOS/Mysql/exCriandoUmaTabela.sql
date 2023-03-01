#tabela de registro
create database registro
default char set utf8
default collate utf8_general_ci;

use registro;

create table if not exists cadastro(
id int auto_increment,
nome varchar(30) not null,
nascimento date,
sexo enum ('F','M'),
altura decimal (3,2),
nacionalidade varchar (20) default 'Brasil',
primary key (id)
)default char set = utf8;

INSERT INTO `registro`.`cadastro` (`nome`, `nascimento`, `sexo`, `altura`) VALUES ('Dennis', '1986-01-21', 'm', '1.85');
INSERT INTO `registro`.`cadastro` (`nome`, `nascimento`, `sexo`, `altura`, `nacionalidade`) VALUES ('Luara', '1990-06-24', 'f', '1.70', 'França');
INSERT INTO `registro`.`cadastro` (`nome`, `nascimento`, `sexo`, `altura`, `nacionalidade`) VALUES ('Carlos', '2010-12-30', 'm', '1.80', 'Estados Unidos');
INSERT INTO `registro`.`cadastro` (`nome`, `nascimento`, `sexo`, `altura`, `nacionalidade`) VALUES ('Joelma', '2014-02-24', 'f', '1.60', 'Alemanha');

alter table cadastro
add filme_preferido varchar(30);

select * from cadastro;

desc cadastro;

#tabela de filmes
CREATE TABLE if not exists registro.filmes (
  idfilmes INT NOT NULL AUTO_INCREMENT,
  filme VARCHAR(45) NULL,
  genero VARCHAR(45) NULL,
  duração DECIMAL(3,2) NULL,
  PRIMARY KEY (idfilmes))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

select * from filmes;

desc filmes;

INSERT INTO `registro`.`filmes` (`filme`, `genero`, `duração`) VALUES ('Mad Max', 'Ação', '1.20');
INSERT INTO `registro`.`filmes` (`filme`, `genero`, `duração`) VALUES ('Panico', 'terror', '1.30');
INSERT INTO `registro`.`filmes` (`filme`, `genero`, `duração`) VALUES ('Titanic', 'Drama', '2.30');
INSERT INTO `registro`.`filmes` (`filme`, `genero`, `duração`) VALUES ('American Pie', 'Comédia', '0.59');
INSERT INTO `registro`.`filmes` (`filme`, `genero`, `duração`) VALUES ('Homem Aranha', 'Ação', '1.45');
