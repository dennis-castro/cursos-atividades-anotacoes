package fundamentos

class  minhaClasse(
    var nome:String,
    var endereco:String,
    var numero:Int]
) {
    companion object {
        fun criarClasse(){
            return minhaClasse("dennis","testeRua",22)
        }
    }
}

fun main(){
    var segundaClasse = minhaClasse.criarClasse()
}

companion object = server para deixar uma classe com valores padrao