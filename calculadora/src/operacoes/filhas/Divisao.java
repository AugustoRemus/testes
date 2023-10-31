package operacoes.filhas;
import operacoes.Operacao;



public class Divisao extends Operacao{

    public Divisao(){
        super("÷");
    }

    @Override
    public double executar(int x, int y)
    {
        return(x/y);
    }

    @Override
    public double executar(double x, double y)
    {
        return(truncarValor(x/y, getTruncarPadrao()));
    }

    @Override
    public double executar(double x, double y, int truncamento)
    {
        return(truncarValor(x/y , truncamento));
    }


}
