using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovimientoP1 : MonoBehaviour
{
    Vector3 targetpos;
    Vector3 currentPos;
    // Start is called before the first frame update
    void Start()
    {
        targetpos.x = 150;
        targetpos.y = 150;
        targetpos.z = 0;
        //transform.position = targetpos;
        currentPos = targetpos;

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.J))
        {
            currentPos.x = currentPos.x - 20;
            transform.position = currentPos;
        }
        if (Input.GetKeyDown(KeyCode.L))
        {
            currentPos.x = currentPos.x + 20;
            transform.position = currentPos;
        }
        if (Input.GetKeyDown(KeyCode.I))
        {
            currentPos.y = currentPos.y + 20;
            transform.position = currentPos;
        }
        if (Input.GetKeyDown(KeyCode.K))
        {
            currentPos.y = currentPos.y - 20;
            transform.position = currentPos;
        }
    }
}
