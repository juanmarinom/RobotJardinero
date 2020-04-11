using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class Main : MonoBehaviour
{
    // Start is called before the first frame update
    public Text_Behavior t1;
    public Text t2;
    int n;
    void Start()
    {
        n = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            n++;
            n = t1.calculaMisPelotas(n);
            t1.NuevaPulsacion(n);
            
            
            
        }
        if(Input.GetKeyDown(KeyCode.A))
        {
            Debug.Log(n);
        }
    }
}
