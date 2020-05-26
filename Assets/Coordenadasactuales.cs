using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class Coordenadasactuales : MonoBehaviour
{
    public Text cx;
    public Text cy;
    public Text cz;
    int x = 0;
    // Start is called before the first frame update
    void Start()
    {
        cx.text = "0";
        cy.text = "0";
        cz.text = "0";

    }

    // Update is called once per frame
    void Update()
    {
        //cx.text= LOQ SEA DE LA BBDD;
        //cy.text= LOQ SEA DE LA BBDD;
        //cz.text= LOQSEA;
    }
}
