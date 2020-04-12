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
    public Button btn_connect;
    public Text EstadoConnection;
    public Text EstadoBusqueda;
    public Dropdown Selector;
    public Button btn_Buscar;
    public Button btn_Estudio_11;
    TcpClient client;
    TcpListener servidor;
    Socket sock;
    int port;
    void Start()
    {
        btn_connect.onClick.AddListener(Connect);
        btn_Buscar.onClick.AddListener(realizarBusqueda);
        btn_Estudio_11.onClick.AddListener(Estudio);
    }

    // Update is called once per frame
    void Update()
    {
        
    }


    //Conexion con el programa servidor que esta a la espera (visión o movimientos)
    void Connect()
    {
        //Convert port number to text with error handling 
        if (!int.TryParse("8000", out port))
        {
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Port number no valied";
            print("Putada");
        }

        //Attemps to make connection
        try
        {
            client = new TcpClient("127.0.0.1", port);
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Connection Made";

        }
        catch (System.Net.Sockets.SocketException)
        {
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Connection Failed";
        }

    }

    //Envío TipoPlanta
    void realizarBusqueda()
    {
        try
        {
            string message = "BUSCAR " + Selector.captionText.text; //set message variable to input
            int byteCount = Encoding.ASCII.GetByteCount(message); //Measures bytes required to send ASCII data
            byte[] sendData = new byte[byteCount]; //Prepares variable size for required data
            sendData = Encoding.ASCII.GetBytes(message); //Sets the sendData variable to the actual binary data (from the ASCII)
            NetworkStream stream = client.GetStream(); //Opens up the network stream
            stream.Write(sendData, 0, sendData.Length); //Transmits data onto the stream
            EstadoConnection.text = "Consulta realizada sobre" + Selector.captionText.text;
            

        }
        catch (System.NullReferenceException) //Error if socket not open
        {
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Fallo al enviar datos";
        }

        //toolStripButton3 -- Close Connection


    }

    void Estudio()
    {
        try
        {
            string message = "ESTUDIAR LA POSICIÓN 1-1" ;//set message variable to input
            int byteCount = Encoding.ASCII.GetByteCount(message); //Measures bytes required to send ASCII data
            byte[] sendData = new byte[byteCount]; //Prepares variable size for required data
            sendData = Encoding.ASCII.GetBytes(message); //Sets the sendData variable to the actual binary data (from the ASCII)
            NetworkStream stream = client.GetStream(); //Opens up the network stream
            stream.Write(sendData, 0, sendData.Length); //Transmits data onto the stream
            EstadoConnection.text = "Consulta realizada sobre" + Selector.captionText.text;


        }
        catch (System.NullReferenceException) //Error if socket not open
        {
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Fallo al enviar datos";
        }

        //toolStripButton3 -- Close Connection


    }


}
