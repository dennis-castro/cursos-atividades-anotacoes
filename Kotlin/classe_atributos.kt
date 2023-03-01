package fundamentos
//var -é uma variavel mutavel
//val -nao mutavel


class Carro(var cor: String,val anoFabricacao: Int, val dono: Dono)

data class  Dono(var nome: String,var idade: Int)

fun main(){
    var carro= Carro("Branco",2020, Dono("Dennis",23))

    println(carro.cor)
    carro.cor = "Preto"
    println(carro.cor)
    println(carro.dono)
    carro.dono.nome = "Luara"
    println(carro.dono)
}