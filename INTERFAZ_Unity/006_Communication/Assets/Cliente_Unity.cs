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

public class Cliente_Unity : MonoBehaviour
{
    //Atributos necesarios para los sockets en Unity
    int port; //Puerto de comunicación. Se establece uno para Vrep y otro para la visión
    TcpClient client;
    TcpListener Server;
    NetworkStream stream;
    void Start()
    {
       

    }

    public Cliente_Unity(int puerto)
    {
        //Al crear un elemento d etipo Cliente_Unity, se inicializará al comienzo del programa. Por lo tanto, se debe de abrir previamente los servidores para que se produzca la conexion
        port = puerto;
        IPAddress localAddr = IPAddress.Parse("127.0.0.1");

        client = new TcpClient("127.0.0.1", port);
        stream = client.GetStream();

    }
    //Envio_Vrep puede mandar: 
        //- O una posicion final de la base que el robot debe alcanzar, en cuyo caso el mensaje seria del tipo 040-040-150. Al concluir el movimiento. vrep devuelve la posicion final de la base REAL.
        //o peticiones. Pej: PBase, que al recibirlo Vrep obtendria la posicion de la base sin moverla y se la pasa a Unity.
    public bool Envio_Vrep(string PosObjetivo, float xBaseRobot, float yBaseRobot)
    {   //Pos objetivo con formato 000-000-000 donde los tres difitos definen X-Y-Altura
        char separador = '-';

        byte[] msg = System.Text.Encoding.ASCII.GetBytes(PosObjetivo);
        stream.Write(msg, 0, msg.Length);

   
        byte[] buffer = new byte[1024];
        int bytes = stream.Read(buffer, 0, buffer.Length);
        if (bytes > 0)
        {
            //Decodificamos el mensaje leido 
            var PosFinal = Encoding.UTF8.GetString(buffer);
            var Pfinal = PosFinal;
            //El envío de Vrep con la posicion final de la base tiene el formato X-Y. Debemos separarlo para asignarlo a las variables xBaseRobot e yBaseRobot
            var posicionFinal = PosFinal.Split(separador);
            //DUDO DE QUE ESTA CONVERSION SEA ADECUADA. SINO LO PASAMOS COMO STRING PARA FUERA Y YA ESTA
            //xBaseRobot = (float)System.Convert.ToSingle(posicionFinal[0]);
            //yBaseRobot = (float)System.Convert.ToSingle(posicionFinal[1]);
            return true;
        }
        else return false;
    }


    //Tipos de peticiones: 
    //-Analiza posicion: Hay que mandarle la posicion
    //-Busca Tipo planta: Recorre las 6 imagenes para buscar la requerida

    //Formato identificación tipo planta
    //0 - Margarita
    //1 - Diente de leon
    //2 - Rosa
    //3 - Girasol
    //4 . Tulipan

    public bool EnvioVision(string Peticion)
    {
        byte[] msg = System.Text.Encoding.ASCII.GetBytes(Peticion);
        stream.Write(msg, 0, msg.Length);


        byte[] buffer = new byte[1024];
        int bytes = stream.Read(buffer, 0, buffer.Length);
        //En el caso de la vision, es suficiente con comprobar que hemos recibido un mensaje de vuelta para saber que ha concluido

        if (bytes > 0)
        {
            return true;
        }
        else return false;
    }
    public void EnvioMierda(string select)
    {
        try
        {
            // Set the TcpListener on port 8000.

            string data = "000-000-150";
            
            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);
            stream.Write(msg, 0, msg.Length);

            
            byte[] buffer = new byte[1024];
            int bytes = 0;
            while (bytes <= 0)
            {
                bytes = stream.Read(buffer, 0, buffer.Length);
            }
             
            
            // Enter the listening loop.
            while (true)
            {
                

                // Perform a blocking call to accept requests.
                // You could also use server.AcceptSocket() here.
                TcpClient client = Server.AcceptTcpClient();
                



                // Get a stream object for reading and writing


                int i;



                // Shutdown and end connection
                client.Close();
            }
        }
        catch (SocketException e)
        {
            
        }
        finally
        {
            // Stop listening for new clients.
            Server.Stop();
        }

        
    }

}
