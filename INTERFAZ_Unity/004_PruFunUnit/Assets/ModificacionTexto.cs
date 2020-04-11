using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ModificacionTexto : MonoBehaviour
{
    // Start is called before the first frame update
    public Text t1;
    void Start()
    {
        t1.text = "SIN REGISTROS";
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.C))
        {
            t1.text = "CACTUS";
        }

    }
}
