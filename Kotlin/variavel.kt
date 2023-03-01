package fundamentos

fun main(){
    var nome = "nome" //mutavel
    val nomeVal = "nome" //nao mutavel
}

class variaveis(){
    lateinit var teste: String // para passa depois a variavel

    fun inicarVar(){
        teste = "Teste"
    }
}