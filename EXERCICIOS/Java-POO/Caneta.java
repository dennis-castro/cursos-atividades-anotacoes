//classe Caneta
public class Caneta {
    String modelo;
    String cor;
    float ponta;
    int carga;
    boolean tampada;

    void status() {
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Cor: " + this.cor);
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Carga: " + this.carga);
        System.out.println("Está tampada? " + this.tampada);
    }

    void rabiscar() {
        if (this.tampada == true) {
            System.out.println("ERRO! Não posso rabiscar.");
        } else {
            System.out.println("Estou rabiscando!");
        }

    }

    void tampar() {
        this.tampada = true;

    }

    void destampar() {
        this.tampada = false;

    }
}

//programa
public static void main(String[] args) {
    Caneta c1 = new Caneta();
    c1.cor = "Azul";
    c1.ponta = 0.5f;
    c1.tampada = false; 
    c1.destampar();
    c1.status();
    c1.rabiscar();
    
    Caneta c2  = new Caneta();
    c2.cor = "Vermelha";
    c2.ponta = 1.0f;
    c2.tampada =false;
    c2.status();
    c2.tampar();
    c2.rabiscar();
            
}


