import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class Controle {

    @FXML
    private TextField EntradaDois;

    @FXML
    private TextField entradaUm;

    @FXML
    private TextField lugar;

    @FXML
    void dividir(ActionEvent event){

        if (entradaUm.getText().equals("") || EntradaDois.getText().equals(""))
    {
         lugar.setText("Caixa em branco");
    }
    else

        try{
            Float u;
            u = Float.parseFloat(entradaUm.getText());
            Float d;
            d = Float.parseFloat(EntradaDois.getText());
            Float imprimir = u / d;
            lugar.setText(imprimir.toString());
        }
        catch (NumberFormatException erro){
             lugar.setText("Caracter invalido");
        }
    }

    @FXML
    void multiplicar(ActionEvent event) {

       if (entradaUm.getText().equals("") || EntradaDois.getText().equals(""))
    {
         lugar.setText("Caixa em branco");
    }
    else

        try{
            Float u;
            u = Float.parseFloat(entradaUm.getText());
            Float d;
            d = Float.parseFloat(EntradaDois.getText());
            Float imprimir = u * d;
            lugar.setText(imprimir.toString());
        }
        catch (NumberFormatException erro){
             lugar.setText("Caracter invalido");
        }
    }

    @FXML
    void somar(ActionEvent event)  {

    if (entradaUm.getText().equals("") || EntradaDois.getText().equals(""))
    {
         lugar.setText("Caixa em branco");
    }
    else

        try{
            Float u;
            u = Float.parseFloat(entradaUm.getText());
            Float d;
            d = Float.parseFloat(EntradaDois.getText());
            Float imprimir = u + d;
            lugar.setText(imprimir.toString());
        }
        catch (NumberFormatException erro){
             lugar.setText("Caracter invalido");
        }
        

        
    }

    @FXML
    void subtrair(ActionEvent event) {

        if (entradaUm.getText().equals("") || EntradaDois.getText().equals(""))
    {
         lugar.setText("Caixa em branco");
    }
    else

        try{
            Float u;
            u = Float.parseFloat(entradaUm.getText());
            Float d;
            d = Float.parseFloat(EntradaDois.getText());
            Float imprimir = u - d;
            lugar.setText(imprimir.toString());
        }
        catch (NumberFormatException erro){
             lugar.setText("Caracter invalido");
        }
    }

}
