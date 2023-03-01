select * from gafanhotos;

#ex01
select * from gafanhotos
where sexo = 'F' 
order by nome;

#ex02
select * from gafanhotos
where nascimento between '2000/01/01' and '2015/12/31'
order by nascimento;

#ex03
select * from gafanhotos
where sexo = 'M' and profissao = 'programador'
order by nome;

#ex04
select * from gafanhotos
where nome like 'j%' and sexo= 'F' and nacionalidade =  'brasil';

#ex05
select nome, nacionalidade, peso from gafanhotos
where nome like '%silva%' and sexo = 'M' and peso < 100 and nacionalidade not like 'brasil';

#ex06
select max(altura) from gafanhotos
where sexo = 'M' and nacionalidade = 'brasil';

#ex07
select avg(peso) from gafanhotos;

#ex08
select min(peso) from gafanhotos
where sexo = 'F' and nasgafanhotoscimento between '1990/01/01' and '2000/12/31' and nacionalidade not like 'brasil';

#ex09
select count(*) from gafanhotos
where sexo = 'F' and altura > '1.90';
