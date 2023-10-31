package operacoes.filhas;
import operacoes.Operacao;

public class Multiplicacao extends Operacao{

    public Multiplicacao()
    {
        super("x");
    }
    
    @Override
    public double executar(int x, int y)
    {
        return(x*y);
    }

    @Override
    public double executar(double x, double y)
    {
        return(truncarValor(x*y, getTruncarPadrao()));
    }

    @Override
    public double executar(double x, double y, int truncamento)
    {
        return(truncarValor(x*y, truncamento));
    }
}
