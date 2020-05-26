using System.Collections;
using System.Collections.Generic;
using System.Xml.Schema;
using UnityEngine;
using UnityEngine.UI;


public class MAININTERFAZ_V1 : MonoBehaviour
{
    public Text estrobot;
    public Color Color;
    // Start is called before the first frame update
    void Start()
    {
        estrobot.text = "OFF";
        estrobot.color = Color.red; 
        
    }
    public void Actualizatexto()
    {
        if (estrobot.text == "OFF")
        {
            estrobot.text = " ROBOT CONECTADO. LOS SOCKETS CLIENTES SE HAN CREADO CORRECTAMENTE";
            estrobot.color = Color.green;
        }

  
    }
}
