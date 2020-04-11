using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class Text_Behavior : MonoBehaviour
{

    public Text TEXTO;
    void Start()
    {
        TEXTO.text = "Numero de intentos = 0";
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void NuevaPulsacion(int anterior) 
    {
        int nuevo = anterior + 1;
        TEXTO.text = "Numero de intentos = " + nuevo;
    }

    public int calculaMisPelotas(int number)
    {
        return number + 5;
    }
    
}
