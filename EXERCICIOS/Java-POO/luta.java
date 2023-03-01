//classe lutador
public class Lutador {
    //atributos
    private String nome;
    private String nacionalidade;
    private int idade;
    private float altura;
    private float peso;
    private String categoria;
    private int vitorias, derrotas, empates;
    
   //metodos publicos
    public void apresentar(){
        System.out.println("------------------------------------------------------------------");
        System.out.println("CHEGOUUUU A HORA!!! vamos apresentar o lutador "+ this.getNome());
        System.out.println("Diretamente do "+ this.getNacionalidade());
        System.out.println("Com "+this.getIdade()+" anos e "+this.getAltura()+" de altura");
        System.out.println("Pesando "+ this.getPeso()+" kilos");
        System.out.println(this.getVitorias()+" Vitorias");
        System.out.println(this.getDerrotas()+" Derrotas");
        System.out.println(this.getEmpates()+" Empates");
    }
    public void status(){
        System.out.println(this.getNome()+" lutador peso " +this.getCategoria());
        System.out.println(this.getVitorias()+" Vitorias");
        System.out.println(this.getDerrotas()+" Derrotas");
        System.out.println(this.getEmpates()+" Empates");
    }
    public void ganharLuta(){
        this.setVitorias(this.getVitorias() + 1);
        
    }
    public void perderLuta(){
        this.setDerrotas(this.getDerrotas() + 1);
        
    }
    public void empatarLuta(){
        this.setEmpates(this.getEmpates() + 1);
        
    }
            
    
    //metodos especiais

    public Lutador(String no, String na, int id,float al, float pe, int vi, int de, int em) {
        this.nome = no;
        this.nacionalidade = na;
        this.idade = id;
        this.altura = al;
        this.setPeso(pe);
        this.vitorias = vi;
        this.derrotas = de;
        this.empates = em;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        this.setCategoria();
    }

    public String getCategoria() {
        return categoria;
    }

    private void setCategoria() {
        if(this.getPeso() < 52.2){
            this.categoria = "Invalido";
        }else if(this.getPeso()<= 70.3){
            this.categoria = "Leve";
        }else if(this.getPeso()<= 83.9){
            this.categoria = "Médio";
        }else if(this.getPeso()<= 120.2){
            this.categoria = "Pesado";
        }else{
            this.categoria = "Invalido";
        }
    }

    public int getVitorias() {
        return vitorias;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }
    
    
}

//classe luta
import java.util.Random;

public class Luta {
    //atributos
    private Lutador desafiado;
    private Lutador desafiante;
    private int rounds;
    private boolean aprovada;
    
    //metodos
    public void marcarLuta(Lutador l1, Lutador l2){
        if (l1.getCategoria()== l2.getCategoria()
                && l1 != l2){
            this.setAprovada(true);
            this.setDesafiado(l1);
            this.setDesafiante(l2);
        }else{
            this.setAprovada(false);
            this.setDesafiado(null);
            this.setDesafiante(null);
        }
            
        
    }
    public void lutar(){
        if (this.aprovada){
            System.out.println("###desafiado###");
            this.desafiado.apresentar();
            System.out.println("###desafiante###");
            this.desafiante.apresentar();
            
            Random aleatorio = new Random();
            int vencedor = aleatorio.nextInt(3);// sorteia entre 0,1,2
            switch(vencedor){
                case 0: //empate
                    System.out.println("=====Resultado da luta=====");
                    System.out.println("Empatou...");
                    this.desafiado.empatarLuta();
                    this.desafiante.empatarLuta();
                    break;
                
                case 1: //desafiado vence
                    System.out.println("=====Resultado da luta=====");
                    System.out.println("Vitoria do... "+ this.desafiado.getNome());
                    this.desafiado.ganharLuta();
                    this.desafiante.perderLuta();
                    break;
                    
                case 2: //desafiante vence
                    System.out.println("=====Resultado da luta=====");
                    System.out.println("Vitoria do..."+this.desafiante.getNome());
                    this.desafiante.ganharLuta();
                    this.desafiado.perderLuta();
                    break;
            } 
            
        }else{
            System.out.println("A luta não pode acontecer !!");
        }
        System.out.println("==============================");
    }
    
    //metodos especias

    public Lutador getDesafiado() {
        return desafiado;
    }

    public void setDesafiado(Lutador desafiado) {
        this.desafiado = desafiado;
    }

    public Lutador getDesafiante() {
        return desafiante;
    }

    public void setDesafiante(Lutador desafiante) {
        this.desafiante = desafiante;
    }

    public int getRounds() {
        return rounds;
    }

    public void setRounds(int rounds) {
        this.rounds = rounds;
    }

    public boolean isAprovada() {
        return aprovada;
    }

    public void setAprovada(boolean aprovada) {
        this.aprovada = aprovada;
    }
    
}

//programa
public class ufc {

    public static void main(String[] args) {
        Lutador l[] = new Lutador[6]; 
        l[0] = new Lutador("Prety Boy", "França", 31, 1.75f, 68.9f, 11, 2, 1);
        l[1] = new Lutador("Putsscript", "Brasil", 29, 1.68f, 57.8f, 14, 2, 2);
        l[2] = new Lutador("Mike Tyson", "Estados Unidos", 50, 1.70f, 90f, 25, 2, 0);
        l[3] = new Lutador("Anderson S", "China", 22, 1.85f, 110.4f, 10,2,1);
        l[4] = new Lutador("jackie C", "Japão", 70, 1.50f, 58f, 2, 4 ,0);
        l[5] = new Lutador("Jaspion", "Colombia", 90, 1.90f, 89f, 30, 0,1);
        
        
    Luta UFC01 = new Luta();
    UFC01.marcarLuta(l[2], l[5]);
    UFC01.lutar();
    //l[0].status();
    //l[1].status();
    }
    
}
