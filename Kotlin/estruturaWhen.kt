package fundamentos

fun main() {


    val x = 10

    when (x) {
        5,-5 -> println("x == 5")
        8 -> println("x == 8")
        10 -> {
            println("x==10")
            println("10 é uma dezena!")
        }
        in 10..15-> println("x esta entre 10  e 15")
        !in 16..20 -> println("x não esta no range de 16 a 20")
        else -> println("numero nao encontrado")
    }
    when{
    comecaComOi(5) -> println("5")
    comecaComOi("oi tudo bem ?")-> println("olaaaaaaaaaa")
    }
}



fun comecaComOi(x:Any): Boolean{
    return when(x){
        is String -> x.startsWith("oi")
        else -> false
    }

}

