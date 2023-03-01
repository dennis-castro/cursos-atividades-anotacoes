package fundamentos

fun main(){
    dizOi(retornaNome(),28)
    dizOi(nome = "luara", idade = 33)

}

fun retornaNome(): String{
    return "Dennis"
}

fun dizOi(nome: String, idade: Int){
    println("Ola ${nome} parabens pelos seu ${idade} anos ")
}
