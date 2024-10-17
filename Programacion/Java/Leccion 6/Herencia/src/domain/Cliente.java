package domain;

import java.util.Date;

public class Cliente extends Persona {

    //Atributos
    private Date fechaRegistro;//importar clase Date
    private boolean vip;
    private static int contadorCliente;
    private int idCliente;

    //Constructor
    public Cliente(Date fechaRegistro, boolean vip, String nombre,char genero, int edad, String direccion) {
        super(nombre, genero, edad, direccion); //utilizamos este constructor para tomar los atributos de la clase padre
        this.idCliente = ++Cliente.contadorCliente;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }


    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append(", idCliente=").append(idCliente);
        sb.append("fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
}
