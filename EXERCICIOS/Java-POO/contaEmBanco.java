//classe abrindo uma conta
package ;

public final class ContaBanco {
    //Atributos
    public int numConta;
    protected String tipo;
    private String dono;
    private float saldo;
    private boolean status;
    //Metodos Personalizados
 public void estadoAtual(){
     System.out.println("---------------------------");
     System.out.println("Conta: "+ this.getNumConta());
     System.out.println("Tipo: "+this.getTipo());
     System.out.println("Dono: "+this.getDono());
     System.out.println("Saldo: "+this.getSaldo());
     System.out.println("Status: "+this.isStatus());
 }
 public void abrirConta(String t){
     this.setTipo(t);
     this.setStatus(true);
     if (t == "CC"){
         this.setSaldo(50);
     }else if(t == "CP"){
         this.setSaldo(150);
     }
     System.out.println("Conta aberta com sucesso!");
 }
 public void fecharConta(){
     if (this.getSaldo() > 0){
         System.out.println("A conta não pode ser fechada esta POSITIVA");
     }else if(this.getSaldo() < 0){
         System.out.println("A conta não pode ser fechada esta NEGATIVA");
     }else{
         System.out.println("Conta fechado com sucesso!");
     }
         
 }
 public void depositar(float v){
     if (this.isStatus()){
         this.setSaldo(this.getSaldo()+v);
         System.out.println("Deposito realizado na conta de "+this.getDono());
     }else{
         System.out.println("Conta fechada impossivel realizar o deposito!");
     }
 }
 public void sacar(float v){
     if (this.isStatus()){
         if(this.getSaldo() >= v){
             this.setSaldo(this.getSaldo() - v);
             System.out.println("Saque realizado da conta de "+ this.getDono());
         }else{
             System.out.println("Saldo insuficiente para saque!");
         }
            
     }else {
         System.out.println("Conta fechada impossivel realizar saque!");
     }
 }
 public void pagarMensal(){
     int v = 0;
     if(this.getTipo() == "CC"){
         v = 12;
     }else if(this.getTipo() == "CP")
         v=20;
     if (this.isStatus()){
         this.setSaldo(this.getSaldo() - v);
         System.out.println("Mensalidade paga com sucesso por "+ this.getDono());
     }
 }
    //Metodos Especiais

    public ContaBanco() {
        this.setSaldo(0);
        this.setStatus(false);
    }

    public int getNumConta() {
        return numConta;
    }

    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getDono() {
        return dono;
    }

    public void setDono(String dono) {
        this.dono = dono;
    }

    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
    
    
    
}

//programa
public class{

    public static void main(String[] args) {
        ContaBanco p1 = new ContaBanco();
        p1.setNumConta(1111);
        p1.setDono("denn");
        p1.abrirConta("CC");
        
        
        ContaBanco p2 = new ContaBanco();
        p2.setNumConta(2222);
        p2.setDono("luara");
        p2.abrirConta("CP");
        
        
        
        p1.depositar(300);
        p2.depositar(500);
        p2.sacar(100);
        
        p1.estadoAtual();
        p2.estadoAtual();
     
    }
    
}