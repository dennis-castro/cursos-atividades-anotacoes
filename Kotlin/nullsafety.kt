package fundamentos

fun main() {
    //list ex:
    var lista: List<Int?> = listOf(1, 2, 3, null, 4)
    var listaNullable: List<Int?>? = null


    var nome : String? = null

    var tamanho : Int = nome?.length ?: 0

    val toShort : Short = nome!!.length.toShort()



    obs:
        !! = tem certeza q a variavel nao é null

        ?: = caso nao tenha nada lado esquerdo considerar o que esta no lado direito

        ? =  se o valor nao for null continua



}

