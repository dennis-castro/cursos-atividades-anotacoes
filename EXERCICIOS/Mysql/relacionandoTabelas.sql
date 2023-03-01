use registro;

desc filmes;
select * from filmes;

desc cadastro;
select * from cadastro;

alter table cadastro
add foreign key (filme_preferido)
references filmes (idfilmes);

select cadastro.nome, filmes.filme, filmes.genero
from cadastro join filmes
on cadastro.filme_preferido = filmes.idfilmes;

