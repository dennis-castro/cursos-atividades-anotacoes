...........................CRIANDO BANCO DE DADOS
create database teste   #criar banco de dados
default character set utf8 #padrão de escrita portugues
default collate utf8_general_ci; #padrão de escrita portugues

..........................CRIANDO TABELAS
create table t1(    #criar tabela 
id int not null auto_increment,  #inteiro - campo obrigatorio - auto preechimento
nome varchar(30)not null,  #campo com 30 espaços para escrita -  campo obrigatorio
nascimento date, #datas
sexo enum ('M', 'F'),   #serve como campo obrigario ou M ou F
peso decimal (5,2),  #cinco casas decimais 000,00
altura decimal (3,2), #tres casas decimais 00,0
nacionalidade varchar(20) default 'Brasil', #campo com 20 espaços para escrita - caso nao insira nada espaço sera preechido como 'brasil'
primary key (id) #chave primaria
)default char set = utf8; #padrão de escrita portugues

.....................................CRIANDO E MANIPULANDO TABELAS P2
create table if not exists tabe1 ( # se nao existir a tabela tabe1 crie!
nome varchar(30) not null unique ,  # campo com 30 espacos -  preechimento obrigatorio - nao pode se repetir
descricao text, # campo com espaço indefinido
carga int unsigned, # inteiro - neutraliza sinais (+ - *)
totaulas int unsigned, #inteiro - neutraliza sinais (+ - *)
ano year default '2022' # ano -  caso nao preecha ano sera 2022
alter table tabe1
add idcurso int first;
add primary key (idcurso);  #  deixa a coluna como chave primaria (obs para isso tem que criar a coluna antes)
)default char set = utf8; # padrao de escrita portugues

..............................USANDO SELECT 
select nome, descrição, ano from (...)
where ano in (2014, 2016)  # operador IN indica que voce esta procurando entre os anos informados
order by ano, nome; # coloca em order ascendente primeiro o ano depois o nome 

select nome, descrição, ano from (...)
where ano between  2014 and 2016 # indica que voce esta procurando na faixa entre 2014 e 2016
order by ano, nome; # coloca em order ascendente primeiro o ano depois o nome 

select nome, carga, totaulas from (...)
where carga > 35 and totaular < 30;  # coloca parametros entre maior e menor 

select * from (gafanhotos)
where nome like '%a'   #seleciona os nomes que tem a letra A no fim da palavra

select * from (gafanhotos)
where nome like 'a%';  #seleciona os nomes que tem a letra A no começo

select * from (gafanhotos)
where nome like '%a%'; # seleciona os nomes que tem a letra A em qualquer posição

select * from (gafanhotos)
where nome like 'p_h'; # seleciona as palavras que tenham uma letra entre p e h

select * from (gafanhotos)
where nome not like %a%; # seleciona as palavras que nao contem a letra A 

select distinct nacionalidade from gafanhotos
order by nacionalidade   # seleciona os paises sem repetir caso ja tenha na lista 

select nacionalidade, count (* ou ...) from gafanhotos
group by nacionalidade  # agrupa todos os campos repetidos  junto com count conta quantos campos esta agrupado

select nacionalidade count (* ou ...) from gafanhotos
group by nacionalidade
having count(*) > 3;   # mostra agrupado somente quem tem grupos maior que 3.. obs so mostra o campo que voce agrupou (nacionalidade) 

select * from cursos;
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos); # seleciona os cursos acima da media sem a necessidade de ficar alterando a media 


select count(*) from cursos; # serve para contar campos

select max(carga) from cursos; # vai selecionar a maior carga  

select min(carga) from cursos; # vai selecionar a menor carga

obs:
% ...significa poder vazio seguido de qualquer coisa
_ ... significa que possui uma letra a frente
sum ... para somar
avg ... para tirar media

...................................CRIANDO REGISTROS
insert into t1 values # inserindo dados na tabela t1 - valores
(default, 'Dennis', '1986-01-21', 'M', '85', '1.85', 'Brasil'),# id, nome, data, sexo, peso, alura, nacionalidade
(default, 'luara', '1990-6-24', 'F', '60', '1.60', 'Italia');

..................................MOSTRANDO DADOS
select * from t1; # seleciona *toda tabela de t1 para mostrar dados
desc  t1; # mostra a estrutura da tabela

......................................MANIPULANDO TABELAS
alter table t1 # alterando tabela
*add profissao varchar(10); # adiciona a coluna o campo profissao
*drop profissao; # deleta o campo selecionado
*add profissao varchar(10) after nome; #adiciona o campo profissao depois do nome 
*add codigo int first; # adiciona o campo na primeira posição
*modify profissao varchar(20) not null default ''; # modifica o campo alterando os constrants 
*change profissao prof varchar(20) not null  default ''; # modifica o nome da coluna 
*rename to t22; # muda o nome da tabela
*add primary key (...);  #  deixa a coluna como chave primaria para nao ter problema de repetição (obs para isso tem que criar a coluna antes)

...................................CRIANDO UMA CHAVE ESTRANGEIRA #chave de realçao entre tabelas
alter table gafanhotos
add column cursopreferido int;# adiciona um campo na tabela 

alter table gafanhotos
add foreign key (cursopreferido) # adiciona uma chave como referencia
references cursos (idcurso); # usando como referencia "idcurso"

select g.nome, c.nome, c.ano  # seleciona os campos para amostra
from gafanhotos as g join cursos as c # AS(funciona para simplificar a escrita um apelido) JOIN(funciona para unir as tabelas)
on c.idcurso = g.cursopreferido # funciona para identificar o que sera mostrado entre as relaçoes das tabelas 
order by g.nome; # ordena por nome 

select g.nome, c.nome, c.ano  # seleciona os campos para amostra
from gafanhotos as g left join cursos as c # neste caso colocamos a palavra left entre gafanhotos e cursos (LEFT ira mostrar todos os registros do lado esquerdo(gafanhotos))
on c.idcurso = g.cursopreferido # funciona para identificar o que sera mostrado entre as relaçoes das tabelas 
.....................................MODIFICANDO ERROS NA TABELA
update t1 #atualizar
set nome = 'html5', ano = '2015'  #configurar - nome recebe novo nome (html5) e ano recebe (2015)
where idcurso = '1'  # referencia onde mudar  ex: where (primary key)  linha '1'
limit 1; # limita o numero de linhas a ser modificada

delete from t1
where id = '3' # apaga a linha especificada (3) da coluna 'id'
limit 1

truncate t1; # apaga todos registros da tabela e mantem a estrura





