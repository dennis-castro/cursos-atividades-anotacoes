package fundamentos

fun main(){
    var lista = listOf(1,2,3,4)
    val pares = lista.filter { it % 2 == 0 }.first()
    println(pares)
    //modo de achar o primeiro numero par


    var lista = listOf(1,2,3,4)
    lista.forEach {
        println(it)
    }
    // usando for para passar por cada elemento da lista

    var lista = listOf(1,2,3,4)
    for (num in lista){
        println(num)
    // usando for para passar por cada elemento da lista

    }

    println(lista[0])//mostra a posição 0 na lista
    println(lista.size)//quantidade de registro que contem a lista
    println(lista.indexOf(4))//mostra a posição que esta o numero 4 na lista

    var lista = mutableListOf(1,2,3,4,5)//mutable gera uma lista mutavel

    lista.add(8)//adiciona um elemento a lista
    lista.removeAt(2)//remove usando como base a posição
    lista.remove(2)//remove o elemento
    lista[0] = 20//adiciona o 20 na posição 0

    lista.sort() // coloca em ordem alfabetica
    lista.shuffle()//embaralha a lista

    var setNumeros = setOf(1,2,3,4)// a mesma coisa de lista porem nao registra chave duplicada
    var setNumeros = mutableSetOf()// set mutavel


    var mapNomeIdade = mapOf("dennis" to 21, "luara" to 30)
    mapNomeIdade["carol"] = 22 // em mapof nao pode existir chave duplicada apenas valores
    mapNomeIdade.putIfAbsent("marcos",11)//caso nao tenha lista ele agrega a lista


}