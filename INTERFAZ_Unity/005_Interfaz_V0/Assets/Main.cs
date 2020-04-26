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
using System.Threading.Tasks;



public class Main : MonoBehaviour
{
    // Start is called before the first frame update
    int[] color = new int[6];
    int[] DF = new int[6];
    string[] Tipo = new string[6];
    public Text[] color_ = new Text[6];
    public Text[] DF_ = new Text[6];
    public Text[] Tipo_ = new Text[6];
    public Button[] ConsultaPos_= new Button[6];
    public Dropdown ConsultaPlanta;
    public Button ConsultaPanta;
    public Image Delta; 
    void Start()
    { 
        for(int i=0;i>6;i++)
        {
            color[i] = -1;
            DF[i] = -1;
            Tipo[i] = "SIN BUSQUEDAS REGISTRADAS";

        }

        
    }

    // Update is called once per frame
    void Update()
    {
        Actualiza();
        
    }

    void Actualiza()
    {
        

        
            for (int i = 0; i < 6; i++)
            {
                if (color[i] < 0 || DF[i] < 0)
                {
                    Tipo_[i].text= "SIN BUSQUEDAS REGISTRADAS";
                    DF_[i].text = " ";
                    color_[i].text = " ";
                }
                else
                {
                    DF_[i].text = "DF =  " + DF[i].ToString();
                    color_[i].text = "CLR =  " + color[i].ToString();
                    Tipo_[i].text = Tipo[i];
                }
                



            }
        }

    //Si la información que almacenamos al consultar la base de datos es:
        //Cons_Posicion :  posición en la que se encuentra la planta consultada en la base de datos(1,2,3,4,5,6)
        //Cons_Tipo: Tipo consultado en la base de datos
        //Cons_DF: DF consultada en la base de datos; 
        //Cons_color: color consultado en la base de datos;
    
    void Cargar_Consulta(int Pos, string tipo, int DensFoliar, int Color)
    {
        Tipo[Pos] = tipo;
        DF[Pos] = DensFoliar;
        color[Pos] = Color;

    }

    void Consulta_Planta()
    {
        int Cons_Posicion;
        string Cons_Tipo;
        int Cons_DF;
        int Cons_color;
        //CODIGO DE CONSULTA A LA BASE DE DATOS Y ALMACENAMIENTO EN LAS VARIABLES DECLARADAS

        Cons_Posicion = 1;
        Cons_Tipo = "Prueba";
        Cons_DF = 1;
        Cons_color = 1;
        Cargar_Consulta(Cons_Posicion, Cons_Tipo, Cons_DF, Cons_color);

    }

    //Respecto a la información del robot, necesitamos su posicion 2D, que obtenemos desde la socket que se comunica con vrep
    void PosRobot()
    {

    }
}
