
import java.util.Scanner;
import operacoes.Operacao;
import operacoes.filhas.Soma;
import operacoes.filhas.Subtracao;
import operacoes.filhas.Divisao;
import operacoes.filhas.Multiplicacao;
import javafx.application.Application;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;


public class Main extends Application {

    
    public static void main(String[] args) throws Exception {

        launch(args);

        
        Operacao multi = new Multiplicacao();
        Operacao div = new Divisao();
        Operacao sub = new Subtracao();
        Operacao soma = new Soma();
        Operacao lista[] = {multi, div, sub, soma};


        double x = 0;
        double y = 0;
        int precisao = 0;

        Scanner scanner = new Scanner(System.in);

        System.out.printf("insira o valor de X\n");
        x = scanner.nextDouble();
        System.out.printf("insira o valor de Y\n");
        y = scanner.nextDouble();
        System.out.printf("insira o valor de prescisao da resposta\npadrao: %d\n", div.getTruncarPadrao());
        precisao = scanner.nextInt();

        for(int i = 0; i <=2; i++)
        {
        System.out.println(x + lista[i].toString() + y + " = " + lista[i].executar(x, y));
        System.out.println(x + lista[i].toString() + y + " = " + lista[i].executar(x, y, precisao));
        }

        
        
        
    }

    @Override
    public void start(Stage arg0) throws Exception {
        
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("mainScen.fxml"));
        Parent root = fxmlLoader.load();
        Scene tela = new Scene(root);

        arg0.setScene(tela);
        arg0.show();
    }
    
   
}
