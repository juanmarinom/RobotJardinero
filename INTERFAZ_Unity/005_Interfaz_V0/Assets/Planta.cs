using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Planta : MonoBehaviour
{
    string Tipo;
    int color;
    int densFoliar;
    public Button search;
    public Text Info_Tipo;
    public Text Info_DF;
    public Text Info_color;

    
    void Start()
    {
        Tipo = "Sin Registros";
        color = -1;
        densFoliar = -1;
        
    }

    // Update is called once per frame
    void Update()
    {
        Actualiza();
    }

    void Actualiza()
    {
        if( color < 0 || densFoliar < 0 )
        {
            Info_DF.text = "Densidad Foliar = - ";
            Info_color.text = "Color = - ";
        }else
        {
            Info_DF.text = "Densidad Foliar = " + densFoliar.ToString();
            Info_color.text = "Color = " + color.ToString();
        }
        Info_Tipo.text = Tipo;
    }
}
