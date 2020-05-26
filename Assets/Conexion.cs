using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Net;
using System.Net.Sockets;
using System;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
//using System.Threading.Tasks;
using System.IO;
//using UnityEditor.PackageManager;
//using UnityEditorInternal;

public class Conexion : MonoBehaviour
{
    // Start is called before the first frame update
    public Dropdown Selector;
    public Button btn_Buscar;
    Cliente_Unity clienteVision;
    Cliente_Unity clienteVrep;
    int portC=8000,portV=8001;
    public Text posx, posy, posz;
    public Text hastaahora;
    public Text coordenviadas;
    public InputField coordDest;
    void Start()
    {
        posx.text = " esperando...";
        posy.text = " esperando...";
        posz.text = " esperando...";

    }
    public void Crearsocketsclientes()
    {
        clienteVrep = new Cliente_Unity(portC);
        Debug.Log("El socket cliente para comunicarse con V-Rep se ha creado correctamente");
        clienteVision = new Cliente_Unity(portV);
        Debug.Log("El socket cliente para comunicarse con Visiónn se ha creado correctamente");
    }

    public void conectar()
    {
        ComunicacionVREP();     
        ComunicacionVision();
    }

    public void EspPos()
    {
        string data = "";
        string cadena = "";
        data = coordDest.text.ToString();
        cadena = clienteVrep.Envio_Vrep(data);
        //if(CONDICION DE Q HA IDO BIEN)
        //coordenviadas.text = " EL ROBOT SE HA MOVIDO CON ÉXITO A LAS COORDENADAS SELECCIONADAS";
        //coordenviadas.color = color.Green;
        //else {
        //coordenviadas.text = "ERROR: LAS COORDENADAS ELEGIDAS ESTÁN FUERA DEL RANGO DE ACCIÓN DEL ROBOT O EL FORMATO ELEGIDO NO ES EL CORRECTO";
        //coordenviadas.color = color.Red;
        //  }
        char separador = '/';
        var posicionFinal = cadena.Split(separador);
        Debug.Log(" LA POSICION X ES: " + posicionFinal[0]);
        Debug.Log(" LA POSICION Y ES: " + posicionFinal[1]);
        Debug.Log(" LA POSICION Z ES: " + posicionFinal[2]);
        posx.text = "X:     " + posicionFinal[0] + " mm";
        posy.text = "Y:     " + posicionFinal[1] + " mm";
        posz.text = "Z:     " + posicionFinal[2] + " mm";
    }

    //FALTA REVISAR LAS POSICIONES 
    public void ComunicacionVREP()
    {
        string cadena = "";
        string data = "";

        if (Selector.captionText.text == "PLANTA 1")
        {
            data = "-100/+100/+150";
        }

        if (Selector.captionText.text == "PLANTA 2")
        {
            data = "+000/+100/+150";
        }
        if (Selector.captionText.text == "PLANTA 3")
        {
            data = "+100/+100/+150";
        }

        if (Selector.captionText.text == "PLANTA 4")
        {
            data = "-100/-100/+150";
        }
        if (Selector.captionText.text == "PLANTA 5")
        {
            data = "+000/-100/+150";
        }

        if (Selector.captionText.text == "PLANTA 6")
        {
            data = "+100/-100/+150";
        }

        cadena = clienteVrep.Envio_Vrep(data);
        char separador = '/';
        var posicionFinal = cadena.Split(separador);
        Debug.Log(" LA POSICION X ES: " + posicionFinal[0]);
        Debug.Log(" LA POSICION Y ES: " + posicionFinal[1]);
        posx.text = "X:     " + posicionFinal[0] + " mm";
        posy.text = "Y:     " + posicionFinal[1] + " mm";
        posz.text = "Z:     " + posicionFinal[2] + " mm";
    }

    public void ComunicacionVision()
    {
        //string cadena = "";
        string data = "";
        if (Selector.captionText.text == "PLANTA 1")
        {
            data = "1";
        }

        if (Selector.captionText.text == "PLANTA 2")
        {
            data = "2";
        }
        if (Selector.captionText.text == "PLANTA 3")
        {
            data = "3";
        }

        if (Selector.captionText.text == "PLANTA 4")
        {
            data = "4";
        }
        if (Selector.captionText.text == "PLANTA 5")
        {
            data = "5";
        }

        if (Selector.captionText.text == "PLANTA 6")
        {
            data = "6";
        }

        bool respuesta = clienteVision.EnvioVision(data);
        Debug.Log("La comunicación con el modulo de vision termino con: " + respuesta);
        hastaahora.text = ("SE HA ESTUDIADO LA " + Selector.captionText.text.ToString());
    }
}