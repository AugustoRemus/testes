package operacoes.filhas;
import operacoes.Operacao;
public class Soma extends Operacao{

    public Soma(){
        super("+");
    }

    @Override
    public double executar(int x, int y) {
        return x + y;
    }

    @Override
    public double executar(double x, double y) {
        return this.truncarValor(x + y, getTruncarPadrao());
    }

    @Override
    public double executar(double x, double y, int truncamento) {
        return this.truncarValor(x + y, truncamento);
    }  
}
