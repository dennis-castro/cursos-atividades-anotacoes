package fundamentos

class Pessoa(var nome: String, var idade: Int){
    override fun toString(): String {
        return "Classe:Pessoa, nome:${nome} idade: ${idade}"
    }
}

fun main(){
    var dennis = Pessoa("Dennis", 24)
    println(dennis)
}