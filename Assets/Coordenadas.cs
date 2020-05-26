using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class Coordenadas : MonoBehaviour
{
    public Text mensaje;
    public InputField a, b, c;
    double m, n, p;
    double limite = 250.00;
    // Start is called before the first frame update
    void Start()
    {
      
    }

    // Update is called once per frame
    void Update()
    {
       
    }
    public void mandarrobot()
    {
        //MANDAR POR SOCKETS LAS COORDENADAS
        m = double.Parse(a.text);
        n = double.Parse(b.text);
        p = double.Parse(c.text);
        //ENVIAR LAS COORDENADAS CON UN TIPO DE PETICION
        //INCLUIR COMPROBACION DE COORDENADAS VALIDAS AQUI, ANTES DE EJECUTAR EL CONTROL Y MANDAR EL ROBOT A PARLA
    }
    public void Enviarcoord()
    {
        
        if (double.Parse(a.text) < limite &&  double.Parse(b.text) < limite && double.Parse(a.text) > -limite && double.Parse(b.text) > -limite)
        {
            mensaje.text = "COORDENADAS ENVIADAS CORRECTAMENTE";
        }
        else
        {
            mensaje.text = "LAS COORDENADAS ESTÁN FUERA DEL ALCANCE DEL ROBOT";
        }
    }
}
