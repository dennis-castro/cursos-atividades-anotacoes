package fundamentos

fun main(){
    println(numExt(5))
}

fun numExt(num: Int): String{
    if(num == 4){
        return "quatro"
    }else if(num == 5){
        return "cinco"
    }else{
        return "Numero não encontrado"
    }
}