package fundamentos

//usando for
fun main (){
    //cont()
    //contReverso()
    //contPar()
    //contParame(2,20)
    contador()
}

fun cont(){
    for (num in 1..10){
        println(num)
    }
}

fun contReverso(){
    for (num in 10 downTo 1){
        println(num)
    }
}

fun contPar(){
    for (num in 2..10 step 2)
        println(num)
}

fun contParame(ini: Int, fim: Int){
    for (num in ini..fim){
        println(num)
    }
}


//usando while
fun contador(){
    var c = 1
    while (c < 10){
        println(c)
        c++
    }
}

