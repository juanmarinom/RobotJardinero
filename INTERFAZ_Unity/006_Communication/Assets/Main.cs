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
using System.IO;

public class Main : MonoBehaviour
{
    // Start is called before the first frame update
    public Button btn_connect;
    public Text EstadoConnection;
    public Text EstadoBusqueda;
    public Dropdown Selector;
    public Button btn_Buscar;
    TcpClient client;
    TcpListener server;
    Socket sock;
    Cliente_Unity clienteVision;
    Cliente_Unity clienteVrep;
    int port;
    NetworkStream stream;
    void Start()
    {
        btn_connect.onClick.AddListener(Connect_client);
        btn_Buscar.onClick.AddListener(PruebaSock);
        clienteVrep = new Cliente_Unity(8000);
        //Int32 port = 8000;
        // IPAddress localAddr = IPAddress.Parse("127.0.0.1");

        //TcpListener server = new TcpListener(port);
        // client = new TcpClient("127.0.0.1", port);

        // Start listening for client requests.
        //EstadoConnection.text = "mandada la mierda";
        //server.Start();
        // stream = client.GetStream();
    }

    // Update is called once per frame
    void Update()
    {

    }


    //Conexion con el programa servidor que esta a la espera (visión o movimientos)
    void Connect_client()
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
            EstadoConnection.text = "Connection Made client";

        }
        catch (System.Net.Sockets.SocketException)
        {
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Connection Failed";
        }

    }
    void Connect_server()
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
            IPAddress localAddr = IPAddress.Parse("127.0.0.1");
            server = new TcpListener(localAddr, port);
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Connection Made server";

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
        Connect_client();
        try
        {
            string message = Selector.captionText.text; //set message variable to input
            int byteCount = Encoding.ASCII.GetByteCount(message); //Measures bytes required to send ASCII data
            byte[] sendData = new byte[byteCount]; //Prepares variable size for required data
            sendData = Encoding.ASCII.GetBytes(message); //Sets the sendData variable to the actual binary data (from the ASCII)
            NetworkStream stream = client.GetStream(); //Opens up the network stream
            stream.Write(sendData, 0, sendData.Length); //Transmits data onto the stream
            EstadoConnection.text = "Consulta realizada sobre" + Selector.captionText.text;


            //Recepcion de realizada



        }
        catch (System.NullReferenceException) //Error if socket not open
        {
            //Adds debug to list box and shows message box
            EstadoConnection.text = "Fallo al enviar datos";
        }

        Connect_server();
        // Buffer for reading data
        Byte[] bytes = new Byte[256];
        String data = null;

        // Enter the listening loop.




    }
    public void SecuenciaCompleta()
    {
        
        try
        {
            // Set the TcpListener on port 8000.

            string data = "";
            if (Selector.captionText.text=="MARGARITA")
            {
                data = "000-000-150";
            }
                
            if(Selector.captionText.text == "ROSA")
            {
                data = "040-040-200";
            }

            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);
            stream.Write(msg, 0, msg.Length);

            EstadoConnection.text = "mandada la mierda";
            byte[] buffer = new byte[1024];
            int bytes = stream.Read(buffer,0,buffer.Length);
            if (bytes < 0)
            {
                EstadoConnection.text = "sin recepcion";
            }
            else
                EstadoConnection.text = "recibido";

            // Enter the listening loop.
            while (true)
            {
                Console.Write("Waiting for a connection... ");

                // Perform a blocking call to accept requests.
                // You could also use server.AcceptSocket() here.
                TcpClient client = server.AcceptTcpClient();
                EstadoBusqueda.text = "Connected!";

                

                // Get a stream object for reading and writing
               

                int i;

                

                // Shutdown and end connection
                client.Close();
            }
        }
        catch (SocketException e)
        {
            Console.WriteLine("SocketException: {0}", e);
        }
        finally
        {
            // Stop listening for new clients.
            server.Stop();
        }

        Console.WriteLine("\nHit enter to continue...");
        Console.Read();
    }
    public void PruebaSock()
    {
        float x=0, y=0;
        string data = "";
        if (Selector.captionText.text == "MARGARITA")
        {
            data = "000-000-150";
        }

        if (Selector.captionText.text == "ROSA")
        {
            data = "040-040-200";
        }

        clienteVrep.Envio_Vrep(data, x, y);

    }
}

