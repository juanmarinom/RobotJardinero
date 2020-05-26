using UnityEngine;
using System.Data;
using Mono.Data.Sqlite;
using System.IO;
using System;
using UnityEngine.UI;
/// <summary>
/// CATEGORÍAS DE LAS PLANTAS:
/// 
/// 1-- MARGARITA
/// 2-- DIENTEDELEON
/// 3-- ROSA
/// 4-- GIRASOLES
/// 5-- TUILPANES
/// 
/// REVISAR QUE TODOS LOS MODULOS TrABAJEN ASÍ
/// 
/// </summary>
public class SqliteTest: MonoBehaviour
{
	public Slider a, b, c, d, e, f;
	public Gradient g;
	public float posX;
	public float posY;
	public int categoria;
	//int aux, aux2;
	public Text tipo;
	public Image fill, fill2, fill3, fill4, fill5, fill6;
	public Text txt1, txt2, txt3, txt4, txt5, txt6;
	public Image tipoflor;
	public Sprite margarita, rosa, dientdleon, tulip, girasol;
	public Text yahayflor;
	public void buscarporposicion()
	{
		string connection = "URI=file:" + Application.dataPath + "/../../bin/database.db";

		a.value = 0; 
		yahayflor.text = "VAYA, PARECE QUE EL ROBOT NO SABE QUE FLOR HAY AQUÍ...";

		IDbConnection dbcon = (IDbConnection) new SqliteConnection(connection);
		dbcon.Open();
		IDbCommand cmnd_read = dbcon.CreateCommand();
		IDataReader reader;
		if ((posX != 0.0f || posY != 0.0f) && categoria == 0)
		{
			//Leer todos los datos de la posicion seleccionada
			string query = "SELECT * FROM plantas WHERE posicion_x =" + posX.ToString() + " AND posicion_y =" + posY.ToString();
			cmnd_read.CommandText = query;
			reader = cmnd_read.ExecuteReader();

			while (reader.Read())
			{
				//Cada columna será una posición de reader
				Debug.Log("id: " + reader[0] + " " + reader[1] + " " + reader[2] + " " + reader[3] + " " + reader[4] + " " + reader[5]);

				//TO DO: Se deberá guardar cada dato en su correspondiente variable	
				//barra de salud
				int aux = 0;
				aux = System.Convert.ToInt32(reader[5]);
				a.value = (float)aux;
				fill.color = g.Evaluate(a.normalizedValue);

				//tipo de flor
				switch (System.Convert.ToInt32(reader[1]))
				{
					case 1: 
						tipo.text = " LA PLANTA " + reader[0] + " ES UNA MARGARITA CON " + reader[5] + " % DE SALUD Y " + reader[4] + "  PET/RAD ";
						tipoflor.sprite = margarita;
						yahayflor.text = "";

						break;
					case 2: 
						tipo.text = " LA PLANTA " + reader[0] + " ES UN DIENTE DE LEON CON " + reader[5] + " % DE SALUD Y " + reader[4] + "  DE FRONDOSIDAD ";
						tipoflor.sprite = dientdleon;
						yahayflor.text = "";
						break;
					case 3: 
						tipo.text = " LA PLANTA " + reader[0] + " ES UNA ROSA CON " + reader[5] + " % DE SALUD Y " + reader[4] + "  PET/RAD ";
                        tipoflor.sprite = rosa;
						yahayflor.text = "";
						break;
					case 4: 
						tipo.text = " LA PLANTA " + reader[0] + " ES UN GIRASOL CON " + reader[5] + " % DE SALUD Y " + reader[4] + "  PET/RAD ";
                        tipoflor.sprite = girasol;
						yahayflor.text = "";
						break;
					case 5:
						tipo.text = " LA PLANTA " + reader[0] + " ES UN TULIPAN CON " + reader[5] + " % DE SALUD Y " + reader[4] + "  PET/RAD ";
                        tipoflor.sprite = tulip;
						yahayflor.text = "";
						break;
				}
			}
		}
		else
		{
			tipo.text = "EL ROBOT NO HA ANALIZADO ESTA POSICIÓN";
			Debug.Log("Error en la consulta.");
		}
		// Close connection
		dbcon.Close();
	}

	public void buscarportipo()

	{// Crear base de datos en la ruta "/Database"
		txt1.text = "LA PLANTA 1 NO ES DEL TIPO DE FLOR SELECCIONADO";
		txt2.text = "LA PLANTA 2 NO ES DEL TIPO DE FLOR SELECCIONADO";
		txt3.text = "LA PLANTA 3 NO ES DEL TIPO DE FLOR SELECCIONADO";
		txt4.text = "LA PLANTA 4 NO ES DEL TIPO DE FLOR SELECCIONADO";
		txt5.text = "LA PLANTA 5 NO ES DEL TIPO DE FLOR SELECCIONADO";
		txt6.text = "LA PLANTA 6 NO ES DEL TIPO DE FLOR SELECCIONADO";
		string connection = "URI=file:" + Application.dataPath + "/../../bin/database.db";
		// Open connection
		IDbConnection dbcon = new SqliteConnection(connection);
		dbcon.Open();
		IDbCommand cmnd_read = dbcon.CreateCommand();
		IDataReader reader;
		if (categoria > 0 && posX == 0.0f && posY == 0.0f)
		{
			//Leer todos los datos de la categoría seleccionada
			string query = "SELECT * FROM plantas WHERE categoria_id =" + categoria.ToString();
			cmnd_read.CommandText = query;
			reader = cmnd_read.ExecuteReader();
			int cont = 0;
			while (reader.Read())
			{
				//Cada columna será una posición de reader
				Debug.Log("id: " + reader[0] + " " + reader[1] + " " + reader[2] + " " + reader[3] + " " + reader[4] + " " + reader[5]);
				//TO DO: Se deberá guardar cada dato en su correspondiente variable	
				int aux = 0;
				aux = System.Convert.ToInt32(reader[5]);
				cont = cont + 1;

				if (cont == 1)
				{
					a.value = (float)aux;
					fill.color = g.Evaluate(a.normalizedValue);
					switch (System.Convert.ToInt32(reader[1]))
					{
						case 1:
							txt1.text = " LA PLANTA " + cont + " ES UNA MARGARITA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 2:
							txt1.text = " LA PLANTA " + cont + " ES UN DIENTE DE LEON CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  DE FRONDOSIDAD ";
							break;
						case 3:
							txt1.text = " LA PLANTA " + cont + " ES UNA ROSA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 4:
							txt1.text = " LA PLANTA " + cont + " ES UN GIRASOL CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 5:
							txt1.text = " LA PLANTA " + cont + " ES UN TULIPAN CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
					}
				}
				if (cont == 2)
				{
					b.value = (float)aux;
					fill2.color = g.Evaluate(b.normalizedValue);
					switch (System.Convert.ToInt32(reader[1]))
					{
						case 1:
							txt2.text = " LA PLANTA " + cont + " ES UNA MARGARITA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
						break;
						case 2:
							txt2.text = " LA PLANTA " + cont + " ES UN DIENTE DE LEON CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  DE FRONDOSIDAD ";
						break;
						case 3:
							txt2.text = " LA PLANTA " + cont + " ES UNA ROSA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
						break;
						case 4:
							txt2.text = " LA PLANTA " + cont + " ES UN GIRASOL CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
						break;
						case 5:
							txt2.text = " LA PLANTA " + cont + " ES UN TULIPAN CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
					}
				}
				if (cont == 3)
				{
					c.value = (float)aux;
					fill3.color = g.Evaluate(c.normalizedValue);
					switch (System.Convert.ToInt32(reader[1]))
					{
						case 1:
							txt3.text = " LA PLANTA " + cont + " ES UNA MARGARITA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 2:
							txt3.text = " LA PLANTA " + cont + " ES UN DIENTE DE LEON CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  DE FRONDOSIDAD  ";
							break;
						case 3:
							txt3.text = " LA PLANTA " + cont + " ES UNA ROSA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 4:
							txt3.text = " LA PLANTA " + cont + " ES UN GIRASOL CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 5:
							txt3.text = " LA PLANTA " + cont + " ES UN TULIPAN CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
					}
				}
				if (cont == 4)
				{
					d.value = (float)aux;
					fill4.color = g.Evaluate(d.normalizedValue);
					switch (System.Convert.ToInt32(reader[1]))
					{
						case 1:
							txt4.text = " LA PLANTA " + cont + " ES UNA MARGARITA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 2:
							txt4.text = " LA PLANTA " + cont + " ES UN DIENTE DE LEON CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  DE FRONDOSIDAD  ";
							break;
						case 3:
							txt4.text = " LA PLANTA " + cont + " ES UNA AMAPOLA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 4:
							txt4.text = " LA PLANTA " + cont + " ES UN GIRASOL CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 5:
							txt4.text = " LA PLANTA " + cont + " ES UN TULIPAN CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
					}
				}
				if (cont == 5)
				{
					e.value = (float)aux;
					fill5.color = g.Evaluate(e.normalizedValue);
					switch (System.Convert.ToInt32(reader[1]))
					{
						case 1:
							txt5.text = " LA PLANTA " + cont + " ES UNA MARGARITA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 2:
							txt5.text = " LA PLANTA " + cont + " ES UN DIENTE DE LEON CON " + reader[5] + " % DE SALUD  Y " + reader[4] + " DE FRONDOSIDAD  ";
							break;
						case 3:
							txt5.text = " LA PLANTA " + cont + " ES UNA ROSA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 4:
							txt5.text = " LA PLANTA " + cont + " ES UN GIRASOL CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 5:
							txt5.text = " LA PLANTA " + cont + " ES UN TULIPAN CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
					}
				}
				if (cont == 6)
				{
					f.value = (float)aux;
					fill6.color = g.Evaluate(f.normalizedValue);
					switch (System.Convert.ToInt32(reader[1]))
					{
						case 1:
							txt6.text = " LA PLANTA " + cont + " ES UNA MARGARITA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 2:
							txt6.text = " LA PLANTA " + cont + " ES UN DIENTE DE LEON CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  DE FRONDOSIDAD ";
							break;
						case 3:
							txt6.text = " LA PLANTA " + cont + " ES UNA ROSA CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 4:
							txt6.text = " LA PLANTA " + cont + " ES UN GIRASOL CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
						case 5:
							txt6.text = " LA PLANTA " + cont + " ES UN TULIPAN CON " + reader[5] + " % DE SALUD  Y " + reader[4] + "  PET/RAD ";
							break;
					}
				}
				Debug.Log(cont);
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
