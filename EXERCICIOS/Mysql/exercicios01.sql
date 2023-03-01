use cadastro;

select * from gafanhotos;

#ex01
select profissao, count(*) from gafanhotos
group by profissao
order by profissao;

#ex02
select sexo, count(*) from gafanhotos
where nascimento >= '2005/01/01'
group by sexo;

#ex03
select nacionalidade, count(*) from gafanhotos
where nacionalidade != 'brasil'
group by nacionalidade
having count(*) > 3;

#ex04
select altura, peso, count(peso) from gafanhotos
where peso > 100
group by altura
having altura > (select avg(altura) from gafanhotos)
order by altura;










