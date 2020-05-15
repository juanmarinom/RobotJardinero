using UnityEngine;
using System.Data;
using Mono.Data.Sqlite;
using System.IO;

public class SqliteTest : MonoBehaviour
{
	public float posX;
	public float posY;
	public int categoria;

	// Use this for initialization
	void Start()
	{

		// Crear base de datos en la ruta "/Database"
		string connection = "URI=file:" + Application.dataPath + "/Database/base_de_prueba.db";
		

		// Open connection
		IDbConnection dbcon = new SqliteConnection(connection);
		dbcon.Open();
		IDbCommand cmnd_read = dbcon.CreateCommand();
		IDataReader reader;

		//-----BUSQUEDA POR POSICION-------

		if (posX>0.0f && posY>0.0f && categoria==0)
		{
			//Leer todos los datos de la posicion seleccionada
			string query = "SELECT * FROM plantas WHERE posicion_x =" + posX.ToString() + "AND posicion_y =" + posY.ToString();
			cmnd_read.CommandText = query;
			reader = cmnd_read.ExecuteReader();
			while (reader.Read())
			{
				//Cada columna será una posición de reader
				Debug.Log("id: " + reader[0].ToString() + reader[1].ToString() + reader[2].ToString() + reader[3].ToString() + reader[4].ToString());
				
				//TODO: Se deberá guardar cada dato en su correspondiente variable				

			}


		}

		//-----BUSQUEDA POR CATEGORIA-------

		else if (categoria>0 && posX == 0.0f && posY ==0.0f)
		{
			//Leer todos los datos de la categoría seleccionada
			string query = "SELECT * FROM plantas WHERE categoria =" + categoria.ToString();
			cmnd_read.CommandText = query;
			reader = cmnd_read.ExecuteReader();
			while (reader.Read())
			{
				//Cada columna será una posición de reader
				Debug.Log("id: " + reader[0].ToString() + reader[1].ToString() + reader[2].ToString() + reader[3].ToString() + reader[4].ToString());

				//TODO: Se deberá guardar cada dato en su correspondiente variable				

			}
		}

		else
		{
			Debug.Log("Error en la consulta.");
		}
		
		// Close connection
		dbcon.Close();

	}
}