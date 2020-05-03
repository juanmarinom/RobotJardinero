using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class prueba : MonoBehaviour
{
    public Slider p;

    void Update()
    {
        p.minValue = 0;
        p.maxValue = 100;
        p.wholeNumbers = true;
        p.value = 50;

    }


    // Start is called before the first frame update
    void Start()
    {

    }

    public void onValueChange(float value)
    {
        p.value = value;
    }
}
