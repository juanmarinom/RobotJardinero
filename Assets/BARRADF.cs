using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class BARRADF : MonoBehaviour
{
    public Slider p;
    public Gradient g;
    public Image fill;
    public int tipo;
    public float posx;
    public float posy;
    public float densf;
    public SqliteTest a;


    // Start is called before the first frame update
    void Start()
    {
        //p.value = 100;
        //interfaz.text = ("LA DENSIDAD FOLIAR DE LA PLANTA ES: ");
        //posx.text = "LA POSICIÓN X ES: ";
        //posy.text = "LA POSICIÓN Y ES: ";
    }

    // Update is called once per frame
    void Update()
    {
        // fill.color = g.Evaluate(p.value);
        //interfaz.color = g.Evaluate(p.normalizedValue);
        //tipo.color = g.Evaluate(p.normalizedValue);
        //tipo.text = "EL TIPO DE FLOR EN CUESTIÓN ES: " /*+ tipo[i].ToString()*/;
        ////StartCoroutine("Esperar");
        //Actualizaposicion();
       
    }
     void Actualizaposicion()
    {
        
        //x = x + 0.1f;
        //posx.text =  x.ToString();
        //y = y + 0.2f;
        //posy.text = y.ToString();

    }
    //IEnumerator Esperar()
    //{
    //    yield return new WaitForSeconds(10);
    //}
}


//"DF =  " + DF[i].ToString()